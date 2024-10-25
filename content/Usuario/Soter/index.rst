.. _doc-soter:

====================
Aplicación Web Soter
====================

Bienvenido a la documentación de **Soter**, un sistema web diseñado para el **control de accesos de visitas** en una empresa. Este recurso ofrece una guía detallada sobre el uso de las funcionalidades de Soter, proporcionando ejemplos, tutoriales paso a paso y soluciones a problemas comunes para facilitar su uso.

Soter tiene como objetivo principal brindar seguridad a las instalaciones de la empresa mediante un control exhaustivo de los usuarios (visitas) que entran y salen de la ubicación. A través de este sistema, los guardias de seguridad pueden gestionar la **revisión de permisos**, el **control de objetos** y **vehículos autorizados**, la **supervisión de accesos a áreas específicas** entre otras dentro de las instalaciones.

Este manual está dirigido principalmente a **guardias de seguridad** y **personal administrativo** que interactúan directamente con la gestión de entradas y salidas de visitantes. Las herramientas que Soter proporciona incluyen la capacidad de reportar **incidencias**, **fallas**, gestionar **objetos perdidos** y llevar a cabo funcionalidades específicas para tareas diarias de los guardias de seguridad, optimizando el control y la vigilancia en la empresa.

Requisitos previos
==================

Para utilizar el sistema **Soter** de manera óptima, es importante cumplir con los siguientes requisitos previos:

**Navegador compatible**

El sistema es compatible con los navegadores más utilizados, incluyendo:

- Google Chrome (versión más reciente)
- Mozilla Firefox (versión más reciente)
- brave web browser (versión más reciente)

**Resolución de pantalla** 

Aunque Soter es adaptable a cualquier dispositivo, se recomienda una resolución mínima de 1024x768 píxeles para una visualización adecuada en computadoras de escritorio y tablets. 

En dispositivos móviles, la interfaz se ajusta automáticamente para facilitar la navegación. 

.. note:: Actualmente, la versión responsive presenta algunos detalles de ajuste menores, que no comprometen la funcionalidad general del sistema

**Conexión a internet**

Se requiere una conexión a internet estable para acceder a las funcionalidades de Soter y garantizar que los datos se registren y sincronicen correctamente.

**Conocimientos básicos de computación**

Se recomienda que los guardias de seguridad tengan conocimientos básicos en el uso de computadoras y navegación web. Sin embargo, Soter ha sido diseñado con una interfaz intuitiva y fácil de usar, por lo que incluso aquellos usuarios que no estén familiarizados con la tecnología encontrarán el sistema accesible y sencillo de manejar. 

Iniciar Sesión
==============

La interfaz de **Login** es el punto de entrada al sistema **Soter**. Permite autenticar su identidad ingresando sus credenciales de acceso. Para iniciar sesión, siga los siguientes pasos:

1. En el navegador de su preferencia, ingrese al siguiente enlace: 

.. code-block::
    
    https://srv.linkaform.com/solucion_accesos/login.html

.. seealso:: Ingrese directamente |aqui| :octicon:`report;1em;sd-text-info`.

2. Escriba el correo y la contraseña en los campos correspondientes.

.. warning:: El correo y la contraseña son los mismos que una cuenta vigente de |linkaform| :octicon:`report;1em;sd-text-info`. 
   
   En caso de no disponer de credenciales, solicítelas al administrador de su empresa o al equipo de Linkaform y lleve a cabo el proceso para :ref:`activar-cuenta-usuario` :octicon:`report;1em;sd-text-info`.

3. Presione el botón ``Continuar``. Será redirigido automáticamente a la interfaz de `turnos <#iniciar-turno>`_ :octicon:`report;1em;sd-text-info`.

.. hint:: Si por algún motivo existe algún problema con la autenticación, le sugerimos iniciar sesión primero en su cuenta de |linkaform| :octicon:`report;1em;sd-text-info` y luego volver a intentar iniciar sesión en |Soter| :octicon:`report;1em;sd-text-info`.

.. image:: /imgs/Soter/Soter1.png
    :width: 880px

.. _iniciar-turno:

Turno
=====

La interfaz de **Turnos** permite realizar el **Check-in** y **Check-out** en la caseta de vigilancia correspondiente. Observe la siguiente imagen que muestra la interfaz completa:

.. image:: /imgs/Soter/Soter4.png
   :width: 880px

Esta interfaz muestra datos importantes sobre la caseta y su situación actual. Considere los siguientes elementos importantes:

**Menú**: Ubicado en la parte superior, este menú proporciona acceso a otras funcionalidades del sistema. Está disponible únicamente cuando el guardia inicia su turno. 

**Botón de Iniciar/Cerrar Turno**: Ubicado en la parte superior derecha de la interfaz, este botón le permitirá iniciar o cerrar su turno. Su apariencia cambiará según el estado del turno. 

Si el **Estatus** de la caseta es **Disponible** podrá iniciar su turno de forma regular.

.. image:: /imgs/Soter/Soter2.png

Si el **Estatus** de la caseta es **No Disponible**, no podrá iniciar su turno hasta que:

- Cambie de caseta utilizando la opción en el apartado de **Información de la ubicación**.
- O utilice la opción de **Forzar Cierre** en el apartado de **Información de la caseta** para liberar la caseta y poder iniciar su turno.

.. image:: /imgs/Soter/Soter3.png

Revise las siguientes pestañas para obtener más detalles y casos de uso sobre cada componente de la interfaz.

.. tab-set::

    .. tab-item:: Información Personal

        En este apartado, encontrará la información personal de su cuenta, incluyendo los siguientes detalles:

        - **Nombre**: Su nombre completo registrado en la cuenta.
        - **Puesto**: El puesto o cargo que ocupa.
        - **Correo electrónico**: La dirección de correo asociada a su cuenta.

        **Cambiar Imagen de Perfil**

        Para actualizar la imagen de su perfil, siga estos pasos:

        1. Presione el botón ``Cambiar Imagen``.
        2. Seleccione la nueva imagen desde su dispositivo. La imagen se actualizará automáticamente en su perfil.

        .. image:: /imgs/Soter/Soter16.png

    .. tab-item:: Información de la Ubicación

        Esta sección muestra la información detallada sobre la ubicación actual de la caseta en la que se encuentra. Podrá encontrar la siguiente información:

        - **Ubicación**: Muestra el nombre de la planta o instalación donde se encuentra la caseta.
        - **Ciudad**: Indica la ciudad en la que está ubicada la planta.
        - **Estado**: Muestra el estado correspondiente a la ubicación.
        - **Dirección**: Proporciona la dirección completa de la planta.
        - **Caseta**: Muestra la caseta específica dentro de la planta que está siendo utilizada.
        
        .. image:: /imgs/Soter/Soter5.png  

        **Cambiar Caseta**
        
        Observe el botón ubicado en la esquina superior de la sección. Este botón permite cambiar de una caseta a otra, incluso a una caseta de otra ubicación. Para cambiar entre casetas o ubicaciones, siga los siguientes pasos:

        .. grid:: 2
            :gutter: 0

            .. grid-item-card::
                :columns: 6

                1. Seleccione el botón ``Cambiar Caseta``. Se abrirá un modal.
                2. Seleccione una caseta de la lista que se muestra en el modal.

                .. important:: Al seleccionar la nueva caseta, verifique que la ubicación sea la misma en la que se encuentra. Esto es importante, ya que cualquier acción o registro que haga quedará asociado a esa caseta y ubicación. 
                
                .. warning:: Al seleccionar una caseta, no podrá ver el estado de la misma (es decir, si está disponible o no). Si selecciona una caseta no disponible, podrá tomar otras medidas, como forzar el cierre. Continúe leyendo la siguiente pestaña para más información.

            .. grid-item-card::
                :columns: 6

                .. image:: /imgs/Soter/Soter6.png      

    .. tab-item:: Información de la Caseta

        Este apartado muestra el estado actual de disponibilidad de la caseta seleccionada en la ubicación. En esta sección, podrá encontrar la siguiente información:

        **Estatus de la Caseta**: Indica la disponibilidad de la caseta. 

        Si la caseta está **Disponible**, se mostrará únicamente este campo y el guardia podrá iniciar turno presionando el botón correspondiente.

        .. image:: /imgs/Soter/Soter7.png

        Si la caseta **No está Disponible**, se mostrarán:

        - **Guardia en turno**: Muestra el nombre del guardia actualmente en turno en esa caseta.
        - **Fecha de Inicio de turno**: Indica la fecha y hora en que el guardia actual inició su turno.

        .. image:: /imgs/Soter/Soter9.png

        **Forzar Cierre**

        Observe el botón ubicado en la esquina superior de la sección. Este botón permite al guardia finalizar el turno actual de manera manual, por ejemplo, en caso de que el guardia anterior no haya registrado su salida. Para forzar el cierre, siga los siguientes pasos:

        1. Seleccione el botón ``Forzar Cierre``. Se abrirá un modal.
        2. Lea cuidadosamente el mensaje del modal. Encontrará información relevante acerca del guardia que tiene el turno actual en la caseta que desea cerrar.
        3. Presione el botón ``Sí`` para confirmar o ``Cancelar`` para abortar la operación.

        .. image:: /imgs/Soter/Soter8.png  

        .. warning:: Utilice esta funcionalidad con precaución y únicamente en situaciones donde sea absolutamente necesario cerrar el turno de forma forzada.

    .. tab-item:: Guardias de Apoyo

        Este apartado le permite seleccionar a otros guardias que estarán activos junto a usted durante el turno en la misma caseta. Los guardias de apoyo son aquellos que colaboran en situaciones de emergencia, relevos u otras necesidades.

        Para agregar guardias de apoyo a su turno y asegurarse de que estén disponibles para asistirle, siga estos pasos:

        1. Revise la lista de guardias disponibles en la misma ubicación.
        2. Marque la casilla junto al nombre del guardia que desea agregar como apoyo.
        3. Inicie el turno.

        .. image:: /imgs/Soter/Soter10.png

        **Agregar Guardia de Apoyo**

        Este proceso está disponible únicamente cuando el turno ya ha sido iniciado y desea agregar a un nuevo guardia como apoyo. Al iniciar el turno, solo se mostrarán los guardias seleccionados previamente. 

        Para agregar un nuevo guardia a la lista de apoyo, siga estos pasos:

        1. Presione el botón ``Agregar guardia de apoyo`` ubicado en la parte inferior derecha de la sección. Se abrirá un modal.
        2. Identifique al o los guardias que desea agregar y presione el botón ``Seleccionar``. Automáticamente, estos guardias se agregarán a la lista de la sección.

        .. image:: /imgs/Soter/Soter11.png

        **Check-out Guardia de Apoyo**

        Para hacer Check-out a un guardia de apoyo, siga estos pasos:

        1. Presione el icono de salida ubicado junto al nombre del guardia. Esto abrirá un modal.
        2. Presione ``Sí`` para confirmar el **Check-out** del guardia en su turno, o presione ``Cancelar`` para mantener la lista de apoyo.

        .. image:: /imgs/Soter/Soter12.png

    .. tab-item:: Resumen de Actividad

        Esta sección le proporciona información adicional y relevante sobre la situación actual de la caseta y su entorno. Aquí encontrará datos clave para el monitoreo y control de las instalaciones, lo que facilitará la toma de decisiones y la coordinación de acciones de seguridad, incluyendo:

        - **Visitas dentro**: Indica el número de visitas que actualmente se encuentran dentro de las instalaciones de la ubicación.
        
        - **Artículos Concesionados**: Indica el número artículos entregados temporalmente a los empleados de la ubicación que aún no han sido devueltos.

        - **Incidentes Pendientes**: Indica el número de incidentes que han sido reportados pero que aún no se han resuelto. Esta información es importante para dar seguimiento a situaciones que requieren atención inmediata.

        - **Vehículos Estacionados**: Indica el número de vehículos que se encuentran estacionados dentro de la ubicación.

        - **Gafetes Pendientes**: Indica el número de gafetes que aún no han sido devueltos por las visitas.

        .. image:: /imgs/Soter/Soter13.png

    .. tab-item:: Estado del turno

        Este apartado le proporciona información detallada sobre la situación actual de la caseta, incluyendo la fecha y hora actuales, que son las mismas que se registrarán al momento de iniciar o finalizar un turno. El estatus de la caseta dependerá del estado del turno:

        - **Cerrado**: Indica que aún no ha iniciado su turno.
        - **Abierto**: Indica que el turno ya ha sido iniciado.

        .. image:: /imgs/Soter/Soter14.png
        
        .. note:: Tenga en cuenta que la fecha y hora que se registran en el Check-in y Check-out corresponden al momento exacto en que presiona el botón para iniciar o cerrar el turno.

    .. tab-item:: Notas

        .. image:: /imgs/Soter/Soter15.png

        .. seealso:: Consulte la sección sobre `notas <#section-notas>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. _section-notas:

Notas
=====

La funcionalidad de **Notas** le permite agregar y gestionar mensajes para comunicarse con otros guardias de seguridad que estén en diferentes turnos. Este apartado actúa como un tipo de chat o bitácora para dejar notas, pendientes y mensajes importantes que deban ser considerados por los siguientes turnos.

Puede acceder a la sección completa de todas las notas de las siguientes maneras:

1. Desde la interfaz de `turnos <#iniciar-turno>`_ :octicon:`report;1em;sd-text-info`: Presione el botón azul de lista ubicado en la esquina superior de la bitácora de notas.
2. Desde cualquier sección: Seleccione su fotografía de perfil, ubicada en la esquina superior de la pantalla y luego elija la opción ``Notas``.

.. image:: /imgs/Soter/Soter22.png

Al acceder, encontrará información sobre las notas de la caseta actual, dónde:

**Ubicación**

Le permite cambiar entre diferentes ubicaciones o casetas dentro de la misma empresa. Por ejemplo, puede acceder a una sucursal diferente y seleccionar una caseta específica en esa ubicación.

.. attention:: Si cambia de ubicación o caseta, la información de la bitácora se actualizará automáticamente para reflejar los datos correspondientes a la nueva selección.

**Información**

Muestra tarjetas (cards) con información relevante y útil para el monitoreo de la situación actual, lo que facilita estar al tanto de pendientes y eventos importantes. Dependiendo de la sección, las tarjetas mostrarán la cantidad de diferentes elementos, como por ejemplo:
   
- **Notas del día**: Número de notas registradas de la fecha actual.
- **Notas abiertas**: Cantidad de notas que aún están activas y requieren atención.
- **Notas estancadas**: Notas que no han tenido actualizaciones recientes o que están pendientes de resolución.

.. image:: /imgs/Soter/Soter23.png
    :width: 880px

Si desea colapsar la información de la caseta para visualizar solo la información de la sección:

- Presione el ícono de flecha hacia abajo. El contenido se ocultará.
- Si desea volver a ver la información, presione el mismo ícono nuevamente.

Bitácora de Notas
-----------------

La bitácora de notas le muestra un registro de todas las notas, entre las columnas podrá encontrar:

- **Folio**: Identificador único de la nota.
- **Guardia**: El nombre del guardia que dejó la nota.
- **Apertura**: Fecha en que se creó la nota.
- **Cierre**: Si la nota ya fue cerrada, se mostrará la fecha de cierre.
- **Nota**: Título de la nota.
- **Archivo**: Documentos de evidencia.
- **Fotografía**: Imágenes de evidencia.
- **Comentarios**: Detalles adicionales o seguimiento de la nota.

.. image:: /imgs/Soter/Soter17.png
    :width: 880px

Agregar Nota
------------

Para agregar una nueva nota, siga estos pasos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card::
        :columns: 6

        1. Presione el botón ``+Nueva Nota`` ubicado en la parte superior de la bitácora.
        2. Complete la información requerida en los siguientes campos:

        - **Nota**: Ingrese un título descriptivo para identificar la nota.
        - **Documento**: Adjunte uno o más documentos como evidencia relacionada.
        - **Fotografía**: Adjunte una o varias imágenes como evidencia visual.
        - **Comentario**: Añada detalles adicionales o comentarios relevantes sobre la nota.

        3. Presione el botón ``Agregar`` para confirmar, o ``Cancelar`` si desea anular la operación.

    .. grid-item-card::
        :columns: 6

        .. image:: /imgs/Soter/Soter18.png

Cerrar Nota
-----------

El cierre de una nota es una confirmación de que la situación o el pendiente indicado en la nota ya ha sido resuelto o leído. Para cerrar una nota, siga estos pasos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card::
        :columns: 6

        1. Localice la nota que desea cerrar en la bitácora.
        2. Haga clic en el primer ícono de la columna de opciones, ubicado en la misma fila que la nota. Esto abrirá un modal de confirmación.
        3. Revise la información y presione ``Sí`` para confirmar el cierre de la nota, o ``Cancelar`` si decide no realizar la acción.

    .. grid-item-card::
        :columns: 6

        .. image:: /imgs/Soter/Soter19.png

Visualizar Nota
---------------

Para ver el contenido de una nota de manera detallada sin tener que desplazarse por la tabla, siga estos pasos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card::
        :columns: 6

        1. Identifique la nota que desea visualizar.
        2. Haga clic en el segundo ícono de vista, ubicado en la columna de opciones en la misma fila que la nota. Esto abrirá un modal que mostrará toda la información de la nota.
        3. Presione ``Cerrar`` para salir del modal y regresar a la lista de notas.

    .. grid-item-card::
        :columns: 6

        .. image:: /imgs/Soter/Soter20.png

Editar Nota
-----------

Para editar una nota existente, siga estos pasos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card::
        :columns: 6

        1. Identifique la nota que desea editar en la bitácora.
        2. Haga clic en el tercer ícono de edición, ubicado en la columna de opciones de la misma fila que la nota. Esto abrirá un modal con la información de la nota.
        3. Modifique los campos que necesiten actualización.
        4. Presione ``Editar`` para confirmar los cambios, o ``Cancelar`` si decide no realizar la acción.

        .. note:: Al editar una nota, la fecha de creación de la nota no se modificará; solo se actualizará la información contenida en la misma.

    .. grid-item-card::
        :columns: 6

        .. image:: /imgs/Soter/Soter21.png

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

Buscar Pase de Entrada
----------------------

Para buscar un pase de entrada, siga estos pasos y asegúrese de que el visitante cumpla con lo siguiente:

1. En el campo ``Codigo User``, escanee el QR que le mostrará el visitante.

.. image:: /imgs/Soter/Soter61.png

.. note:: El visitante deberá mostrarle el gafete que el personal administrativo le hizo llegar. Observe el siguiente ejemplo de QR que el visitante le debe mostrar:

    .. image:: /imgs/Soter/Soter26.png
        :width: 500px

2. Presione el botón de lupa para buscar al visitante. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

Si la visita no tiene el QR, pero está seguro de que cuenta con un pase de seguridad, siga estos pasos:

1. Presione el ícono de lista ubicado en la barra buscadora. Se abrirá un modal.
2. Identifique al visitante por el nombre o la fotografía. Utilice el buscador en caso de tener múltiples pases.
3. Presione sobre el nombre del visitante. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

.. warning:: Al buscar un pase de entrada por QR o desde la lista, el pase debe estar **Activo**. Si, por algún motivo, el pase no aparece por los medios mencionados, considere buscarlos en los `pases temporales <#pases-temp>`_ :octicon:`report;1em;sd-text-info`.

.. image:: /imgs/Soter/Soter27.png
    :width: 500px

Nuevo Pase de Entrada
---------------------

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
- **Tipo de perfil**: Seleccione el tipo de perfil que tendrá la visita.

.. note:: El **tipo de perfil** define los límites y permisos de la visita. Según el perfil asignado, los requisitos varían ya que algunos perfiles requieren condiciones más estrictas que otros.

    Para pases de entrada espontáneos, es habitual seleccionar un perfil de  **visita general** o **candidatos**.

3. Presione ``Crear`` para confirmar los datos y generar el pase de entrada. Será redirigido al :ref:`detalle-pase` :octicon:`report;1em;sd-text-info`.

.. warning:: Al crear un pase de entrada, **no** se está concediendo automáticamente el acceso al visitante.

.. image:: /imgs/Soter/Soter28.png
    :width: 500px

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

        1. Presione el botón **+Agregar Vehículo**. Se abrirá un modal.
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

.. _bitacora:

Bitácoras
=========

La interfaz de **Bitácoras** facilita el control y monitoreo de las entradas y salidas de las visitas, proporcionando un registro detallado de cada movimiento a través de una bitácora.

.. attention:: Este apartado está disponible únicamente cuando haya iniciado su turno. Para acceder, presione la opción **Bitácoras** ubicada en el menú superior.

    .. image:: /imgs/Soter/Soter56.png

La bitácora está organizada en varias columnas, dónde:

- **Folio**: Identificador único del registro.
- **Entrada**: Fecha y hora en la que el visitante ingresó.
- **Visitante**: Nombre completo del visitante.
- **Tipo**: Perfil del visitante (e.g., visita general, proveedor).
- **Contratista**: Razón social de la empresa a la que pertenece el visitante (si aplica).
- **Gafete**: Identificación asignada al visitante para su acceso (si aplica).
- **Visita a**: Persona o departamento al que el visitante se dirige.
- **Caseta Entrada**: Caseta por la que ingresó el visitante.
- **Caseta Salida**: Caseta por la que el visitante registró su salida.
- **Salida**: Fecha y hora de salida del visitante.
- **Comentarios**: Observaciones adicionales sobre el pase de la visita.

.. image:: /imgs/Soter/Soter60.png
    :width: 880px
    
Visualizar Información de la Visita
-----------------------------------

Para consultar los datos relevantes de una visita y su pase, siga estos pasos:

1. Identifique la visita de interés en la lista de registros.
2. En la columna de **Opciones**, seleccione el primer ícono de usuario. Se abrirá un modal con la información detallada del pase de la visita.

.. image:: /imgs/Soter/Soter57.png

3. Presione ``Cerrar`` para salir del modal.

.. image:: /imgs/Soter/Soter58.png

Asignar o Recibir Gafete
------------------------

Desde la bitácora, es posible asignar o recibir un gafete para una visita. Siga los siguientes pasos:

1. Identifique la visita que requiere la asignación o recepción del gafete.

.. note:: Las visitas que no tengan información en los campos **Caseta Salida** o **Salida** son aquellas que aún se encuentran dentro de las instalaciones.

2. En la columna de **Opciones**, seleccione el segundo ícono (representado como una tarjeta).

.. image:: /imgs/Soter/Soter51.png

3. Consulte la documentación según lo requiera:

.. seealso:: Consulte :ref:`asignacion-gafete` :octicon:`report;1em;sd-text-info` para más detalles.

.. seealso:: Consulte :ref:`recibimiento-gafete` :octicon:`report;1em;sd-text-info` para más detalles.

Agregar Equipo
--------------

Desde la bitácora, puede registrar más equipos o herramientas que un visitante desee ingresar a las instalaciones. Siga los siguientes pasos:

1. Identifique la visita que requiere agregar equipos.

2. En la columna de **Opciones**, seleccione el tercer ícono.

.. image:: /imgs/Soter/Soter52.png

3. Consulte :ref:`detalle-pase` :octicon:`report;1em;sd-text-info` en la sección **Equipos autorizados**.

Agregar Vehículo
----------------

Desde la bitácora, puede registrar el vehículo con el que el visitante desea ingresar a las instalaciones.

.. note:: Solo se puede registrar un vehículo por visita. Si ya se ha asignado un vehículo previamente en el pase, no será posible añadir otro.

Para agregar un vehículo, siga los pasos:

1. Identifique la visita que requiere agregar un vehículo.

2. En la columna de **Opciones**, seleccione el cuarto ícono.

.. image:: /imgs/Soter/Soter53.png

3. Consulte :ref:`detalle-pase` :octicon:`report;1em;sd-text-info` en la sección **Vehículos autorizados**.

Registrar Salida
----------------

Desde la la bitácora, puede registrar la salida de un visitante, siga los siguientes pasos:

1. Identifique la visita cuya salida desea registrar.

.. note:: Las visitas que no tengan información en los campos **Caseta Salida** o **Salida** son candidatos para registrar su salida.

2. En la columna de **Opciones**, seleccione el ícono correspondiente para la salida. Abrirá el modal correspondiente.

.. image:: /imgs/Soter/Soter54.png

3. Presione ``Confirmar`` para completar el registro de la salida.

.. image:: /imgs/Soter/Soter55.png
    :width: 400px

.. note:: No es posible registrar la salida de un visitante que ya ha abandonado las instalaciones. Observe la alerta.

    .. image:: /imgs/Soter/Soter59.png
        :width: 400px

Incidencias
===========

La interfaz de **Incidencias** permite la gestión de incidentes o fallas que se presentan en las instalaciones.

.. warning:: Este apartado está disponible únicamente cuando haya iniciado su turno. Para acceder, presione la opción **Incidentes** ubicada en el menú superior.

   .. image:: /imgs/Soter/Soter71.png

Al acceder, encontrará la información de la caseta actual. Esta sección de la interfaz proporciona la situación actual sobre la caseta, dónde:

**Ubicación**

Permite confirmar la ubicación y caseta en la que se encuentra actualmente y cambiar entre diferentes ubicaciones o casetas dentro de la misma empresa.

.. attention:: Si cambia de ubicación o caseta, la información de la bitácora se actualizará automáticamente para reflejar los datos correspondientes a la nueva selección.

**Información**

Muestra tarjetas con información relevante y útil para el monitoreo de la situación actual, lo que facilita estar al tanto de pendientes y eventos importantes. Dependiendo de la sección, las tarjetas mostrarán la cantidad de diferentes elementos, como por ejemplo:

- **Fallas x día**: Muestra el número total de fallas reportadas en el día, lo que ayuda a identificar la frecuencia de problemas que ocurren en las instalaciones.
- **Fallas por resolver**: Indica la cantidad de fallas que aún no han sido atendidas o solucionadas, lo que permite priorizar y dar seguimiento a los problemas pendientes.

Si desea colapsar la información de la caseta para visualizar solo la información de la sección:

- Presione el ícono de flecha hacia abajo. El contenido se ocultará.
- Si desea volver a ver la información, presione el mismo ícono nuevamente.

.. image:: /imgs/Soter/Soter75.png
    :width: 880px

Bitácora de Incidentes
----------------------

Un incidente es cualquier evento inesperado que interrumpe una actividad o proceso, sin que necesariamente implique un mal funcionamiento de un equipo o sistema.

En la bitácora de incidentes, los registros se organizan según su nivel de prioridad, mostrando primero los incidentes **Críticos** para una atención inmediata. La bitácora está organizada en varias columnas, donde:

- **Ubicación**: Indica la ubicación donde ocurrió el incidente.
- **Lugar del incidente**: Especifica el área exacta dentro de la ubicación donde ocurrió el evento.
- **Fecha**: Registra la fecha en la que el incidente fue reportado.
- **Incidente**: Tipo de incidente reportado.
- **Evidencia**: Muestra fotografías o archivos subidos como evidencia del incidente.
- **Comentarios**: Detalles adicionales sobre el evento, proporcionando contexto o información relevante para del incidente.
- **Reporta**: Indica el nombre del guardia o personal que reportó el incidente.

.. image:: /imgs/Soter/Soter76V.png
    :width: 880px

Para filtrar los registros de los incidentes por prioridad:

1. Identifique el selector ubicado en la parte superior de la bitácora.
2. Seleccione la prioridad donde:

- **Crítico**: Incidentes con daños severos que tienen un alto impacto en las actividades o instalaciones.
- **Alta**: Incidentes que implican daños significativos, aunque no tan severos como los críticos.
- **Mediana**: Incidentes que presentan daños moderados y cuyo impacto es limitado.
- **Baja**: Incidentes con daños menores que no afectan de forma considerable las operaciones o instalaciones.

Los registros de la bitácora se actualizarán automáticamente para mostrar solo los incidentes de la prioridad seleccionada.

.. image:: /imgs/Soter/Soter72.png

.. _nuevo-incident:

Nuevo Incidente
^^^^^^^^^^^^^^^

.. attention:: En Soter, el levantamiento de un reporte para un incidente funciona como un registro de los eventos que afectan una actividad o proceso. Sin embargo, no incluye un mecanismo de seguimiento o cierre del incidente, lo que significa que el reporte se limita a documentar el evento sin un proceso adicional para su resolución o cierre.

Reportar un nuevo incidente es un proceso sencillo, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Presione el botón azul ``+Nuevo Incidente``, ubicado en la parte superior derecha de la bitácora. Esto abrirá el modal correspondiente.
3. Complete los campos, según lo requiera, donde:

- **Ubicación**: Seleccione la ubicación donde ocurrió el incidente.
- **Área**: Indique la zona específica dentro de la ubicación donde se produjo el incidente.

.. image:: /imgs/Soter/Soter76.png

- **Fecha**: Especifique la fecha exacta del incidente.
- **Hora**: Ingrese la hora en que ocurrió el incidente.

.. image:: /imgs/Soter/Soter77.png

- **Reporta**: Seleccione el guardia que reporta el incidente.

.. image:: /imgs/Soter/Soter78.png

- **Prioridad**: Seleccione entre baja, media, alta o crítica, según la gravedad del incidente.

.. image:: /imgs/Soter/Soter79.png

- **Incidencia**: Seleccione el tipo de incidente de la lista predefinida.

.. image:: /imgs/Soter/Soter80.png
    :width: 650px

.. note:: Al seleccionar la opción **Depósitos** como tipo de incidencia, se desplegarán dos campos adicionales relacionados con dinero, donde:

    - **Tipo de Depósito**: Especifique el tipo de depósito.
    - **Cantidad**: Ingrese el monto del depósito. Puede agregar más de un depósito y el sistema calculará el total.

    Esta selección es la única que modifica el contenido del modal.

    .. image:: /imgs/Soter/Soter74.png
        :width: 500px

- **Comentarios**: Agregue información adicional que pueda ser útil para entender la situación.

.. image:: /imgs/Soter/Soter81.png

- **Tipo de daño**: Seleccione si el daño fue a materiales o a personas.

.. image:: /imgs/Soter/Soter82.png

- **Daños**: Describa los daños causados.

.. image:: /imgs/Soter/Soter83.png

- **Evidencia**: Adjunte imágenes o videos que respalden el reporte.
- **Documentos**: Suba documentos adicionales si es necesario.

.. image:: /imgs/Soter/Soter84.png

- **Personas involucradas**: Ingrese el nombre completo de cada persona involucrada y seleccione si es un afectado o un testigo.

.. image:: /imgs/Soter/Soter85.png

.. note:: No hay un límite en la cantidad de personas que pueden ser agregadas como involucradas. Añada tantas como sea necesario para asegurar que todos los involucrados estén debidamente registrados.

- **Acciones tomadas**: Registre las medidas que se tomaron en respuesta al incidente, junto con el responsable de cada acción.

.. image:: /imgs/Soter/Soter86.png

4. Presione ``Crear`` para finalizar el registro.

Visualizar Incidente
^^^^^^^^^^^^^^^^^^^^

Para consultar los detalles de un incidente registrado en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique el incidente deseado.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar el incidente específico que desea revisar.

5. Haga clic en el ícono de vista ubicado en la misma fila del incidente que desea revisar. Esto abrirá un modal que mostrará todos los detalles del incidente seleccionado de forma completa.

.. image:: /imgs/Soter/Soter88.png

6. Una vez revisada la información, presione el botón de ``Cerrar`` o el ícono ``X`` para salir de la ventana de detalles y regresar a la lista de la bitácora de incidentes.

.. image:: /imgs/Soter/Soter89.gif

Actualizar Incidente
^^^^^^^^^^^^^^^^^^^^

Para actualizar la información de un incidente registrado en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique el incidente que desea actualizar.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar el incidente específico que desea modificar.

5. Haga clic en el ícono de **editar** ubicado en la misma fila del incidente. Esto abrirá un modal con todos los detalles del incidente en modo de edición.

.. image:: /imgs/Soter/Soter90.png

6. Realice los cambios necesarios en los campos que desee actualizar. 

.. seealso:: Consulte los campos en la sección `nuevo incidente <#nuevo-incident>`_ :octicon:`report;1em;sd-text-info`.

7. Una vez que haya realizado las modificaciones, presione el botón ``Actualizar`` para confirmar la información del incidente. Recibirá un mensaje de confirmación indicando que la información ha sido actualizada exitosamente.

.. image:: /imgs/Soter/Soter91.png
    :width: 500px

8. Presione el botón de ``OK`` para cerrar de la ventana y regresar a la lista de la bitácora de incidentes.

.. image:: /imgs/Soter/Soter92.png

Eliminar un Registro
^^^^^^^^^^^^^^^^^^^^

Para eliminar un incidente específico de la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique el incidente que desea eliminar.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar el incidente específico que desea eliminar.

5. Seleccione el icono **Eliminar** ubicado en la misma fila del incidente que desea borrar.

.. image:: /imgs/Soter/Soter93.png

6. Presione ``Confirmar`` para proceder con la eliminación del incidente. Recibirá un mensaje de confirmación indicando que el registro ha sido eliminado exitosamente.

.. image:: /imgs/Soter/Soter94.png
    :width: 500px

Eliminar Múltiples Registros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para eliminar varios incidentes al mismo tiempo de la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique los incidentes que desea eliminar.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar los incidentes específicos que desea eliminar.

5. Seleccione las casillas de los registros que desea eliminar.
6. Presione el botón ``Eliminar`` ubicado en la esquina superior de la bitácora.

.. image:: /imgs/Soter/Soter95.png
    :width: 880px

7. Presione ``Confirmar`` para proceder con la eliminación de los registros seleccionados.

.. image:: /imgs/Soter/Soter96.png
    :width: 500px

8. Presione ``OK`` para cerrar el modal de confirmación y finalizar el proceso.

.. image:: /imgs/Soter/Soter97.png
    :width: 500px

Bitácora de Fallas
------------------

La bitácora de **fallas** permite registrar y realizar un seguimiento de problemas técnicos o malfuncionamientos que ocurren en las instalaciones. 

.. attention:: A diferencia de los incidentes, las fallas requieren un proceso de resolución para poder ser cerradas, asegurando que los problemas sean atendidos y solucionados de manera adecuada.

En la bitácora de fallas, los registros se organizan según el estado, mostrando primero las fallas abiertas para una atención inmediata. La bitácora está organizada en varias columnas, donde:

- **Fecha y Hora**: Indica el momento en que se reportó la falla.
- **Estado**: Muestra el estado actual de la falla.

.. note:: 
    
    - **Abierto**: Pendiente de resolver.
    - **Cerrado**: Falla resuelta.

- **Ubicación**: Indica la ubicación donde ocurrió la falla.
- **Lugar de la falla**: Especifica la zona exacta dentro de la ubicación donde se presentó el problema.
- **Falla**: Tipo de problema o malfuncionamiento reportado.
- **Evidencia**: Fotografías o documentos que respalden la existencia de la falla y faciliten su comprensión para los responsables.
- **Comentarios**: Observaciones adicionales relacionadas con la falla, como detalles de su origen o posibles soluciones.
- **Reporta**: Guardia o persona que realizó el reporte de la falla.
- **Responsable**: Responsable para dar seguimiento a la falla y asegurar su solución.

.. image:: /imgs/Soter/Soter98.png
    :width: 850px

Nueva Falla
^^^^^^^^^^^

Para registrar una nueva falla en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Presione el botón azul ``+Nueva Falla`` ubicado en la esquina derecha de la bitácora. Se abrirá un modal para el registro de la nueva falla.
4. Complete los campos requeridos según corresponda:

- **Ubicación**: Seleccione la ubicación donde se ha presentado la falla.
- **Área**: Seleccione el área específica dentro de la ubicación donde ocurrió la falla.
- **Fecha**: Indique la fecha en la que se detectó la falla.
- **Hora**: Registre la hora exacta de la detección de la falla.
- **Falla**: Seleccione el tipo de falla de la lista predefinida. 
- **Objeto afectado**: Especifique el objeto que ha sido afectado por la falla (si aplica).

.. note:: Algunas fallas están relacionadas con objetos que afectan. Por ejemplo, la falla **Mal funcionamiento de equipos informáticos** puede afectar a un objeto específico como una laptop, servidor, etc.

- **Evidencia**: Adjunte fotografías u otros archivos visuales que muestren la falla detectada.
- **Documentación**: Adjunte documentos relevantes a la falla (manuales, informes técnicos, etc.).
- **Comentarios**: Agregue detalles adicionales que consideren importantes para el seguimiento de la falla.
- **Reporta**: Guardia o personal que está reportando la falla.
- **Responsable a solucionar**: Seleccione la persona encargada de resolver la falla.

5. Presione ``Registrar`` para finalizar el registro de la falla.

.. image:: /imgs/Soter/Soter99.png
    :width: 500px

Visualizar Falla
^^^^^^^^^^^^^^^^

Para consultar los detalles de una falla registrada en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Ubique la falla deseada.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna.

4. Haga clic en el ícono de vista ubicado en la misma fila de la falla que desea revisar. Esto abrirá un modal que mostrará todos los detalles de la falla seleccionada.

.. image:: /imgs/Soter/Soter100.png

5. Una vez revisada la información, presione el botón ``Cerrar`` o el ícono ``X`` para salir de la ventana de detalles y regresar a la lista de la bitácora de fallas.

.. image:: /imgs/Soter/Soter101.png
    :width: 650px

Actualizar una falla
^^^^^^^^^^^^^^^^^^^^

Para modificar los detalles de una falla registrada en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Ubique la falla deseada.

.. note:: Si hay múltiples registros, la búsqueda por columna le permitirá encontrar la falla específica de manera más eficiente.

4. Haga clic en el ícono de edición ubicado en la misma fila de la falla que desea actualizar. Esto abrirá un modal con los detalles de la falla.

.. image:: /imgs/Soter/Soter102.png

5. Modifique los campos necesarios.

.. seealso:: Consulte los campos en la sección `nueva falla <#nueva-falla>`_ :octicon:`report;1em;sd-text-info`.

7. Una vez que haya realizado las modificaciones necesarias, presione el botón ``Actualizar`` para confirmar los cambios.

.. note:: Las actualizaciones se reflejarán de inmediato en la bitácora de fallas y estarán disponibles para todos los usuarios autorizados.

.. image:: /imgs/Soter/Soter103.png
    :width: 650px

Cerrar Falla
^^^^^^^^^^^^

A diferencia de los incidentes, las fallas requieren un proceso de seguimiento que implica la revisión del problema y la eventual resolución para poder marcar el registro como **Cerrado**. Esto asegura que todos los problemas técnicos sean debidamente atendidos y resueltos, manteniendo la operatividad de las instalaciones.

.. attention:: El cierre de una falla es un proceso que corresponde únicamente al responsable asignado al momento de crear la falla.

Para cerrar una falla registrada en la bitácora una vez que ha sido solucionada, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**. 
3. Ubique la falla que desea cerrar.

.. note:: Si hay múltiples registros, la búsqueda por columna le permitirá encontrar la falla específica de manera más eficiente.

4. Haga clic en el ícono de **check** (palomita) ubicado en la misma fila de la falla que desea cerrar. Esto abrirá un modal.

.. image:: /imgs/Soter/Soter104.png

6. Complete los siguientes campos en el modal de cierre:

- **Folio del reporte de acción correctiva**: Ingrese el número de folio correspondiente a la acción correctiva que se llevó a cabo para solucionar la falla.
- **Comentario**: Agregue un comentario detallando la solución aplicada o cualquier observación relevante sobre el proceso de cierre.
- **Evidencia de solución**: Cargue fotografías que muestren la solución implementada y el estado actual de la situación.
- **Documento de solución**: Adjunte cualquier documento relevante que respalde la solución aplicada, como reportes de mantenimiento, certificados de reparación, etc.

7. Una vez que haya completado todos los campos, presione el botón ``Cerrar`` para finalizar el proceso.

.. image:: /imgs/Soter/Soter105.png
    :width: 650px

.. warning:: 
    
    - Una falla solo puede ser cerrada una vez. 
    - Al cerrar la falla, el registro se actualizará y pasará a la sección de **Resueltos**.
    - Una vez que una falla está marcada como resuelta, no podrá ser editada ni cerrada nuevamente.

    .. image:: /imgs/Soter/Soter106.png
        :width: 780px

Eliminar un Registro
^^^^^^^^^^^^^^^^^^^^

1. Ubíquese en la interfaz de ``Fallas`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Filtre las fallas según su estado (opcional).

.. note:: Si tiene muchos registros, utilice la barra de búsqueda para encontrar la falla específica que desea eliminar.

4. Ubique la falla deseada en la bitácora.
5. Seleccione el ícono de **Eliminar** (ícono de papelera) en la misma fila de la falla que desea eliminar.

.. image:: /imgs/Soter/Soter107.png

6. Presione el botón ``Confirmar`` en el modal de confirmación para proceder con la eliminación de la falla.

.. image:: /imgs/Soter/Soter108.png

Eliminar Múltiples Registros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Ubíquese en la interfaz de ``Fallas`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas** para visualizar los registros.
3. Filtre las fallas según su estado (opcional).

.. note:: Utilice la barra de búsqueda si desea buscar y seleccionar registros específicos para eliminar.

4. Marque las casillas de verificación de las fallas que desea eliminar.
5. Presione el botón ``Eliminar`` ubicado en la esquina superior de la bitácora.

.. image:: /imgs/Soter/Soter109.png
    :width: 880px

6. En el modal de confirmación, presione ``Confirmar`` para eliminar las fallas seleccionadas.

.. image:: /imgs/Soter/Soter96.png
    :width: 500px

7. Presione ``OK`` para cerrar el modal de confirmación y regresar a la lista actualizada de fallas.

.. image:: /imgs/Soter/Soter110.png
    :width: 500px

.. LIGAS DE INTERÉS EXTERNO 

.. |Soter| raw:: html

    <a href="https://srv.linkaform.com/solucion_accesos/login.html" target="_blank">Soter</a>
    
.. |aqui| raw:: html

    <a href="https://srv.linkaform.com/solucion_accesos/login.html" target="_blank">aquí</a>

.. |linkaform| raw:: html

   <a href="https://www.linkaform.com/" target="_blank">LinkaForm</a>