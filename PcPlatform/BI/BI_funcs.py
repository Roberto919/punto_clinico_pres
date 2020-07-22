## ANALYZING BUSINESS DATA - FUNCTIONS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 20 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import pandas as pd

import re

from datetime import *

import plotly.graph_objects as go


## Ancillary modules

from BI_params import *





'------------------------------------------------------------------------------------------'
#######################
## Generic functions ##
#######################


## Function to add week number as string
def add_week_num(row):
    """
    Function to add week number as string
    """

    week_num = str(datetime.isocalendar(row)[1])

    if len(week_num) == 2:
        res = str(datetime.isocalendar(row)[0]) + '-' + week_num
    else:
        res = str(datetime.isocalendar(row)[0]) + '-' + '0' + week_num

    return res





'------------------------------------------------------------------------------------------'
#####################################################
## Data analysis - Appointments - Cleaning main df ##
#####################################################


## Cleaning imported dataframes - Appointments dataframe
def dfa_clean(dfa):
    """
    Cleaning imported dataframes - Appointments dataframe
    """


    ## Function to clean ASUNTO column
    """
    Function to clean ASUNTO column
    """
    def Asunto_synth(row):

        res = 0

        for sp in specialties_ref:
            for sp_t in specialties_ref[sp]:
                if sp_t in row:
                    res = sp
                    break

        if res == 0:
            res = 'OTROS'
            # res = row

        return res


    ## Eliminating non relevant columns
    nrc = [col for col in dfa.columns if col not in rc]
    dfa.drop(nrc, axis=1, inplace=True)


    ## Parsing date
    dfa['FECHA'] = pd.to_datetime(dfa['FECHA'], format='%Y-%m-%d')


    ## Cleaning entries in columns ASUNTO and NOMBRE DEL CLÍNICO
    c_cols = ['ASUNTO', 'NOMBRE DEL CLÍNICO']
    dfa.loc[:, c_cols] = dfa.loc[:, c_cols].fillna('NO_INFO')
    for col in c_cols:

        dfa[col] = dfa[col].str.upper()

        ccf = [
            lambda x: re.sub('Á', 'A', x),
            lambda x: re.sub('É', 'E', x),
            lambda x: re.sub('Í', 'I', x),
            lambda x: re.sub('Ó', 'O', x),
            lambda x: re.sub('Ú', 'U', x),
        ]

        for fun in ccf:
            dfa[col] = dfa[col].apply(fun)


    ## Clean ASUNTO column
    dfa['ASUNTO_sinth'] = dfa['ASUNTO'].apply(Asunto_synth)


    ## Eliminating entries with appointment status different from "Completada"
    m1 = dfa['ESTADO DE LA CITA'] == 'Completada'
    dfa = dfa.loc[m1, :]


    ## Adding index column
    dfa.insert(0, '#', range(1, dfa.shape[0] + 1))


    ## Adding week number as string
    dfa['Week_num'] = dfa.loc[:, 'FECHA'].apply(add_week_num)


    return dfa





'------------------------------------------------------------------------------------------'
###############################################
## Data analysis - Appointments - Analysis 1 ##
###############################################


## Creating dataframe with sum of appoitments per week per speciality
def count_appointments_specialities(dfa):
    """
    Creating dataframe with sum of appoitments per week per speciality
    """


    ## Eliminating from analysis specialities that account for a participation smaller that the set treshold
    def selecting_sps_over_treshold(dfax):

        dfx = dfax.copy()

        dfx.loc['Sum', :] = dfx.sum()

        all_sum = dfx.loc['Sum', :].sum()

        dfx.loc['Part_sum', :] = dfx.loc['Sum', :]/all_sum

        rc_sps = [col for col in dfx.columns if dfx.loc['Part_sum', col] > sp_tsh]

        return rc_sps



    dfax = dfa.copy()


    ## Leaving only relevant columns
    rc = [
        '#',
        'Week_num',
        'ASUNTO_sinth'
    ]
    dfax.drop([nrc for nrc in dfax.columns if nrc not in rc], axis=1, inplace=True)


    ## Counting appointments and filling Null values
    dfax = dfax.groupby(['Week_num', 'ASUNTO_sinth']).count().unstack().fillna('0')
    dfax.columns = dfax.columns.droplevel()
    # print(dfax)
    # dfax.drop('(#, OTROS)', axis=1, inplace=True)


    ## Eliminating from analysis specialities that account for a participation smaller that the set treshold
    rc_sps = selecting_sps_over_treshold(dfax)
    dfax.drop([nrc for nrc in dfax.columns if nrc not in rc_sps], axis=1, inplace=True)


    return dfax



## Display bar graph with count of all confirmed appointments per week per speciality
def analysis_1_graph(dfax):

    ## x-axis
    x_axis = list(dfax.index.unique())

    ## Bars
    sps = dfax.columns

    ## Create and display graph
    fig = go.Figure(data=
                    [go.Bar(name=sp, x=x_axis, y=dfax[sp]) for sp in sps]
                   )

    fig.update_layout(
        title = 'Conteo de citas confirmadas por especialidad',
        xaxis_title = 'Semana',
        yaxis_title = 'Número de citas',
        barmode='group',
        autosize=False,
        width=1500,
        height=500
    )
    fig.update_xaxes(type="category")

    fig.show()
