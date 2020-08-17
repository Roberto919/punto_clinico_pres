 ## ANALYZING TELEMEDICINE SURVEY RESULTS - DASHBOARD FILE
#### Author: Rob (GH: Roberto919)
#### Date: 21 July 2020
#### Content for the dashboard is based on the following source: https://www.notion.so/Estructura-y-contenido-de-la-presentaci-n-fa3a1f6130194586a360903cdf5efb3a





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries

import dash
import dash_core_components as dcc
import dash_html_components as html


## Ancillary modules

from TelemedSurvey_params import *
from TelemedSurvey_funcs import *





'------------------------------------------------------------------------------------------'
#################################
## Dashboard's main parameters ##
#################################

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}





'------------------------------------------------------------------------------------------'
######################
## Dashboard graphs ##
######################


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





'------------------------------------------------------------------------------------------'
############################
## Dashboard text content ##
############################


## Text for slide 2

#### Slide title
S2_title = '''
Resultados de la encuesta
'''

#### Text for results 1
S2_R1 = '''
Oportunidad para ofrecer una herramienta que inicie una tendencia
'''
txt_A1_A5 = '''
La opinión de los médicos acerca del uso de plataformas para la gestión de sus actividades y la realización de teleconsultas está dividida, pero es posible que esto se deba a que no han encontrado la herramienta adecuada.
'''
txt_A1 = '''
- Los resultados finales sí mostraron una diferencia por especialidad en el grado de aceptación de consultas médicas a distancia.
'''
txt_A5 = '''
- Con una adopción baja-media de la plataforma, podríamos lograr el objetivo inicial de lograr que los médicos den un mínimo de 6 teleconsultas al mes.
'''

#### Text for results 2
S2_R2 = '''
Mejorar las plataformas que actualmente usan los médicos
'''
txt_A3_A6 = '''
Los resultados de la encuesta sugieren que la baja adopción de herramientas tecnológicas por parte de los médicos pudiera representar un área de oportunidad interesante a explorar.
'''
txt_A3 = '''
- Muchos médicos ni siquiera reportan el uso de una plataforma de asistencia.
'''
txt_A6_1 = '''
- La mayoría de los médicos utilizan las herramientas/plataformas inadecuadas para el uso que le dan.
'''
txt_A6_2 = '''
- A pesar de que existen varias plataformas comerciales en el mercado, pocas de ellas fueron mencionadas por los médicos encuestados.
'''

#### Text for results 3
S2_R3 = '''
Funcionalidades que buscan los médicos
'''
txt_A7 = '''
La automatización/simplificación de tareas rutinarias es un gran área de oportunidad para agregar valor a los médicos.
'''





'------------------------------------------------------------------------------------------'
########################
## Creating dashboard ##
########################


## Coding layout of dashboard
def dashboard_layout():
    """
    Coding layout of dashboard
    """

    app.layout = html.Div(
        children=[


            # '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            ## Project title
            html.H1(
                children='Iniciativa de telemedicina',
                style={
                    'textAlign': 'center'
                }
            ),
            # '------------------------------------------------------------------------------'


            # '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            ## Slide title
            html.H2(
                children=S2_title,
                style={
                    'textAlign': 'center'
                }
            ),

            # ## Blanck space separator
            # html.Div(
            #     children='''
            #     '''
            # ),
            # '------------------------------------------------------------------------------'


            # '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            ## Results and message 1: oportunity to offer a tool that starts a trend


            #### Result title
            html.H3(
                children=S2_R1
            ),

            #### Result message
            html.H5(
                children=txt_A1_A5
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

                    ## Graph A5
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
            # '------------------------------------------------------------------------------'


            # '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            ## Results and message 2: improve tools currently used by doctors


            #### Result title
            html.H3(
                children=S2_R2
            ),

            #### Result message
            html.H5(
                children=txt_A3_A6
            ),

            #### Graphs

            ## Graph A1
            html.Div(
                children=[
                    dcc.Graph(
                        id='Gráfica análisis 3',
                        figure=fig_A3
                    ),
                    txt_A3
                ], className='six columns'
            ),

            ## Graph A5
            html.Div(
                children=[
                    dcc.Graph(
                        id='Gráfica análisis 6',
                        figure=fig_A6
                    ),
                    txt_A6_1,
                    txt_A6_2
                ], className='six columns'
            ),
            # '------------------------------------------------------------------------------'


            # '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            ## Results and message 3: automate routinary tasks


            #### Result title
            # html.H3(
            #     children=S2_R3
            # ),
            #
            # #### Result message
            # html.H5(
            #     children=txt_A7
            # ),

            #### Graphs

            ## Graph A7
            # html.Div(
            #     children=[
            #         dcc.Graph(
            #             id='Gráfica análisis 7',
            #             figure=fig_A7
            #         ),
            #     ], className='six columns'
            # ),
            # '------------------------------------------------------------------------------'





            # dcc.Markdown(
            #     children=txt_A1_A5
            # ),


        ]
    )


    ## Executing dashboard
    app.run_server(debug=True)
