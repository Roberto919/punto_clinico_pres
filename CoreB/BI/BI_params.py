## ANALYZING BUSINESS DATA - PARAMETERS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 20 July 2020





'------------------------------------------------------------------------------------------'
#####################
## Base parameters ##
#####################


## Data

#### Myle
data_loc = 'Data/20200922'
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

colabs_dict_ref = {
    "ALVARADO, JULIETA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "ANAYA, VERONICA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "ARRIOLA ZAMARRIPA, MANUEL DE JESUS": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "ARROYO COUTIÑO, IBER": {
        "Medico_activo": False,
        "Especialidad": [
            "UROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "ASCENCIO BARRIENTOS, CARLOS NORBERTO": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina",
            "Punto Clínico- Basílica",
            "LABORATORIO- Basílica"
        ]
    },
    "AVENDAÑO PEREZ, AURIA VIRIDIANA": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "AYALA PEREYRO, CINTHYA GUADALUPE": {
        "Medico_activo": False,
        "Especialidad": [
            "MEDICINA GENERAL"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "BURGOS ROJO CED. ESP. 11249003, OLIVIA QUETZALLI": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "BUSTILLO DEL CUETO, EDUARDO": {
        "Medico_activo": False,
        "Especialidad": [
            "PEDIATRIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina"
        ]
    },
    "CADENA OBANDO, DIEGO ANDRES": {
        "Medico_activo": False,
        "Especialidad": [
            "ENDOCRINOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "LABORATORIO- Basílica"
        ]
    },
    "CANO CONTRERAS, ANA DELFINA": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clínico- Coapa",
            "LABORATORIO- Coapa",
            "Punto Clinico- Marina"
        ]
    },
    "CASTILLON BENAVIDES, NIDIA KAREN": {
        "Medico_activo": False,
        "Especialidad": [
            "ALERGOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "CATALAN SANTOS, SILVIA": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "CEPEDA, MONICA": {
        "Medico_activo": False,
        "Especialidad": [
            "MEDICINA GENERAL"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "CHAYA SALGADO, SAID": {
        "Medico_activo": False,
        "Especialidad": [
            "DERMATOLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina",
            "LABORATORIO- Marina"
        ]
    },
    "CHIRINOS RAMOS, JOCELIN VIVIANA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "CITALAN PROJ, HARRY WILLIAM": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "CORNEJO ROSALES, ERIKA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "DE LA TORRE TRUEBA, DULCE MARIA": {
        "Medico_activo": True,
        "Especialidad": [
            "DERMATOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "ENRIQUEZ ROMAN, ARLETTE": {
        "Medico_activo": False,
        "Especialidad": [
            "ENDOCRINOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina",
            "LABORATORIO- Marina",
            "LABORATORIO- Basílica"
        ]
    },
    "ERAZO PEREZ, LUSVI LUDGARDIZ": {
        "Medico_activo": False,
        "Especialidad": [
            "NEUMOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa",
            "LABORATORIO- Coapa"
        ]
    },
    "ESCOBAR VALDIVIA, EMMANUEL JESUS": {
        "Medico_activo": False,
        "Especialidad": [
            "UROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "ESPINOZA CHOQUE, ROSELENNY": {
        "Medico_activo": True,
        "Especialidad": [
            "NEFROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "FRANCO ESTRADA, SILVIA": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina",
            "Punto Clínico- Basílica"
        ]
    },
    "FREIRE GUFFANTI, JUAN CARLOS": {
        "Medico_activo": False,
        "Especialidad": [
            "UROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "GALINDO VILLARREAL , DOLORES MARYSOL": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "GARCIA CRUZ, LILIANA ESTHER": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "LABORATORIO- Basílica"
        ]
    },
    "GARCIA LOZADA, MARISOL": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "GARCIA MARTINEZ, ESTELA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "GOMEZ GARCIA, THALIA STEPHANIE": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa",
            "LABORATORIO- Coapa",
            "Punto Clinico- Marina"
        ]
    },
    "GOMEZ, ANTONY OMAR": {
        "Medico_activo": True,
        "Especialidad": [
            "MEDICINA GENERAL"
        ],
        "Sitios": [
            "Punto Clinico- Marina"
        ]
    },
    "GONZALEZ SANDOVAL, ALMA VERONICA": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina"
        ]
    },
    "GUEMES QUINTO, AGUSTIN": {
        "Medico_activo": True,
        "Especialidad": [
            "PROCTOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "GUTIERREZ ZAMORA , JULIETA": {
        "Medico_activo": True,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "HERNANDEZ MARTINEZ, ORLANDO JOSE": {
        "Medico_activo": False,
        "Especialidad": [
            "UROLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina",
            "Punto Clínico- Basílica"
        ]
    },
    "HERNANDEZ SOTO, TAYMI": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina",
            "Punto Clínico- Basílica",
            "LABORATORIO- Basílica"
        ]
    },
    "HERNANDEZ, YASELIN": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "HERRERA PALMA, MARISOL": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "IBARRA SALCE, RAUL": {
        "Medico_activo": False,
        "Especialidad": [
            "ENDOCRINOLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina"
        ]
    },
    "ISLAS DE LA ROSA, GUADALUPE": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "JAIME LEAL, OMAR": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina"
        ]
    },
    "JAIME, PATRICIA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "JIMENEZ MENDOZA, DAYRA REBECA": {
        "Medico_activo": True,
        "Especialidad": [
            "DERMATOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "JUAREZ HERRERA, NORMA": {
        "Medico_activo": False,
        "Especialidad": [
            "DERMATOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa",
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina",
            "LABORATORIO- Coapa"
        ]
    },
    "LOPEZ ORTIZ, SAMANTHA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "MARCANO PILLKAHN, JOHANNA CAROLINA": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "?"
        ]
    },
    "MARTINEZ CORONA, MARICELA": {
        "Medico_activo": False,
        "Especialidad": [
            "ENDOCRINOLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina"
        ]
    },
    "MEDEL RINCON, MARIA AZUCENA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "MERCADO, SANDRA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "MONTERO MARQUEZ , MIGUEL ANGEL": {
        "Medico_activo": False,
        "Especialidad": [
            "OTORRINOLARINGOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "N\\A": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP",
            "UROLOGIA",
            "GINECOLOGIA",
            "GASTROENTEROLOGIA",
            "ALERGOLOGIA",
            "PEDIATRIA",
            "DERMATOLOGIA",
            "MEDICINA GENERAL",
            "ENDOCRINOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina",
            "Punto Clínico- Coapa"
        ]
    },
    "OCHOA, JESSICA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "PAGAZA RAMIREZ, RUBEN": {
        "Medico_activo": True,
        "Especialidad": [
            "MEDICINA GENERAL"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "PEREZ RIOS, BERTHA LUCIA": {
        "Medico_activo": False,
        "Especialidad": [
            "DERMATOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina"
        ]
    },
    "PIEDRAS PONCE, GUADALUPE MONSERRAT": {
        "Medico_activo": False,
        "Especialidad": [
            "NUTRICION"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina",
            "LABORATORIO- Basílica"
        ]
    },
    "PIÑA, LUIS ALBERTO": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "RANGEL BISTRAIN , JULIAN ALEJANDRO": {
        "Medico_activo": False,
        "Especialidad": [
            "UROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina",
            "LABORATORIO- Basílica"
        ]
    },
    "REYNOSO ALMAZAN, ARIANA LIZBETH": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Marina"
        ]
    },
    "RUELAS GONZALEZ, SANDRA": {
        "Medico_activo": False,
        "Especialidad": [
            "DERMATOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina",
            "LABORATORIO- Basílica"
        ]
    },
    "RUIZ RANGEL, PAOLA": {
        "Medico_activo": False,
        "Especialidad": [
            "ENDOCRINOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clínico- Coapa"
        ]
    },
    "SALGADO PARRA  CED. ESP. 11502236, ERIKA GUADALUPE": {
        "Medico_activo": False,
        "Especialidad": [
            "GASTROENTEROLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Basílica",
            "Punto Clinico- Marina",
            "LABORATORIO- Basílica"
        ]
    },
    "SILVA SERRANO, JUANITA": {
        "Medico_activo": False,
        "Especialidad": [
            "ENDOCRINOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa",
            "Punto Clinico- Marina"
        ]
    },
    "SUPPORT      , MEDFAR": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP",
            "GINECOLOGIA",
            "UROLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina",
            "Punto Clínico- Basílica"
        ]
    },
    "TORRES ONTIVEROS, ALMA GABRIELA": {
        "Medico_activo": False,
        "Especialidad": [
            "PEDIATRIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina"
        ]
    },
    "TREJO GONZALEZ, NORMA PATRICIA": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "TUTT GONZALEZ, GIOVANNA": {
        "Medico_activo": False,
        "Especialidad": [
            "NUTRICION"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "VARGAS RAMIREZ, GABRIELA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "VARGAS, ADRIANA": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Basílica"
        ]
    },
    "VAZQUEZ GALLARDO, GRISEL": {
        "Medico_activo": True,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "VILLA CASTRO, VIRGINIA BERENICE": {
        "Medico_activo": False,
        "Especialidad": [
            "OTRA_ESP"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    },
    "VILLALOBOS BENITEZ, OSBERT": {
        "Medico_activo": False,
        "Especialidad": [
            "DERMATOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa",
            "Punto Clínico- Basílica"
        ]
    },
    "VIÑALS RODRIGUEZ, IALA LAURA": {
        "Medico_activo": False,
        "Especialidad": [
            "GINECOLOGIA"
        ],
        "Sitios": [
            "Punto Clinico- Marina",
            "Punto Clínico- Coapa"
        ]
    },
    "ZAMORA GARCIA, ALBERTO": {
        "Medico_activo": False,
        "Especialidad": [
            "CARDIOLOGIA"
        ],
        "Sitios": [
            "Punto Clínico- Coapa"
        ]
    }
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
