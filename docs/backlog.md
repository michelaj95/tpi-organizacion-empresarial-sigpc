# Backlog ágil del SIGPC

## Criterio de organización

El backlog prioriza los flujos mínimos de la primera versión del SIGPC. Las historias se redactan en formato formal y se vinculan con el proceso BPMN, el diccionario de datos y los indicadores del proyecto. El estado consignado representa el corte de seguimiento utilizado para evidenciar las tres columnas obligatorias del tablero.

| ID | Prioridad | Estimación | Estado | Entidades principales |
|---|---:|---:|---|---|
| HU-01 | Alta | 8 puntos | Listo | Cliente, Proyecto, Usuario |
| HU-02 | Alta | 13 puntos | En Progreso | Proyecto, Tarea, RegistroHora, Incidencia |
| HU-03 | Media | 8 puntos | Por Hacer | Proyecto, Tarea, RegistroHora, Incidencia, HitoFacturacion |

## HU-01 — Alta de clientes y proyectos

**Como** integrante del área Comercial, **quiero** registrar clientes, solicitudes y datos obligatorios de un proyecto en el SIGPC, **para** que las áreas involucradas trabajen con información única y completa.

### Criterios de aceptación

- El sistema exige los campos obligatorios de Cliente y Proyecto antes de permitir el alta.
- El CUIT del cliente no puede repetirse.
- Un proyecto nuevo queda asociado a un único cliente y a un responsable activo.
- El estado inicial del proyecto es `Propuesto`.
- Cuando faltan datos, el sistema informa qué campos deben completarse y conserva el borrador sin crear registros duplicados.
- Al aprobarse la propuesta, el SIGPC cambia el estado a `Aprobado` y notifica a los responsables.

### Tareas vinculadas

- Definir formulario y validaciones.
- Implementar control de CUIT único.
- Crear relación Cliente–Proyecto.
- Probar caminos de datos completos e incompletos.

## HU-02 — Seguimiento del trabajo

**Como** responsable del área de Tecnología, **quiero** planificar tareas, asignar responsables y registrar horas e incidencias, **para** controlar el avance y corregir desvíos antes de la entrega.

### Criterios de aceptación

- Cada tarea pertenece a un proyecto y posee responsable, prioridad, fechas previstas y estado controlado.
- Las horas registradas deben ser mayores que cero e identificar usuario y fecha.
- El tablero permite distinguir tareas pendientes, en curso, bloqueadas y terminadas.
- Una incidencia queda asociada al proyecto, con prioridad, responsable, estado y fecha de apertura.
- El responsable puede comparar horas previstas y reales y visualizar alertas por vencimiento.
- No se puede cerrar el proyecto si existen tareas críticas o incidencias bloqueantes abiertas.

### Tareas vinculadas

- Diseñar flujo de estados de Tarea.
- Implementar asignación de responsables.
- Incorporar registro de horas.
- Integrar incidencias y alertas.
- Ejecutar pruebas de cierre con bloqueos pendientes.

## HU-03 — Indicadores para Dirección

**Como** integrante de Dirección, **quiero** consultar indicadores consolidados de avance, tiempos, calidad y facturación, **para** tomar decisiones basadas en información trazable.

### Criterios de aceptación

- El panel muestra avance, cumplimiento de fechas, desvío de horas, incidencias y situación de hitos de facturación.
- Los resultados pueden filtrarse por proyecto y período.
- Cada indicador permite identificar los registros de origen utilizados en su cálculo.
- Al menos el 95 % de las consultas habituales responde en dos segundos o menos bajo el escenario de prueba definido.
- Los datos cerrados no pueden modificarse sin conservar usuario, fecha y valor anterior.

### Tareas vinculadas

- Definir consultas y fórmulas.
- Diseñar panel resumido.
- Incorporar filtros y trazabilidad.
- Ejecutar prueba de rendimiento.
- Validar resultados con Dirección.

## Política de movimiento

- **Por Hacer:** historia priorizada y con criterios de aceptación, aún no iniciada.
- **En Progreso:** existe trabajo activo y una persona responsable.
- **Listo:** todos los criterios fueron verificados y no quedan defectos bloqueantes.

El cambio de estado debe quedar visible en el historial del tablero y vinculado con el issue correspondiente.

