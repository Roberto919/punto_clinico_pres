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
import lorem
import pathlib


## Ancillary modules

from TelemedSurvey_params import *
from TelemedSurvey_funcs import *





'------------------------------------------------------------------------------------------'
#################################
## Dashboard's main parameters ##
#################################


# Path
BASE_PATH = pathlib.Path(__file__).parent.resolve()
DATA_PATH = BASE_PATH.joinpath("Data").resolve()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__) #, external_stylesheets=external_stylesheets

server = app.server

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
def dashboard_layout_old():
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



## Coding layout based on multipage report
def dashboard_layout_new():
    """
    Coding layout of dashboard based on ploty example of multipage report
    """

    app.layout = html.Div(
        children=[
##'------------------------------------------------------------------------------------------'
            ## Slide 3.1 - Encuestas a médicos de la red de Chopo - Características de la encuesta
            html.Div(
                [
                    html.Div(
                        [   #### Encabezado de la página
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [   ####
                                                    # html.Div(
                                                    #     html.H5(""),
                                                    #     className="page-1a"
                                                    # ),
                                                    html.Div(
                                                        [
                                                            html.H5("Encuestas a médicos de la red de Chopo"),
                                                            html.H6("Características de la encuesta"),
                                                        ],
                                                        className="page-1b",
                                                    ),
                                                ],
                                                className="page-1c",
                                            )
                                        ],
                                        className="page-1d",
                                    ),
                                    html.Div(
                                        [
                                            html.H1(
                                                [
                                                    # html.Span("03", className="page-1e"),
                                                    # html.Span("19"),
                                                ]
                                            ),
                                            # html.H6("Suscipit nibh vita")
                                        ],
                                        className="page-1f",
                                    ),
                                ],
                                className="page-1g",
                            ),
                            #### Left part of the page -> Quesitons that were asked to the doctors
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6("1. ¿Ha considerado ofrecer teleconsultas?", className="page-1h"),
                                            html.P("Opción múltiple"),
                                            # html.P("    - Sí"),
                                            # html.P("    - No"),
                                        ],
                                        className="page-1i"
                                    ),
                                    html.Div(
                                        [
                                            html.H6("2. ¿Qué demanda espera de las teleconsultas?", className="page-1h"),
                                            html.P("Opción múltiple"),
                                            # html.P("    - 1: No será común"),
                                            # html.P("    - 2: Poco común"),
                                            # html.P("    - 3: Neutral"),
                                            # html.P("    - 4: Muy Común"),
                                            # html.P("    - 5: Totalmente Común"),
                                        ],
                                        className="page-1i"
                                    ),
                                    html.Div(
                                        [
                                            html.H6("3. ¿Cuenta con alguna plataforma de gestón? ¿Qué plataforma?", className="page-1h"),
                                            html.P("Opción binaria y pregunta abierta"),
                                            # html.P("    - Sí"),
                                            # html.P("    - No"),
                                            # html.P("    - Especificar la plataforma"),
                                        ],
                                        className="page-1i"
                                    ),
                                    html.Div(
                                        [
                                            html.H6("4. ¿Cuenta con alguna plataforma de teleconsultas? ¿Qué plataforma?", className="page-1h"),
                                            html.P("Opción binaria y pregunta abierta"),
                                            # html.P("    - Sí"),
                                            # html.P("    - No"),
                                            # html.P("    - Especificar la plataforma"),
                                        ],
                                        className="page-1i"
                                    ),
                                    html.Div(
                                        [
                                            html.H6("5. ¿Qué funcionalidades quisiera tener en una plataforma?", className="page-1h"),
                                            html.P("Opción múltiple y pregunta abierta"),
                                            # html.P("    - Administración de citas"),
                                            # html.P("    - Aplicación de promociones de descuento para clientes"),
                                            # html.P("    - Creación automática de videoconferencias con clientes para teleconsultas"),
                                            # html.P("    - Despliegue de encuestas de satisfacción de clientes"),
                                            # html.P("    - Envío y recepción de documentos con cliente (e.g. resultados de estudios, recetas médicas)"),
                                            # html.P("    - Especificar cualquier otra"),
                                        ],
                                        className="page-1i"
                                    ),
                                    html.Div(
                                        [
                                            html.H6("6. ¿Qué tanta disposición tiene por pagar por una plataforma de gestión y teleconsultas?", className="page-1h"),
                                            html.P("Opción múltiple"),
                                            # html.P("    - No pagaría por una"),
                                            # html.P("    - Menos de $100"),
                                            # html.P("    - Menos de $750"),
                                            # html.P("    - Más de $750"),
                                        ],
                                        className="page-1i"
                                    ),
                                    html.Div(
                                        [
                                            html.H6("7. ¿Qué tan regular sería el uso de su plataforma?", className="page-1h"),
                                            html.P("Opción múltiple"),
                                            # html.P("    - 1: No la utilizaría"),
                                            # html.P("    - 2: Con poca regularidad"),
                                            # html.P("    - 3: Neutral"),
                                            # html.P("    - 4: Con cierta regularidad"),
                                            # html.P("    - 5: Regularmente")
                                        ],
                                        className="page-1i",
                                    ),
                                ],
                                className="page-1j"
                            ),
                            #### Right part of the page -> survey summary
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H6(
                                                "Médicos internistas",
                                                className="page-1h"
                                            ),
                                            html.P(" "),
                                            html.P("- En base de contactos: 3,703"),
                                            html.P("- Con permiso para recibir publicidad: 882"),
                                            html.P("- Número de encuestas objetivo: 300"),
                                            html.P("- Número de encuestas respondidas: 577"),
                                        ],
                                        className="page-1k"
                                    ),
                                    html.Div(
                                        [
                                            html.H6(
                                                "Médicos endocrinólogos",
                                                className="page-1h"
                                            ),
                                            html.P(" "),
                                            html.P("- En base de contactos: 669"),
                                            html.P("- Con permiso para recibir publicidad: 177"),
                                            html.P("- Número de encuestas objetivo: 230"),
                                            html.P("- Número de encuestas respondidas: 188"),
                                        ],
                                        className="page-1l"
                                    ),
                                    html.Div(
                                        [
                                            html.H6(
                                                "Ambos",
                                                className="page-1h"
                                            ),
                                            html.P(" "),
                                            html.P("- En base de contactos: 4,372"),
                                            html.P("- Con permiso para recibir publicidad: 1,059"),
                                            html.P("- Número de encuestas objetivo: 530"),
                                            html.P("- Número de encuestas respondidas: 765"),
                                        ],
                                        className="page-1m"
                                    ),
                                ],
                                className="page-1n",
                            ),
                        ],
                        className="subpage"
                    )
                ],
                className="page"
            ),
#'------------------------------------------------------------------------------------------------------------------------'
            ## Slide 3.2.1 - Encuestas a médicos de la red de Chopo - Resultados de la encuesta - Oportunidad para ofrecer una herramienta que inicie una tendencia
            html.Div(
                [
                    html.Div(
                        [
                            #### Encabezado de la página
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [   ####
                                                    # html.Div(
                                                    #     html.H5(""),
                                                    #     className="page-1a"
                                                    # ),
                                                    html.Div(
                                                        [
                                                            html.H5("Encuestas a médicos de la red de Chopo"),
                                                            html.H6("Resultados de la encuesta"),
                                                            # html.H6("Sapo"),
                                                        ],
                                                        className="page-1b",
                                                    ),
                                                ],
                                                className="page-1c",
                                            )
                                        ],
                                        className="page-1d",
                                    ),
                                    html.Div(
                                        [
                                            html.H1(
                                                [
                                                    # html.Span("03", className="page-1e"),
                                                    # html.Span("19"),
                                                ]
                                            ),
                                            # html.H6("Suscipit nibh vita")
                                        ],
                                        className="page-1f",
                                    ),
                                ],
                                className="page-1g",
                            ),
                            #### Gráficas horizontales
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "La opinión de los médicos acerca del uso de plataformas para la gestión de sus actividades y la realización de teleconsultas está dividida, pero es posible que esto se deba a que no han encontrado la herramienta adecuada.",
                                                        className="page-3h"
                                                    ),
                                                    html.Div(
                                                        [
                                                            dcc.Graph(
                                                                id="Gráfica 1 (A1)",
                                                                figure=fig_A1
                                                            )
                                                        ]
                                                    ),
                                                    html.P(
                                                        "Los resultados finales sí mostraron una diferencia por especialidad en el grado de aceptación de consultas médicas a distancia.",
                                                        className="page-3k"
                                                    ),
                                                ],
                                                className="thirdPage first row",
                                            )
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            dcc.Graph(
                                                                id="Gráfica 2 (A5)",
                                                                figure=fig_A5
                                                            )
                                                        ]
                                                    ),
                                                    html.P(
                                                        "Con una adopción baja-media de la plataforma, podríamos lograr el objetivo inicial de lograr que los médicos den un mínimo de 6 teleconsultas al mes.",
                                                        className="page-3k"
                                                    ),
                                                ],
                                                className="thirdPage first row",
                                            )
                                        ]
                                    ),
                                ]
                            )
                        ],
                        className="subpage"
                    )
                ],
                className="page"
            ),
#'------------------------------------------------------------------------------------------------------------------------'
            ## Slide 3.2.2 - Encuestas a médicos de la red de Chopo - Resultados de la encuesta - Mejorar las plataformas que actualmente usan los médicos
            html.Div(
                [
                    html.Div(
                        [
                            #### Encabezado de la página
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [   ####
                                                    # html.Div(
                                                    #     html.H5(""),
                                                    #     className="page-1a"
                                                    # ),
                                                    html.Div(
                                                        [
                                                            html.H5("Encuestas a médicos de la red de Chopo"),
                                                            html.H6("Resultados de la encuesta"),
                                                            # html.H6("Sapo"),
                                                        ],
                                                        className="page-1b",
                                                    ),
                                                ],
                                                className="page-1c",
                                            )
                                        ],
                                        className="page-1d",
                                    ),
                                    html.Div(
                                        [
                                            html.H1(
                                                [
                                                    # html.Span("03", className="page-1e"),
                                                    # html.Span("19"),
                                                ]
                                            ),
                                            # html.H6("Suscipit nibh vita")
                                        ],
                                        className="page-1f",
                                    ),
                                ],
                                className="page-1g",
                            ),
                            #### Main findings
                            html.Div(
                                [
                                    html.Strong(
                                        "Los resultados de la encuesta sugieren que la baja adopción de herramientas tecnológicas por parte de los médicos pudiera representar un área de oportunidad interesante a explorar.",
                                        className="page-3h"
                                    )
                                ]
                            ),
                            ####
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Texto 1",
                                                        className="page-3h"
                                                    )
                                                ]
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Texto 2",
                                                        className="page-3h"
                                                    )
                                                ]
                                            ),
                                        ],
                                        className="title six columns"
                                    ),
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Texto 3",
                                                        className="page-3h"
                                                    )
                                                ]
                                            ),
                                            html.Div(
                                                [
                                                    html.Strong(
                                                        "Texto 4",
                                                        className="page-3h"
                                                    )
                                                ]
                                            ),
                                        ]
                                    ),
                                ]
                            )
                        ],
                        className="subpage"
                    )
                ],
                className="page"
            ),
#'------------------------------------------------------------------------------------------------------------------------'
        ]
    )



    ## Executing dashboard
    app.run_server(debug=True)
