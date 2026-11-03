# Indicadores y estándares de control del SIGPC

## Matriz de indicadores

Los primeros cinco indicadores conservan las metas cuantitativas definidas en la Entrega 2. Los tres restantes controlan la operación posterior a la implantación.

| ID | Indicador y fórmula | Meta | Fuente / evidencia | Frecuencia | Responsable | Acción ante desvío |
|---|---|---|---|---|---|---|
| IC-01 | Cobertura de aceptación = casos críticos aprobados / casos críticos ejecutados × 100 | 100 % y sin defectos bloqueantes | Acta del piloto y resultados de pruebas | Hitos de pruebas y antes de liberar | QA + áreas usuarias | Bloquear la liberación, corregir y repetir los casos fallidos |
| IC-02 | Consultas dentro del umbral = consultas ≤ 2 s / consultas medidas × 100 | ≥ 95 % con 25 usuarios concurrentes, 1.000 clientes, 10.000 proyectos y 50.000 tareas | Informe de 1.000 consultas del entorno de pruebas | Semana 10 y antes de cada versión mayor | Tecnología | Analizar consultas, índices y capacidad; repetir la prueba |
| IC-03 | Exactitud de migración = registros válidos en destino / registros de la muestra × 100 | ≥ 98 % de 100 clientes, 30 proyectos y 50 incidencias | Conciliación origen–destino y registro de errores | Semana 11 y cada migración | Responsable de datos + QA | Corregir mapeos, depurar datos y volver a importar |
| IC-04 | Reducción del tiempo de informe = (tiempo base − tiempo SIGPC) / tiempo base × 100 | ≥ 35 % en diez escenarios equivalentes | Medición de semana 2 y acta del piloto | Semana 12 y trimestral | Líder del proyecto + Dirección | Revisar flujo, automatización y diseño del informe |
| IC-05 | Adopción = usuarios capacitados / usuarios designados × 100; práctica = operaciones correctas / operaciones propuestas × 100 | 100 % de los 10 usuarios capacitados y ≥ 80 % en la práctica | Asistencia y resultados de práctica guiada | Antes del piloto y ante cambios relevantes | Líder + Soporte e infraestructura | Reforzar capacitación y repetir la práctica |
| IC-06 | Cumplimiento de hitos = hitos finalizados en fecha / hitos finalizados × 100 | ≥ 90 % | Fechas previstas y reales del SIGPC | Semanal y al cierre | Responsable de proyecto | Replanificar, reasignar capacidad y registrar causa |
| IC-07 | Desvío de esfuerzo = abs(horas reales − horas previstas) / horas previstas × 100 | ≤ 15 % por proyecto | Tareas y registros de horas | Semanal | Tecnología + Dirección | Revisar estimaciones, alcance y bloqueos |
| IC-08 | Cumplimiento de SLA = incidencias resueltas dentro del plazo / incidencias resueltas × 100 | ≥ 90 %; críticas ≤ 8 h, altas ≤ 24 h y medias ≤ 48 h hábiles | Incidencias, prioridad y marcas temporales | Semanal y mensual | Soporte | Escalar, reasignar y realizar análisis de causa raíz |

## Estándares de auditoría técnica

| Dimensión | Estándar | Evidencia verificable |
|---|---|---|
| Integridad | CUIT y correo de usuario únicos; claves foráneas válidas; registros históricos sin eliminación física | Restricciones de base de datos y pruebas de integridad |
| Trazabilidad | Todo cambio de estado conserva usuario, fecha, valor anterior y valor nuevo | Bitácora de auditoría consultable |
| Acceso | Permisos por rol y principio de mínimo privilegio; usuarios inactivos sin acceso | Matriz de permisos y revisión trimestral |
| Respaldo | Copia diaria y prueba mensual de restauración | Registro de ejecución y acta de restauración |
| Calidad de cambios | La rama estable recibe cambios mediante Pull Request revisado; no se aceptan defectos bloqueantes | Historial de ramas, PR, revisión y pruebas |
| Disponibilidad de datos | Los informes utilizan una misma fuente y permiten rastrear el dato original | Consultas del panel y enlaces a registros de origen |

## Ciclo de control

1. Medir el indicador con la fuente definida.
2. Comparar el resultado con la meta.
3. Registrar el desvío y su causa.
4. Asignar una acción correctiva con responsable y fecha.
5. Repetir la medición y conservar la evidencia.

El control no se limita a informar resultados: cada indicador debe activar una decisión concreta cuando no alcanza el estándar previsto.

