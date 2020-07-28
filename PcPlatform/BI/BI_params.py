## ANALYZING BUSINESS DATA - PARAMETERS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 20 July 2020





'------------------------------------------------------------------------------------------'
#####################
## Base parameters ##
#####################


## Data
data_loc = 'Data/20200723'
sales_data = 'LISTADELASVENTAS.csv'
appointment_data = 'LISTADETALLADADELASCITAS.csv'






'------------------------------------------------------------------------------------------'
#####################
## Data parameters ##
#####################


## General data

meds_dict_ref = {
 'ARROYO COUTIÑO, IBER': {'Especialidad': ['UROLOGIA'],
                           'Sitios': ['Punto Clínico- Coapa']},
 'ASCENCIO BARRIENTOS, CARLOS NORBERTO': {'Especialidad': ['GASTROENTEROLOGIA'],
                                          'Sitios': ['Punto Clinico- Marina',
                                                     'Punto Clínico- Basílica',
                                                     'LABORATORIO- Basílica']},
 'CHAYA SALGADO, SAID': {'Especialidad': ['DERMATOLOGIA'],
                         'Sitios': ['Punto Clinico- Marina',
                                    'LABORATORIO- Marina']},
 'CITALAN PROJ, HARRY WILLIAM': {'Especialidad': ['GASTROENTEROLOGIA'],
                                 'Sitios': ['Punto Clínico- Coapa']},
 'ENRIQUEZ ROMAN, ARLETTE': {'Especialidad': ['ENDOCRINOLOGIA'],
                             'Sitios': ['Punto Clínico- Basílica',
                                        'Punto Clinico- Marina',
                                        'LABORATORIO- Marina',
                                        'LABORATORIO- Basílica']},
 'ERAZO PEREZ, LUSVI LUDGARDIZ': {'Especialidad': ['NEUMOLOGIA'],
                                  'Sitios': ['Punto Clínico- Coapa',
                                             'LABORATORIO- Coapa']},
 'FRANCO ESTRADA, SILVIA': {'Especialidad': ['GASTROENTEROLOGIA'],
                            'Sitios': ['Punto Clinico- Marina',
                                       'Punto Clínico- Basílica']},
 'GARCIA CRUZ, LILIANA ESTHER': {'Especialidad': ['GINECOLOGIA'],
                                 'Sitios': ['Punto Clínico- Basílica',
                                            'LABORATORIO- Basílica']},
 'GOMEZ GARCIA, THALIA STEPHANIE': {'Especialidad': ['GASTROENTEROLOGIA'],
                                     'Sitios': ['Punto Clínico- Coapa',
                                                'Punto Clinico- Marina']},
 'GOMEZ, ANTONY OMAR': {'Especialidad': ['GINECOLOGIA',
                                         'MEDICINA GENERAL',
                                         'OTROS',
                                         'ENDOCRINOLOGIA',
                                         'GASTROENTEROLOGIA',
                                         'DERMATOLOGIA',
                                         'OTORRINOLARINGOLOGIA'],
                        'Sitios': ['Punto Clinico- Marina',
                                   'Punto Clínico- Coapa',
                                   'LABORATORIO- Marina']},
 'HERNANDEZ MARTINEZ, ORLANDO JOSE': {'Especialidad': ['UROLOGIA'],
                                      'Sitios': ['Punto Clinico- Marina',
                                                 'Punto Clínico- Basílica']},
 'HERNANDEZ SOTO, TAYMI': {'Especialidad': ['GINECOLOGIA'],
                           'Sitios': ['Punto Clinico- Marina',
                                      'Punto Clínico- Basílica',
                                      'LABORATORIO- Basílica']},
 'HERNANDEZ, YASELIN': {'Especialidad': ['OTROS'],
                        'Sitios': ['Punto Clínico- Basílica']},
 'IBARRA SALCE, RAUL': {'Especialidad': ['ENDOCRINOLOGIA'],
                         'Sitios': ['Punto Clinico- Marina']},
 'JAIME LEAL, OMAR': {'Especialidad': ['GASTROENTEROLOGIA'],
                       'Sitios': ['Punto Clinico- Marina']},
 'JUAREZ HERRERA, NORMA': {'Especialidad': ['DERMATOLOGIA'],
                           'Sitios': ['Punto Clínico- Coapa',
                                      'Punto Clínico- Basílica',
                                      'Punto Clinico- Marina',
                                      'LABORATORIO- Coapa']},
 'MARTINEZ CORONA, MARICELA': {'Especialidad': ['ENDOCRINOLOGIA'],
                               'Sitios': ['Punto Clinico- Marina']},
 'MONTERO MARQUEZ , MIGUEL ANGEL': {'Especialidad': ['OTORRINOLARINGOLOGIA'],
                                     'Sitios': ['Punto Clínico- Coapa']},
 'N\\A': {'Especialidad': ['OTROS',
                           'UROLOGIA',
                           'GINECOLOGIA',
                           'GASTROENTEROLOGIA',
                           'ALERGOLOGIA',
                           'PEDIATRIA',
                           'DERMATOLOGIA',
                           'MEDICINA GENERAL',
                           'ENDOCRINOLOGIA'],
          'Sitios': ['Punto Clínico- Basílica',
                     'Punto Clinico- Marina',
                     'Punto Clínico- Coapa']},
 'PAGAZA RAMIREZ, RUBEN': {'Especialidad': ['MEDICINA GENERAL',
                                             'OTROS',
                                             'GINECOLOGIA'],
                            'Sitios': ['Punto Clínico- Basílica']},
 'PEREZ RIOS, BERTHA LUCIA': {'Especialidad': ['DERMATOLOGIA'],
                              'Sitios': ['Punto Clínico- Basílica',
                                         'Punto Clinico- Marina']},
 'PIEDRAS PONCE, GUADALUPE MONSERRAT': {'Especialidad': ['NUTRICION'],
                                        'Sitios': ['Punto Clínico- Basílica',
                                                   'Punto Clinico- Marina',
                                                   'LABORATORIO- Basílica']},
 'RANGEL BISTRAIN , JULIAN ALEJANDRO': {'Especialidad': ['UROLOGIA'],
                                         'Sitios': ['Punto Clínico- Basílica',
                                                    'Punto Clinico- Marina',
                                                    'LABORATORIO- Basílica']},
 'RUELAS GONZALEZ, SANDRA': {'Especialidad': ['DERMATOLOGIA'],
                             'Sitios': ['Punto Clínico- Basílica',
                                        'Punto Clinico- Marina',
                                        'LABORATORIO- Basílica']},
 'RUIZ RANGEL, PAOLA': {'Especialidad': ['ENDOCRINOLOGIA'],
                        'Sitios': ['Punto Clínico- Basílica',
                                   'Punto Clínico- Coapa']},
 'SALGADO PARRA  CED. ESP. 11502236, ERIKA GUADALUPE': {'Especialidad': ['GASTROENTEROLOGIA'],
                                                        'Sitios': ['Punto '
                                                                   'Clínico- '
                                                                   'Basílica',
                                                                   'Punto '
                                                                   'Clinico- '
                                                                   'Marina',
                                                                   'LABORATORIO- '
                                                                   'Basílica']},
 'SILVA SERRANO, JUANITA': {'Especialidad': ['ENDOCRINOLOGIA'],
                             'Sitios': ['Punto Clínico- Coapa',
                                        'Punto Clinico- Marina']},
 'TREJO GONZALEZ, NORMA PATRICIA': {'Especialidad': ['GINECOLOGIA'],
                                    'Sitios': ['Punto Clínico- Coapa']},
 'TUTT GONZALEZ, GIOVANNA': {'Especialidad': ['OTROS'],
                             'Sitios': ['Punto Clinico- Marina']},
 'VAZQUEZ GALLARDO, GRISEL': {'Especialidad': ['GINECOLOGIA',
                                               'OTROS',
                                               'UROLOGIA'],
                              'Sitios': ['Punto Clínico- Coapa',
                                         'Punto Clinico- Marina']},
 'VILLALOBOS BENITEZ, OSBERT': {'Especialidad': ['DERMATOLOGIA'],
                                 'Sitios': ['Punto Clínico- Coapa',
                                            'Punto Clínico- Basílica']},
 'VIÑALS RODRIGUEZ, IALA LAURA': {'Especialidad': ['GINECOLOGIA'],
                                  'Sitios': ['Punto Clinico- Marina',
                                             'Punto Clínico- Coapa']},
 'ZAMORA GARCIA, ALBERTO': {'Especialidad': ['CARDIOLOGIA'],
                             'Sitios': ['Punto Clínico- Coapa']},
 'ARRIOLA ZAMARRIPA, MANUEL DE JESUS': {'Especialidad': ['GINECOLOGIA'],
                                        'Sitios': ['Punto Clínico- Basílica']},
 'CADENA OBANDO, DIEGO ANDRES': {'Especialidad': ['ENDOCRINOLOGIA'],
                                 'Sitios': ['Punto Clínico- Basílica',
                                            'LABORATORIO- Basílica']},
 'CANO CONTRERAS, ANA DELFINA': {'Especialidad': ['GASTROENTEROLOGIA'],
                                 'Sitios': ['Punto Clínico- Basílica',
                                            'Punto Clínico- Coapa',
                                            'LABORATORIO- Coapa',
                                            'Punto Clinico- Marina']},
 'ESCOBAR VALDIVIA, EMMANUEL JESUS': {'Especialidad': ['UROLOGIA'],
                                      'Sitios': ['Punto Clínico- Coapa']},
 'GOMEZ GARCIA, THALIA STEPHANIE': {'Especialidad': ['GASTROENTEROLOGIA'],
                                    'Sitios': ['Punto Clínico- Coapa',
                                               'LABORATORIO- Coapa',
                                               'Punto Clinico- Marina']},
 'MONTERO MARQUEZ , MIGUEL ANGEL': {'Especialidad': ['OTORRINOLARINGOLOGIA'],
                                    'Sitios': ['Punto Clínico- Coapa']},
 'OCHOA, JESSICA': {'Especialidad': ['OTROS'],
                    'Sitios': ['Punto Clinico- Marina']},
 'SUPPORT      , MEDFAR': {'Especialidad': ['OTROS', 'GINECOLOGIA', 'UROLOGIA'],
                           'Sitios': ['Punto Clinico- Marina',
                                      'Punto Clínico- Basílica']},
 'ZAMORA GARCIA, ALBERTO': {'Especialidad': ['CARDIOLOGIA'],
                            'Sitios': ['Punto Clínico- Coapa']}

                             }


## Appointments data

rc = [
    'FECHA',
    'ESTADO DE LA CITA',
    'ASUNTO',
    'NOMBRE DEL CLÍNICO',
    'TÍTULO',
    'SITIO'
]

specialties_ref = {
    'GINECOLOGIA': [
        'GINECOLOGIA',
        'ENDOVAGINAL',
        'TRANSVAGINAL',
        'GINECO'
        ],
    'DERMATOLOGIA': [
        'DERMATOLOGIA'
        ],
    'UROLOGIA': [
        'UROLOGIA'
        ],
    'PEDIATRIA': [
        'PEDIATRIA',
        ],
    'ENDOCRINOLOGIA': [
        'ENDOCRINOLOGIA',
        'TIROIDEO',
        'TIROIDES'
        ],
    'OTORRINOLARINGOLOGIA': [
        'OTORRINOLARINGOLOGIA',
        ],
    'GASTROENTEROLOGIA': [
        'GASTROENTEROLOGIA',
        'GASTROENTEROLGIA'
        ],
    'MEDICINA GENERAL': [
        'MEDICINA GENERAL'
        ],
    'NEUMOLOGIA': [
        'NEUMOLOGIA'
        ],
    'CARDIOLOGIA': [
        'CARDIOLOGIA'
        ],
    'NUTRICION': [
        'NUTRICION'
        ],
    'ALERGOLOGIA': [
        'ALERGOLOGIA'
        ]
}


## Treshold to eliminate specialties
sp_tsh = 0.025
