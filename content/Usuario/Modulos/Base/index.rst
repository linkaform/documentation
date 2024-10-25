.. _doc-base:

===========
Módulo Base
===========

El **Módulo Base** proporciona las formas y catálogos necesarios para:

- Configurar y administrar diferentes zonas horarias.
- Registrar y gestionar países para facilitar la organización de datos y procesos específicos por región.
- Administrar divisiones geográficas dentro de los países.
- Registrar compañías, lo que permite la gestión de datos específicos de cada empresa.
- Gestionar contactos asociados con las compañías y otras entidades.

Observe y analice el siguiente diagrama de flujo del módulo base. Este diagrama representa cada paso requerido para llevar a cabo el registro de un contacto.

.. image:: /imgs/Modulos/Base/Base1.png

Catálogos del Módulo Base
=========================

Los catálogos que componen al módulo base son los siguientes:

- **Timezones**: Contiene diferentes zonas horarias.
- **Países**: Incluye una lista de países y sus detalles.
- **Estados**: Proporciona información sobre los estados o divisiones geográficas dentro de los países.
- **Compañías**: Contiene datos de diversas compañías registradas.
- **Contactos**: Almacena la información de contactos relacionados con las compañías y otras entidades.

.. image:: /imgs/Modulos/Base/Base4.png

.. _ver-mas:

.. dropdown:: Ver más

    Para acceder a los catálogos, navegue a la opción ``Catálogos > Catálogos`` en el menú lateral.

    .. image:: /imgs/Modulos/Base/Base5.png

    Para acceder a los registros de los catálogos, diríjase a ``Catálogos > Registros de catálogo`` en el menú lateral.

    .. image:: /imgs/Modulos/Base/Base6.png

    Si al responder un catálogo con catálogos anidados no muestra los registros necesarios, asegúrese de:

    - Actualizar el catálogo.
    - Verificar que el catálogo contenga registros.

    .. image:: /imgs/Modulos/Base/Base10.png

    - Verificar que la configuración del catálogo sea la correcta.

    .. seealso:: Consulte :ref:`campo-catalogo` :octicon:`report;1em;sd-text-info` para más detalles sobre la configuración del catálogo.

Timezones
---------

El catálogo contiene registros de las diferentes zonas horarias del mundo. Observe los registros:

.. image:: /imgs/Modulos/Base/Base7.png

.. note:: Al instalar el módulo, este catálogo ya incluye registros predefinidos.

.. _catalog-paises:

Países
------

El catálogo contiene registros de los 250 países del mundo. Observe que cada registro proporciona el nombre, código del país y el código de marcación.

.. image:: /imgs/Modulos/Base/Base8.png

.. note:: Al instalar el módulo, estos registros ya están incluidos. 

.. _catalog-estados:

Estados
-------

El catálogo contiene los registros de las divisiones administrativas de un país. Consulte las siguientes pestañas para más detalles.

.. tab-set::

    .. tab-item:: Estructura

        El catálogo está compuesto por los siguientes campos:

        - **Nombre del Estado**: El nombre oficial del estado, provincia o región.
        - **Código del Estado**: Identificador único o abreviado para el estado.
        - **País**: Especifica el país al que pertenece el estado
        
        .. seealso:: Consulte el catálogo `países <#catalog-paises>`_ :octicon:`report;1em;sd-text-info` para más detalles.

        .. image:: /imgs/Modulos/Base/Base14.png

    .. tab-item:: Registros

        Observe los siguientes registros:

        .. image:: /imgs/Modulos/Base/Base9.png

        .. seealso:: Al instalar el módulo, se proporciona una lista de registros de los estados de México. Si su país cuenta con estados, provincias, distritos u otras divisiones políticas que no están incluidos en esta lista, puede agregarlos manualmente o realizar una carga masiva de registros. Para más detalles sobre cómo importar registros, consulte la sección :ref:`importar-registros` :octicon:`report;1em;sd-text-info`.

Compañía
--------

El catálogo contiene registros sobre diferentes compañías, lo cual es útil para el :ref:`doc-employee` :octicon:`report;1em;sd-text-info`, facilitando la administración y la relación entre empleados y la empresa.

.. note:: Al instalar el módulo, este catálogo **no** incluye registros demo, por lo que deberá realizar la inserción de los registros que necesite.

.. image:: /imgs/Modulos/Base/Base11.png

.. _catalogo-contacto:

Contacto
--------

El catálogo **Contacto** contiene los mismos registros que de la forma `contacto <#form-contacto>`_ :octicon:`report;1em;sd-text-info`. Para más detalles sobre la estructura, consulte la forma correspondiente.

.. attention:: Este catálogo está preparado para recibir un registro derivado de una forma, por lo tanto, no deberá preocuparse por contestar manualmente el catálogo. Simplemente complete la forma adecuada y LinkaForm se encargará de sincronizar el registro en este catálogo.

Revise los siguientes registros de ejemplo:

.. image:: /imgs/Modulos/Base/Base27.png
    :width: 880px

.. note:: Recuerde que un catálogo es útil para tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

Formularios del Módulo Base
===========================

El formulario que compone al módulo base es el siguiente:

- **Contacto**: Gestiona los contactos asociados con las compañías y otras entidades.

.. image:: /imgs/Modulos/Base/Base3.png

.. _form-contacto:

Contacto
--------

La forma **Contacto** ofrece una funcionalidad similar a la de la lista de contactos en un teléfono. Sirve para almacenar y gestionar la información de contacto de personas y empresas. 

Para responder la forma, revise las siguiente información que detalla los campos necesarios para crear un contacto. Asegúrese de prestar atención a la información proporcionada y las notas importantes.

.. warning:: Antes de responder la forma, asegúrese de tener registros en los catálogos propios del módulo. 

**Nombre de Dirección**: Nombre del alias con el que desea guardar la dirección del contacto.
                
.. note:: Asegúrese de que el nombre sea descriptivo; considere utilizar el nombre completo del contacto en caso de tener múltiples contactos.

**Imagen**: Imagen descriptiva del contacto (opcionalmente).

.. image:: /imgs/Modulos/Base/Base18.png

**Dirección**: Ubicación específica del lugar (número, calle, etc.).

**Colonia**: Nombre del barrio o colonia.

**Ciudad**: Nombre de la ciudad.

**Código Postal**: Código postal de la dirección.

.. image:: /imgs/Modulos/Base/Base19.png

**País**: Nombre del país donde se encuentra la dirección del contacto.

**Estado**: Nombre del estado o región dentro del país.

.. seealso:: Consulte el catálogo `estados <#catalog-estados>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. image:: /imgs/Modulos/Base/Base20.png

**Geolocalización**: Ubicación exacta del contacto.

.. hint:: Ingrese la dirección o las coordenadas de latitud y longitud en la barra de búsqueda, y LinkaForm mostrará automáticamente las coincidencias disponibles para la ubicación proporcionada.

.. image:: /imgs/Modulos/Base/Base22.png

**Teléfono**: Número telefónico del contacto (opcionalmente).
**Email**: Correo electrónico del contacto (opcionalmente).

.. image:: /imgs/Modulos/Base/Base23.png

**Tipo de Contacto**: seleccione según corresponda:
        
- **Empresa**: Dirección de la ubicación de una empresa.
- **Persona**: Dirección personal de la residencia del usuario.
- **Dirección**: Dirección única sobre una ubicación en concreto.

.. image:: /imgs/Modulos/Base/Base25.png

**Status**: seleccione según corresponda:
            
- **Activo**: Si el contacto es vigente y utilizado.
- **Inactivo**: Si el contacto no es utilizado.

.. image:: /imgs/Modulos/Base/Base26.png

.. note:: Cuando crea un registro en la forma, automáticamente se crea un registro sincronizado en el `catálogo contacto <#catalogo-contacto>`_ :octicon:`report;1em;sd-text-info`, que es utilizado por otros módulos. Para más detalle sobre la sincronización de registros consulte la documentación correspondiente.

Ha completado con éxito el proceso de configuración y utilización del módulo base. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.