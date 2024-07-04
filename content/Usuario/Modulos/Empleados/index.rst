.. _doc-employee:

================
Módulo Empleados
================

El **Módulo Empleados** proporciona las configuraciones y datos necesarios para la gestión de empleados en la plataforma. Con las formas y catálogos del módulo puede gestionar información relacionada con:

- **Empleados**: Registro y administración de datos personales y laborales de los empleados.
- **Departamentos**: Gestión de departamentos dentro de la empresa.
- **Roles**: Asignación y administración de roles y permisos de empleados.

Observe y analice el siguiente diagrama de flujo del módulo empleados. Este diagrama representa el flujo de acciones que ocurren al realizar el registro de un empleado.

.. image:: /imgs/Modulos/Empleados/Empleados1.png

Catálogos del Módulo Empleados
==============================

Los catálogos que componen al módulo empleados son los siguientes:

- **Empleados**: Contiene los registros de los empleados.
- **Departamentos**: Incluye una lista de departamentos y sus detalles.
- **Roles**: Proporciona información sobre los roles y permisos asignados a los empleados.

.. _ver-mas:

.. dropdown:: Ver más

    Para acceder a los catálogos, navegue a la opción ``Catálogos > Catálogos`` en el menú lateral.


    Para acceder a los registros de los catálogos, diríjase a ``Catálogos > Registros de catálogo`` en el menú lateral.

    Si al responder un catálogo con catálogos anidados no muestra los registros necesarios, asegúrese de:

    - Actualizar el catálogo.
    - Verificar que el catálogo contenga registros.
    - Verificar que la configuración del catálogo sea la correcta.

    .. seealso:: Consulte :ref:`campo-catalogo` :octicon:`report;1em;sd-text-info` para más detalles sobre la configuración del catálogo.

Catálogo Empleados
------------------

El catálogo **Empleados** contiene registros de los empleados de la empresa.


Catálogo Departamentos
----------------------

El catálogo **Departamentos** contiene registros de los diferentes departamentos de la empresa.

.. note:: Al instalar el módulo, estos registros ya están incluidos. 


Catálogo Puestos
----------------

El catálogo **Puestos** contiene información sobre los roles y permisos asignados a los empleados.

.. note:: El catálogo **Puestos** se utiliza para definir los permisos y accesos de los empleados dentro de la plataforma.

Formularios del Módulo Empleados
================================

El formulario que compone al módulo empleados es el siguiente:

- **Registro de Empleado**: Gestiona la información personal y laboral de los empleados.

Forma Registro de Empleado
--------------------------

La forma **Registro de Empleado** permite almacenar y gestionar la información personal y laboral de los empleados. Esta forma permite realizar varias acciones útiles, como almacenar nombres, números de teléfono, direcciones de correo electrónico, cargos, departamentos y roles de los empleados.

.. note:: 
    
    Cuando crea un registro en la forma, automáticamente se crea un registro sincronizado en el `catálogo empleados <#catalogo-empleados>`_ :octicon:`report;1em;sd-text-info`, que es utilizado por otros módulos. Para más detalle sobre la sincronización de registros consulte la documentación correspondiente.


