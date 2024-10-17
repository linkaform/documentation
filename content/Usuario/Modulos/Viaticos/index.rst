.. _doc-viaticos:

================
Módulo Viáticos
================

El **Módulo de Viáticos** proporciona elementos y configuraciones para administrar el proceso completo de solicitud, autorización, registro de viáticos y gastos relacionados con viajes o fondos asignados como caja chica para empleados.

A continuación, se describe el flujo del proceso del módulo de viáticos, tal como se muestra en el diagrama adjunto.

1. **Solicitud de Viáticos**: El proceso comienza con la creación de una **Solicitud de Viáticos**. Esta solicitud genera un folio de viaje, asignando un presupuesto específico del cual se irán descontando los gastos.

2. **Autorización de Viáticos**: Una vez creada la solicitud, esta pasa por un proceso de **Autorización de Viáticos**. La autorización se realiza desde la misma solicitud, permitiendo el control inmediato del presupuesto asignado.

3. **Entrega de Anticipo**: Después de la autorización, se procede a la **Entrega de Anticipo en Efectivo**, en caso de haberlo solicitado. Este registro se crea automáticamente y actualiza el estatus de la solicitud a ``Autorizado``.

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

Formularios del Módulo Viáticos
===============================

Los formularios que componen el módulo de viáticos son los siguientes:

- **Solicitud de Viáticos**: Permite a los empleados solicitar un monto económico para el gasto de viáticos.
- **Entrega de Efectivo**: Registra la entrega de anticipos en efectivo, en caso de que se hay solicitado efectivo.
- **Reservas de Viáticos**: Facilita la reserva de aspectos logísticos del viaje, como transporte, alojamiento y comida.
- **Registros de Gastos**: Permite a los empleados registrar los gastos incurridos durante el viaje. 
- **Autorización de Viáticos**: Utilizado por el área administrativa para verificar y aprobar todos los gastos registrados una vez que el viaje ha finalizado y todos los gastos han sido reportados.

Para acceder a las formas, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Viáticos``.

.. image:: /imgs/Modulos/Viaticos/Viaticos30.png

.. _solicitud-viaticos:

Solicitud de Viáticos
---------------------

Esta forma está diseñada para ser utilizada tanto por el **empleado** que realiza la solicitud del monto económico para los viáticos del viaje como por el **autorizador** que aprueba dicha solicitud.

Siga el flujo para comprender el proceso que ocurre al responder la forma.

1. **El empleado** realiza una **solicitud de viáticos** mediante la forma **Solicitud de Viáticos**.
2. La solicitud pasa a un estado de **Solicitado**.
3. El **responsable** revisa la solicitud y puede autorizarla.
4. Si la solicitud es autorizada, cambia su estado a **Autorizado**.
5. Una vez autorizada:

   - La solicitud genera un folio de viaje, la cual contiene toda la información de la solicitud.
   - Se genera un registro en la forma `Entrega de Efectivo <#entrega-efectivo>`_ :octicon:`report;1em;sd-text-info` solo si se solicita y se asigna al responsable seleccionado.
   - Se genera un registro en la forma `Reservas de Viaje <#reservas-viajes>`_ :octicon:`report;1em;sd-text-info`.
   - Se genera un registra en el catálogo `Solicitudes de Gastos <#solicitudes-gastos>`_ :octicon:`report;1em;sd-text-info`.

Observe y analice el siguiente diagrama y consulte los puntos anteriores:

.. image:: /imgs/Modulos/Viaticos/Viaticos29.png

Consulte la estructura de la forma. La cual se compone de tres secciones principales:

.. tab-set::

    .. tab-item:: Generales

        Esta sección contiene los detalles básicos de la solicitud, como quién, cuándo, cuánto y para qué se solicitan los viáticos.

        Campos a rellenar por el **empleado**:

        **Empleado**: Nombre del empleado que hace la solicitud 
        
        .. seealso:: La lista de empleados es configurable, revise el catálogo **Empleados** del :ref:`doc-employee` :octicon:`report;1em;sd-text-info` para más detalles.

        .. image:: /imgs/Modulos/Viaticos/Viaticos11.png

        **Destino**: Ubicación al cual se dirige el empleado.

        .. seealso:: La lista de estados no se limita a las actuales, para más detalles consulte el catálogo **Estados** del :ref:`doc-base` :octicon:`report;1em;sd-text-info`.

        .. image:: /imgs/Modulos/Viaticos/Viaticos12.png

        **Motivo**: Motivo de la solicitud de viáticos. Si no encuentra un motivo en la lista de opciones, seleccione ``Otros``. 

        .. seealso:: El listado de motivos es configurable y puede modificarse según lo requiera. Consulte la sección `conceptos de gastos <#conceptos-gastos>`_ :octicon:`report;1em;sd-text-info` para más detalles.
 
        .. image:: /imgs/Modulos/Viaticos/Viaticos13.png

        **Fecha de Salida**: Fecha en que el empleado saldrá.

        .. image:: /imgs/Modulos/Viaticos/Viaticos14.png

        **Fecha de Regreso**: Fecha en que el empleado regresará.

        .. image:: /imgs/Modulos/Viaticos/Viaticos15.png

        **Cantidad de días**: Calculado automáticamente basado en las fechas de salida y regreso.

        .. image:: /imgs/Modulos/Viaticos/Viaticos16.png

        **Medio de transporte**: Medio de transporte que utilizará.

        .. image:: /imgs/Modulos/Viaticos/Viaticos17.png

        **Moneda**: Denominación en la que se solicita el viático. 

        .. seealso:: Consulte el catálogo `moneda <#denominacion-moneda>`_ :octicon:`report;1em;sd-text-info` para más detalles. 

        .. image:: /imgs/Modulos/Viaticos/Viaticos18.png

        **Monto solicitado**: Presupuesto estimado para cubrir los gastos del viaje.

        .. image:: /imgs/Modulos/Viaticos/Viaticos19.png

        **Anticipo en efectivo solicitado**: Indica si se requiere un anticipo en efectivo como parte del presupuesto. 
        
        .. warning:: Si no requiere de algún anticipo en efectivo, indique el campo como vacío o con el valor de 0.
        
        .. image:: /imgs/Modulos/Viaticos/Viaticos22.png

        **Autorizar por**: Responsable que autorizará la solicitud.

        .. seealso:: Para agregar o modificar un responsable consulte el catálogo **Empleados Jefes Directos** del :ref:`doc-employee` :octicon:`report;1em;sd-text-info` 

        .. important:: Al enviar el registro, Linkaform asignará automáticamente el registro de la solicitud al responsable seleccionado para su autorización.

        .. image:: /imgs/Modulos/Viaticos/Viaticos21.png

        **Firma del empleado solicitante**: Firma del solicitante. 
        
        Para firmar siga estos pasos:

        1. Escriba algún indicador que identifique su firma.
        2. Presione el botón ``Aceptar firma`` y espere a que la firma se cargue.

        .. image:: /imgs/Modulos/Viaticos/Viaticos23.png

        **Status**: Estado de la solicitud.

        .. warning:: De manera predeterminada, el estatus será ``Solicitado``. No modifique este estatus bajo ninguna circunstancia. 
            
            Finalmente, envíe la solicitud presionando el botón **Enviar a Aprobación** o el botón flotante a la derecha de su pantalla. Posteriormente, deberá esperar a que el responsable designado revise y autorice su solicitud de viáticos.

        .. image:: /imgs/Modulos/Viaticos/Viaticos24.png

        Campos para el **autorizador**:

        Para visualizar el registro de la solicitud de viáticos, siga estos pasos:

        1. Seleccione el botón de ``Inbox`` en la esquina inferior izquierda de su pantalla.
        2. Identifique el inbox asignado.
        3. Presione ``Editar`` para abrir el registro.

        .. image:: /imgs/Modulos/Viaticos/Viaticos27.png

        4. Revise la solicitud y edite los siguientes campos:

        **Monto autorizado**: Cantidad del monto solicitado que se aprueba.

        .. note:: Si considera que la cantidad solicitada no es la adecuada, escriba la cifra que autoriza. Si coincide con el monto solicitado, coloque la misma cifra.

        .. image:: /imgs/Modulos/Viaticos/Viaticos25.png

        **Firma del autorizador**: Firma de confirmación para autorizar los viáticos.

        Para firmar siga estos pasos:

        1. Escriba algún indicador que identifique su firma.
        2. Presione el botón ``Aceptar firma`` y espere a que la firma se cargue.

        .. image:: /imgs/Modulos/Viaticos/Viaticos26.png

        **Status**: Estado actual de la solicitud.

        .. warning:: Al recibir la solicitud de viáticos, el estatus será ``Solicitado``. 
            
            - Presione el botón ``Autorizar`` si está de acuerdo con la solicitud.
            - Utilice el botón ``Cerrar Solicitud`` **solo** cuando se haya finalizado el proceso de aprobación del gasto.
            
            Para enviar el registro, presione el botón flotante ubicado en la esquina derecha de su pantalla.

        .. image:: /imgs/Modulos/Viaticos/Viaticos28.png

    .. tab-item:: Gastos
        
        Esta sección muestra detalles de todos los montos y gastos actuales del empleado.

        .. attention:: Esta sección está oculta para el empleado y visible únicamente para los responsables. Los registros se generan automáticamente solo cuando se autoriza la solicitud. No modifique esta parte bajo ninguna circunstancia si la visualiza.
            
        Campos incluidos:

        - **Folio**: Identificador de la solicitud de viáticos.
        - **Anticipo efectivo**: Efectivo entregado anticipadamente.
        - **Gasto efectivo**: Gasto realizado con el efectivo entregado.
        - **Gasto por empleado**: Gastos pagados directamente por el empleado.
        - **Gasto a nombre de compañía**: Gastos pagados directamente por la empresa.
        - **Saldo a favor del empleado**: Monto adicional gastado por el empleado que la empresa debe reembolsar.
        - **Presupuesto restante**: Dinero disponible restante del presupuesto autorizado.

        .. image:: /imgs/Modulos/Viaticos/Viaticos31.png

        El grupo repetitivo refleja los movimientos de los gastos generados desde la forma `Registros de Gastos <#registros-gastos>`_ :octicon:`report;1em;sd-text-info`.

        .. image:: /imgs/Modulos/Viaticos/Viaticos32.png
        
        Para entender mejor los campos, considere el siguiente ejemplo:

        .. admonition:: Ejemplo
            :class: pied-piper

            Un empleado debe ir a CDMX para una cita con un cliente y solicita un viático de $5,000. La empresa reserva un hotel por $2,000, que se registra como gasto a nombre de la compañía. El empleado utiliza los $5,000 para cubrir otros gastos, pero debe quedarse un día más, gastando $2,000 adicionales de su propio dinero. Estos $2,000 se registran como saldo a favor del empleado para reembolso posterior.

    .. tab-item:: Configuración

        Esta sección permite ajustar la configuración relacionada con el presupuesto. Por defecto, la configuración está definida para evitar sobregiros. Modifique según sea necesario.

        .. attention:: Esta sección está oculta para el empleado y visible únicamente para los responsables.             

        Campos de configuración:

        **Puede ser sobregirada**: Permite registrar gastos adicionales si el presupuesto se ha agotado.

        .. image:: /imgs/Modulos/Viaticos/Viaticos33.png

        **Límite de sobregiro**: Especifica el monto máximo permitido para el sobregiro. Si está vacío, no hay límite.

        .. image:: /imgs/Modulos/Viaticos/Viaticos34.png

        **Cerrar solicitud en sobregiro**: Permite cerrar la solicitud cuando se alcanza el límite de sobregiro.

        .. image:: /imgs/Modulos/Viaticos/Viaticos35.png

.. _entrega-efectivo: 

Entrega de Efectivo
-------------------

Esta forma está diseñada para que algún departamento o responsable realice la entrega del efectivo solicitado al empleado. La mayoría de los campos vienen prellenados con la información proveniente de la solicitud de viáticos.

.. note:: Si en la `solicitud de viáticos <#solicitud-viaticos>`_ :octicon:`report;1em;sd-text-info` no se ha solicitado un monto en efectivo, no se creará un registro en esta forma. 

Para visualizar al registro de la entrega de efectivo, siga estos pasos:

1. Seleccione el botón ``Inbox`` en la esquina inferior izquierda de su pantalla.
2. Identifique el inbox asignado.
3. Presione ``Editar`` para abrir el registro.
4. Revise la solicitud y actualice los siguientes campos:

.. hint:: Observe que el folio es el mismo que el de la solicitud de viáticos. Este folio permite extraer y mostrar toda la información prellenada en está forma.

    .. image:: /imgs/Modulos/Viaticos/Viaticos36.png

**Fecha del Anticipo**: Fecha actual de entrega del anticipo.

.. image:: /imgs/Modulos/Viaticos/Viaticos37.png

**Anticipo entregado**: Cantidad del monto solicitado que se aprueba.

.. note:: Si considera que la cantidad solicitada no es la adecuada, escriba la cifra que autoriza. Si coincide con el monto solicitado, coloque la misma cifra.

.. image:: /imgs/Modulos/Viaticos/Viaticos38.png

**Método de pago**: Método utilizado para realizar la entrega del anticipo.

.. image:: /imgs/Modulos/Viaticos/Viaticos39.png

**Comprobantes**: Documentación que respalda la entrega del anticipo.

.. image:: /imgs/Modulos/Viaticos/Viaticos40.png

**Status del Anticipo**: Estado actual del proceso de entrega del anticipo.

.. warning:: Por defecto, el estatus será ``En Proceso``. Cambie el estado presionando el botón ``Realizado`` si está conforme.

.. image:: /imgs/Modulos/Viaticos/Viaticos41.png

Finalmente, envíe la entrega de efectivo presionando el botón flotante a la derecha de su pantalla.

.. note:: Cuando se autoriza y entrega el monto de efectivo solicitado, se refleja en la sección de **Gastos** de la `forma solicitud de viáticos <#solicitud-viaticos>`_ :octicon:`report;1em;sd-text-info` y en el `catálogo Solicitudes de Gastos <#solicitudes-gastos>`_ :octicon:`report;1em;sd-text-info`. Observe las siguientes imágenes:

    .. image:: /imgs/Modulos/Viaticos/Viaticos42.png

    .. image:: /imgs/Modulos/Viaticos/Viaticos43.png

.. _reservas-viajes:

Reservas de Viajes
--------------------

Este formulario facilita la reserva de aspectos logísticos del viaje, como transporte y alojamiento. Aunque **no es obligatorio**, la idea es que cuando un empleado haga una solicitud de viaje, un responsable de logística o personal de la empresa reserve el medio de transporte y el hospedaje del empleado al llegar a su destino. Esta forma se divide en tres partes:

.. tab-set::

    .. tab-item:: Generales

        Contiene la información que identifica al empleado, fechas y destino del viaje. Observe el registro:

        .. note:: Esta sección ya viene prellenada.

        .. image:: /imgs/Modulos/Viaticos/Viaticos44.png

    .. tab-item:: Reservas de Transporte

        En esta sección debe colocar los datos del servicio del transportista que recogerá al empleado. Es similar a un servicio tipo ``Uber``. Los campos que la componen son:

        **Proveedor**: Nombre de la empresa de transporte.

        .. image:: /imgs/Modulos/Viaticos/Viaticos48.png

        **Dirección de Origen del Servicio**: La ubicación de donde recogerán al empleado.

        .. image:: /imgs/Modulos/Viaticos/Viaticos46.png

        **Dirección del Servicio**: La geolocalización de la ubicación del transportista, como su estación.

        .. image:: /imgs/Modulos/Viaticos/Viaticos47.png
        
        **Fecha y Hora Programada**: Fecha y hora en la que debe recoger al empleado.

        .. image:: /imgs/Modulos/Viaticos/Viaticos48.png

        .. grid:: 2
            :gutter: 0

            .. grid-item-card:: 
                :columns: 4

                .. image:: /imgs/Modulos/Viaticos/Viaticos49.png

            .. grid-item-card:: 
                :columns: 8

                - **Teléfono del Usuario**: Número de contacto del empleado.
                - **Número de Reservación**: Identificador de la reservación del transporte.
                - **Nombre del Chofer**: Nombre del conductor asignado.
                - **Teléfono del Chofer**: Número de contacto del conductor.
                - **Vehículo del Chofer**: Descripción del vehículo del conductor.
                - **Placas del Vehículo**: Matrícula del vehículo del conductor.
                - **Comprobante/Boleto**: Archivo del comprobante del servicio de transporte.

        **Estatus de la Reserva de Transporte**: Estado actual de la reserva (Pendiente o Confirmada).

        .. image:: /imgs/Modulos/Viaticos/Viaticos50.png

    .. tab-item:: Reservas de Hotel

        En esta sección debe colocar los datos del servicio del hotel en el que se quedará el empleado. Los campos son:

        - **Nombre del Hotel**: Nombre del hotel donde se hospedará el empleado.
        - **Número de Reservación**: Identificador de la reservación del hotel.
        - **Fecha de Entrada**: Fecha de check-in en el hotel.
        - **Fecha de Salida**: Fecha de check-out del hotel.
        - **Estatus de la Reserva del Hotel**: Estado actual de la reserva (Pendiente o Confirmada).
        - **Comprobante de Reservación del Hotel**: Archivo del comprobante de la reservación del hotel.

        .. image:: /imgs/Modulos/Viaticos/Viaticos51.png

.. _form-registro-gastos: 

Registros de Gastos
-------------------

Esta forma está diseñada para ser utilizada tanto por el **empleado** que realiza el registro del gasto como por el **autorizador** que aprueba dicho gasto.

Este formulario permite a los empleados registrar los gastos incurridos durante el viaje. Del monto autorizado en la solicitud `de viáticos <#solicitud-viaticos>`_ :octicon:`report;1em;sd-text-info` se empezarán a descontar. A continuación, se detalla cómo llenar los campos:
 
Campos para el empleado que gasta:

**Fecha del gasto**: Fecha en que se realizó el gasto.

.. image:: /imgs/Modulos/Viaticos/Viaticos52.png

**Solicitud de Gastos**: Este catálogo muestra únicamente los viajes activos.

- **Destino**: Seleccione el destino para el cual se solicitó el viático.
- **Folio**: Seleccione el folio correspondiente.

.. hint:: Si hay más de un folio, identifique el folio de la solicitud de viáticos y compárelo con el del catálogo. 
    
.. image:: /imgs/Modulos/Viaticos/Viaticos53.png

.. note:: Cuando realice un gasto, el catálogo le proporcionará información actualizada sobre los montos restantes y los gastos ejecutados. Observe el siguiente ejemplo, donde el gasto ejecutado es de $3,250 y el monto restante es de $750.

    .. image:: /imgs/Modulos/Viaticos/Viaticos64.png

**Concepto**: Seleccione un concepto de gasto.

.. note:: Dependiendo del concepto, variarán los campos adicionales. Sin embargo, hay ciertos campos obligatorios para todos los conceptos:

    - **Comercio**: Nombre del comercio donde se realizó el gasto.
    - **Detalle del gasto**: Descripción adicional del gasto.

    Por ejemplo, si selecciona el concepto de comida, aparecerá el campo ``Tipo de comida``.

    .. image:: /imgs/Modulos/Viaticos/Viaticos54.png

**Moneda**: Denominación en la que se solicita el viático.

.. note:: La denominación no siempre puede ser la misma con la que solicitó el viático. Puede solicitar un viático en una moneda y gastar en otro tipo de moneda, lo cual es regular si sale fuera del país.
    
.. image:: /imgs/Modulos/Viaticos/Viaticos55.png

**Subtotal**: Monto total del gasto, incluyendo impuestos y propinas.

.. image:: /imgs/Modulos/Viaticos/Viaticos56.png

.. **Total gasto**: Monto total del gasto, incluyendo impuestos y propinas.
.. .. image:: /imgs/Modulos/Viaticos/Viaticos57.png

**Pagado por**

- **Empleado**: Gasto pagado con dinero del empleado. Considerado para reembolso.
- **Compañía**: Gasto pagado con dinero de la compañía, utilizando el anticipo proporcionado por la empresa.

.. important:: Regularmente, **Pagado por empleado** se selecciona cuando ha agotado el presupuesto del viático y aún tiene gastos adicionales. En este caso, los gastos registrados serán reembolsados posteriormente. 
    
    Es importante comprender que esta opción depende de la configuración del sobregiro en la solicitud del viatico. Si la configuración permite sobregiros, podrá seguir presentando gastos incluso si ha agotado el presupuesto de la empresa. Sin embargo, si no se permite el sobregiro, esta opción no estará disponible. 

.. image:: /imgs/Modulos/Viaticos/Viaticos58.png

**Comprobante**: Archivo del comprobante del gasto (factura, ticket, etc.). El comprobante puede ser en formato de imagen o archivo. 

.. image:: /imgs/Modulos/Viaticos/Viaticos59.png

**Página para descargar factura**: URL de la página donde se puede descargar la factura, si la solicita.

.. image:: /imgs/Modulos/Viaticos/Viaticos60.png

**Status del gasto**: Estado del gasto.

.. warning:: Por defecto, el estatus está en ``Por autorizar``. Por ningún motivo lo modifique.

Finalmente, envíe la solicitud presionando el botón flotante a la derecha de su pantalla.

.. image:: /imgs/Modulos/Viaticos/Viaticos61.png

.. hint:: Cada vez que registre un gasto, podrá visualizar los detalles en la sección de **Gastos** dentro de la Solicitud de `Viáticos <#solicitud-viaticos>`_ :octicon:`report;1em;sd-text-info`. Para obtener una visión general de los montos totales sin detalles específicos, consulte el catálogo de Solicitudes `de Gastos <#solicitudes-gastos>`_ :octicon:`report;1em;sd-text-info`. Observe las siguientes imágenes, que muestran un ejemplo del primer gasto registrado.
    
    .. image:: /imgs/Modulos/Viaticos/Viaticos63.png

    .. image:: /imgs/Modulos/Viaticos/Viaticos62.png
        :height: 52px
        :width: 780px

.. important:: Dependiendo de la configuración de la solicitud, si no se permiten sobregiros, al realizar su último registro de gasto de viaje, ya no podrá continuar registrando más gastos. 
    
    En ese punto, todos los registros de gastos pasarán a la etapa de **Aprobación**, donde el departamento correspondiente revisará y aprobará sus gastos.

Campos para el autorizador:

**Total gasto en moneda solicitud**: Total del gasto convertido a la moneda en la que se solicitó el viático.

**Motivo no autorizado**: Razón por la cual el gasto no es autorizado (si aplica).

**Monto autorizado**: Cantidad del gasto que se aprueba.

**Comentarios**: Comentarios adicionales del autorizador.

.. .. _form-autorizacion:

.. Autorización de Viáticos
.. ------------------------

.. Este formulario es utilizado por el área administrativa para verificar y aprobar todos los gastos registrados una vez que el viaje ha finalizado y todos los gastos han sido reportados.

.. .. note:: Pendiente, no sincronizan los registros.

Catálogos del Módulo Viáticos
=============================

Este módulo cuenta con los siguientes catálogos:

- **Conceptos de Gastos**: Contiene registros sobre posibles conceptos de gastos.
- **Moneda**: Proporciona información sobre las diferentes monedas aceptadas para los gastos.
- **Solicitud de Gastos**: Almacena los registros de las solicitudes de viáticos realizadas por los empleados.

Para acceder a los catálogos, seleccione la opción ``Catálogos > Catálogos`` en el menú lateral y ubique la carpeta ``Viáticos``.

.. image:: /imgs/Modulos/Viaticos/Viaticos2.png

.. _conceptos-gastos:

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

.. _denominacion-moneda:

Moneda
------

Este catálogo proporciona información sobre las diferentes denominaciones aceptadas para las solicitudes y gastos relacionados. 

.. tab-set::

    .. tab-item:: Estructura

        Este catálogo incluye:

        - **Moneda**: Representa el símbolo o abreviatura utilizado para identificar la moneda (por ejemplo, USD para dólar estadounidense, COP para pesos colombianos, etc.).

        .. image:: /imgs/Modulos/Viaticos/Viaticos6.png

    .. tab-item:: Registros
        
        Para monedas distintas al peso mexicano, este catálogo ejecuta un script que consulta el tipo de cambio directamente del sitio web del Banco de México (|banxico| :octicon:`report;1em;sd-text-info`) y realizar la conversión necesaria.

        .. warning:: Al instalar el módulo, encontrará registros de las denominaciones de monedas disponibles. Si desea agregar una nueva moneda, asegúrese de verificar con nuestro equipo la disponibilidad del tipo de cambio correspondiente.

        .. image:: /imgs/Modulos/Viaticos/Viaticos5.png

.. _solicitudes-gastos:

Solicitudes de Gastos
---------------------

Este catálogo refleja los montos totales de los gastos actuales del empleado. Aquí podrá visualizar los montos totales asignados, cuánto se ha gastado y cuánto queda disponible.

.. warning:: Por ningún motivo, modifique este catálogo. Es actualizado automáticamente por un script al `registrar un gasto <#form-registro-gastos>`_ :octicon:`report;1em;sd-text-info`, el cual realiza los cálculos necesarios para reflejar la información precisa.

La estructura de este catálogo es similar a la de un registro de gastos, pero se centra en montos totales, gastos ejecutados, saldos y presupuestos restantes. Observa el siguiente ejemplo de registro:

.. image:: /imgs/Modulos/Viaticos/Viaticos62.png
    :height: 52px
    :width: 780px

.. important:: El campo más importante que debe verificar es el **estatus**. Este estado debe coincidir exactamente con el que se refleja en la solicitud de viáticos.

Cuando se realiza el último registro de gasto con el monto autorizado para el viático, el estatus cambia a **En Aprobación**.

.. image:: /imgs/Modulos/Viaticos/Viaticos65.png
   :height: 52px
   :width: 780px

Asegúrese de que el catálogo incluya el filtro necesario al instalar el módulo, especialmente si es responsable de verificar su configuración.

Si no encuentra el filtro, consulte la documentación sobre cómo :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` y aplique estos valores:

.. code-block::
    :caption: Guarde el filtro como ``Autorizados``.

    Campo = Estatus
    Condición = Igual a
    Valor = Autorizado

    //Este filtro mostrará todos los registros de los gastos autorizados.

Ha completado con éxito el proceso de configuración y utilización del módulo viáticos. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.

.. LIGAS EXTERNAS

.. |banxico| raw:: html

   <a href="https://www.banxico.org.mx/" target="_blank">banxico</a>
