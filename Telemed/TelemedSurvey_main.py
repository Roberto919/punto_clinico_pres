## ANALYZING TELEMEDICINE SURVEY RESULTS - MAIN FILE
#### Author: Rob (GH: Roberto919)
#### Date: 21 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import pandas as pd

import numpy as np

import pprint as pp

from datetime import *
from dateutil.relativedelta import relativedelta

from statistics import median, mean

import os

import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff

import dash
import dash_core_components as dcc
import dash_html_components as html


## Ancillary modules

from TelemedSurvey_params import *

from TelemedSurvey_funcs import *





'------------------------------------------------------------------------------------------'
#####################
## Main parameters ##
#####################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)





'------------------------------------------------------------------------------------------'
########################
## Content parameters ##
########################

txt_A1_A3 = '''
La opinión de los médicos acerca del uso de plataformas para la gestión de sus actividades y la realización de teleconsultas está dividida, pero es posible que esto se deba a que no han encontrado la herramienta adecuada.
'''

txt_A1 = '''
Los resultados finales sí mostraron una diferencia por especialidad en el grado de aceptación de consultas médicas a distancia.
'''

txt_A5 = '''
Con una adopción baja-media de la plataforma, podríamos lograr el objetivo inicial de lograr que los médicos den un mínimo de 6 teleconsultas al mes.
'''





'------------------------------------------------------------------------------------------'
#################
## Main script ##
#################


def main_script_func():


    ## Importing and cleaning dataset
    df = pd.read_csv(file_path)
    df = clean_raw_dataset(df)



    ## Data - analysis - General
    #### 1) Have you considered offering a telemedicine service
    dfx_A1 = A1_graph_data(df)
    fig_A1 = A1_graph(dfx_A1)

    #### 3) Do you have an electronic platform that enhances your service?
    dfx_A3 = A3_graph_data(df)
    fig_A3 = A3_graph(dfx_A3)

    #### 5) How regularly would you use the platform
    dfx_A5 = A5_graph_data(df)
    fig_A5 = A5_graph(dfx_A5)

    #### 6) What platforms do you currently use?
    dfx_A6 = A6_graph_data(df)
    fig_A6 = A6_graph(dfx_A6)

    #### 7) What are the attributes that you value the most in a platform?
    dfx_A7 = A7_graph_data(df)
    fig_A7 = A7_graph(dfx_A7)



    ## Creating dashboard
    app.layout = html.Div(
        children=[


            ## Project title
            html.H1(
                children='Iniciativa de telemedicina'
            ),


            ## Results for message 1: oportunity to offer a tool that starts a trend

            #### Main message
            html.Div(
                children=[
                    txt_A1_A3
                ]
            ),

            #### Graphs
            html.Div(
                children=[

                    ## Graph A1
                    html.Div(
                        children=[
                            dcc.Graph(
                                id='Gráfica análisis 1',
                                figure=fig_A1
                            ),
                            txt_A1
                        ], className='six columns'
                    ),

                    ## Graph A2
                    html.Div(
                        children=[
                            dcc.Graph(
                                id='Gráfica análisis 5',
                                figure=fig_A5
                            ),
                            txt_A5
                        ], className='six columns'
                    )
                ]
            ),





            # dcc.Markdown(
            #     children=txt_A1_A3
            # ),


        ]
    )





'------------------------------------------------------------------------------------------'
###########################
## Executing main script ##
###########################

if __name__ == '__main__':
    main_script_func()
    app.run_server(debug=True)
