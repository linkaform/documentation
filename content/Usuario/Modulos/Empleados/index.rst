.. _doc-employee:

================
Módulo Empleados
================

El **Módulo Empleados** proporciona los elementos y configuraciones necesarias para la gestión de empleados. Con las formas y catálogos del módulo, podrá:

- Registrar y administrar datos personales y laborales de los empleados.
- Gestionar y asignar departamentos y puestos dentro de una empresa.

Observe y analice el siguiente diagrama de flujo del módulo. Este diagrama representa el flujo ordenado de acciones necesarias para realizar el registro de un empleado.

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

.. _catalog-departamentos:

Departamentos
-------------

El catálogo contiene registros de los diferentes departamentos de una empresa.

.. image:: /imgs/Modulos/Empleados/Empleados3.png

.. note:: Al instalar el módulo, encontrará registros demo de posibles departamentos. Considere que son solo opciones y siempre puede modificar los campos del catálogo y/o registros. 

.. _catalog-puestos:

Puestos
-------

El catálogo contiene registros sobre los puestos asignados a los empleados.

.. image:: /imgs/Modulos/Empleados/Empleados5.png

.. note:: Del mismo modo, al instalar el módulo, encontrará registros demo de posibles puestos. Considere modificar los campos del catálogo y/o registros. 

.. _catalog-departamentos-puestos:

Configuración de Departamentos y Puestos
----------------------------------------

Este catálogo es una réplica de la forma `configuración de departamentos y puestos <#id3>`_ :octicon:`report;1em;sd-text-info`, con la excepción de los grupos repetitivos.

Debido a la limitación de los catálogos para manejar grupos repetitivos, es necesario realizar la relación entre departamentos y puestos de forma manual. A continuación, se muestra un ejemplo de cómo hacerlo:

.. image:: /imgs/Modulos/Empleados/Empleados8.png

.. seealso:: Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para una importación masiva de registros.

Empleados
---------

Este catálogo es una réplica de la `forma empleados <#id5>`_ :octicon:`report;1em;sd-text-info`. Consulte la documentación correspondiente para más detalles sobre su estructura. Observe los siguientes registros de ejemplo:

.. image:: /imgs/Modulos/Empleados/Empleados9.png

Observe que el catálogo cuenta con algunos filtros. Al instalar el módulo, es importante que verifique la existencia de estos filtros, ya que son utilizados por el módulo de seguridad.

En caso de que no encuentre los filtros necesarios, consulte la documentación sobre cómo :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` para obtener más detalles y aplicarlos con los siguientes valores:

.. code-block::
    :caption: Guarde el filtro con el nombre ``Filtro_empleados``

    Campo = Nombre del departamento
    Condición = NO es igual a
    Valor = Seguridad

    // Este filtro mostrará todos los registros de empleados que no pertenecen al departamento de seguridad.

.. code-block::
    :caption: Guarde el filtro con el nombre ``Filtro_guardias``

    Campo = Nombre del departamento
    Condición = Igual a
    Valor = Seguridad

    // Este filtro mostrará todos los registros de empleados pertenecientes al departamento de seguridad. 

.. warning:: Asegúrese de revisar y aplicar los mismos filtros para el catálogo `jefes directos <#catalog-jefes-directos>`_ :octicon:`report;1em;sd-text-info`.

.. attention:: Este catálogo está preparado para recibir un registro derivado de una forma, por lo tanto, no deberá preocuparse por contestar manualmente el registro en el catálogo. Simplemente preocúpese por responder la forma de `empleados <#id5>`_ :octicon:`report;1em;sd-text-info` y Linkaform se encargará de sincronizar el mismo registro en este catálogo.

.. _catalog-jefes-directos:

Empleados Jefes Directos
------------------------

Este catálogo es otra réplica de la forma `empleados <#id5>`_ :octicon:`report;1em;sd-text-info`. Consulte la documentación correspondiente para más detalles sobre su estructura. Observe los siguientes registros de ejemplo:

.. image:: /imgs/Modulos/Empleados/Empleados11.png

.. warning:: Debido a que un mismo ``ID`` no puede ser utilizado dos veces en el mismo formulario o catálogo, se realiza una copia con los mismos campos pero con ``IDs`` distintos para poder utilizarlo.

Formularios del Módulo Empleados
================================

Los formularios que componen al módulo empleados son los siguientes:

- **Configuración de Departamentos y Puestos**: Administra la relación entre departamentos y puestos.
- **Empleados**: Gestiona la información personal y laboral de los empleados.

.. image:: /imgs/Modulos/Empleados/Empleados13.png

.. _form-departamentos-puestos:

Configuración de Departamentos y Puestos
----------------------------------------

Esta forma le permite relacionar los departamentos con los puestos. Revise el siguiente ejemplo para relacionar un departamento con sus respectivos puestos:

.. image:: /imgs/Modulos/Empleados/Empleados25.png

.. seealso:: Consulte los catálogos `puestos <#catalog-puestos>`_ :octicon:`report;1em;sd-text-info` y `departamentos <#catalog-departamentos>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. warning:: Los registros de esta forma son utilizados por otras formas, lo que requiere que estén disponibles también en un catálogo. Sin embargo, debido a la limitación de que los catálogos no admiten campos de grupo repetitivo, no es posible realizar una sincronización automática en estos casos.

    Por lo tanto, cuando registre la configuración de departamentos y puestos en la forma, asegúrese de también ingresarlo manualmente en el `catálogo configuración de departamentos y puestos <#catalog-departamentos-puestos>`_ :octicon:`report;1em;sd-text-info`. Si tiene múltiples registros, considere utilizar la funcionalidad de importación masiva para agilizar el proceso; consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para más detalles.

    Actualmente, estamos trabajando en una solución para mejorar este flujo y automatizar completamente la sincronización en futuras versiones.

Empleados
---------

Esta forma permite almacenar y gestionar la información personal y laboral de los empleados. 

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

Al crear un nuevo registro en la forma, este se sincroniza automáticamente en dos catálogos distintos, como se muestra en el siguiente diagrama.

.. image:: /imgs/Modulos/Empleados/Empleados24.png
    :align: center

Para sincronizar el registro con el catálogo **Empleados**, se utiliza la acción ``Sync Catalog Records`` en la configuración de flujo.

.. warning:: Si modifica la forma, asegúrese de actualizar el catálogo correspondiente y verifique que el **id** del campo en la forma coincida con el **id** del campo en el catálogo. 

Para la sincronización con el catálogo **Empleados Jefes Directos**, se utiliza la acción ``Forma a Catálogo``.

.. warning:: Si modifica la forma, también asegúrese de actualizar el catálogo **Empleados Jefes Directos**. A diferencia de la acción ``Sync Catalog Records``, la acción ``Forma a Catálogo`` no requiere que los **ids** de los campos sean los mismos, pero tenga cuidado al configurar el flujo. 
    
.. seealso:: Para más detalles sobre configuraciones de flujos de trabajo, consulte :ref:`flujos` :octicon:`report;1em;sd-text-info`.

Ha completado con éxito el proceso de configuración y utilización del módulo de empleados. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.