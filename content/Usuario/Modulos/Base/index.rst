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

Catálogo Timezones
------------------

El catálogo **Timezones** contiene registros de las diferentes zonas horarias del mundo. 

.. note:: Al instalar el módulo, este catálogo ya incluye registros predefinidos.

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Base/Base7.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Base/Base12.png

Catálogo Países
---------------

El catálogo **Países** contiene registros de los 250 países del mundo. Observe que el catálogo proporciona el nombre del país, el código del país y el código de marcación.

.. note:: Al instalar el módulo, estos registros ya están incluidos. 

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Base/Base8.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Base/Base13.png

Catálogo Estados
----------------

Actualmente, el catálogo **Estados** contiene únicamente registros de los 32 estados que componen a México. 

.. caution:: El catálogo **Estados** utiliza el catálogo **Países**. Si tiene conflictos con el catálogo de países, no podrá registrar nuevos estados.

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Base/Base9.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Base/Base14.png

Si los estados, provincias, distritos, o divisiones políticas de su país no se encuentran aquí, podrá registrarlos o importar los registros de manera masiva. 
 
.. seealso:: Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para una carga masiva de registros al catálogo.

Catálogo Compañía
-----------------

El catálogo **Compañía** contiene registros sobre diferentes compañías, lo cual es útil para el :ref:`doc-employee` :octicon:`report;1em;sd-text-info`, facilitando la administración y la relación entre empleados y la empresa.

.. note:: Al instalar el módulo, este catálogo **no** incluye registros demo, por lo que deberá realizar la inserción de los registros que necesite.

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Base/Base11.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Base/Base15.png

Formularios del Módulo Base
===========================

El formulario que compone al módulo base es el siguiente:

- **Contacto**: Gestiona los contactos asociados con las compañías y otras entidades.

.. image:: /imgs/Modulos/Base/Base3.png

Forma Contacto
--------------

La forma **Contacto** ofrece una funcionalidad similar a la de la lista de contactos en un teléfono. Sirve para almacenar y gestionar la información de contacto de personas y empresas. 

Esta forma permite realizar varias acciones útiles, como almacenar nombres, números de teléfono, direcciones de correo electrónico, direcciones físicas, geolocalización y fotos de perfil de los contactos.

.. note:: 
    
    Cuando crea un registro en la forma, automáticamente se crea un registro sincronizado en el `catálogo contacto <#catalogo-contacto>`_ :octicon:`report;1em;sd-text-info`, que es utilizado por otros módulos. Para más detalle sobre la sincronización de registros consulte la documentación correspondiente.

.. tab-set::

    .. tab-item:: Responder

        Antes de responder la forma, asegúrese de tener registros en los `catálogos <#catalogos-del-modulo-base>`_ :octicon:`report;1em;sd-text-info` propios del módulo. 

        Analice la siguiente información para responder la forma y finalizar el proceso:

        **Nombre de Dirección**: Este campo es requerido. Coloque el nombre del alias con el que desea guardar la dirección del contacto.
                
        .. note:: Asegúrese de que el nombre sea descriptivo; considere utilizar el nombre completo del contacto en caso de tener múltiples contactos.
        
        .. image:: /imgs/Modulos/Base/Base18.png

        Opcionalmente, coloque una imagen descriptiva del contacto.

        .. image:: /imgs/Modulos/Base/Base19.png

        Coloque la dirección, colonia, ciudad y código postal del contacto.

        .. image:: /imgs/Modulos/Base/Base21.png

        Coloque el país y estado del contacto. 

        .. note:: Observe que se utiliza el catálogo estados. Si tiene dificultades para seleccionar una opción, siga los estos `pasos <#ver-mas>`_ :octicon:`report;1em;sd-text-info`.

        .. image:: /imgs/Modulos/Base/Base20.png

        En el campo **Geolocalización**, coloque la dirección del contacto en la barra de búsqueda. Automáticamente, Linkaform le mostrará coincidencias de la dirección proporcionada. 
        
        Observe que después del gráfico muestra la latitud y longitud.

        .. image:: /imgs/Modulos/Base/Base22.png

        Coloque el teléfono del contacto.

        .. note:: Campo no requerido.

        .. image:: /imgs/Modulos/Base/Base23.png

        Coloque el email del contacto.

        .. note:: Campo no requerido.

        .. image:: /imgs/Modulos/Base/Base24.png

        En el campo **Tipo de Contacto**, seleccione según corresponda:
        
        - **Empresa**: Dirección de la ubicación de una empresa.
        - **Persona**: Dirección personal de la residencia del usuario.
        - **Dirección**: Dirección única sobre una ubicación en concreto.

        .. image:: /imgs/Modulos/Base/Base25.png

        En el campo **Status**, seleccione según corresponda:
            
        - **Activo**: Si el contacto es vigente y utilizado.
        - **Inactivo**: Si el contacto no es utilizado.

        .. image:: /imgs/Modulos/Base/Base26.png

    .. tab-item:: Registro

        .. image:: /imgs/Modulos/Base/Base17.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Base/Base16.png

Ha completado con éxito el proceso de configuración y utilización del módulo base. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.