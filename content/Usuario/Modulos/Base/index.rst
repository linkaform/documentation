===========
Módulo Base
===========

El **Módulo Base** proporciona las configuraciones y datos básicos necesarios para la operación de otros módulos. Con las formas y catálogos del módulo puede gestionar información relacionada con:

- **Zonas Horarias (Timezones)**: Configuración y administración de diferentes zonas horarias.
- **Países**: Registro y gestión de países para facilitar la organización de datos y procesos específicos por región.
- **Estados**: Administración de divisiones geográficas dentro de los países.
- **Compañías**: Registro de compañías, lo que permite la gestión de datos específicos de cada empresa.
- **Contactos**: Gestión de contactos asociados con las compañías y otras entidades.

Observe y analice el siguiente diagrama de flujo del módulo base. Este diagrama representa el flujo de acciones que ocurren al realizar el registro de un contacto.

.. image:: /imgs/Modulos/Base/Base2.png

Catálogos del Módulo Base
=========================

Los catálogos que componen al módulo base son los siguientes:

- **Timezones**: Contiene diferentes zonas horarias.
- **Países**: Incluye una lista de países y sus detalles.
- **Estados**: Proporciona información sobre los estados o divisiones geográficas dentro de los países.
- **Compañías**: Contiene datos de diversas compañías registradas.
- **Contactos**: Almacena la información de contactos relacionados con las compañías y otras entidades.

.. image:: /imgs/Modulos/Base/Base4.png

Para acceder a los catálogos, navegue a la opción ``Catálogos > Catálogos`` en el menú lateral.

.. image:: /imgs/Modulos/Base/Base5.png

Para acceder a los registros de los catálogos, diríjase a ``Catálogos > Registros de catálogo`` en el menú lateral.

.. image:: /imgs/Modulos/Base/Base6.png

Catálogo Timezones
------------------

El catálogo **Timezones** contiene registros de las diferentes zonas horarias del mundo. Al instalar el módulo, este catálogo ya incluye registros predefinidos.

.. image:: /imgs/Modulos/Base/Base7.png

Catálogo Países
---------------

El catálogo **Países** contiene registros de los 250 países del mundo. Al instalar el módulo, estos registros ya están incluidos. Observe que el catálogo proporciona el nombre del país, el código del país y el código de marcación.

.. image:: /imgs/Modulos/Base/Base8.png

Catálogo Estados
----------------

Actualmente, el catálogo **Estados** contiene únicamente registros de los 32 estados que componen a México. 

.. image:: /imgs/Modulos/Base/Base9.png

.. caution:: El catálogo **Estados** utiliza el catálogo **Países**. Si aún no tiene el catálogo de países, no podrá registrar nuevos estados.

Si los estados, provincias, distritos, o divisiones políticas de su país no se encuentran aquí, podrá registrarlos o importar los registros de manera masiva. 
 
.. seealso:: Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para una carga masiva de registros al catálogo.

Formularios del Módulo Base
===========================

El formulario que compone al módulo base es el siguiente:

- **Contacto**: Gestiona los contactos asociados con las compañías y otras entidades.

.. image:: /imgs/Modulos/Base/Base3.png
