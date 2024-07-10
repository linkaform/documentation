.. _doc-ubicaciones:

==================
Módulo Ubicaciones
==================

El **Módulo Ubicaciones** proporciona las herramientas necesarias para gestionar y administrar información relacionada con diferentes ubicaciones y sus áreas asociadas. Con las formas y catálogos del módulo, podrá:

- Registrar y administrar datos sobre diversas ubicaciones físicas.
- Gestionar y clasificar áreas dentro de cada ubicación.

.. warning:: Antes de utilizar el módulo, asegúrese de contar con las configuraciones y registros necesarios del :ref:`doc-base` :octicon:`report;1em;sd-text-info`.

Observe y analice el siguiente diagrama de flujo del módulo ubicaciones. Este diagrama representa el flujo de acciones necesarias para registrar y gestionar información de ubicaciones y áreas.

.. image:: /imgs/Ubicaciones/Ubicaciones1.png

.. _catalog-ubicaciones:

Catálogos del Módulo Ubicaciones
================================

Los catálogos que componen el módulo de ubicaciones son los siguientes:

- **Tipo de Áreas**: Clasifica los diferentes tipos de áreas dentro de las ubicaciones.
- **Ubicaciones**: Registra todas las ubicaciones gestionadas.
- **Áreas de las Ubicaciones**: Contiene registros sobre las áreas específicas dentro de cada ubicación.
- **Áreas de las Ubicaciones Salidas**: Copia del catálogo áreas de las ubicaciones.

Para acceder a los catálogos, seleccione la opción ``Catálogos > Catálogos`` en el menú lateral y ubique la carpeta ``Ubicaciones``.

.. image:: /imgs/Ubicaciones/Ubicaciones2.png

.. _catalog-tipo-areas:

Tipo de Áreas
-------------

El catálogo **Tipo de Áreas** contiene los diferentes tipos de áreas que pueden existir dentro de una ubicación. Este catálogo se utiliza para clasificar las áreas y facilita la organización y búsqueda.

.. note:: Al instalar el módulo, encontrará registros de ejemplo en este catálogo. Estos son solo opciones sugeridas y puede modificar los campos y registros según sea necesario.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Tipo de Áreas** incluye:

        - **Tipo de Área**: Nombre descriptivo del tipo de área.

        .. image:: /imgs/Ubicaciones/Ubicaciones3.png

    .. tab-item:: Registros

        Ejemplo de registros en el catálogo de **Tipo de Áreas**.

        .. image:: /imgs/Ubicaciones/Ubicaciones4.png

Ubicaciones
===========

El catálogo **Ubicaciones** contiene los registros de todas las ubicaciones de las sucursales dependientes de su empresa. 
Este catálogo se sincroniza con la forma de `Ubicaciones <#form-ubicaciones>`_ :octicon:`report;1em;sd-text-info`.

.. attention:: Este catálogo está preparado para recibir un registro derivado de una forma, por lo tanto, no deberá preocuparse por contestar manualmente el registro en el catálogo. Simplemente preocúpese por responder la forma de `empleados <#id5>`_ :octicon:`report;1em;sd-text-info` y Linkaform se encargará de sincronizar el mismo registro en este catálogo.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Ubicaciones** incluye los siguientes campos:

        - **Ubicación**: Nombre descriptivo de la ubicación.
        - **Contacto**: Dirección física de la ubicación.

        .. note:: Observe que ``Contacto`` es un catálogo del módulo base.

    .. tab-item:: Registros

        Ejemplo de registros en el catálogo de **Ubicaciones**:

.. note:: Recuerde que un catálogo actúa como una base de datos donde se puede tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

.. _catalog-areas-ubicacion:

Áreas Dentro de la Ubicación
----------------------------

El catálogo **Áreas Dentro de la Ubicación** contiene los registros de todas las áreas específicas dentro de cada ubicación.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Áreas Dentro de la Ubicación** incluye los siguientes campos:
        - **Ubicación**: Nombre de la ubicación a la que pertenece el área.
        - **Área**: Nombre descriptivo del área.
        - **Tipo de Área**: Tipo de área (enlace al catálogo **Tipo de Áreas**).
        - **Descripción**: Descripción detallada del área.



    .. tab-item:: Registros

        Ejemplo de registros en el catálogo de **Áreas Dentro de la Ubicación**:



.. _catalog-areas-ubicacion-salidas:

Áreas Dentro de la Ubicación Salidas
------------------------------------

El catálogo **Áreas Dentro de la Ubicación Salidas** contiene registros de las salidas de cada área dentro de una ubicación.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo **Áreas Dentro de la Ubicación Salidas** incluye los siguientes campos:
        - **Ubicación**: Nombre de la ubicación a la que pertenece el área.
        - **Área**: Nombre del área que tiene la salida.
        - **Salida**: Descripción de la salida.
        - **Destino**: Nombre del destino al que lleva la salida.

    .. tab-item:: Registros

        Ejemplo de registros en el catálogo de **Áreas Dentro de la Ubicación Salidas**:



Formas del Módulo Ubicaciones
============================

Las formas que componen el módulo de ubicaciones son las siguientes:

- **Ubicaciones**: Permite ingresar y gestionar toda la información relevante sobre las diferentes ubicaciones.
- **Áreas Dentro de la Ubicación**: Permite ingresar y gestionar toda la información relevante sobre las diferentes áreas dentro de una ubicación específica.

.. _form-ubicaciones:

Ubicaciones
-----------

La forma **Ubicaciones** permite ingresar y gestionar toda la información relevante sobre las diferentes ubicaciones. Al crear un nuevo registro en esta forma, se sincroniza automáticamente con el `catálogo ubicaciones <#catalog-ubicaciones>`_ :octicon:`report;1em;sd-text-info`.

Para acceder a la forma, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Ubicaciones``.

.. attention:: Si realiza modificaciones en la forma de ``Ubicaciones``, asegúrese de actualizar también el catálogo de ``Ubicaciones`` y verificar que los identificadores de los campos sean los mismos.

.. _form-areas-ubicacion:

Áreas Dentro de la Ubicación
----------------------------

La forma **Áreas Dentro de la Ubicación** permite ingresar y gestionar toda la información relevante sobre las diferentes áreas dentro de una ubicación específica. Al crear un nuevo registro en esta forma, se sincroniza automáticamente con el `catálogo áreas dentro de la ubicación <#catalog-areas-ubicacion>`_ :octicon:`report;1em;sd-text-info`.

Para acceder a la forma, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Áreas Dentro de la Ubicación``.

.. attention:: Si realiza modificaciones en la forma de ``Áreas Dentro de la Ubicación``, asegúrese de actualizar también el catálogo de ``Áreas Dentro de la Ubicación`` y verificar que los identificadores de los campos sean los mismos.

Ha completado con éxito el proceso de configuración y utilización del módulo de ubicaciones. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.







