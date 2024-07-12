.. _doc-viaticos:

================
Módulo Viáticos
================

El **Módulo de Viáticos** gestiona y administra el proceso completo de solicitud, autorización, registro de viáticos y gastos relacionados con viajes o fondos asignados como caja chica para empleados.

A continuación, se describe el flujo del proceso del módulo de viáticos, tal como se muestra en el diagrama adjunto.

1. **Solicitud de Viáticos**: El proceso comienza con la creación de una **Solicitud de Viáticos**. Esta solicitud genera un folio de viaje, asignando un presupuesto específico del cual se irán descontando los gastos.

2. **Autorización de Viáticos**: Una vez creada la solicitud, esta pasa por un proceso de **Autorización de Viáticos**. La autorización se realiza desde la misma solicitud, permitiendo el control inmediato del presupuesto asignado.

3. **Entrega de Anticipo**: Después de la autorización, se procede a la **Entrega de Anticipo en Efectivo**, en caso de haberlo solicitado. Este registro se crea automáticamente y actualiza el estatus de la solicitud a "Autorizado".

4. **Reserva de Viajes**: De manera paralela, se puede proceder con la **Reserva de Viajes**, asegurando que todos los aspectos logísticos del viaje estén cubiertos.

5. **Registros de Gastos de Viaje**: Durante el viaje, los gastos se registran en la la forma **Registros de Gastos de Viaje**. En la **solicitud de viáticos** podrá visualizar un resumen de todos los gastos realizados.

6. **Autorización Final de Viáticos**: Una vez que todos los gastos están registrados y la solicitud llega a cero (o se cierra el viaje), se realiza una **Autorización Final de Viáticos**. Esta autorización es realizada por un área administrativa, la cual verifica y aprueba los gastos.

7. **Cierre del Proceso**: Finalmente, el proceso se cierra una vez que todos los gastos han sido autorizados y registrados, asegurando un control completo y detallado de los viáticos.

Observe y analice el siguiente diagrama del módulo viáticos y siga los puntos anteriores:

.. image:: /imgs/Modulos/Viaticos/Viaticos1.png

.. warning:: Antes de utilizar el módulo, asegúrese de tener instalados y configurados los registros necesarios del :ref:`doc-base` :octicon:`report;1em;sd-text-info` y del :ref:`doc-employee` :octicon:`report;1em;sd-text-info`.

.. .. mermaid::

    graph TD;
        subgraph Flujo_Módulo_Empleados;
            4[EMPLEADOS] --> |Sincroniza registro| 4.1[CATÁLOGO Empleados];
            4.2[CATÁLOGO Empleados Jefes Directos] --> |Sincroniza registro| 4.1;
            4.1 --> |Sincroniza registro| 4;
            4 --> M[MODULO Contacto];
            3[Configuración de Departamentos y Puestos] --> |Sincroniza registro| 4;
            4 --> 3;
            1[CATÁLOGO Departamentos] --> 3;
            2[CATÁLOGO Puestos] --> 3;
            3.1[CATÁLOGO Configuración de Departamentos y Puestos] --> 3;
            4 --> 3.1;
            3.1 --> 4;
            4 --> 1;
            4 --> 2;
            4.1 --> 4.2;
        end;
        T[CATÁLOGO Teams];


Catálogos del Módulo Viáticos
=============================

Este módulo cuenta con los siguientes catálogos:

- **Conceptos de Gastos**: Contiene registros sobre posibles conceptos de gastos.
- **Moneda**: Proporciona información sobre las diferentes monedas aceptadas para los gastos.
- **Responsables de Autorizar Gastos**: Incluye una lista de responsables que pueden autorizar y gestionar los gastos.
- **Solicitud de Gastos**: Almacena los registros de las solicitudes de viáticos realizadas por los empleados.

.. image:: /imgs/Modulos/Viaticos/Viaticos2.png

Conceptos de Gastos
-------------------

Este catálogo registra los diferentes tipos de gastos que pueden ser solicitados por los empleados dentro de una solicitud de gasto. 

.. tab-set::

    .. tab-item:: Estructura

        Este catálogo incluye los siguientes campos principales:

        - **Concepto**: Describe el tipo de gasto o el motivo por el cual se realiza la solicitud del gasto.
        - **Cuenta Contable**: Especifica la cuenta contable asociada al concepto de gasto, si corresponde.

        .. image:: /imgs/Modulos/Viaticos/Viaticos4.png

    .. tab-item:: Registros

        .. note:: Al instalar el módulo, encontrará registros de posibles conceptos de gasto. Considere que son solo opciones y siempre puede modificar los campos del catálogo y/o registros. 

        .. image:: /imgs/Modulos/Viaticos/Viaticos3.png

Moneda
------

Este catálogo proporciona información sobre las diferentes denominaciones aceptadas para los gastos relacionados. 

.. tab-set::

    .. tab-item:: Estructura

        Este catálogo incluye:

        - **Moneda**: Representa el símbolo o abreviatura utilizado para identificar la moneda (por ejemplo, USD para dólar estadounidense, COP para pesos colombianos, etc.).

        .. image:: /imgs/Modulos/Viaticos/Viaticos6.png

    .. tab-item:: Registros
        
        Para monedas distintas al peso mexicano, este catálogo ejecuta un script que consulta el tipo de cambio directamente del sitio web del Banco de México (|banxico| :octicon:`report;1em;sd-text-info`) y realizar la conversión necesaria.

        .. warning:: Al instalar el módulo, encontrará registros de las denominaciones de monedas disponibles. Si desea agregar una nueva moneda, asegúrese de verificar con nuestro equipo la disponibilidad del tipo de cambio correspondiente.

        .. image:: /imgs/Modulos/Viaticos/Viaticos5.png

.. _responsable-autorizador:

Responsables de Autorizar Gastos
--------------------------------

Este catálogo contiene información sobre las personas responsables de autorizar y gestionar los gastos, como jefes de departamento, finanzas o recursos humanos.

.. note:: Este catálogo es adecuado si no requiere muchas especificaciones sobre el responsable de autorizar los gastos. Sin embargo, si necesita más detalles sobre dicho responsable, utilice el :ref:`doc-employee` :octicon:`report;1em;sd-text-info`.

.. tab-set::

    .. tab-item:: Estructura

        Este catálogo incluye campos como:

        - **Nombre**: Responsable de autorizar gastos.                                                                                                                                   
        - **Correo Electrónico**: Dirección de correo electrónico del responsable.

        .. image:: /imgs/Modulos/Viaticos/Viaticos8.png

    .. tab-item:: Registros

        .. warning:: Revise la veracidad de los datos de este catálogo, ya que son utilizados para notificar y asignar registros al responsable y autorizar los gastos.

        .. image:: /imgs/Modulos/Viaticos/Viaticos7.png

Solicitud de Gastos
-------------------

Este catálogo contiene todas las solicitudes autorizadas. Aquí se reflejan todos los gastos del empleado relacionados con cada solicitud. 

Es útil para visualizar la matemática de los gastos, ya que permite ver el monto total asignado, cuánto se ha gastado y cuánto queda disponible.

.. tab-set::

    .. tab-item:: Estructura
        
        El catálogo **Solicitud de Gastos** incluye los siguientes campos:

        .. .. image:: /imgs/Modulos/Viaticos/Viaticos9.png

    .. tab-item:: Registros

        Ejemplo de registros en el catálogo de **Solicitud de Gastos**:

        .. important:: Este catálogo se actualiza automáticamente a partir de los registros de la forma `solicitud de gastos <#form-solicitud-gastos>`_ :octicon:`report;1em;sd-text-info`, la cual realizará los cálculos necesarios para reflejarlos en este catálogo.

        .. .. image:: /imgs/Modulos/Viaticos/Viaticos10.png

        Observe que el catálogo cuenta con un filtro. Verifique que el catálogo tenga el filtro necesario al instalar el módulo.

        Si no encuentra el filtro, consulte la documentación sobre cómo :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` y aplique estos valores:

        .. code-block::
            :caption: Guarde el filtro como ``Autorizados``.

            Campo = Estatus
            Condición = Igual a
            Valor = Autorizado

            //Este filtro mostrará todos los registros de los gastos autorizados.

Formularios del Módulo Viáticos
===============================

Los formularios que componen el módulo de viáticos son los siguientes:

- **Solicitud de Viáticos**: Permite a los empleados solicitar un monto económico para el gasto de viáticos.
- **Entrega de Efectivo**: Registra la entrega de anticipos en efectivo, en caso de que se hay solicitado efectivo.
- **Reservas de Viáticos**: Facilita la reserva de aspectos logísticos del viaje, como transporte, alojamiento y comida.
- **Registros de Gastos**: Permite a los empleados registrar los gastos incurridos durante el viaje. 
- **Autorización de Viáticos**: Utilizado por el área administrativa para verificar y aprobar todos los gastos registrados una vez que el viaje ha finalizado y todos los gastos han sido reportados.

Para estructurar el contenido sobre la **Solicitud de Viáticos** de manera clara y concisa, se pueden utilizar secciones y subsecciones. A continuación, te presento una estructura mejorada que incorpora las ideas mencionadas:

Solicitud de Viáticos
---------------------

La forma **Solicitud de Viáticos** permite a los empleados crear una solicitud de viáticos, generando un folio de viaje y asignando un presupuesto específico del cual se irán descontando los gastos. Esta forma está diseñada para ser utilizada tanto por el empleado que realiza la solicitud como por el autorizador que aprueba la solicitud.

1. **Creación de Solicitud**: El empleado realiza la solicitud de viáticos.
2. **Asignación al Autorizador**: La solicitud se envía al autorizador a través del inbox.
3. **Autorización**: El autorizador revisa y aprueba la solicitud de viáticos.

La solicitud de viáticos se compone de tres secciones principales:

.. tab-set::

    .. tab-item:: Generales

        Esta sección contiene los detalles básicos de la solicitud, como quién, cuándo, cuánto y para qué se solicitan los viáticos.

        Campos a rellenar por el empleado:
        - **Empleado**: Nombre del empleado que hace la solicitud (usa el catálogo **Empleados** del :ref:`doc-employee` :octicon:`report;1em;sd-text-info`).

        - **Destino**: Destino al cual se dirige el empleado (usa el catálogo **Estados** del :ref:`doc-base` :octicon:`report;1em;sd-text-info`).

        - **Motivo**: Motivo de la solicitud de viáticos.
        - **Fecha de Salida**: Fecha en que el empleado saldrá.
        - **Fecha de Regreso**: Fecha en que el empleado regresará.
        - **Cantidad de días**: Calculado automáticamente basado en las fechas de salida y regreso.
        - **Medio de transporte**: Medio de transporte que se utilizará.
        - **Moneda**: Moneda en la que se solicita el viático. Permite seleccionar la moneda adecuada y realizar conversiones automáticas.
        - **Monto solicitado**: Presupuesto estimado para cubrir los gastos del viaje.
        - **Autorizar por**: Responsable que autorizará la solicitud (usa el catálogo **Responsables de Autorizar Gastos** :octicon:`report;1em;sd-text-info`).

        - **Anticipo en efectivo solicitado**: Indica si se requiere un anticipo en efectivo como parte del presupuesto.
        - **Firma del empleado solicitante**: Firma del solicitante.
        - **Status**: Estado de la solicitud (solicitado, autorizado, en aprobación, vencida, sobregirada, cerrada).

        Botones disponibles:

        - **Autorizar**: Solo visible para el autorizador.
        - **Enviar a Aprobación**: Envía la solicitud a la etapa de aprobación.
        - **Cerrar Solicitud**: Solo visible para el autorizador.

        Campos para el autorizador:

        - **Monto autorizado**: Cantidad del monto solicitado que se aprueba.
        - **Firma del autorizador**: Firma de confirmación para autorizar los viáticos.

    .. tab-item:: Gastos

        Esta sección muestra un resumen de todos los gastos del empleado, reflejados automáticamente desde la forma `Solicitud de Gastos <#registros-gastos>`_ :octicon:`report;1em;sd-text-info`.

        Campos incluidos:

        - **Folio**: Identificador de la solicitud de viáticos.
        - **Anticipo efectivo**: Efectivo entregado anticipadamente.
        - **Gasto efectivo**: Gasto realizado con el efectivo entregado.
        - **Gasto por empleado**: Gastos pagados directamente por el empleado.
        - **Gasto a nombre de compañía**: Gastos pagados directamente por la empresa.
        - **Saldo a favor del empleado**: Monto adicional gastado por el empleado que la empresa debe reembolsar.
        - **Presupuesto restante**: Dinero disponible restante del presupuesto autorizado.

        Ejemplo:

        Un empleado debe ir a CDMX para una cita con un cliente y solicita un viático de $5,000. La empresa reserva un hotel por $2,000, que se registra como gasto a nombre de la compañía. El empleado utiliza los $5,000 para cubrir otros gastos, pero debe quedarse un día más, gastando $2,000 adicionales de su propio dinero. Estos $2,000 se registran como saldo a favor del empleado para reembolso posterior.

    .. tab-item:: Configuración

        Esta sección permite ajustar la configuración relacionada con el presupuesto.

        Campos de configuración:

        - **Puede ser sobregirada**: Permite registrar gastos adicionales si el presupuesto se ha agotado.
        - **Límite de sobregiro**: Especifica el monto máximo permitido para el sobregiro. Si está vacío, no hay límite.
        - **Cerrar solicitud en sobregiro**: Permite cerrar la solicitud cuando se alcanza el límite de sobregiro.

        .. warning:: Cuando se crea un nuevo registro en esta forma, asegúrese de sincronizarlo con el catálogo `Solicitud de Gastos <#solicitud-de-gastos>`_ :octicon:`report;1em;sd-text-info`. Verifique que la configuración de sincronización esté correctamente definida.

.. _form-solicitud-gastos:

Solicitud de Gastos
-------------------

lorem 

Entrega de Efectivo
-------------------

Este formulario se utiliza para registrar la entrega de anticipos en efectivo. Una vez realizada la entrega, el sistema actualiza automáticamente el estatus de la solicitud a "Autorizado". Los campos principales incluyen:

- **Folio de Solicitud**: Número de identificación de la solicitud de viáticos asociada.
- **Monto Entregado**: Cantidad de dinero entregada al empleado.
- **Fecha de Entrega**: Fecha en la que se realiza la entrega del anticipo.
- **Responsable de Entrega**: Nombre de la persona que realiza la entrega del dinero.

.. image:: /imgs/Modulos/Viaticos/ViaticosEntrega.png

Reservas de Viáticos
--------------------

Este formulario facilita la reserva de aspectos logísticos del viaje, como transporte y alojamiento, asegurando que todos los elementos necesarios para el viaje estén cubiertos. Los campos principales incluyen:

- **Folio de Solicitud**: Número de identificación de la solicitud de viáticos asociada.
- **Tipo de Reserva**: Tipo de reserva realizada (por ejemplo, "Vuelo", "Hotel").
- **Proveedor**: Nombre del proveedor del servicio.
- **Costo de la Reserva**: Costo total de la reserva realizada.
- **Fecha de Reserva**: Fecha en la que se realiza la reserva.
- **Estado de la Reserva**: Estado actual de la reserva (por ejemplo, "Confirmada", "Pendiente").

.. image:: /imgs/Modulos/Viaticos/ViaticosReserva.png

.. _registros-gastos:

Registros de Gastos de Viaje
----------------------------

Este formulario permite a los empleados registrar los gastos incurridos durante el viaje. En este formulario se puede visualizar un resumen detallado de todos los gastos realizados. Los campos principales incluyen:

- **Folio de Solicitud**: Número de identificación de la solicitud de viáticos asociada.
- **Tipo de Gasto**: Tipo de gasto realizado (por ejemplo, "Comida", "Transporte").
- **Monto del Gasto**: Cantidad de dinero gastada.
- **Fecha del Gasto**: Fecha en la que se realizó el gasto.
- **Descripción del Gasto**: Detalles adicionales sobre el gasto.

.. image:: /imgs/Modulos/Viaticos/ViaticosGastos.png

Autorización de Viáticos
------------------------

Este formulario es utilizado por el área administrativa para verificar y aprobar todos los gastos registrados una vez que el viaje ha finalizado y todos los gastos han sido reportados. Los campos principales incluyen:

- **Folio de Solicitud**: Número de identificación de la solicitud de viáticos asociada.
- **Monto Total Autorizado**: Cantidad total de dinero autorizada para los gastos del viaje.
- **Estado de la Autorización**: Estado actual de la autorización (por ejemplo, "Aprobado", "Rechazado").
- **Fecha de Autorización**: Fecha en la que se realiza la autorización final.
- **Comentarios del Aprobador**: Observaciones

.. LIGAS EXTERNAS

.. |banxico| raw:: html

   <a href="https://www.banxico.org.mx/" target="_blank">banxico</a>
