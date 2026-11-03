# Trabajo colaborativo con Git y GitHub

## Estructura de ramas

| Rama | Propósito | Resultado esperado |
|---|---|---|
| `main` | Mantener la versión estable | README y documentación aprobada |
| `docs/consolidacion-tpi` | Integrar y revisar las Entregas 1, 2 y 3 | PDFs y coherencia documental |
| `feature/bpmn-proceso` | Incorporar el proceso modelado | Diagramas y explicación BPMN |
| `feature/backlog-control` | Incorporar gestión ágil y control | Historias, tablero e indicadores |

## Convención de commits

Se utiliza un prefijo breve y una descripción específica en modo imperativo:

- `docs: incorporar síntesis de las entregas previas`
- `feat: modelar proceso integral del SIGPC en BPMN`
- `feat: documentar historias de usuario y criterios`
- `docs: definir indicadores y estándares de auditoría`
- `fix: corregir roles y flujos de mensaje del BPMN`

No se utilizan mensajes genéricos como “cambios”, “actualización” o “final”.

## Pull Request y revisión

**PR de integración:** https://github.com/michelaj95/tpi-organizacion-empresarial-sigpc/pull/4

La revisión debe ser realizada por una cuenta distinta de la autora. El revisor verifica:

- que los flujos de secuencia no crucen pools;
- que las interacciones con el cliente utilicen flujos de mensaje;
- que las excepciones tengan retorno o final explícito;
- que las historias conserven el formato formal;
- que las metas coincidan con la planeación previa;
- que los enlaces del README y del PDF funcionen.

Los comentarios se resuelven mediante un commit posterior y quedan visibles en la conversación del PR antes de su integración.

## Tablero

**Enlace:** https://github.com/users/michelaj95/projects/1

El tablero utiliza las columnas **Por Hacer**, **En Progreso** y **Listo**. Cada tarjeta se vincula con un issue del repositorio y conserva responsable, prioridad, estimación y criterios de aceptación.

