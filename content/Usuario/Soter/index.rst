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

``https://srv.linkaform.com/solucion_accesos/login.html`` 

.. seealso:: Ingrese directamente |aqui| :octicon:`report;1em;sd-text-info`.

2. Escriba el correo y la contraseña en los campos correspondientes.

.. warning:: El correo y la contraseña son los mismos que una cuenta vigente de |linkaform| :octicon:`report;1em;sd-text-info`. 
   
   En caso de no disponer de credenciales, solicítelas al administrador de su empresa o al equipo de Linkaform y lleve a cabo el proceso para :ref:`activar-cuenta-usuario` :octicon:`report;1em;sd-text-info`.

3. Presione el botón ``Continuar``. Será redirigido automáticamente a la interfaz de `turnos <#iniciar-turno>`_ :octicon:`report;1em;sd-text-info`.

.. hint:: Si por algún motivo existe algún problema con la autenticación, le sugerimos iniciar sesión primero en su cuenta de |linkaform| :octicon:`report;1em;sd-text-info` y luego volver a intentar iniciar sesión en |Soter| :octicon:`report;1em;sd-text-info`.

.. image:: /imgs/Soter/Soter1.png
    :width: 880px

.. _iniciar-turno:

Iniciar Turno
=============

La interfaz de **Turnos** permite realizar el **Check-in** y **Check-out** en la caseta de vigilancia correspondiente. Observe la siguiente imagen que muestra la interfaz completa:

.. image:: /imgs/Soter/Soter4.png
   :width: 880px

Esta interfaz muestra datos importantes sobre la caseta y su situación actual. Considere los siguientes elementos importantes:

**Menú**: Ubicado en la parte superior, este menú proporciona acceso a otras funcionalidades del sistema. Está disponible únicamente cuando el guardia inicia su turno. 

**Botón de Iniciar/Cerrar Turno**: Ubicado en la parte superior derecha de la interfaz, este botón cambiará de acuerdo con el estado del turno. 

- Si el turno aún no ha comenzado, el botón permitirá iniciar el turno. 

.. image:: /imgs/Soter/Soter2.png

- Si el turno ya está activo, el botón permitirá cerrar el turno, registrando el final de la jornada en la caseta.

.. image:: /imgs/Soter/Soter3.png

Revise las siguientes pestañas para obtener más detalles y casos de uso sobre cada componente de la interfaz.

.. tab-set::

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

        **Estatus de la Caseta**: Indica si la caseta está **Disponible** o **No Disponible**. 

        .. grid:: 2
            :gutter: 0

            .. grid-item-card::
                :columns: 6

                Si la caseta está **Disponible**, se mostrará únicamente este campo y el guardia podrá iniciar turno presionando el botón correspondiente.

            .. grid-item-card::
                :columns: 6

                .. image:: /imgs/Soter/Soter7.png

            .. grid-item-card::
                :columns: 6

                Si la caseta **No está Disponible**, se mostrarán:

                - **Guardia en Turno**: Muestra el nombre del guardia actualmente en turno en esa caseta.
                - **Fecha de Inicio de Turno**: Indica la fecha y hora en que el guardia actual inició su turno.

            .. grid-item-card::
                :columns: 6

                .. image:: /imgs/Soter/Soter9.png

        **Forzar Cierre**

        Observe el botón ubicado en la esquina superior de la sección. Este botón permite al guardia finalizar el turno actual de manera manual, por ejemplo, en caso de que el guardia anterior no haya registrado su salida. Para forzar el cierre, siga los siguientes pasos:

        1. Seleccione el botón ``Forzar Cierre``. Se abrirá un modal.
        2. Lea cuidadosamente el mensaje del modal. Encontrará información relevante acerca del guardia que tiene el turno actual en la caseta que desea cerrar.
        3. Presione el botón ``Sí`` para confirmar o ``Cancelar`` para abortar la operación.

        .. image:: /imgs/Soter/Soter8.png  

        .. warning:: Use esta funcionalidad con precaución y únicamente en situaciones donde sea absolutamente necesario cerrar el turno de forma forzada.

        **Consideraciones para Iniciar Turno**

        Si el **Estatus** de la caseta es **Disponible** el guardia podrá iniciar su turno de forma regular.
        Si el **Estatus** de la caseta **No Disponible**, el guardia no podrá iniciar su turno hasta que:

        - Cambie de caseta utilizando la opción en el apartado de **Información de la Ubicación**.
        - O utilice la opción de **Forzar Cierre** para liberar la caseta y poder iniciar su turno.

    .. tab-item:: Guardias de Apoyo

        lorem

    .. tab-item:: Información de ingreso

        lorem

    .. tab-item:: Datos de la Caseta

        lorem

    .. tab-item:: Notas

        lorem 

    .. tab-item:: Información Personal

        lorem
.. _proceso-registro-visitantes:

Proceso de Registro de Visitantes 
=================================

lorem inpus



.. LIGAS DE INTERÉS EXTERNO 

.. |Soter| raw:: html

    <a href="https://srv.linkaform.com/solucion_accesos/login.html" target="_blank">Soter</a>
    
.. |aqui| raw:: html

    <a href="https://srv.linkaform.com/solucion_accesos/login.html" target="_blank">aquí</a>

.. |linkaform| raw:: html

   <a href="https://www.linkaform.com/" target="_blank">LinkaForm</a>