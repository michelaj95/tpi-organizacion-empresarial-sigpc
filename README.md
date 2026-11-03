# Sistema Integrado de Gestión de Proyectos y Clientes (SIGPC)

Trabajo Práctico Integrador de **Organización Empresarial** — Tecnicatura Universitaria en Programación a Distancia, Universidad Tecnológica Nacional.

**Integrante:** Michela Juárez  
**Organización analizada:** Multitronik Solutions S.R.L.  
**Tablero de gestión:** PENDIENTE_PUBLICACION_TABLERO  
**Documento final:** [TPI final consolidado](docs/entregas/TPI_Final_Michela_Juarez.pdf)

## Descripción

Multitronik Solutions S.R.L. es una empresa ficticia que desarrolla soluciones de software para pequeñas y medianas empresas. El caso parte de un problema organizacional concreto: la información de clientes y proyectos está distribuida entre correos electrónicos, planillas y herramientas independientes.

El SIGPC centraliza el ciclo de vida de cada proyecto y conecta a Comercial, Tecnología, Soporte, Finanzas, Recursos Humanos y Dirección. La primera versión contempla clientes, proyectos, tareas, registro de horas, incidencias, hitos de facturación e indicadores para la toma de decisiones.

## Objetivo del proyecto

Desarrollar e implementar en doce semanas una primera versión operativa del SIGPC que reduzca cargas duplicadas, mejore la trazabilidad de tareas, horas, costos e incidencias y permita que las áreas trabajen con información consistente.

## Alcance documental

El repositorio reúne las cuatro etapas del TPI:

1. Organización y enfoque sistémico.
2. Diagnóstico FODA, objetivos y planeación temporal.
3. Estructura formal y diccionario de datos inicial.
4. Proceso BPMN, gestión colaborativa, backlog ágil y mecanismos de control.

## Proceso modelado

El BPMN representa la **gestión integral de un proyecto de software**, desde la recepción de la solicitud del cliente hasta el cierre del proyecto y la revisión de indicadores. Incluye:

- un pool externo para el Cliente;
- lanes internos para Comercial, SIGPC, Dirección, Tecnología, Soporte y Finanzas;
- tareas humanas y automatizadas;
- flujos de mensaje entre el cliente y Multitronik;
- compuertas exclusivas para datos incompletos, aprobación, aceptación de la entrega y acreditación del pago;
- ciclos de corrección y seguimiento para los casos excepcionales.

Los diagramas y su explicación se encuentran en [`docs/bpmn`](docs/bpmn/README.md).

## Backlog ágil

Las tres historias de usuario se derivan de necesidades ya identificadas en las entregas anteriores:

| ID | Historia de usuario | Estado de referencia |
|---|---|---|
| HU-01 | Como integrante de Comercial, quiero registrar clientes, solicitudes y datos obligatorios de un proyecto en el SIGPC, para que las áreas involucradas trabajen con información única y completa. | Listo |
| HU-02 | Como responsable de Tecnología, quiero planificar tareas, asignar responsables y registrar horas e incidencias, para controlar el avance y corregir desvíos antes de la entrega. | En Progreso |
| HU-03 | Como integrante de Dirección, quiero consultar indicadores consolidados de avance, tiempos, calidad y facturación, para tomar decisiones basadas en información trazable. | Por Hacer |

El detalle, los criterios de aceptación y la prioridad están documentados en [`docs/backlog.md`](docs/backlog.md).

## Control y auditoría técnica

La matriz de control conserva las metas cuantitativas definidas en la Entrega 2 y agrega controles operativos para la etapa posterior a la implementación. Incluye aceptación funcional, rendimiento, calidad de migración, reducción del tiempo de informes, capacitación, cumplimiento de plazos, desvío de esfuerzo y resolución de incidencias.

Ver [`docs/indicadores-control.md`](docs/indicadores-control.md).

## Estrategia de versionado

- `main`: versión estable y documentación aprobada.
- `docs/consolidacion-tpi`: integración y revisión de las entregas previas.
- `feature/bpmn-proceso`: modelado y documentación del proceso BPMN.
- `feature/backlog-control`: historias de usuario, tablero e indicadores.

Los cambios se integran mediante Pull Requests. La evidencia de ramas, commits y revisión se registra en [`docs/trabajo-colaborativo.md`](docs/trabajo-colaborativo.md).

## Declaración de Uso de IA

Se utilizó ChatGPT como asistente para comparar la consigna con el material de la cátedra, ordenar el documento consolidado, explorar alternativas de modelado BPMN, formular controles medibles y revisar redacción y formato. Los prompts se construyeron con restricciones explícitas: mantener el mismo caso de Multitronik y el SIGPC, conservar las decisiones de las entregas anteriores, utilizar notación BPMN estándar, reutilizar las metas cuantitativas ya aprobadas y no inventar enlaces ni evidencias de GitHub.

Los resultados no se incorporaron de manera automática. Se contrastaron con las Entregas 1, 2 y 3 y con la bibliografía de la materia; se acotó el proceso para evitar funciones ajenas al sistema; se corrigieron roles, flujos de mensaje y compuertas; se formalizaron tres historias de usuario a partir de necesidades previamente documentadas; y se verificaron manualmente coherencia, ortografía, cifras, vínculos y legibilidad de los diagramas. La autora conserva la responsabilidad intelectual sobre las decisiones y la versión final.

## Documentación

- [Backlog e historias de usuario](docs/backlog.md)
- [Indicadores y estándares de control](docs/indicadores-control.md)
- [Proceso BPMN](docs/bpmn/README.md)
- [Trabajo colaborativo y evidencias](docs/trabajo-colaborativo.md)
- [Entregas en PDF](docs/entregas/README.md)

