
Accesos
=======

El apartado de **Accesos** permite gestionar y controlar las entradas y salidas de los visitantes, así como visualizar toda la información relacionada con sus pases.

.. attention:: Este apartado está disponible únicamente cuando inicia su turno. Para acceder, presione la opción **Accesos** ubicada en el menú superior.

    .. image:: /imgs/Soter/Soter25.png

Información de Caseta
---------------------

Esta interfaz actúa como una vista previa antes de acceder al detalle de los `pases de entrada <#detalle-pase>`_ :octicon:`report;1em;sd-text-info`. Proporciona un panorama general sobre la caseta actual, donde se realizará la gestión de pases.
 
1. **Ubicación**: Le permite confirmar la ubicación y caseta en la que se encuentra actualmente.

.. warning:: Al ingresar a **Accesos**, no podrá cambiar entre casetas ni ubicaciones. 
    
    Todo el flujo de información registrada en accesos estará vinculada a la ubicación con la que inició su turno. Si desea cambiar, debe cerrar su turno e iniciar en la caseta o ubicación deseada.

2. **Información**: Muestra tarjetas (cards) con información relevante y útil para el monitoreo de la situación actual de la caseta, encontrará:
   
- **Visitas en el día**: Muestra el número total de visitas registradas en la ubicación durante el día actual.
- **Visitas dentro**: Indica la cantidad de visitas que actualmente se encuentran dentro de las instalaciones de la caseta.
- **Vehículos dentro**: Refleja el número de vehículos que han ingresado y permanecen dentro de la ubicación.
- **Salidas registradas**: Informa la cantidad de visitas que han sido registradas como salidas durante el día.

.. image:: /imgs/Soter/Soter24.png
    :width: 880px

.. _buscador-pases:

Buscar Pase por Código
----------------------

Para buscar un pase de entrada por código, siga los siguientes pasos:

1. En el campo ``Escanear pase``, escanee la invitación que le mostrará el visitante.
2. Presione el botón de lupa para buscar al visitante. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

.. image:: /imgs/Soter/Soter61.png

Buscar Pase por Lista de Pases
------------------------------

Si la visita no tiene evidencia del pase de entrada, pero está seguro de que cuenta con un pase, siga estos pasos:

1. Presione el ícono de lista ubicado en la barra buscadora.
2. Identifique al visitante por el nombre o la fotografía. Utilice el buscador en caso de tener múltiples pases.
3. Presione sobre el nombre del visitante. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

.. warning:: Al buscar un pase de entrada por QR o desde la lista, el pase debe estar **Activo**. Si, por algún motivo, el pase no aparece por los medios mencionados, considere buscarlos en los `pases temporales <#pases-temp>`_ :octicon:`report;1em;sd-text-info`.

.. image:: /imgs/Soter/Soter27.png
    :width: 500px

Buscar Pase por QR
------------------

Para buscar un pase de entrada mediante un código QR, siga estos pasos:  

1. Presione ``Escanear un pase`` y escanee el código QR que le mostrará el visitante. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.  

.. note:: El visitante deberá presentar el gafete enviado por el personal administrativo. A continuación, se muestra un ejemplo del código QR que el visitante debe mostrar:  

    .. image:: /imgs/Soter/Soter129.png  
        :width: 300px 

Habilitar Auto Acceso
---------------------

Esta funcionalidad permite registrar automáticamente el ingreso o la salida al escanear el código QR del pase de entrada.

Para habilitar el autoacceso, siga estos pasos:

1. Presione el botón ``Habilitar auto acceso``. Se abrirá la cámara del dispositivo.
2. Solicite al visitante que muestre el código QR de su pase de entrada. Una vez escaneado, el sistema registrará automáticamente el ingreso o la salida.

.. image:: /imgs/Soter/Soter128.png
    :width: 500px

.. warning:: Si el autoacceso es negado, revise los detalles del pase escaneándolo nuevamente o consultándolo en la lista de pases para verificar el motivo.

Nueva Visita
------------

Crear un nuevo pase de entrada para visitas espontáneas es un proceso sencillo. Siga los siguientes pasos:

.. note:: Esta opción solo está disponible en la interfaz donde se muestra la información de la caseta.

1. Presione ``+Nueva Visita``. Se abrirá el modal correspondiente.

.. image:: /imgs/Soter/Soter62.png

2. Complete los siguientes campos, todos son requeridos:

- **Nombre completo**: Ingrese el nombre completo de la persona que realizará la visita.
- **Fotografía**: Capture una fotografía reciente del visitante.
- **Identificación**: Capture una fotografía de una identificación oficial del visitante (INE, pasaporte, etc.) para validar su identidad.
- **Empresa**: Indique la empresa a la que pertenece la visita (si lo requiere).
- **Área que visita**: Especifique la sección o área dentro de las instalaciones que el visitante puede acceder.
- **Visita a**: Ingrese el nombre de la persona o el departamento que el visitante tiene intención de ver durante su visita.
- **Motivo de Visita**: Seleccione el tipo de perfil que tendrá la visita.

.. note:: El **tipo de perfil** define los límites y permisos de la visita. Según el perfil asignado, los requisitos varían ya que algunos perfiles requieren condiciones más estrictas que otros.

    Para pases de entrada espontáneos, es habitual seleccionar un perfil de  **visita general** o **candidatos**.

.. image:: /imgs/Soter/Soter28.png
    :width: 500px

3. Presione ``Crear`` para confirmar los datos y generar el pase de entrada. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

.. warning:: Al crear un pase de entrada, **no** se está concediendo automáticamente el acceso al visitante.

.. _pases-temp:

Pases Temporales
----------------

Los **pases temporales** corresponden a aquellas visitas cuyo pase tiene el estatus de **vencido** o **en proceso**. 
Para consultar los pases temporales, siga estos pasos:

1. Presione ``Pases temporales``. Se abrirá el modal correspondiente.

.. image:: /imgs/Soter/Soter63.png

2. Identifique al visitante por el nombre o la fotografía. Utilice el buscador en caso de tener múltiples pases.
3. Haga clic sobre el nombre del visitante. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

.. warning:: Considere que un visitante con un pase temporal no es candidato para ingresar a las instalaciones. Para ello, deberá ponerse en contacto con el personal administrativo para actualizar su estatus. Consulte :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

.. image:: /imgs/Soter/Soter29.png
    :width: 500px

.. _detalle-pase:

Detalle del Pase de Entrada
---------------------------

Un pase de entrada es una invitación generada por el personal administrativo para permitir el acceso de los visitantes a las instalaciones de la ubicación. Este pase detalla todos los requisitos que el visitante debe cumplir antes de ser autorizado para ingresar. 

.. warning:: Es su responsabilidad, como guardia de seguridad, verificar que se cumplan todos los requisitos solicitados para la visita antes de autorizar su acceso. Una vez que haya confirmado que todo está en regla, proceda a `registrar el ingreso <#registrar-visita>`_ :octicon:`report;1em;sd-text-info`.

Observe la siguiente imagen que muestra la interfaz completa:

.. image:: /imgs/Soter/Soter30.png
   :width: 880px

Revise las siguientes pestañas para obtener más detalles y casos de uso sobre cada apartado de la interfaz.

.. tab-set::

    .. tab-item:: Información personal

        En este apartado, podrá encontrar información personal de la visita, incluyendo:

        .. grid:: 2
            :gutter: 0

            .. grid-item-card::
                :columns: 6

                - **Folio**: Identificador único del pase de entrada.
                
                .. note:: El folio es distinto del código QR.

                - **Etiqueta de pase**: Ubicada en la esquina superior derecha, esta etiqueta especifica si el pase es para registrar una **Entrada** o **Salida**. 
                
                .. note:: La etiqueta cambia de acuerdo con el estado del pase.
                
                - **Fotografía**: Imagen del visitante.
                
                - **Identificación**: Imagen de una identificación del visitante.
                
                - **Nombre**: Nombre completo del visitante.
                
                - **Tipo de pase**: Especifica el tipo de pase asignado a la visita.

                .. attention:: Preste especial atención al tipo de pase, ya que determina los permisos que el visitante debe cumplir. Consulte el apartado sobre permisos y certificaciones para más detalles.

                - **Empresa**: Razón social del contratista que recibe la visita (si aplica).
                
                - **Motivo de visita**: Razón por la cual el visitante ingresa a las instalaciones.

            .. grid-item-card::
                :columns: 6

                .. image:: /imgs/Soter/Soter34.png

        - **Visita a**: Empleados dentro de la instalación a quienes el visitante se dirigirá.

        .. note:: Por cada empleado, tendrá las siguientes opciones:

            - **Llamada**: Permite realizar una llamada en caso necesario.

            .. image:: /imgs/Soter/Soter35.png
                :width: 500px

            - **Mensaje**: Facilita la comunicación con el empleado cuando sea requerido.

            .. image:: /imgs/Soter/Soter36.png
                :width: 500px

            Estas opciones suelen utilizarse para contactar a la persona que generó el pase de entrada. Si encuentra algún inconveniente relacionado con el estatus, permisos, accesos permitidos o cualquier otra situación, contacte a la persona correspondiente.

        - **Gafete y locker**: Especifica el gafete y locker asignados al visitante, estos campos varían según si se ha asignado un gafete.
        
        - **Estatus**: Este campo le permite conocer si el pase de entrada está **activo**.

        .. caution:: Si el estatus es diferente a **activo**, no podrá registrar la entrada del visitante.

        - **Vigencia del pase**: Indica la fecha de vencimiento del pase.

        - **Días disponibles**: Muestra los días en que la visita está autorizada para ingresar a las instalaciones. 
        
        .. note:: Los días permitidos se resaltan en color negro.

    .. tab-item:: Comentarios/instrucciones de visita
        
        Estos comentarios se refieren a detalles sobre la interacción con el visitante, como indicaciones para su atención, acompañamiento durante la visita, instrucciones especiales, etc.

        .. admonition:: Ejemplo
            :class: pied-piper
 
            Ejemplos de estos comentarios podrían ser: 
            
            - La visita necesita acompañamiento durante todo el recorrido
            - El visitante está interesado en revisar las instalaciones de producción.

        Para agregar un comentario, siga estos pasos:

        1. Presione el botón verde ``+Agregar comentario``.

        .. image:: /imgs/Soter/Soter37.png
            :width: 500px
            
        2. Escriba el comentario para el pase de entrada.
        3. Presione ``Agregar`` para confirmar los datos. Podrá ver el comentario en la sección correspondiente.
        
        .. image:: /imgs/Soter/Soter38.png

    .. tab-item:: Últimos accesos

        Esta sección muestra un historial reciente de las entradas y salidas del visitante. Esta sección incluye:

        - **Visitó a**: Empleado al que se dirigió el visitante.
        - **Fecha y hora**: Detalles de la fecha y hora de cada acceso.
        - **Duración**: Tiempo que el visitante permaneció en las instalaciones.
        - **Comentarios**: Notas relevantes registradas durante cada acceso, que pueden incluir instrucciones o detalles adicionales para próximas entradas.

        .. image:: /imgs/Soter/Soter39.png
            :width: 500px

        Para visualizar el comentario de un acceso, simplemente seleccione el ícono de mensaje correspondiente.

        .. image:: /imgs/Soter/Soter40.png
            :width: 500px

    .. tab-item:: Permisos/certificaciones

        Esta sección presenta una lista de los permisos y certificaciones que el visitante debe cumplir antes de ingresar a las instalaciones. Esto incluye documentación, aprobaciones específicas y pruebas que varían según el perfil del visitante. En esta sección deberá:

        - Verificar el estado de cada permiso, que puede ser **autorizado**, **pendiente** o **vencido**. 

        .. warning:: Asegúrese de que todos los permisos tengan un estatus **autorizado**, ya que esto garantiza que solo quienes cumplen con los requisitos puedan acceder.

        - Contactar a la persona responsable si algún permiso o certificación presenta un estatus diferente al **autorizado**, para que se realicen las actualizaciones necesarias en la documentación del visitante.

        .. note:: El proceso de actualización es una tarea que le compete al área administrativa que generó el pase de entrada.

        .. image:: /imgs/Soter/Soter41.png
            :width: 500px
        
        .. attention:: Es su responsabilidad asegurarse de que se cumplan todos los requisitos especificados.

    .. tab-item:: Accesos permitidos

        Esta sección específica las áreas a las que un visitante tiene autorización ingresar. Esta sección incluye:

        - **Área**: Lista de áreas específicas a las que el visitante tiene acceso.
        - **Comentario**: Cualquier requisito adicional que deba cumplir el visitante para ingresar a las áreas autorizadas, como portar un gafete, equipo o estar acompañado por personal autorizado.

        .. image:: /imgs/Soter/Soter42.png
            :width: 500px

    .. tab-item:: Equipos autorizados

        Esta sección le permite registrar cualquier equipo o herramienta que un visitante desee ingresar a las instalaciones.

        **Seleccionar Equipo**

        La selección de un equipo especifica su **autorización** y queda registrada junto con el ingreso del visitante. Para seleccionar un equipo, siga:

        1. Marque la casilla correspondiente a la herramienta o equipo que deseas autorizar.

        .. note:: Si aún no hay equipos en la bitácora, añada uno nuevo. Este se registrará y seleccionará automáticamente en la bitácora.

        .. image:: /imgs/Soter/Soter43.png

        **Visualizar Equipos Registrados**

        A medida que un visitante pasa más tiempo en las instalaciones, se crea un historial de equipos utilizados. Para consultar todos los registros de los equipos, siga:

        1. Presione el botón azul de lista ubicado en la esquina superior de la bitácora. Se abrirá un modal con todos los equipos o herramientas registrados en el pase de la visita.
        2. Presione **Cerrar** para salir del modal.

        .. image:: /imgs/Soter/Soter44.png

        **Agregar Equipo**

        Para agregar un nuevo equipo, siga los siguientes pasos:

        1. Presione el botón **+Agregar Equipo**. Se abrirá el modal correspondiente.

        .. note:: Si agrega equipos desde la `bitácora <#bitacora>`_ :octicon:`report;1em;sd-text-info`, presione el tercer icono.

            .. image:: /imgs/Soter/Soter52.png

        2. Complete los siguientes campos:

        - **Tipo de Equipo**: Seleccione la clasificación del equipo o herramienta.
        - **Nombre del Artículo**: Descripción o denominación específica del equipo o herramienta.
        - **Marca**: Fabricante del equipo (opcional).
        - **Modelo**: Indica el modelo del equipo.
        - **Número de Serie**: Identificador único del equipo (opcional).
        - **Color**: Seleccione el color del equipo o herramienta.

        3. Presione el botón **Agregar** para confirmar los datos. El registro se reflejará en la bitácora.

        .. image:: /imgs/Soter/Soter45.png

    .. tab-item:: Vehículos Autorizados

        Esta sección permite el registro de un vehículo con el que el visitante desea ingresar a las instalaciones (si aplica).

        **Seleccionar Vehículo**

        La selección de un vehículo indica su **autorización** y se asocia al ingreso del visitante. 
        
        .. note:: Si agrega un vehículo desde la `bitácora <#bitacora>`_ :octicon:`report;1em;sd-text-info`, presione el cuarto icono.

            .. image:: /imgs/Soter/Soter53.png

        Para autorizar un vehículo:

        1. Marque el botón de opción única correspondiente al vehículo que desea autorizar.

        .. note:: Si aún no hay vehículos registrados, añada uno nuevo. Este se registrará y seleccionará automáticamente. Considere que solo se puede registrar un vehículo por visita.

        .. image:: /imgs/Soter/Soter46.png

        **Visualizar Vehículos Registrados**

        Si un visitante ha utilizado varios vehículos durante diferentes visitas, se genera un historial. Para consultar estos registros:

        1. Presione el botón azul de lista ubicado en la esquina superior de la bitácora. Se abrirá un modal con todos los vehículos registrados para la visita.
        2. Presione **Cerrar** para salir del modal.

        .. image:: /imgs/Soter/Soter47.png

        **Agregar Vehículo**

        Para añadir un nuevo vehículo, siga estos pasos:

        1. Presione el botón **+Agregar Vehículo**.
        2. Complete los campos requeridos:

        - **Tipo de Vehículo**: Seleccione la categoría del vehículo, como automóvil, camioneta, moto, entre otros.
        - **Marca**: Seleccione la marca, como Toyota, Ford, Honda, etc.
        - **Modelo**: Ingrese el modelo específico del vehículo.
        - **Color**: Seleccione el color del vehículo.
        - **Estado**: Indique la condición del vehículo.

        .. note:: Al seleccionar un tipo, las opciones de marca y modelo se ajustan a la selección.

        3. Presione **Agregar** para confirmar la información. El registro se reflejará en la bitácora.

        .. image:: /imgs/Soter/Soter48.png

.. _comentarios-pase:

Agregar comentario de Pase
--------------------------

Estos comentarios se centran en las condiciones específicas del acceso del visitante, como requisitos o restricciones del pase de entrada.

Al agregar un comentario sobre el pase, este se registra automáticamente en el momento de registrar la entrada del visitante. Los comentarios se almacenan como parte de los registros en la sección de **últimos accesos**. Para más información, consulte el apartado de `detalle del pase <#detalle-pase>`_ :octicon:`report;1em;sd-text-info`.

Para agregar un comentario, siga estos pasos:

1. Busque el pase de entrada del visitante. Utilice la barra de búsqueda para localizar el pase.

.. seealso:: Consulte `buscar pases <#buscador-pases>`_ :octicon:`report;1em;sd-text-info` para más detalles.

2. Presione el botón rojo ``+Agregar comentario``, ubicado en la parte superior del pase.

.. image:: /imgs/Soter/Soter68.png

3. Escriba el comentario para el pase de entrada.

.. admonition:: Ejemplo
    :class: pied-piper

    Ejemplos de estos comentarios podrían ser:
            
    - El pase es válido solo hasta las 3:00 PM.
    - El visitante debe entregar su identificación al finalizar la visita.

4. Presione ``Agregar`` para confirmar los datos.

.. image:: /imgs/Soter/Soter33.png

.. _asignacion-gafete:

Asignar Gafete
--------------

El proceso de asignar un gafete está disponible unicamente antes de registrar el ingreso de la visita. Este proceso implica otorgar a un identificador físico que contiene información relevante sobre la identidad y autorización para acceder a ciertas áreas del visitante.

.. note:: Asignar un gafete no es un procedimiento obligatorio.

Para asignar un gafete, siga estos pasos:

1. Busque el pase de entrada del visitante. Utilice la barra de búsqueda para localizar el pase.

.. seealso:: Consulte `buscar pases <#buscador-pases>`_ :octicon:`report;1em;sd-text-info` para más detalles.

2. Presione el botón ``Asignar Gafete``, ubicado en la parte superior del pase.

.. image:: /imgs/Soter/Soter69.png

.. note:: Si realiza la asignación de un gafete desde la `bitácora <#bitacora>`_ :octicon:`report;1em;sd-text-info`, presione el segundo icono sobre id.

    .. image:: /imgs/Soter/Soter51.png

2. Complete los campos correspondientes:

- **Número de gafete**: Seleccione el gafete deseado.
- **Tipo de documento de garantía**: Seleccione el documento que el visitante dejará como garantía.
- **Locker de seguridad**: Seleccione el locker de seguridad.

3. Presione ``Asignar gafete`` para confirmar los datos.

.. image:: /imgs/Soter/Soter32.png
    :width: 500px
        
.. note:: Consulte el apartado de **Información personal** en el `detalle del pase <#detalle-pase>`_ :octicon:`report;1em;sd-text-info`, para visualizar el registro del gafete.

.. _registrar-visita:

Registrar Ingreso
-----------------

El proceso de registrar el ingreso de un visitante permite controlar su acceso, asegurando que se cumplan todos los requisitos y permisos necesarios antes de permitir la entrada. Siga estos pasos para realizar el registro de ingreso:

1. Busque el pase de entrada del visitante. Utilice la barra de búsqueda para localizar el pase.

.. seealso:: Consulte `buscar pases <#buscador-pases>`_ :octicon:`report;1em;sd-text-info` para más detalles.

2. Verifique los detalles del pase y asegúrese de que la información esté completa y actualizada, incluyendo permisos, áreas de acceso, equipos o vehículos asignados.

.. seealso:: Consulte los `detalles del pase <#detalle-pase>`_ :octicon:`report;1em;sd-text-info`.

3. Asigne un gafete. Aunque no es obligatorio, la asignación de un gafete le permite tener un mejor control de la visita.

.. seealso:: Consulte los `asignar pase <#asignacion-gafete>`_ :octicon:`report;1em;sd-text-info` para más detalles.

4. Agregue comentarios al pase, según lo requiera.

.. seealso:: Consulte `agregar comentarios <#comentarios-pase>`_ :octicon:`report;1em;sd-text-info` para más detalles.

5. Presione el botón ``Registrar ingreso``, ubicado en la parte superior del detalle del pase.

.. image:: /imgs/Soter/Soter64.png
    :width: 880px

.. note:: Si la opción no está disponible, significa que la visita ya ha sido registrada como ingresada. Observe la etiqueta del pase:

    - Si el ingreso aún no ha sido registrado, la etiqueta mostrará **Entrada**.
    - Si el ingreso ya ha sido registrado, la etiqueta mostrará **Salida**.
    
    El menú de opciones cambiará automáticamente según la situación del pase, facilitando la selección de la acción correspondiente.

6. Observe el mensaje de confirmación, presione ``OK`` para cerrar el modal 

.. image:: /imgs/Soter/Soter66.png

.. seealso:: Para verificar la actualización del registro, consulte la sección de :ref:`bitacora` :octicon:`report;1em;sd-text-info` y revise los registros de entradas y salidas.

.. _recibimiento-gafete:

Recibir Gafete
--------------

El proceso de recibir un gafete está disponible únicamente antes de registrar la salida de la visita. Este procedimiento permite liberar el gafete y el locker asignado al visitante. Para completar el proceso de recibir un gafete, siga estos pasos:

1. Busque el pase de entrada del visitante. Utilice la barra de búsqueda para localizar el pase.

.. seealso:: Consulte `buscar pases <#buscador-pases>`_ :octicon:`report;1em;sd-text-info` para más detalles.

2. Haga clic el botón ``Recibir Gafete``, ubicado en la parte superior del pase.

.. image:: /imgs/Soter/Soter70.png

.. note:: Si recibe un gafete desde la `bitácora <#bitacora>`_ :octicon:`report;1em;sd-text-info`, presione el segundo icono sobre id.

    .. image:: /imgs/Soter/Soter51.png

3. Revise cuidadosamente la información proporcionada y confirme la acción seleccionando el botón ``Confirmar``

.. image:: /imgs/Soter/Soter50.png
    :width: 500px
        
.. warning:: Si el visitante tiene un gafete asignado y necesita registrar su salida, primero deberá completar el proceso de recepción del gafete. De lo contrario, el sistema no permitirá continuar.

    .. image:: /imgs/Soter/Soter49.png
        :width: 500px

.. _registrar-salida:

Registrar Salida
----------------

El proceso de registrar la salida de un visitante permite controlar y documentar la finalización de la estancia del visitante en las instalaciones. Siga los siguientes pasos para realizar este proceso:

1. Busque el pase de entrada del visitante. Utilice la barra de búsqueda para localizar el pase.

.. seealso:: Consulte `buscar pases <#buscador-pases>`_ :octicon:`report;1em;sd-text-info` para más detalles.

2. Reciba el gafete (si aplica).

.. warning:: Si la visita tiene un gafete asignado, no será posible registrar la salida hasta que se realice el proceso de recepción del gafete. Consulte `recibimiento de gafete <#recibimiento-gafete>`_ :octicon:`report;1em;sd-text-info`.

3. Presione el botón ``Registrar salida``, ubicado en la parte superior del detalle del pase.

.. note:: Este botón estará visible solo si la visita aún está registrada como activa (es decir, no se ha marcado su salida).

   .. image:: /imgs/Soter/Soter65.png

4. Observe el mensaje de confirmación, presione ``OK`` para cerrar el modal.

.. image:: /imgs/Soter/Soter67.png

.. seealso:: Para verificar la actualización del registro, consulte la sección de :ref:`bitacora` :octicon:`report;1em;sd-text-info` y revise los registros de entradas y salidas.
