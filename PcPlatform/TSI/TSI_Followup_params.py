## DATE RELATED TO PROJECT DEVELOPMENT TASKS, DEADLINES AND ADVANCEMENTS
#### Author: Rob (GH: Roberto919)
#### Date: 25 June 2020





'------------------------------------------------------------------------------------------'
#############
## Imports ##
#############

from datetime import *





'------------------------------------------------------------------------------------------'
################
## Parameters ##
################


## Definition dictionary
def_dict = {
    'No.': {
        'relevant': False
    },
    'Nombre de tarea': {
        'relevant': False
    },
    'Duración': {
        'relevant': False
    },
    'Comienzo': {
        'relevant': False
    },
    'Fin': {
        'relevant': False
    },
    'Comienzo.1': {
        'relevant': True,
        'gantt_name': 'Start'
    },
    'Fin.1': {
        'relevant': True,
        'gantt_name': 'Finish'
    },
    'Predecesoras': {
        'relevant': False
    },
    '% completado': {
        'relevant': True,
        'gantt_name': 'Complete'
    },
    'Tarea_strip': {
        'relevant': True,
        'gantt_name': 'Task'
    }
}
