.. _soter-turno:

=====
Turno
=====

Esta funcionalidad permite al usuario iniciar y cerrar su turno en la caseta de vigilancia asignada, además de consultar información relevante sobre la caseta y su estado actual. 

Observe la siguiente imagen que muestra la interfaz completa y considere los siguientes apartados para más detalles.

.. hint:: Revise las siguientes secciones para obtener más detalles y casos de uso sobre cada componente de la interfaz.

.. image:: /imgs/Soter/Soter4.png  
   :width: 880px

Información Personal
--------------------

En este apartado, encontrará la información personal de su cuenta, incluyendo los siguientes detalles:

- **Nombre**: Su nombre completo registrado en la cuenta.
- **Puesto**: El puesto o cargo que ocupa.
- **Correo electrónico**: La dirección de correo asociada a su cuenta.

.. warning:: Si los datos son incorrectos, comuníquese con su administrador para solicitar la corrección.
    
Cambiar Imagen de Perfil
^^^^^^^^^^^^^^^^^^^^^^^^

Para actualizar la imagen de su perfil, siga estos pasos:

1. Presione el botón ``Cambiar Imagen``.
2. Seleccione la nueva imagen desde su dispositivo. La imagen se actualizará automáticamente en su perfil.

.. image:: /imgs/Soter/Soter16.png

Información de la Ubicación
---------------------------

Esta sección muestra información detallada sobre la ubicación actual de la caseta en la que se encuentra. Podrá encontrar la siguiente información:

- **Ubicación**: Muestra el nombre de la planta o instalación donde se encuentra la caseta.
- **Ciudad**: Indica la ciudad en la que está ubicada la planta.
- **Estado**: Muestra el estado correspondiente a la ubicación.
- **Dirección**: Proporciona la dirección completa de la planta.
- **Caseta**: Indica la caseta dentro de la planta que está asignada para su uso.

.. warning:: El inicio de su turno quedará registrado en la caseta seleccionada.

.. image:: /imgs/Soter/Soter5.png  

.. _estado-caseta:

Estado de la Caseta
^^^^^^^^^^^^^^^^^^^

Este apartado muestra el estado actual de disponibilidad de la caseta seleccionada en la ubicación.

Si la caseta está **disponible**, se mostrará únicamente este dato y podrá iniciar turno.

.. image:: /imgs/Soter/Soter7V2.png

Si la caseta **no está disponible**, no podrá iniciar turno hasta que `cambie de caseta <#cambiar-caseta>`_ :octicon:`report;1em;sd-text-info` o `fuerce el cierre <#forzar-cierre>`_ :octicon:`report;1em;sd-text-info`, según sea necesario.

Cuando una caseta no está disponible, se muestran los siguientes datos:

- **Guardia en turno**: Nombre del guardia actualmente en turno en esa caseta.
- **Fecha de Inicio de turno**: Indica la fecha y hora en que el guardia actual inició su turno.

.. image:: /imgs/Soter/Soter9V2.png

.. _cambiar-caseta:

Cambiar Caseta
^^^^^^^^^^^^^^

Esta funcionalidad le permite cambiar entre diferentes ubicaciones y/o casetas. Para realizar el cambio, siga estos pasos:

1. Haga clic en el botón **Cambiar Caseta**, ubicado en la esquina superior de la sección.
2. Seleccione una caseta de la lista desplegada en el modal. La información de la ubicación se actualizará automáticamente.
                
.. image:: /imgs/Soter/Soter6.png      

.. warning:: Verifique que la ubicación sea la misma en la que se encuentra, ya que cualquier acción o registro que haga quedará asociado a esa caseta y ubicación. 

.. _forzar-cierre:

Forzar Cierre
^^^^^^^^^^^^^

Esta funcionalidad permite finalizar manualmente un turno en caso de que el guardia anterior no haya registrado su salida. Es útil para asegurar que la caseta quede disponible para su uso.

.. note:: Esta opción solo está disponible si la caseta seleccionada **no está disponible**.

Para forzar el cierre de la caseta, siga los siguientes pasos:

1. Seleccione el botón ``Forzar Cierre`` ubicado en la parte inferior de la sección.
2. Lea cuidadosamente el mensaje y presione el botón ``Sí`` para confirmar el cierre o ``Cancelar`` para abortar la operación.

.. image:: /imgs/Soter/Soter8.png  

.. caution:: Utilice esta funcionalidad con precaución y únicamente en situaciones donde sea absolutamente necesario cerrar el turno de forma forzada.

Guardias de Apoyo
-----------------

Los **guardias de apoyo** son aquellos que asisten en situaciones de emergencia, relevos u otras necesidades operativas. En este apartado, podrá seleccionar a otros guardias activos para que inicien su turno en la misma caseta y colaboren en las labores de vigilancia.

Para agregar guardias de apoyo a su turno, siga estos pasos:

1. Revise la lista de guardias disponibles en la misma ubicación.
2. Marque la casilla junto al nombre del guardia que desea agregar como apoyo.

.. image:: /imgs/Soter/Soter10.png

Agregar Guardia de Apoyo
^^^^^^^^^^^^^^^^^^^^^^^^

Esta funcionalidad permite agregar nuevos **guardias de apoyo** una vez que ha iniciado el turno.  

.. note:: Al comenzar el turno, solo aparecerán los guardias que hayan sido seleccionados previamente.

Para agregar un nuevo guardia a la lista de apoyo, siga estos pasos:

1. Presione el botón ``Agregar guardia de apoyo`` ubicado en la parte inferior derecha de la sección.
2. Identifique al o los guardias que desea agregar y presione el botón ``Seleccionar``. Automáticamente, estos guardias se agregarán a la lista de la sección.

.. image:: /imgs/Soter/Soter11.png

Finalizar Turno de un Guardia de Apoyo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para registrar la salida de un guardia de apoyo, siga estos pasos:

1. Presione el icono de salida ubicado junto al nombre del guardia.
2. Presione ``Sí`` para confirmar la salida del guardia o presione ``Cancelar`` para mantenerlo en la lista.

.. image:: /imgs/Soter/Soter12.png
    :width: 600px

Resumen de Actividad
--------------------

Esta sección muestra un panorama general del estado actual de la caseta y su entorno, aquí podrá encontrar:

- **Visitas dentro**: Indica el número de visitas que actualmente se encuentran dentro de las instalaciones de la ubicación.

- **Artículos Concesionados**: Cantidad de artículos prestados temporalmente a empleados que aún no han sido devueltos.

- **Incidentes Pendientes**: Total de incidentes reportados que aún no han sido resueltos y requieren seguimiento.

- **Vehículos Estacionados**: Número de vehículos registrados dentro de la ubicación.

- **Gafetes Pendientes**: Cantidad de gafetes entregados a visitantes que aún no han sido devueltos.

.. image:: /imgs/Soter/Soter13.png

Estado del turno
----------------

Este apartado muestra la situación actual del turno, dónde:

- **Cerrado**: Indica que aún no ha iniciado el turno.
- **Iniciado**: Indica que el turno ya ha sido iniciado.

.. image:: /imgs/Soter/Soter14.png
        
.. note:: 
    
    Considere que la fecha y hora mostradas corresponden al momento exacto en que presiona el botón para iniciar o cerrar el turno.

    El estado del turno afectará directamente el `estado de la caseta <#estado-caseta>`_ :octicon:`report;1em;sd-text-info`.  

    - Al **iniciar turno**, la caseta **no estará disponible** para otros guardias (si aplica).
    - Al **cerrar turno**, la caseta volverá a estar **disponible** para su asignación.

Notas
-----

.. image:: /imgs/Soter/Soter15.png

.. seealso:: Consulte la sección sobre `notas <#section-notas>`_ :octicon:`report;1em;sd-text-info` para más detalles.

Iniciar/Cerrar Turno
--------------------

Para  iniciar o finalizar un turno en la caseta asignada, siga los pasos:

1. Presione el botón correspondiente, ubicado en la parte superior derecha de la interfaz.

.. note:: La apariencia del botón cambiará según el estado del turno (**activo** o **cerrado**).  

.. admonition:: Ejemplo
    :class: pied-piper

    Una vez iniciado el turno, el menú se habilitará con acceso a las funcionalidades permitidas.

    .. image:: /imgs/Soter/Soter2.png

    .. image:: /imgs/Soter/Soter3.png

.. hint:: Antes de iniciar turno, revise toda la información proporcionada en la sección.