# Proceso BPMN del SIGPC

## Proceso seleccionado

Se modela la **gestión integral de un proyecto de software**, desde la solicitud inicial del cliente hasta el cierre administrativo y la revisión de indicadores. Es el proceso más representativo del SIGPC porque conecta la captación comercial, el alta del proyecto, la ejecución técnica, la gestión de incidencias, la facturación y el control directivo.

Para conservar la legibilidad, el proceso se presenta en dos fragmentos unidos por un par de eventos intermedios de enlace denominados **A**. Ambos fragmentos pertenecen al mismo proceso y deben leerse de izquierda a derecha.

1. [Admisión y alta del proyecto](bpmn_01_admision_alta.svg)
2. [Ejecución, aceptación y cierre](bpmn_02_ejecucion_cierre.svg)

## Participantes

- **Cliente:** pool externo de caja negra. Inicia la solicitud, responde pedidos de información, evalúa la propuesta y la entrega, y realiza el pago.
- **Comercial:** releva requisitos, prepara propuestas y administra la respuesta del cliente.
- **SIGPC:** valida datos, crea el proyecto, notifica, publica entregas, actualiza hitos y consolida métricas.
- **Dirección:** aprueba la propuesta y revisa los indicadores finales.
- **Tecnología / Desarrollo:** planifica, ejecuta, registra horas, prueba y corrige.
- **Soporte:** recibe la validación y registra incidencias cuando la entrega no es aceptada.
- **Finanzas:** emite la factura, registra el pago y gestiona recordatorios.

## Flujo estándar

1. Comercial recibe la solicitud, releva requisitos y el SIGPC valida los datos.
2. Comercial prepara la propuesta y Dirección la aprueba.
3. El cliente acepta; el SIGPC crea el proyecto y notifica a los responsables.
4. Tecnología planifica, ejecuta y prueba la solución.
5. El SIGPC publica la entrega y Soporte recibe la validación del cliente.
6. Finanzas factura, registra el pago y el SIGPC cierra el proyecto.
7. Dirección revisa los indicadores consolidados.

## Excepciones controladas

- **Datos incompletos:** se solicita información adicional y se repite la validación.
- **Propuesta no aprobada internamente:** se ajustan alcance y costo y vuelve a evaluarse.
- **Cambios pedidos por el cliente:** se ajusta la propuesta y se reinicia su aprobación.
- **Propuesta rechazada:** se registra el resultado y finaliza esa instancia.
- **Pruebas fallidas:** se corrigen defectos y se repiten las pruebas.
- **Entrega no aceptada:** Soporte registra una incidencia, Tecnología corrige y se realiza una nueva entrega.
- **Pago no acreditado:** se envía un recordatorio, se espera el vencimiento y se verifica nuevamente.

## Convenciones verificadas

- Los flujos de secuencia permanecen dentro del pool de Multitronik.
- Los intercambios con el cliente se representan con flujos de mensaje discontinuos.
- Las decisiones utilizan compuertas exclusivas y cada salida está rotulada.
- Las tareas automatizadas se asignan al lane del SIGPC.
- Los caminos excepcionales regresan a una actividad válida o finalizan de forma explícita.

Los SVG son vectoriales y pueden ampliarse sin pérdida de calidad. Se regeneran con `python tools/generar_bpmn.py`.

