.. _doc-employee:

================
Módulo Empleados
================

El **Módulo Empleados** proporciona las configuraciones y datos necesarios para la gestión de empleados, útil para otros módulos. Con las formas y catálogos del módulo, podrá:

- Registrar y administrar datos personales y laborales de los empleados.
- Gestionar y asignar departamentos y puestos dentro de la empresa.

Observe y analice el siguiente diagrama de flujo del módulo empleados. Este diagrama representa el flujo de acciones necesarias para realizar el registro de un empleado.

.. image:: /imgs/Modulos/Empleados/Empleados1.png

.. warning:: Antes de utilizar el módulo de empleados, asegúrese de contar con las configuraciones y registros necesarios del :ref:`doc-base` :octicon:`report;1em;sd-text-info`.

Catálogos del Módulo Empleados
==============================

Los catálogos que componen el módulo de empleados son los siguientes:

- **Departamentos**: Incluye una lista de departamentos.
- **Puestos**: Proporciona información sobre los puestos asignados a los empleados.
- **Configuración de Departamentos y Puestos**: Contiene registros sobre la relación entre departamentos y puestos.
- **Teams**: Contiene información sobre los diferentes equipos de trabajo.
- **Empleados**: Almacena los registros de los empleados.
- **Empleados Jefes Directos**: Copia del catálogo empleados.

.. image:: /imgs/Modulos/Empleados/Empleados2.png

.. _ver-config:

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

Departamentos
-------------

El catálogo **Departamentos** contiene registros de los diferentes departamentos de una empresa.

.. note:: Al instalar el módulo, encontrará registros demo de posibles departamentos. Considere que son solo opciones y siempre puede modificar los campos del catálogo y/o registros. 

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Empleados/Empleados3.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Empleados/Empleados4.png

Puestos
-------

El catálogo **Puestos** contiene información sobre los puestos asignados a los empleados.

.. note:: Del mismo modo que el catálogo de departamentos, encontrará registros demo de posibles puestos. Considere que son solo opciones y siempre puede modificar los campos del catálogo y/o registros. 

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Empleados/Empleados5.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Empleados/Empleados6.png

Configuración de Departamentos y Puestos
----------------------------------------

Este catálogo contiene la relación entre departamentos y puestos.

.. caution:: Este catálogo debe contener los mismos registros que la forma `Configuración de Departamentos y Puestos <#id3>`_ :octicon:`report;1em;sd-text-info`. Revise la documentación correspondiente para más detalles importantes sobre este catálogo.

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Empleados/Empleados7.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Empleados/Empleados8.png

Empleados
---------

El catálogo **Empleados** contiene los mismos registros detallados de los empleados que de la `forma empleados <#id5>`_ :octicon:`report;1em;sd-text-info`. Este catálogo es de suma utilidad, ya que es utilizado por otros módulos. 

.. attention:: Este catálogo está preparado para recibir un registro derivado de una forma, por lo tanto, no deberá preocuparse por contestar manualmente el registro en el catálogo. Simplemente preocúpese por responder la forma de `empleados <#id5>`_ :octicon:`report;1em;sd-text-info` y Linkaform se encargará de sincronizar el mismo registro en este catálogo.

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Empleados/Empleados9.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Empleados/Empleados10.png

.. note:: Recuerde que un catálogo actúa como una base de datos donde se puede tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

Empleados Jefes Directos
------------------------

El catálogo **Empleados Jefes Directos** contiene registros de los empleados de la empresa.  

.. caution:: Este catálogo contiene los mismos registros que la forma `empleado <#id5>`_ :octicon:`report;1em;sd-text-info`. Este catálogo está preparado para recibir un registro derivado de la forma, por lo tanto, no deberá preocuparse por contestar manualmente el registro en el catálogo.

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Empleados/Empleados11.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Empleados/Empleados12.png

.. warning:: Debido a que un mismo ``ID`` no puede ser utilizado dos veces en el mismo formulario o catálogo, se realiza una copia con los mismos campos pero con ``IDs`` distintos para poder utilizarlo.

Formularios del Módulo Empleados
================================

Los formularios que componen al módulo empleados son los siguientes:

- **Configuración de Departamentos y Puestos**: Administra la relación entre departamentos y puestos.
- **Empleados**: Gestiona la información personal y laboral de los empleados.

.. image:: /imgs/Modulos/Empleados/Empleados13.png

Configuración de Departamentos y Puestos
----------------------------------------

Esta forma le permitirá relacionar los registros del departamento con los registros de los puestos.

.. warning:: Cuando crea un nuevo registro en esta forma, este debe sincronizarse con el catálogo `Configuracion de Departamentos y Puestos <#configuracion-de-departamentos-y-puestos>`_ :octicon:`report;1em;sd-text-info`. Sin embargo, recuerde que un catálogo no contiene el campo sobre grupo repetitivo, por lo que no es posible aplicar el flujo de sincronización automáticamente.
    
    Por lo tanto, si crea un registro en la forma, asegúrese de registrarlo manualmente en el catálogo. Si son varios registros, considere hacer la importación masiva.

    Actualmente, se está trabajando para solucionar este detalle. 

.. tab-set::

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Empleados/Empleados14.png

    .. tab-item:: Estructura

        .. image:: /imgs/Modulos/Empleados/Empleados15.png

Empleados
---------

Esta forma permite almacenar y gestionar la información personal y laboral de los empleados. 

Cuando crea un nuevo registro en la forma, este se encarga de sincronizar el mismo registro en dos catálogos distintos, observe el siguiente diagrama.


.. image:: /imgs/Modulos/Empleados/Empleados24.png
    :align: center

Para sincronizar el registro con el catálogo ``Empleados`` utiliza la acción ``Sync Catalog Records`` en la configuración de flujo.

.. attention:: Si modifica la forma de ``Empleados``, asegúrese de modificar el catálogo de ``Empleados`` y revise que el ``id`` del campo de la forma sea el mismo que el ``id`` del campo del catálogo. 

Mientras que para la sincronización con el catálogo ``Empleados Jefes Directos`` utiliza la acción ``Forma a Catálogo``.

.. attention:: Si modifica la forma de ``Empleados``, asegúrese de modificar el catálogo de ``Empleados Jefes Directos``. A diferencia de la acción ``Sync Catalog Records``, al utilizar la acción ``Forma a Catálogo`` no obliga a que los ``ids`` de los campos sean los mismos, pero tenga cuidado al configurar el flujo. 
    
.. seealso:: Para más detalles sobre configuraciones de flujos de trabajo consulte :ref:`flujos` :octicon:`report;1em;sd-text-info`.
    
Al responder la forma, considere las diferentes secciones de las páginas que contienen la forma.

.. tab-set::

    .. tab-item:: Datos Generales

        En este apartado podrá registrar información básica del empleado. Dentro de este apartado los campos más importantes son:

        - Estatus dentro de la empresa
        - Estatus de disponibilidad 

        .. image:: /imgs/Modulos/Empleados/Empleados16.png

    .. tab-item:: Domicilio

        En este apartado podrá registrar la dirección física del empleado. Observe que la forma utiliza el catálogo ``Contacto`` del módulo base. 

        .. seealso:: Consulte :ref:`doc-base` :octicon:`report;1em;sd-text-info` para más detalles.

        .. image:: /imgs/Modulos/Empleados/Empleados17.png

    .. tab-item:: Detalles de Contratación

        En este apartado podrá registrar información sobre la contratación del empleado.

        Observe que la forma utiliza el catálogo ``Compañía`` y ``Empleados Jefes Directos`` del módulo base.

        .. seealso:: Consulte :ref:`doc-base` :octicon:`report;1em;sd-text-info` para más detalles.

        .. image:: /imgs/Modulos/Empleados/Empleados18.png

    .. tab-item:: Puestos de Trabajo

        En este apartado podrá registrar información sobre los puestos que ha ocupado o ocupa actualmente el empleado y el ambiente en el que se desarrolla.

        Observe que se utiliza el catálogo ``Configuración de Departamentos y Puestos`` del módulo base.

        .. note:: Si tiene dificultades para seleccionar una opción, siga los pasos indicados en `pasos <#ver-config>`_ :octicon:`report;1em;sd-text-info`.

        .. image:: /imgs/Modulos/Empleados/Empleados19.png

    .. tab-item:: Datos Bancarios

        Esta sección es útil para recabar información bancaria del empleado para el pago de salarios u otros fines.

        .. image:: /imgs/Modulos/Empleados/Empleados20.png

    .. tab-item:: Formas de Contacto

        En esta sección podrá registrar otras formas de contacto con el empleado.

        .. image:: /imgs/Modulos/Empleados/Empleados21.png

    .. tab-item:: Documentos

        Permite el almacenamiento de documentos relacionados con el empleado.

        .. image:: /imgs/Modulos/Empleados/Empleados22.png

    .. tab-item:: Link

        Este apartado registra datos adicionales para el módulo de accesos. Son identificaciones para el acceso a un portal de control de visitas.

        .. seealso:: Consulte el módulo de accesos si desea conocer más detalles.

        .. image:: /imgs/Modulos/Empleados/Empleados23.png

Ha completado con éxito el proceso de configuración y utilización del módulo de empleados. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.