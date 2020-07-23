## ANALYZING TELEMEDICINE SURVEY RESULTS - FUNCTIONS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 21 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots


## Ancillary modules

from TelemedSurvey_params import *





'------------------------------------------------------------------------------------------'
#######################
## Generic functions ##
#######################


## Determine difference in years between two dates
def difference_between_years(row):
    """
    Determine difference in years between two dates
    """
    res = relativedelta(datetime.now(), row).years
    return res



## Creating variables count crossing table
def vars_cross_df(df, ct_col, rc):
    """
    Creating variables count crossing table
        args:
            df (dataframe): dataframe that contains columns that will be crossed
            ct_col (list): list of one element with the name of the column that will serve as a reference to count crossings
            rc (list): list of columns that will be crossed
        returns:
            dfx (dataframe): resulting crossed table
    """

    dfx = df.copy()

    ## Creating crossing table
    dfx = dfx.loc[:, rc + ct_col].groupby(rc).count().unstack()
    dfx.columns = dfx.columns.droplevel()
    dfx.fillna(value=0, inplace=True)

    return dfx



## Crossing possible names from reference dictionary
def search_names_dict(row, ref_dict):
    """
    Crossing possible names from reference dictionary
    """

    res = 'Otra'

    for entry in ref_dict:
        for ref in ref_dict[entry]:
            if ref in row:
                res = entry
                break
        if res != 'Otra':
            break


    return res





'------------------------------------------------------------------------------------------'
##############################
## Imported data processing ##
##############################


## Cleaning imported dataset
def clean_raw_dataset(df):
    """
    Cleaning imported dataset
    """


    ## Adding first two numbers to year in order to complete date
    """
    Adding first two numbers to year in order to complete date
    """
    def fix_date(row):

        if row == '0':
            return '01/01/1900'

        year = int(row.split(sep='/')[2])

        if year > 10 & year < 99:
            fix = '19' + row[-2:]
            res = row[:-2] + fix
        else:
            fix = '20' + row[-2:]
            res = row[:-2] + fix

        return res


    ##


    ## Eliminating non relevant columns
    nrc = [nrc for nrc in df.columns if nrc not in simp_rcol_names]
    df.drop(nrc, axis=1, inplace=True)


    ## Simplifying column names
    df.rename(columns=simp_rcol_names, inplace=True)


    ## Adding column with serial number
    df.insert(0, '#', range(1, df.shape[0] + 1))


    ## Cleaning dirty columns
    df['Ha considerado ofrecer teleconsulta?'] = df['Ha considerado ofrecer teleconsulta?'].apply(lambda x: 'NO' if x == 'No' else x)
    df['Cuenta con plataforma de gestión?'] = df['Cuenta con plataforma de gestión?'].apply(lambda x: 'NO' if x == 'No' else x)
    df['Cuenta con plataforma de teleconsultas?'] = df['Cuenta con plataforma de teleconsultas?'].apply(lambda x: 'NO' if x == 'No' else x)


    return df





'------------------------------------------------------------------------------------------'
######################################################################
## Analysis 1 - Have you considered offering a telemedicine service ##
######################################################################


## Creating graph data
def A1_graph_data(df):
    """
    Creating graph data
    """


    dfx = df.copy()


    rc = [
        '#',
        'Especialidad',
        'Ha considerado ofrecer teleconsulta?'
    ]
    nrc = [col for col in dfx.columns if col not in rc]
    dfx.drop(nrc, axis=1, inplace=True)

    dfx = dfx.groupby(['Especialidad', 'Ha considerado ofrecer teleconsulta?']).count().unstack()

    dfx.columns = dfx.columns.droplevel()

    dfx.loc['Todos', :] = dfx.sum()

    dfx = dfx.loc[:, 'NO':'SI'].div(dfx.sum(axis=1), axis=0)


    return dfx



## Creting A1 graph
def A1_graph(dfx):
    """
    Creting A1 graph
    """

    ## x-axis
    x_axis = dfx.index

    ## Bars
    bars = dfx.columns

    ## Create and display graph
    fig = go.Figure(data=
                    [go.Bar(name=bar, x=x_axis, y=dfx[bar], text=(dfx[bar]*100).astype(str).str[:5] + '%', textposition='auto') for bar in bars]
                   )

    fig.update_layout(
        title = 'Ha considerado ofrecer teleconsulta?',
        xaxis_title = 'Especialista',
        yaxis_title = 'Participación',
        barmode='group',
        # autosize=False,
        # width=1500,
        # height=500
    )
    fig.update_xaxes(type="category")

    fig.show()





'------------------------------------------------------------------------------------------'
###################################################################
## Analysis 2 - How common do you think it will be for patients? ##
###################################################################


## Creating graph data
def A3_graph_data(df):
    """
    Creating graph data
    """


    dfx = df.copy()

    rc = [
        'Cuenta con plataforma de gestión?',
        'Cuenta con plataforma de teleconsultas?'
    ]

    dfx = vars_cross_df(dfx, ['#'], rc)

    dfx = dfx/dfx.sum().sum()


    return dfx


## Creting A3 graphs
def A3_graph(dfx):
    """
    Creting A3 graphs
    """

    fig = go.Figure(
        data=go.Heatmap(
            z=dfx.values,
            x=dfx.columns,
            y=dfx.index,
            # type='heatmap'
            colorscale='Viridis'
        )
    )

    fig.update_layout(
        title = 'Adopción de plataformas digitales por parte de los médicos',
        xaxis_title = 'Cuenta con plataforma de teleconsultas?',
        yaxis_title = 'Cuenta con plataforma de gestión?',
    )

    fig.show()





'------------------------------------------------------------------------------------------'
#######################################################
## Analysis 3 - What platforms do you currently use? ##
#######################################################


## Creating graph data
def A6_graph_data(df):
    """
    Creating graph data
    """


    ## Creting graph for analysis 1 - which administration platform?
    def A6_graph1_data(df):
        """
        Creting graph for analysis 1 - which administration platform?
        """

        dfx1 = df.copy()

        # m1 = dfx1['Cuenta con plataforma de gestión?'] == 'SI'
        # m2 = dfx1['Qué plataforma de gestión?'].isnull()
        # print('Número de médicos que sí tienen plataforma de gestión pero no respondieron cual', df.loc[(m1 & m2), :].shape)

        rc = [
            'Cuenta con plataforma de gestión?',
            'Qué plataforma de gestión?'
        ]

        dfx1.drop([col for col in dfx1.columns if col not in rc], axis=1, inplace=True)

        m1 = dfx1['Cuenta con plataforma de gestión?'] == 'SI'
        dfx1 = dfx1.loc[m1, :]
        dfx1.fillna('No_especificado', inplace=True)

        dfx1['Qué plataforma de gestión?'] = dfx1['Qué plataforma de gestión?'].str.lower().str.strip()

        dfx1['Ref_match'] = dfx1['Qué plataforma de gestión?'].apply(lambda x: search_names_dict(x, platforms_names))


        return dfx1


    ## Creting graph for analysis 1 - which virtual doctor platform?
    def A6_graph2_data(df):
        """
        Creting graph for analysis 1 - which telemedicine platform?
        """

        dfx2 = df.copy()

        rc = [
            'Cuenta con plataforma de teleconsultas?',
            'Qué plataforma de teleconsulta?'
        ]

        dfx2.drop([col for col in dfx2.columns if col not in rc], axis=1, inplace=True)

        m1 = dfx2['Cuenta con plataforma de teleconsultas?'] == 'SI'
        dfx2 = dfx2.loc[m1, :]
        dfx2.fillna('No_especificado', inplace=True)

        dfx2['Qué plataforma de teleconsulta?'] = dfx2['Qué plataforma de teleconsulta?'].str.lower().str.strip()

        dfx2['Ref_match'] = dfx2['Qué plataforma de teleconsulta?'].apply(lambda x: search_names_dict(x, platforms_names))


        return dfx2


    ## Main function

    dfx1 = A6_graph1_data(df)

    dfx2 = A6_graph2_data(df)


    return dfx1, dfx2
