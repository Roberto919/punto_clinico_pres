## ANALYZING BUSINESS DATA - PARAMETERS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 20 July 2020





'------------------------------------------------------------------------------------------'
#####################
## Base parameters ##
#####################


## Data

#### Myle
data_loc = 'Data/20200901'
sales_data = 'GenerateBillingCSVRequest.csv'
appointment_data = 'LISTADETALLADADELASCITAS.csv'

#### Pharmacy
# data_loc = 'Data/20200908'
# sales_basilica = 'Historico_Ventas_Basilica.xlsx'
# appointment_data = 'LISTADETALLADADELASCITAS.csv'




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
 'GOMEZ, ANTONY OMAR': {'Especialidad': ['MEDICINA GENERAL'],
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
 'HERNANDEZ, YASELIN': {'Especialidad': ['OTRA_ESP'],
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
 'N\\A': {'Especialidad': ['OTRA_ESP',
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
                                             'OTRA_ESP',
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
 'TUTT GONZALEZ, GIOVANNA': {'Especialidad': ['OTRA_ESP'],
                             'Sitios': ['Punto Clinico- Marina']},
 'VAZQUEZ GALLARDO, GRISEL': {'Especialidad': ['GINECOLOGIA',
                                               'OTRA_ESP',
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
 'OCHOA, JESSICA': {'Especialidad': ['OTRA_ESP'],
                    'Sitios': ['Punto Clinico- Marina']},
 'SUPPORT      , MEDFAR': {'Especialidad': ['OTRA_ESP', 'GINECOLOGIA', 'UROLOGIA'],
                           'Sitios': ['Punto Clinico- Marina',
                                      'Punto Clínico- Basílica']},
 'ZAMORA GARCIA, ALBERTO': {'Especialidad': ['CARDIOLOGIA'],
                            'Sitios': ['Punto Clínico- Coapa']},
 'MARCANO PILLKAHN, JOHANNA CAROLINA': {'Especialidad': ['GASTROENTEROLOGIA'],
                            'Sitios': ['?']},
 'BURGOS ROJO CED. ESP. 11249003, OLIVIA QUETZALLI': {'Especialidad': ['GINECOLOGIA'],
                            'Sitios': ['?']},
 'BUSTILLO DEL CUETO, EDUARDO': {'Especialidad': ['PEDIATRIA'],
                            'Sitios': ['?']},
 'AVENDAÑO PEREZ, AURIA VIRIDIANA': {'Especialidad': ['GINECOLOGIA'],
                            'Sitios': ['?']},
                             }


specialties_ref = {
    'GINECOLOGIA': [
        'GINECOLOGIA',
        'ENDOVAGINAL',
        'TRANSVAGINAL',
        'GINECO',
        'CERVIX',
        'VAGIN',
        'DIU',
        "OBSTETRIC",
        "EMBARAZ",
        "PROLACTIN",
        "COLPOSCOPIA",
        "PAPANICOLAOU"
        ],
    'DERMATOLOGIA': [
        'DERMATOLOGIA'
        ],
    'UROLOGIA': [
        'UROLOGIA',
        'PROST',
        "RENAL",
        "PENESCOPIA",
        "ANDROSCOPIA"
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
        'OTORRINOLARINGO',
        "CERUMEN"
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
        ],
    'NEUROLOGIA': [
        'NEUROLOG'
        ],
    'PROCTOLOGIA': [
        'PROCTOLOG'
        ],
}


locations_ref = {
    'BASILICA': [
        'LABORATORIO- Basílica',
        'Punto Clínico- Basílica'
    ],
    'COAPA': [
        'LABORATORIO- Coapa',
        'Punto Clínico- Coapa'
    ],
    'MARINA': [
        'LABORATORIO- Marina',
        'Punto Clinico- Marina'
    ]
}


business_line_ref = {
    "CONSULTA": [
        "CONSULTA MEDICA",
        "CONSULTA ESPECIALISTA",
        "CONSULTA DE",
        "CONSULTA MEDICINA GENERAL",
        "CONSULTA GENERAL",
        "OTORRINOLARINGOLOGIA",
        "CARDIOLOGIA",
        "TELECONSULTA",
        "DIETA",
        "REVISION"
    ],
    "LABORATORIO": [
        "CHECK UP",
        "PERFIL TIROIDEO",
        "BIOMETRIA HEMATICA",
        "QUIMICA DE",
        "HEMOGLOBINA",
        "INSULINA",
        "CULTIVO",
        "EXAMEN",
        "PRUEBA",
        "COPROCULTIVO",
        "AMILASA",
        "VDRL",
        "AMIBA",
        "HORMONA",
        "WINTROBE",
        "GLUCOSA",
        "PROLACTINA",
        "TIEMPO DE",
        "PERFIL",
        "GRUPO SANGUINEO",
        "VIRUS INMUNODEFICIENCIA",
        "HIV",
        "CITOLOGIA",
        "ANTICUERPOS",
        "ANTIGENO",
        "PROGESTERONA",
        "DEHIDROEPIANDROSTERONA",
        "TRANSAMINASA"
    ],
    "ULTRASONIDO": [
        "ULTRASON"
    ],
    "PROCEDIMIENTOS": [
        "ELECTROFULGURACION",
        "COLPOSCOPIA",
        "PAPANICOLAOU",
        "RASTREO",
        "INFOGRAFIA",
        "BIOPSIA",
        "BIOPISA",
        "APLICACION DE",
        "TOMA",
        "RETIRO",
        "EXTRACCCION",
        "INSERCION",
        "ENVIADO A",
        "CRIOTERAPIA",
        "SCOPIA",
        "CIRUGIA",
        "INYECCION",
        "ELECTROCARDIOGRAMA",
        "EKG",
        "ESFEROLISIS",
        "CURACION",
        "VERRUGA"
    ]
}





'------------------------------------------------------------------------------------------'
##################################
## Appointments data parameters ##
##################################

rca = [
    'FECHA',
    'ESTADO DE LA CITA',
    'ASUNTO',
    'NOMBRE DEL CLÍNICO',
    'TÍTULO',
    'SITIO'
]


## Treshold to eliminate specialties
sp_tsh = 0.025





'------------------------------------------------------------------------------------------'
###########################
## Sales data parameters ##
###########################

rcs = [
    'State',
    'BillDate',
    'Provider',
    'SiteInfo',
    'PaymentMethod',
    'BilledBy',
    'DescriptionES',
    'Quantity',
    'UnitPrice',
    'Total'
]
