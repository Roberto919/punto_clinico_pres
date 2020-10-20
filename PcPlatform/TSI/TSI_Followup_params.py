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
    },
    'RevRobf': {
        'relevant': True,
        'gantt_name': 'Complete'
    },
}



## List of followup activities
followup_dev_activities = {
    "0": {
        "Seed - Proyecto consultorios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "1": {
        "Proyecto consultorios - Inicio": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "2": {
        "Proyecto consultorios - Diseño pantallas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "3": {
        "Proyecto consultorios - Analisis": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "4": {
        "Proyecto consultorios - Desarrollo": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "5": {
        "Proyecto consultorios - Pruebas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "6": {
        "Proyecto consultorios - Liberación": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "7": {
        "Proyecto consultorios - Fin": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "8": {
        "Diseño pantallas - Personalización menú superior": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "9": {
        "Diseño pantallas - Diseño de lateral izquierdo-buscador": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "10": {
        "Diseño pantallas - Calendario de vista por mes con colores con acciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "11": {
        "Diseño pantallas - Calendario de vista por día": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "12": {
        "Diseño pantallas - Lista de pacientes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "13": {
        "Diseño pantallas - Lista de Médicos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "14": {
        "Diseño pantallas - Criterios de impresión": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "15": {
        "Diseño pantallas - Calendario de vista por semana": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "16": {
        "Diseño pantallas - Alta rapida de pacientes-buscador": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "17": {
        "Diseño pantallas - Busqueda avanzada, filtros de citas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "18": {
        "Diseño pantallas - Detalles de citas:Alta, Consulta, Actualización": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "19": {
        "Diseño pantallas - Expediente clinico paciente": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "20": {
        "Diseño pantallas - Historia clinica del paciente": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "21": {
        "Diseño pantallas - Sección de Resumen medico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "22": {
        "Expediente clinico paciente - Encabezado expediente clinico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "23": {
        "Expediente clinico paciente - Lateral expediente clinico(iconos)": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "24": {
        "Expediente clinico paciente - Pantalla Datos demograficos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "25": {
        "Expediente clinico paciente - Pantalla Contactos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "26": {
        "Expediente clinico paciente - Pantalla Profesional a cargo": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "27": {
        "Expediente clinico paciente - Pantalla Relaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "28": {
        "Expediente clinico paciente - Agenda rapida de cita del paciente": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "29": {
        "Expediente clinico paciente - Pantalla lateral izquierda, Historial de citas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "30": {
        "Expediente clinico paciente - Pantalla Cita-Detalle de consulta": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "31": {
        "Expediente clinico paciente - Pantalla Cita-Mensajeria": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "32": {
        "Expediente clinico paciente - Pantalla Cita-Tarea": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "33": {
        "Expediente clinico paciente - Pantalla Cita-Recordatorio": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "34": {
        "Expediente clinico paciente - Pantalla Cita-Comunicaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "35": {
        "Expediente clinico paciente - Pantalla Cita-Cargos a paciente": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "36": {
        "Expediente clinico paciente - Pantalla de administrar documentos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "37": {
        "Expediente clinico paciente - Pantalla de carga de documentos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "38": {
        "Historia clinica del paciente - Encabezado de la historia clinica": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "39": {
        "Sección de Resumen medico - Pantalla de Historial medico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "40": {
        "Sección de Resumen medico - Pantalla lateral izquierda, Antecedentes y diagnosticos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "41": {
        "Sección de Resumen medico - Pantalla de Alergias e intolerancia": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "42": {
        "Sección de Resumen medico - Pantalla Habitos sociales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "43": {
        "Sección de Resumen medico - Pantalla Alertas y necesidades especiales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "44": {
        "Sección de Resumen medico - Pantalla antecedentes familiares": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "45": {
        "Sección de Resumen medico - Pantalla Inmunizaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "46": {
        "Sección de Resumen medico - Pantalla Medicamentos activos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "47": {
        "Sección de Resumen medico - Pantalla signos vitales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "48": {
        "Sección de Resumen medico - Control de escala de dolor": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "49": {
        "Sección de Resumen medico - Pantalla de aprobacion de historia clinica": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "50": {
        "Sección de Resumen medico - Notas de Evolución": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "51": {
        "Sección de Resumen medico - Evaluación": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "52": {
        "Sección de Resumen medico - Plan": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "53": {
        "Sección de Resumen medico - Comunicaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "54": {
        "Notas de Evolución - Pantalla de motivo de consulta": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "55": {
        "Notas de Evolución - Pantalla de Principio, Evolución, Estado": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "56": {
        "Notas de Evolución - Pantalla de Exploración": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "57": {
        "Notas de Evolución - Pantalla de notas manuscritas (cámara)": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "58": {
        "Notas de Evolución - Pantalla de imágenes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "59": {
        "Notas de Evolución - Pantalla de otras notas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "60": {
        "Evaluación - Pantalla de Antecedentes y diagnosticos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "61": {
        "Plan - Pantalla de recetas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "62": {
        "Plan - Pantalla de solicitud de examen": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "63": {
        "Plan - Pantalla de solicitud de interconsulta": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "64": {
        "Plan - Pantalla de seguimiento y plan": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "65": {
        "Plan - Pantalla de comunicaciones-Nuevo recordatorio": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "66": {
        "Plan - Pantalla de comunicaciones-Nuevo mensaje": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "67": {
        "Plan - Pantalla nuevo cargo": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "68": {
        "Comunicaciones - Pantalla bandeja comunicaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "69": {
        "Comunicaciones - Pantalla Recordatorios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "70": {
        "Comunicaciones - Pantalla de mensajes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "71": {
        "Comunicaciones - Pantalla Tareas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "72": {
        "Comunicaciones - Nuevas pantallas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "73": {
        "Pantalla Recordatorios - Pantalla de recordatorio": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "74": {
        "Pantalla de mensajes - Pantalla Mensajes-Enviados": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "75": {
        "Pantalla de mensajes - Pantalla Mensajes-Borrador": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "76": {
        "Pantalla de mensajes - Pantalla Mensajes-Archivo": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "77": {
        "Pantalla de mensajes - Pantalla Mensajes-Basura": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "78": {
        "Pantalla Tareas - Pantalla Tareas-Enviados": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "79": {
        "Pantalla Tareas - Pantalla Tareas-Borrador": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "80": {
        "Pantalla Tareas - Pantalla Tareas-Archivo": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "81": {
        "Pantalla Tareas - Pantalla Tareas-Basura": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "82": {
        "Nuevas pantallas - Apertura de horarios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "83": {
        "Nuevas pantallas - Creación de horarios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "84": {
        "Nuevas pantallas - Resultados": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "85": {
        "Nuevas pantallas - Pantalla de comunicaciones - nueva tarea": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "86": {
        "Nuevas pantallas - Portafolios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "87": {
        "Analisis - Análisis de usuarios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "88": {
        "Analisis - Análisis de roles seguridad": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "89": {
        "Analisis - Análisis de politicas de seguridad": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "90": {
        "Analisis - Análisis de sucursales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "91": {
        "Analisis - Análisis de figuras tributarias": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "92": {
        "Analisis - Análisis de especialidades": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "93": {
        "Analisis - Análisis de pacientes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "94": {
        "Analisis - Análisis de lista de precios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "95": {
        "Analisis - Análisis de Nemóticos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "96": {
        "Analisis - Análisis de tipos de servicios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "97": {
        "Analisis - Análisis de Servicios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "98": {
        "Analisis - Análisis de Medicamentos e insumos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "99": {
        "Analisis - Análisis de proveedor": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "100": {
        "Analisis - Análisis de consultorios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "101": {
        "Analisis - Análisis de tipo de recurrencia": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "102": {
        "Analisis - Análisis de agendas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "103": {
        "Analisis - Análisis de Doctores": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "104": {
        "Analisis - Análisis de instituciones de referencia": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "105": {
        "Analisis - Análisis de Historia clinica": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "106": {
        "Analisis - Análisis de notas clinicas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "107": {
        "Analisis - Análisis de Expediente de documentos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "108": {
        "Analisis - Análisis de politicas de descuentos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "109": {
        "Analisis - Análisis de Orden de servicio": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "110": {
        "Analisis - Análisis de generación de venta": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "111": {
        "Analisis - Análisis de facturación": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "112": {
        "Analisis - Análisis de cuentas por cobrar": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "113": {
        "Analisis - Análisis de turnos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "114": {
        "Analisis - Análisis de Cajas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "115": {
        "Analisis - Analisis de cajeros": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "116": {
        "Analisis - Analisis de cotizaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "117": {
        "Analisis - Análisis de teleconsultas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "118": {
        "Analisis - Análisis de reportes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "119": {
        "Analisis - Análisis de encuesta de satisfacción y reportes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "120": {
        "Análisis de notas clinicas - Nueva nota": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "121": {
        "Análisis de notas clinicas - Problemas activos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "122": {
        "Análisis de notas clinicas - Historial médico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "123": {
        "Análisis de notas clinicas - Historial quirúrgico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "124": {
        "Análisis de notas clinicas - Historial psiquiátrico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "125": {
        "Análisis de notas clinicas - Historial Gineco-Obstétrico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "126": {
        "Análisis de notas clinicas - Medicamentos activos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "127": {
        "Análisis de notas clinicas - Alergias e intolerancias": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "128": {
        "Análisis de notas clinicas - Hábitos sociales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "129": {
        "Análisis de notas clinicas - Alertas y necesidades especiales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "130": {
        "Análisis de notas clinicas - Inmunizaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "131": {
        "Análisis de notas clinicas - Antecedentes familiares": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "132": {
        "Análisis de notas clinicas - Nueva nota": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "133": {
        "Análisis de notas clinicas - Problemas activos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "134": {
        "Análisis de notas clinicas - Historial médico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "135": {
        "Análisis de notas clinicas - Historial quirúrgico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "136": {
        "Análisis de notas clinicas - Historial psiquiátrico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "137": {
        "Análisis de notas clinicas - Historial Gineco-Obstétrico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "138": {
        "Análisis de notas clinicas - Medicamentos activos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "139": {
        "Análisis de notas clinicas - Alergias e intolerancias": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "140": {
        "Análisis de notas clinicas - Hábitos sociales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "141": {
        "Análisis de notas clinicas - Alertas y necesidades especiales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "142": {
        "Análisis de notas clinicas - Inmunizaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "143": {
        "Análisis de notas clinicas - Antecedentes familiares": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "144": {
        "Análisis de notas clinicas - Comentarios de Historia Clínica (para todos)": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "145": {
        "Desarrollo - Implementación modulo de seguridad": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "146": {
        "Desarrollo - Implementacion de figuras tributarias": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "147": {
        "Desarrollo - Implementación de especialidades": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "148": {
        "Desarrollo - Implementación catalogos varios define paciente": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "149": {
        "Desarrollo - Implementación de lista de precios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "150": {
        "Desarrollo - Implementación de Nemóticos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "151": {
        "Desarrollo - Implementación de tipos de servicios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "152": {
        "Desarrollo - Implementación de servicios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "153": {
        "Desarrollo - Implementación de Medicamentos e insumos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "154": {
        "Desarrollo - Implementación de proveedor": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "155": {
        "Desarrollo - Implementación de tipo de recurrencia": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "156": {
        "Desarrollo - Implementación de catalogos de doctores": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "157": {
        "Desarrollo - Implementación de instituciones de referencia": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "158": {
        "Desarrollo - Implementación de pacientes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "159": {
        "Desarrollo - Implementación de consultorios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "160": {
        "Desarrollo - Apertura de horarios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "161": {
        "Desarrollo - Creación de horarios": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "162": {
        "Desarrollo - Implementación de agenda": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "163": {
        "Desarrollo - Implementación servicio ambulatorio": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "164": {
        "Desarrollo - Implementación de notas médicas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "165": {
        "Desarrollo - Implementación de notas clinicas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "166": {
        "Desarrollo - Implementación de expedientes de documentos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "167": {
        "Desarrollo - Implementación de politicas de descuento": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "168": {
        "Desarrollo - Implementación de orden de servicio": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "169": {
        "Desarrollo - Implementación de generación de venta": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "170": {
        "Desarrollo - Implementación de facturación": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "171": {
        "Desarrollo - Implementación de cuentas por cobrar": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "172": {
        "Desarrollo - Implementación de turnos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "173": {
        "Desarrollo - Implementación de cajeros": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "174": {
        "Desarrollo - Implementación de Cajas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "175": {
        "Desarrollo - Implementación de cotizaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "176": {
        "Desarrollo - Implementacion de teleconsultas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "177": {
        "Desarrollo - Implementación de reportes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "178": {
        "Desarrollo - Integración de encuentas de satisfacción": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "179": {
        "Desarrollo - Integracion de modulos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "180": {
        "Implementación de agenda - Búsqueda de pacientes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "181": {
        "Implementación de agenda - Detalle de pacientes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "182": {
        "Implementación de agenda - 3 doctores por tipo de agenda": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "183": {
        "Implementación de agenda - Botones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "184": {
        "Implementación de agenda - Asignación de citas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "185": {
        "Implementación de agenda - Alta de un nuevo paciente": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "186": {
        "3 doctores por tipo de agenda - Diaria": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "187": {
        "3 doctores por tipo de agenda - Semanal": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "188": {
        "3 doctores por tipo de agenda - Mensual": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "189": {
        "Botones - Refrescar": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "190": {
        "Botones - Lista de pacientes por atender": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "191": {
        "Botones - Lista de médicos registrados.": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "192": {
        "Botones - Impresión": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "193": {
        "Asignación de citas - Selección del Dr.": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "194": {
        "Asignación de citas - Selección del día de consulta de disponibilidad": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "195": {
        "Asignación de citas - Mostrar disponibilidad y seleccionar un horario": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "196": {
        "Asignación de citas - Actualizar la agenda y Google Calendar": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "197": {
        "Asignación de citas - Ingresar datos del paciente": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "198": {
        "Comentarios de Historia Clínica (para todos) - Historial médico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "199": {
        "Comentarios de Historia Clínica (para todos) - Historial quirúrgico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "200": {
        "Comentarios de Historia Clínica (para todos) - Historial psiquiátrico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "201": {
        "Comentarios de Historia Clínica (para todos) - Historial Gineco-Obstétrico": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "202": {
        "Comentarios de Historia Clínica (para todos) - Medicamentos activos": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "203": {
        "Comentarios de Historia Clínica (para todos) - Alergias e intolerancias": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "204": {
        "Comentarios de Historia Clínica (para todos) - Hábitos sociales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "205": {
        "Comentarios de Historia Clínica (para todos) - Alertas y necesidades especiales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "206": {
        "Comentarios de Historia Clínica (para todos) - Inmunizaciones": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "207": {
        "Comentarios de Historia Clínica (para todos) - Antecedentes familiares": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "208": {
        "Implementación de notas clinicas - Notas de evolución": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "209": {
        "Pruebas - Generación de casos de uso y pruebas unitarias": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "210": {
        "Pruebas - Revisión interna": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "211": {
        "Pruebas - Integración y despliegue": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "212": {
        "Pruebas - Pruebas Integrales": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "213": {
        "Pruebas - Matriz de pruebas": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "214": {
        "Pruebas - Ajustes": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "215": {
        "Pruebas - Hoja de Implementación": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "216": {
        "Liberación - Generar solicitud de migración": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "217": {
        "Liberación - Liberación": {
            "Revisada": 0,
            "Notas": "-"
        }
    },
    "218": {
        "Liberación - Validación productiva": {
            "Revisada": 0,
            "Notas": "-"
        }
    }
}
