.. _doc-ubicaciones:

==================
Módulo Ubicaciones
==================

El **Módulo Ubicaciones** proporciona las herramientas necesarias para gestionar y administrar información relacionada con diferentes ubicaciones y sus áreas asociadas. 

.. warning:: Antes de utilizar el módulo, asegúrese de contar con las configuraciones y registros necesarios del :ref:`doc-base` :octicon:`report;1em;sd-text-info`.

Observe y analice el siguiente diagrama de flujo del módulo ubicaciones. Este diagrama representa el flujo de acciones necesarias para registrar y gestionar información de ubicaciones y áreas.

.. image:: /imgs/Modulos/Ubicaciones/ubicaciones1.png

Formas del Módulo Ubicaciones
=============================

Las formas que componen el módulo de ubicaciones son las siguientes:

- **Ubicaciones**: Registra todas las ubicaciones gestionadas.
- **Áreas de las Ubicaciones**: Contiene registros sobre las áreas específicas dentro de cada ubicación.

Para acceder a las formas, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Ubicaciones``.

.. image:: /imgs/Modulos/Ubicaciones/Ubicaciones9.png

.. _form-ubicaciones:

Ubicaciones
-----------

Esta forma permite registrar múltiples ubicaciones, útil para administrar diversas sucursales pertenecientes a una misma empresa.

Al crear un nuevo registro en esta forma, se sincroniza automáticamente con el `catálogo ubicaciones <#catalog-ubicaciones>`_ :octicon:`report;1em;sd-text-info`. Para sincronizar el registro con el catálogo, la forma utiliza la acción ``Sync Catalog Records`` en la configuración de flujo.

.. seealso:: Para más detalles sobre configuración de flujos de trabajo consulte :ref:`flujos` :octicon:`report;1em;sd-text-info`.

.. attention:: Si realiza modificaciones a la forma, asegúrese de actualizar también el catálogo de ``Ubicaciones`` y verifique que los identificadores de los campos sean los mismos.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Ubicaciones** incluye los siguientes campos:

        - **Ubicación**: Nombre descriptivo de la ubicación.
        - **Dirección**: Dirección de la ubicación (enlazado al catálogo **Contacto** del :ref:`doc-base` :octicon:`report;1em;sd-text-info`).

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones10.png

    .. tab-item:: Registros

        Analice el siguiente registro.

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones11.png

.. _form-areas-ubicacion:

Áreas de las Ubicaciones
----------------------------

Esta forma permite registrar toda información a cerca de las diferentes áreas dentro de una ubicación específica. 

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Áreas de las Ubicaciones** incluye los siguientes campos:

        - **Nombre del Área**: Nombre de la área específica.
        - **Tipo de Área**: Tipo al que pertenece el área (enlazado al catálogo `Tipo de Áreas <#catalog-tipo-areas>`_ :octicon:`report;1em;sd-text-info`).
        - **Ubicación**: Ubicación a la que pertenece el área (enlazado al catálogo `Ubicaciones <#catalog-ubicaciones>`_ :octicon:`report;1em;sd-text-info`).
        - **Dirección**: Dirección específica del área dentro de la ubicación (enlazado al catálogo **Contacto** del :ref:`doc-base` :octicon:`report;1em;sd-text-info`).
        - **Estatus del Área**: Estado actual del área (**abierta**, **cerrada**, **clausurada**, en **mantenimiento**, **disponible**, **ocupada**).
        - **Estatus**: Estado administrativo del área (**activa** o **inactiva**).
        - **QR Área**: Código QR asociado al área para su identificación y acceso.
        
        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones12.png

    .. tab-item:: Registros

        Cuando registre una nueva área dentro de una ubicación, es posible que no cuente con una dirección específica. En tal caso, utilice la dirección de la ubicación general.

        Sin embargo, para ubicaciones que no se encuentran físicamente dentro del edificio pero forman parte de la misma instalación, utilice una dirección específica. Por ejemplo:

        Para casetas de vigilancia, que se encuentran en diferentes puntos fuera de la instalación, asegúrese de asignar una dirección específica para cada una. Observe la siguiente imagen.

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones13.png

        Cuando crea un nuevo registro en la forma, este se sincroniza automáticamente en dos catálogos distintos, como se muestra en el siguiente diagrama.

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones14.png
            :align: center

        Para sincronizar el registro con el catálogo **Áreas de las Ubicaciones**, se utiliza la acción ``Sync Catalog Records`` en la configuración de flujo. Para la sincronización con el catálogo **Áreas de las Ubicaciones Salidas**, se emplea la acción ``Forma a Catálogo``.

        .. warning:: Si realiza modificaciones en la forma, asegúrese de actualizar también los catálogos. 
            
            Para la acción ``Sync Catalog Records``, verifique que los identificadores de los campos sean los mismos. La acción ``Forma a Catálogo`` no requiere que los **ids** de los campos coincidan, pero es importante configurar el flujo correctamente.

        .. seealso:: Para más detalles sobre configuraciones de flujos de trabajo consulte :ref:`flujos` :octicon:`report;1em;sd-text-info`.

Catálogos del Módulo Ubicaciones
================================

Los catálogos que componen el módulo de ubicaciones son los siguientes:

- **Ubicaciones**: Registra todas las ubicaciones gestionadas.
- **Tipo de Áreas**: Clasifica los diferentes tipos de áreas dentro de las ubicaciones.
- **Áreas de las Ubicaciones**: Contiene registros sobre las áreas específicas dentro de cada ubicación.
- **Áreas de las Ubicaciones Salidas**: Copia del catálogo áreas de las ubicaciones.

Para acceder a los catálogos, seleccione la opción ``Catálogos > Catálogos`` en el menú lateral y ubique la carpeta ``Ubicaciones``.

.. image:: /imgs/Modulos/Ubicaciones/Ubicaciones2.png

.. _catalog-ubicaciones:

Ubicaciones
-----------

Este catálogo contiene los mismos registros que la `forma ubicaciones <#form-ubicaciones>`_ :octicon:`report;1em;sd-text-info`.

.. important:: Este catálogo está preparado para recibir un registro derivado de una forma, por lo tanto, no deberá preocuparse por contestar manualmente el registro en el catálogo. Simplemente responda la forma `ubicaciones <#form-ubicaciones>`_ :octicon:`report;1em;sd-text-info` y Linkaform se encargará de sincronizar el mismo registro en este catálogo.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Ubicaciones** incluye los siguientes campos:

        - **Ubicación**: Nombre descriptivo de la ubicación.
        - **Dirección**: Dirección de la ubicación (enlazado al catálogo **Contacto** del :ref:`doc-base` :octicon:`report;1em;sd-text-info`).

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones5.png

    .. tab-item:: Registros

        Observe los registros en el catálogo de **Ubicaciones**.

        .. note:: Recuerde que un catálogo actúa como una base de datos donde se puede tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones6.png

.. _catalog-tipo-areas:

Tipo de Áreas
-------------

Este catálogo clasifica las diferentes áreas dentro de una ubicación.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Tipo de Áreas** incluye:

        - **Tipo de Área**: Nombre descriptivo del tipo de área.

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones3.png

    .. tab-item:: Registros

        Observe los registros en el catálogo **Tipo de Áreas**.

        .. note:: Al instalar el módulo, encontrará registros de ejemplo en este catálogo. Estos son solo opciones sugeridas y puede modificar los campos y registros según sea necesario.

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones4.png

.. _catalog-areas-ubicacion:

Áreas de las Ubicaciones
----------------------------

Este catálogo contiene los mismos registros que la `forma áreas dentro de la ubicación <#form-areas-ubicacion>`_ :octicon:`report;1em;sd-text-info`.

.. attention:: El catálogo **Áreas de las Ubicaciones Salidas** replica la estructura, campos y configuraciones del catálogo **Áreas de las Ubicaciones**.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Áreas de las Ubicaciones** incluye los siguientes campos:

        - **Nombre del Área**: Nombre de la área específica.
        - **Tipo de Área**: Tipo al que pertenece el área.
        - **Ubicación**: Ubicación a la que pertenece el área.
        - **Dirección**: Dirección específica del área dentro de la ubicación.
        - **Estatus del Área**: Estado actual del área (**abierta**, **cerrada**, **clausurada**, en **mantenimiento**, **disponible**, **ocupada**).
        - **Estatus**: Estado administrativo del área (**activa** o **inactiva**).
        - **QR Área**: Código QR asociado al área para su identificación y acceso.
        
        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones7.png

    .. tab-item:: Registros

        Ejemplo de registros en el catálogo de **Áreas de las Ubicaciones**:

        .. important:: Este catálogo se actualiza automáticamente a partir de los registros de la forma `áreas dentro de la ubicación <#form-areas-ubicacion>`_ :octicon:`report;1em;sd-text-info`, por lo que no es necesario ingresar datos manualmente. Simplemente complete la forma y Linkaform sincronizará los registros en este catálogo.

        .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones8.png
        
        Observe que el catálogo cuenta con algunos filtros. Al instalar el módulo, es importante que verifique la existencia de estos filtros, ya que son utilizados por el módulo de accesos.

        En caso de que no encuentre los filtros necesarios, consulte la documentación sobre cómo :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` para obtener más detalles y aplicarlos con los siguientes valores:

        .. code-block::
            :caption: Guarde el filtro con el nombre ``Filtro_areas_comunes``

            Campo = Tipo De Area
            Condición = NO es igual a
            Valor = Caseta

            // Este filtro mostrará todos los registros de áreas, excepto las de las casetas.

        .. code-block::
            :caption: Guarde el filtro con el nombre ``Filtro_casetas``

            Campo = Tipo De Area
            Condición = Igual a
            Valor = Caseta

            // Este filtro mostrará todos los registros de casetas.

        .. warning:: Asegúrese de revisar y aplicar los mismos filtros para el catálogo **Áreas de las Ubicaciones Salidas**. 

Ha completado con éxito el proceso de configuración y utilización del módulo de ubicaciones. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.


