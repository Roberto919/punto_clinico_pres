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
        "Proyecto consultorios": {
            "Revisada": 0
        }
    },
    "1": {
        "Inicio": {
            "Revisada": 0
        }
    },
    "2": {
        "Diseño pantallas": {
            "Revisada": 0
        }
    },
    "3": {
        "Personalización menú superior": {
            "Revisada": 0
        }
    },
    "4": {
        "Diseño de lateral izquierdo-buscador": {
            "Revisada": 0
        }
    },
    "5": {
        "Calendario de vista por mes con colores con acciones": {
            "Revisada": 0
        }
    },
    "6": {
        "Calendario de vista por día": {
            "Revisada": 0
        }
    },
    "7": {
        "Lista de pacientes": {
            "Revisada": 0
        }
    },
    "8": {
        "Lista de Médicos": {
            "Revisada": 0
        }
    },
    "9": {
        "Criterios de impresión": {
            "Revisada": 0
        }
    },
    "10": {
        "Calendario de vista por semana": {
            "Revisada": 0
        }
    },
    "11": {
        "Alta rapida de pacientes-buscador": {
            "Revisada": 0
        }
    },
    "12": {
        "Busqueda avanzada, filtros de citas": {
            "Revisada": 0
        }
    },
    "13": {
        "Detalles de citas:Alta, Consulta, Actualización": {
            "Revisada": 0
        }
    },
    "14": {
        "Expediente clinico paciente": {
            "Revisada": 0
        }
    },
    "15": {
        "Encabezado expediente clinico": {
            "Revisada": 0
        }
    },
    "16": {
        "Lateral expediente clinico(iconos)": {
            "Revisada": 0
        }
    },
    "17": {
        "Pantalla Datos demograficos": {
            "Revisada": 0
        }
    },
    "18": {
        "Pantalla Contactos": {
            "Revisada": 0
        }
    },
    "19": {
        "Pantalla Profesional a cargo": {
            "Revisada": 0
        }
    },
    "20": {
        "Pantalla Relaciones": {
            "Revisada": 0
        }
    },
    "21": {
        "Agenda rapida de cita del paciente": {
            "Revisada": 0
        }
    },
    "22": {
        "Pantalla lateral izquierda, Historial de citas": {
            "Revisada": 0
        }
    },
    "23": {
        "Pantalla Cita-Detalle de consulta": {
            "Revisada": 0
        }
    },
    "24": {
        "Pantalla Cita-Mensajeria": {
            "Revisada": 0
        }
    },
    "25": {
        "Pantalla Cita-Tarea": {
            "Revisada": 0
        }
    },
    "26": {
        "Pantalla Cita-Recordatorio": {
            "Revisada": 0
        }
    },
    "27": {
        "Pantalla Cita-Comunicaciones": {
            "Revisada": 0
        }
    },
    "28": {
        "Pantalla Cita-Cargos a paciente": {
            "Revisada": 0
        }
    },
    "29": {
        "Pantalla de administrar documentos": {
            "Revisada": 0
        }
    },
    "30": {
        "Pantalla de carga de documentos": {
            "Revisada": 0
        }
    },
    "31": {
        "Historia clinica del paciente": {
            "Revisada": 0
        }
    },
    "32": {
        "Encabezado de la historia clinica": {
            "Revisada": 0
        }
    },
    "33": {
        "Sección de Resumen medico": {
            "Revisada": 0
        }
    },
    "34": {
        "Pantalla de Historial medico": {
            "Revisada": 0
        }
    },
    "35": {
        "Pantalla lateral izquierda, Antecedentes y diagnosticos": {
            "Revisada": 0
        }
    },
    "36": {
        "Pantalla de Alergias e intolerancia": {
            "Revisada": 0
        }
    },
    "37": {
        "Pantalla Habitos sociales": {
            "Revisada": 0
        }
    },
    "38": {
        "Pantalla Alertas y necesidades especiales": {
            "Revisada": 0
        }
    },
    "39": {
        "Pantalla antecedentes familiares": {
            "Revisada": 0
        }
    },
    "40": {
        "Pantalla Inmunizaciones": {
            "Revisada": 0
        }
    },
    "41": {
        "Pantalla Medicamentos activos": {
            "Revisada": 0
        }
    },
    "42": {
        "Pantalla signos vitales": {
            "Revisada": 0
        }
    },
    "43": {
        "Control de escala de dolor": {
            "Revisada": 0
        }
    },
    "44": {
        "Pantalla de aprobacion de historia clinica": {
            "Revisada": 0
        }
    },
    "45": {
        "Notas de Evolución": {
            "Revisada": 0
        }
    },
    "46": {
        "Pantalla de motivo de consulta": {
            "Revisada": 0
        }
    },
    "47": {
        "Pantalla de Principio, Evolución, Estado": {
            "Revisada": 0
        }
    },
    "48": {
        "Pantalla de Exploración": {
            "Revisada": 0
        }
    },
    "49": {
        "Pantalla de notas manuscritas (cámara)": {
            "Revisada": 0
        }
    },
    "50": {
        "Pantalla de imágenes": {
            "Revisada": 0
        }
    },
    "51": {
        "Pantalla de otras notas": {
            "Revisada": 0
        }
    },
    "52": {
        "Evaluación": {
            "Revisada": 0
        }
    },
    "53": {
        "Pantalla de Antecedentes y diagnosticos": {
            "Revisada": 0
        }
    },
    "54": {
        "Plan": {
            "Revisada": 0
        }
    },
    "55": {
        "Pantalla de recetas": {
            "Revisada": 0
        }
    },
    "56": {
        "Pantalla de solicitud de examen": {
            "Revisada": 0
        }
    },
    "57": {
        "Pantalla de solicitud de interconsulta": {
            "Revisada": 0
        }
    },
    "58": {
        "Pantalla de seguimiento y plan": {
            "Revisada": 0
        }
    },
    "59": {
        "Pantalla de comunicaciones-Nuevo recordatorio": {
            "Revisada": 0
        }
    },
    "60": {
        "Pantalla de comunicaciones-Nuevo mensaje": {
            "Revisada": 0
        }
    },
    "61": {
        "Pantalla nuevo cargo": {
            "Revisada": 0
        }
    },
    "62": {
        "Comunicaciones": {
            "Revisada": 0
        }
    },
    "63": {
        "Pantalla bandeja comunicaciones": {
            "Revisada": 0
        }
    },
    "64": {
        "Pantalla Recordatorios": {
            "Revisada": 0
        }
    },
    "65": {
        "Pantalla de recordatorio": {
            "Revisada": 0
        }
    },
    "66": {
        "Pantalla de mensajes": {
            "Revisada": 0
        }
    },
    "67": {
        "Pantalla Mensajes-Enviados": {
            "Revisada": 0
        }
    },
    "68": {
        "Pantalla Mensajes-Borrador": {
            "Revisada": 0
        }
    },
    "69": {
        "Pantalla Mensajes-Archivo": {
            "Revisada": 0
        }
    },
    "70": {
        "Pantalla Mensajes-Basura": {
            "Revisada": 0
        }
    },
    "71": {
        "Pantalla Tareas": {
            "Revisada": 0
        }
    },
    "72": {
        "Pantalla Tareas-Enviados": {
            "Revisada": 0
        }
    },
    "73": {
        "Pantalla Tareas-Borrador": {
            "Revisada": 0
        }
    },
    "74": {
        "Pantalla Tareas-Archivo": {
            "Revisada": 0
        }
    },
    "75": {
        "Pantalla Tareas-Basura": {
            "Revisada": 0
        }
    },
    "76": {
        "Nuevas pantallas": {
            "Revisada": 0
        }
    },
    "77": {
        "Apertura de horarios": {
            "Revisada": 0
        }
    },
    "78": {
        "Creación de horarios": {
            "Revisada": 0
        }
    },
    "79": {
        "Resultados": {
            "Revisada": 0
        }
    },
    "80": {
        "Pantalla de comunicaciones - nueva tarea": {
            "Revisada": 0
        }
    },
    "81": {
        "Portafolios": {
            "Revisada": 0
        }
    },
    "82": {
        "Analisis": {
            "Revisada": 0
        }
    },
    "83": {
        "Análisis de usuarios": {
            "Revisada": 0
        }
    },
    "84": {
        "Análisis de roles seguridad": {
            "Revisada": 0
        }
    },
    "85": {
        "Análisis de politicas de seguridad": {
            "Revisada": 0
        }
    },
    "86": {
        "Análisis de sucursales": {
            "Revisada": 0
        }
    },
    "87": {
        "Análisis de figuras tributarias": {
            "Revisada": 0
        }
    },
    "88": {
        "Análisis de especialidades": {
            "Revisada": 0
        }
    },
    "89": {
        "Análisis de pacientes": {
            "Revisada": 0
        }
    },
    "90": {
        "Análisis de lista de precios": {
            "Revisada": 0
        }
    },
    "91": {
        "Análisis de Nemóticos": {
            "Revisada": 0
        }
    },
    "92": {
        "Análisis de tipos de servicios": {
            "Revisada": 0
        }
    },
    "93": {
        "Análisis de Servicios": {
            "Revisada": 0
        }
    },
    "94": {
        "Análisis de Medicamentos e insumos": {
            "Revisada": 0
        }
    },
    "95": {
        "Análisis de proveedor": {
            "Revisada": 0
        }
    },
    "96": {
        "Análisis de consultorios": {
            "Revisada": 0
        }
    },
    "97": {
        "Análisis de tipo de recurrencia": {
            "Revisada": 0
        }
    },
    "98": {
        "Análisis de agendas": {
            "Revisada": 0
        }
    },
    "99": {
        "Análisis de Doctores": {
            "Revisada": 0
        }
    },
    "100": {
        "Análisis de instituciones de referencia": {
            "Revisada": 0
        }
    },
    "101": {
        "Análisis de Historia clinica": {
            "Revisada": 0
        }
    },
    "102": {
        "Análisis de notas clinicas": {
            "Revisada": 0
        }
    },
    "115": {
        "Análisis de Expediente de documentos": {
            "Revisada": 0
        }
    },
    "116": {
        "Análisis de politicas de descuentos": {
            "Revisada": 0
        }
    },
    "117": {
        "Análisis de Orden de servicio": {
            "Revisada": 0
        }
    },
    "118": {
        "Análisis de generación de venta": {
            "Revisada": 0
        }
    },
    "119": {
        "Análisis de facturación": {
            "Revisada": 0
        }
    },
    "120": {
        "Análisis de cuentas por cobrar": {
            "Revisada": 0
        }
    },
    "121": {
        "Análisis de turnos": {
            "Revisada": 0
        }
    },
    "122": {
        "Análisis de Cajas": {
            "Revisada": 0
        }
    },
    "123": {
        "Analisis de cajeros": {
            "Revisada": 0
        }
    },
    "124": {
        "Analisis de cotizaciones": {
            "Revisada": 0
        }
    },
    "125": {
        "Análisis de teleconsultas": {
            "Revisada": 0
        }
    },
    "126": {
        "Análisis de reportes": {
            "Revisada": 0
        }
    },
    "127": {
        "Análisis de encuesta de satisfacción y reportes": {
            "Revisada": 0
        }
    },
    "128": {
        "Desarrollo": {
            "Revisada": 0
        }
    },
    "129": {
        "Implementación modulo de seguridad": {
            "Revisada": 0
        }
    },
    "130": {
        "Implementacion de figuras tributarias": {
            "Revisada": 0
        }
    },
    "131": {
        "Implementación de especialidades": {
            "Revisada": 0
        }
    },
    "132": {
        "Implementación catalogos varios define paciente": {
            "Revisada": 0
        }
    },
    "133": {
        "Implementación de lista de precios": {
            "Revisada": 0
        }
    },
    "134": {
        "Implementación de Nemóticos": {
            "Revisada": 0
        }
    },
    "135": {
        "Implementación de tipos de servicios": {
            "Revisada": 0
        }
    },
    "136": {
        "Implementación de servicios": {
            "Revisada": 0
        }
    },
    "137": {
        "Implementación de Medicamentos e insumos": {
            "Revisada": 0
        }
    },
    "138": {
        "Implementación de proveedor": {
            "Revisada": 0
        }
    },
    "139": {
        "Implementación de tipo de recurrencia": {
            "Revisada": 0
        }
    },
    "140": {
        "Implementación de catalogos de doctores": {
            "Revisada": 0
        }
    },
    "141": {
        "Implementación de instituciones de referencia": {
            "Revisada": 0
        }
    },
    "142": {
        "Implementación de pacientes": {
            "Revisada": 0
        }
    },
    "143": {
        "Implementación de consultorios": {
            "Revisada": 0
        }
    },
    "144": {
        "Apertura de horarios": {
            "Revisada": 0
        }
    },
    "145": {
        "Creación de horarios": {
            "Revisada": 0
        }
    },
    "146": {
        "Implementación de agenda": {
            "Revisada": 0
        }
    },
    "147": {
        "Búsqueda de pacientes": {
            "Revisada": 0
        }
    },
    "148": {
        "Detalle de pacientes": {
            "Revisada": 0
        }
    },
    "149": {
        "3 doctores por tipo de agenda": {
            "Revisada": 0
        }
    },
    "150": {
        "Diaria": {
            "Revisada": 0
        }
    },
    "151": {
        "Semanal": {
            "Revisada": 0
        }
    },
    "152": {
        "Mensual": {
            "Revisada": 0
        }
    },
    "154": {
        "Refrescar": {
            "Revisada": 0
        }
    },
    "155": {
        "Lista de pacientes por atender": {
            "Revisada": 0
        }
    },
    "156": {
        "Lista de médicos registrados.": {
            "Revisada": 0
        }
    },
    "157": {
        "Impresión": {
            "Revisada": 0
        }
    },
    "158": {
        "Asignación de citas": {
            "Revisada": 0
        }
    },
    "159": {
        "Selección del Dr.": {
            "Revisada": 0
        }
    },
    "160": {
        "Selección del día de consulta de disponibilidad": {
            "Revisada": 0
        }
    },
    "161": {
        "Mostrar disponibilidad y seleccionar un horario": {
            "Revisada": 0
        }
    },
    "162": {
        "Actualizar la agenda y Google Calendar": {
            "Revisada": 0
        }
    },
    "163": {
        "Ingresar datos del paciente": {
            "Revisada": 0
        }
    },
    "164": {
        "Alta de un nuevo paciente": {
            "Revisada": 0
        }
    },
    "165": {
        "Implementación servicio ambulatorio": {
            "Revisada": 0
        }
    },
    "166": {
        "Implementación de notas médicas": {
            "Revisada": 0
        }
    },
    "167": {
        "Nueva nota": {
            "Revisada": 0
        }
    },
    "168": {
        "Problemas activos": {
            "Revisada": 0
        }
    },
    "169": {
        "Historial médico": {
            "Revisada": 0
        }
    },
    "170": {
        "Historial quirúrgico": {
            "Revisada": 0
        }
    },
    "171": {
        "Historial psiquiátrico": {
            "Revisada": 0
        }
    },
    "172": {
        "Historial Gineco-Obstétrico": {
            "Revisada": 0
        }
    },
    "173": {
        "Medicamentos activos": {
            "Revisada": 0
        }
    },
    "174": {
        "Alergias e intolerancias": {
            "Revisada": 0
        }
    },
    "175": {
        "Hábitos sociales": {
            "Revisada": 0
        }
    },
    "176": {
        "Alertas y necesidades especiales": {
            "Revisada": 0
        }
    },
    "177": {
        "Inmunizaciones": {
            "Revisada": 0
        }
    },
    "178": {
        "Antecedentes familiares": {
            "Revisada": 0
        }
    },
    "180": {
        "Historial médico": {
            "Revisada": 0
        }
    },
    "181": {
        "Historial quirúrgico": {
            "Revisada": 0
        }
    },
    "182": {
        "Historial psiquiátrico": {
            "Revisada": 0
        }
    },
    "183": {
        "Historial Gineco-Obstétrico": {
            "Revisada": 0
        }
    },
    "184": {
        "Medicamentos activos": {
            "Revisada": 0
        }
    },
    "185": {
        "Alergias e intolerancias": {
            "Revisada": 0
        }
    },
    "186": {
        "Hábitos sociales": {
            "Revisada": 0
        }
    },
    "187": {
        "Alertas y necesidades especiales": {
            "Revisada": 0
        }
    },
    "188": {
        "Inmunizaciones": {
            "Revisada": 0
        }
    },
    "189": {
        "Antecedentes familiares": {
            "Revisada": 0
        }
    },
    "190": {
        "Implementación de notas clinicas": {
            "Revisada": 0
        }
    },
    "191": {
        "Notas de evolución": {
            "Revisada": 0
        }
    },
    "192": {
        "Implementación de expedientes de documentos": {
            "Revisada": 0
        }
    },
    "193": {
        "Implementación de politicas de descuento": {
            "Revisada": 0
        }
    },
    "194": {
        "Implementación de orden de servicio": {
            "Revisada": 0
        }
    },
    "195": {
        "Implementación de generación de venta": {
            "Revisada": 0
        }
    },
    "196": {
        "Implementación de facturación": {
            "Revisada": 0
        }
    },
    "197": {
        "Implementación de cuentas por cobrar": {
            "Revisada": 0
        }
    },
    "198": {
        "Implementación de turnos": {
            "Revisada": 0
        }
    },
    "199": {
        "Implementación de cajeros": {
            "Revisada": 0
        }
    },
    "200": {
        "Implementación de Cajas": {
            "Revisada": 0
        }
    },
    "201": {
        "Implementación de cotizaciones": {
            "Revisada": 0
        }
    },
    "202": {
        "Implementacion de teleconsultas": {
            "Revisada": 0
        }
    },
    "203": {
        "Implementación de reportes": {
            "Revisada": 0
        }
    },
    "204": {
        "Integración de encuentas de satisfacción": {
            "Revisada": 0
        }
    },
    "205": {
        "Integracion de modulos": {
            "Revisada": 0
        }
    },
    "206": {
        "Pruebas": {
            "Revisada": 0
        }
    },
    "207": {
        "Generación de casos de uso y pruebas unitarias": {
            "Revisada": 0
        }
    },
    "208": {
        "Revisión interna": {
            "Revisada": 0
        }
    },
    "209": {
        "Integración y despliegue": {
            "Revisada": 0
        }
    },
    "210": {
        "Pruebas Integrales": {
            "Revisada": 0
        }
    },
    "211": {
        "Matriz de pruebas": {
            "Revisada": 0
        }
    },
    "212": {
        "Ajustes": {
            "Revisada": 0
        }
    },
    "213": {
        "Hoja de Implementación": {
            "Revisada": 0
        }
    },
    "214": {
        "Liberación": {
            "Revisada": 0
        }
    },
    "215": {
        "Generar solicitud de migración": {
            "Revisada": 0
        }
    },
    "216": {
        "Liberación": {
            "Revisada": 0
        }
    },
    "217": {
        "Validación productiva": {
            "Revisada": 0
        }
    },
    "218": {
        "Fin": {
            "Revisada": 0
        }
    }
}
