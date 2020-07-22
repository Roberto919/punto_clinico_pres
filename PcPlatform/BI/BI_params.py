## ANALYZING BUSINESS DATA - PARAMETERS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 20 July 2020





'------------------------------------------------------------------------------------------'
#####################
## Base parameters ##
#####################


## Data
data_loc = 'Data/20200620'
sales_data = 'LISTADELASVENTAS.csv'
appointment_data = 'LISTADETALLADADELASCITAS.csv'






'------------------------------------------------------------------------------------------'
#####################
## Data parameters ##
#####################


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
sp_tsh = 0.05
