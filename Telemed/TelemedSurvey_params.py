## ANALYZING TELEMEDICINE SURVEY RESULTS - PARAMETERS FILE
#### Author: Rob (GH: Roberto919)
#### Date: 21 July 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############

import os





'------------------------------------------------------------------------------------------'
######################
## Basic parameters ##
######################


## Data file
source_path = 'Sources'
file = [f for f in os.listdir(path=source_path) if '.csv' in f]
file_path = os.path.join(source_path, file[0])





'------------------------------------------------------------------------------------------'
########################
## Dataset parameters ##
########################


## Relevant columns and simplified names
simp_rcol_names = {
    'Especialidad del Médico': 'Especialidad',
    '¿Ha considerado ofrecer consultas  médicas a distancia (teleconsultas) a través de videoconferencias a sus pacientes?': 'Ha considerado ofrecer teleconsulta?',
    '¿Del 1 al 5, qué tan común considera que será que sus pacientes soliciten teleconsultas médicas para atender sus padecimientos?': 'Demanda esperada de teleconsultas',
    '¿Cuenta con alguna plataforma digital que le ayude con la administración de sus servicios médicos (Por Ejemplo: con la gestión de citas, pagos, seguimiento a pacientes)?': 'Cuenta con plataforma de gestión?',
    '¿Cuáles?': 'Qué plataforma de gestión?',
    '¿Cuenta con alguna plataforma digital para ofrecer teleconsultas?': 'Cuenta con plataforma de teleconsultas?',
    '¿Cuáles?2': 'Qué plataforma de teleconsulta?',
    'Seleccione las funcionalidades que considera importantes para que estén presentes en una plataforma digital que lo apoye con la gestión de sus servicios médicos.': 'Funcionalidades relevantes',
    '¿Cuánto estaría dispuesto a pagar mensualmente por el uso de la plataforma descrita?': 'Disponibilidad de pago',
    'Si le ofrecieran una plataforma digital a un precio competitivo para facilitarle la gestión de su agenda de citas, cobros y seguimientos a pacientes, así como la posibilidad de llevar a cabo telec...': 'Regularidad de uso si tuviera plataforma'
}





'------------------------------------------------------------------------------------------'
#########################
## Analysis parameters ##
#########################


platform_features_options = {
    'Creación automática de videoconferencias con clientes para teleconsultas': [
        'Creación automática de videoconferencias con clientes para teleconsultas',
        'Creación automática de videoconferencias con clientes',
        'Creación automática de videoconferencias'
    ],
    'Envío y recepción de documentos con cliente (e.g. resultados de estudios, recetas médicas)': [
        'Envío y recepción de documentos con cliente (e.g. resultados de estudios, recetas médicas)',
        'Envío y recepción de documentos con cliente (estudios, recetas médicas)',
    ],
    'Administración de citas': [
        'Administración de citas',
    ],
    'Gestión de pagos': [
        'Gestión de pagos',
    ],
    'Despliegue de encuestas de satisfacción de clientes': [
        'Despliegue de encuestas de satisfacción de clientes',
    ],
    'Aplicación de promociones de descuento para clientes': [
        'Aplicación de promociones de descuento para clientes',
    ]
}


## Grouping platform names (Analysis 6)
platforms_names = {
    'Doctoralia': [
        'doctoralia',
        'dralia',
        'doctoralis',
        'doctorolia'
    ],
    'Zoom': [
        'zoom',
        'soom'
    ],
    'Huli': [
        'huli'
    ],
    'Medikato': [
        'medikato'
    ],
    'Elionor': [
        'elionor',
        'eleonor'
    ],
    'Doctor Anytime': [
        'doctor anytime'
    ],
    'Nimbo': [
        'nimbo'
    ],
    'Metlife': [
        'metlife',
        'metlife'
    ],
    'Kidoc': [
        'kidoc',
        'kidok'
    ],
    'Medsi': [
        'medsi'
    ],
    'Clinic cloud': [
        'clínic cloud'
    ],
    'Google calendar': [
        'google calendar'
    ],
    'Whatsapp': [
        'whatsapp',
        'whats'
    ],
    'Skype': [
        'skype',
        'skipe'
    ],
    'Evernote': [
        'evernote',
    ],
    'Plataforma Chopo': [
        'chopo'
    ],
    'Ayuda secretaria': [
        'secretaria'
    ],
    'Software hospital': [
        'hospital',
        'hosopital'
    ],
    'Personal': [
        'propio',
        'propia',
        'personal',
        'personalizada'
    ],
}
