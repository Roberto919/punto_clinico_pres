## ANALYZING TELEMEDICINE SURVEY RESULTS - FUNCTIONS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 21 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff


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
        # else:
        #     res=row

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
################################################################################
## Analysis 3 - Do you have either a telemedicine or administrative platform? ##
################################################################################


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

    
    fig = ff.create_annotated_heatmap(
        dfx.values,
        x=list(dfx.columns),
        y=list(dfx.index),
        annotation_text=dfx.applymap(lambda x: str(x*100)[:5] + '%').values
    )

    fig.update_layout(
        # title = 'Adopción de plataformas digitales por parte de los médicos',
        # annotations=annotations,
        title={
            'text': 'Uso de plataformas por parte de los médicos',
            'y': 0.97
        },
        xaxis_title = 'Cuenta con plataforma de teleconsultas?',
        yaxis_title = 'Cuenta con plataforma de gestión?',
        # height=750
    )

    # fig.show()
    return fig





'------------------------------------------------------------------------------------------'
########################################################
## Analysis 5 - How often would you use the platform? ##
########################################################


## Creating graph data
def A5_graph_data(df):
    """
    Creating graph data
    """

    ## Copying main dataframe
    dfx = df.copy()

    ## Selecting only relevant columns
    rc = [
        '#',
        'Especialidad',
        'Regularidad de uso si tuviera plataforma'
    ]
    nrc = [col for col in dfx.columns if col not in rc]
    dfx.drop(nrc, axis=1, inplace=True)

    ## Grouping results
    dfx = dfx.groupby(['Especialidad', 'Regularidad de uso si tuviera plataforma']).count().unstack()
    dfx.columns = dfx.columns.droplevel()

    ## Adding 'Ambos' row
    dfx.loc['Ambos', :] = dfx.sum()

    ## Converting all values to percentages
    dfx['Sum'] = dfx.sum(axis=1)
    for col in dfx.columns:
        dfx[col] = dfx[col]/dfx['Sum']
    dfx.drop(['Sum'], axis=1, inplace=True)


    return dfx





## Creating graph
def A5_graph(dfx):
    """
    Creating graph
    """

    ## Creating figure
    fig = go.Figure()

    ## Color RGB coordinates
    color_rgb_start = np.array([213, 202, 235])
    color_delta = np.array([30, 0, 20])

    ## Craeting each bar for the graph
    for col in dfx.columns:
        #### Color that will be assigned to the bar
        color = 'rgb' + str(tuple(color_rgb_start - color_delta*list(dfx.columns).index(col)))

        #### Crating each bar
        fig.add_trace(
            go.Bar(
                y=dfx.index,
                x=dfx[col],
                name=col,
                orientation='h',
                text=(dfx[col]*100).astype(str).str[:5] + '%',
                textposition='auto',
                marker_color=color
                # text=dfx[col],
                # textposition='outside'
            )
        )

    ## Figure layout
    fig.update_layout(
        xaxis = dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0.15, 1]
        ),
        yaxis = dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False
        ),
        barmode='stack',
        showlegend=False,
        title='Regularidad de uso de la plataforma',
        plot_bgcolor='rgb(255,255,255)'
        # margin=dict(l=40, r=10, t=140, b=80),
    )

    ## Annotations
    annotations = []

    #### Labeling 'y' axis
    for idx in dfx.index:
        annotations.append(
            dict(
                xref='paper',
                yref='y',
                x=0.14,
                y=idx,
                xanchor='right',
                text=str(idx),
                showarrow=False,
                align='right'
            )
        )

    # for col in dfx.columns:
    #     #### Labeling the first percentage of each bar (x_axis)
    #     annotations.append(
    #         dict(
    #             xref='x',
    #             yref='y',
    #             x=dfx[col],
    #             y=idx,
    #             text='hola',
    #             showarrow=False,
    #         )
    #     )

    #### Aupdating figure with annotations
    fig.update_layout(
        annotations=annotations,
        autosize=False,
        height=350
        )

    ## Display figure
    # fig.show()
    return fig





'------------------------------------------------------------------------------------------'
#######################################################
## Analysis 6 - What platforms do you currently use? ##
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

        dfx1 = pd.DataFrame(dfx1['Ref_match'].value_counts())
        dfx1.rename(columns={'Ref_match': 'Plataforma de gestión'}, inplace=True)

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

        dfx2 = pd.DataFrame(dfx2['Ref_match'].value_counts())
        dfx2.rename(columns={'Ref_match': 'Plataforma de teleconsultas'}, inplace=True)

        return dfx2


    ## Main function
    #### Counting the number of platforms mentioned (sanitized names)
    dfx1 = A6_graph1_data(df)
    dfx2 = A6_graph2_data(df)

    #### Joining the results obtained
    dfx = dfx1.join(dfx2)
    dfx.fillna(0, inplace=True)

    # #### Calculating total
    # dfx.loc['Total', :] = dfx.sum()


    return dfx



## Creating graph
def A6_graph(dfx):
    """
    Creating graph
    """

    ## Creating figure
    fig = go.Figure()

    ## Craeting each bar for the graph
    for col in dfx.columns:
        fig.add_trace(
            go.Bar(
                x=dfx.index,
                y=dfx[col],
                name=col,
                text=dfx[col],
                textposition='outside'
            )
        )

    ## Figure adjustments
    fig.update_layout(
        height=750,
        width=1250,
        title='Plataformas mencionados por los médicos',
        xaxis_title = 'Plataforma',
        yaxis_title = 'Médicos usuarios',
        plot_bgcolor='rgb(255,255,255)'
    )

    ## Displaying figure
    # fig.show()
    return fig





'------------------------------------------------------------------------------------------'
#################################################################################
## Analysis 7 - What are the attributes that you value the most in a platform? ##
#################################################################################


## Creating graph data
def A7_graph_data(df):
    """
    Creating graph data
    """

    ## Copying main dataframe
    dfx = df.copy()

    ## Selecting only relevant columns
    rc = [
        '#',
        'Especialidad',
        'Funcionalidades relevantes'
    ]
    nrc = [col for col in dfx.columns if col not in rc]
    dfx.drop(nrc, axis=1, inplace=True)

    ## Converting atributes to list of attributes
    dfx.loc[:, 'Funcionalidades relevantes'] = dfx['Funcionalidades relevantes'].apply(lambda x: x.split(sep=';'))

    ## Exploding dataframe based on attributes and doing some cleaning
    dfx = dfx.explode('Funcionalidades relevantes')
    dfx.loc[:, 'Funcionalidades relevantes'] = dfx['Funcionalidades relevantes'].apply(lambda x: x.strip())
    dfx.loc[:, 'Funcionalidades relevantes'] = dfx['Funcionalidades relevantes'].apply(lambda x: search_names_dict(x, platform_features_options))
    m1 = dfx['Funcionalidades relevantes'].isin(list(platform_features_options.keys()))
    dfx = dfx.loc[m1, :]

    ## Grouping values and adding total
    dfx = dfx.groupby(['Especialidad', 'Funcionalidades relevantes']).count().unstack()
    dfx.columns = dfx.columns.droplevel()
    dfx.loc['Ambos', :] = dfx.sum()


    return dfx.T



## Creating graph
def A7_graph(dfx):
    """
    Creating graph
    """


    ## Function to add line breaks to long strings of text
    def adding_breaks_to_text(txt_lst):
        """
        """

        ## Parámeters
        t = 22
        cl = 0
        new_lst = []

        ## Modifying loop
        for txt in txt_lst:
            txt = txt.split(sep=' ')
            for w in txt:
                cl+=len(w)
                if cl >= t:
                    res=txt.index(w)
                    cl = 0
                    txt.insert(res, '<br>')
            new_lst.append(' '.join(txt))
            cl = 0

        return new_lst


    ## Creating figure
    fig = go.Figure()

    ## Adding bars to figure
    for col in dfx.columns:
        fig.add_trace(
            go.Bar(
                y=adding_breaks_to_text(dfx.index),
                x=dfx[col],
                name=col,
                orientation='h',
                text=dfx[col].astype(int),
                textposition='inside'
            )
        )

    ## Figure specifications
    fig.update_layout(
        height=1000,
        title='Atributos de la plataforma relevantes para los médicos',
        xaxis_title = 'Número de menciones',
        plot_bgcolor='rgb(255,255,255)'
    )


    # fig.show()
    return fig
