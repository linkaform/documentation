.. _doc-viaticos:

================
Módulo Viáticos
================

El **Módulo Viáticos** proporciona las configuraciones y datos necesarios para la gestión y control eficiente de los gastos de viaje. Con las formas y catálogos del módulo, podrá:

- Registrar y administrar solicitudes de viáticos presentadas por parte de los empleados.
- Autorizar solicitudes de viáticos.
- Controlar gastos de viaje a traves del seguimiento detallado de los gastos realizados durante los viajes de los empleados.

Observe y analice el siguiente diagrama de flujo del módulo viáticos. Este diagrama representa el flujo de acciones necesarias para realizar la solicitud, autorización y registro de gastos de viáticos.

.. image:: /imgs/Modulos/Viaticos/Viaticos1.png

.. .. mermaid::

    graph TD;
        subgraph Flujo_Módulo_Empleados;
            4[EMPLEADOS] --> |Sincroniza registro| 4.1[CATÁLOGO Empleados];
            4.2[CATÁLOGO Empleados Jefes Directos] --> |Sincroniza registro| 4.1;
            4.1 --> |Sincroniza registro| 4;
            4 --> M[MODULO Contacto];
            3[Configuración de Departamentos y Puestos] --> |Sincroniza registro| 4;
            4 --> 3;
            1[CATÁLOGO Departamentos] --> 3;
            2[CATÁLOGO Puestos] --> 3;
            3.1[CATÁLOGO Configuración de Departamentos y Puestos] --> 3;
            4 --> 3.1;
            3.1 --> 4;
            4 --> 1;
            4 --> 2;
            4.1 --> 4.2;
        end;
        T[CATÁLOGO Teams];

.. warning:: Para utilizar el módulo de viáticos, asegúrese de contar con las configuraciones y registros necesarios en el :ref:`doc-employee` :octicon:`report;1em;sd-text-info`.

Catálogos del Módulo Viáticos
=============================

Este módulo cuenta con los siguientes catálogos:

- **Conceptos de Gastos**: Contiene registros sobre posibles conceptos de gastos.
- **Moneda**: Proporciona información sobre las diferentes monedas aceptadas para los gastos.
- **Responsables de Autorizar Gastos**: Incluye una lista de responsables que pueden autorizar y gestionar los gastos.
- **Solicitud de Gastos**: Almacena los registros de las solicitudes de viáticos realizadas por los empleados.

.. image:: /imgs/Modulos/Viaticos/Viaticos2.png

.. _ver-config-viaticos:

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

Conceptos de Gastos
-------------------

El catálogo **Conceptos de Gastos** está diseñado para gestionar y registrar los diferentes tipos de gastos que pueden ser solicitados dentro de una solicitud de gasto. Este catálogo permite a los empleados seleccionar el concepto adecuado al realizar sus solicitudes de viáticos. 

.. tab-set::

    .. tab-item:: Registros

        .. note:: Al instalar el módulo, encontrará registros demo de posibles conceptos de gasto. Considere que son solo opciones y siempre puede modificar los campos del catálogo y/o registros. 

        .. image:: /imgs/Modulos/Viaticos/Viaticos3.png

    .. tab-item:: Estructura

        Este catálogo incluye los siguientes campos principales:

        - **Concepto**: Describe el tipo de gasto o el motivo por el cual se realiza la solicitud de viáticos.
        - **Cuenta Contable**: Especifica la cuenta contable asociada al concepto de gasto.

        .. image:: /imgs/Modulos/Viaticos/Viaticos4.png

Moneda
------

El catálogo **Moneda** contiene información sobre las diferentes denominaciones aceptadas para los gastos. Este catálogo permite a los usuarios seleccionar la moneda adecuada al realizar o autorizar solicitudes de gastos.

.. tab-set::

    .. tab-item:: Registros
        
        .. note:: Al instalar el módulo, encontrará registros que muestran posibles denominaciones de monedas. Tenga en cuenta que puede ajustar los campos del catálogo y modificar los registros según lo requiera.

        .. image:: /imgs/Modulos/Viaticos/Viaticos5.png

    .. tab-item:: Estructura

        Este catálogo incluye:

        - **Moneda**: Representa el símbolo o abreviatura utilizado para identificar la moneda (por ejemplo, USD para dólar estadounidense, COP para pesos colombianos, etc.).

        .. image:: /imgs/Modulos/Viaticos/Viaticos6.png

Responsables de Autorizar Gastos
--------------------------------

Este catálogo contiene la información sobre las personas responsables de autorizar y gestionar los gastos. 

.. tab-set::

    .. tab-item:: Registros

        .. warning:: Tenga cuidado con la veracidad de los datos de este catálogo, ya que son utilizados para notificar al responsable de manera electrónica para autorizar los gastos.

        .. image:: /imgs/Modulos/Viaticos/Viaticos7.png

    .. tab-item:: Estructura

        Este catálogo incluye campos como:

        - **Nombre**: Responsable de autorizar gastos.                                                                                                                                   
        - **Correo Electrónico**: Dirección de correo electrónico del responsable.

        .. image:: /imgs/Modulos/Viaticos/Viaticos8.png

Solicitud de Gastos
-------------------

El catálogo **Solicitud de Gastos** contiene los registros de las solicitudes de viáticos realizadas por los empleados.

.. attention:: Este catálogo está preparado para recibir un registro derivado de una forma, por lo tanto, no deberá preocuparse por contestar manualmente el registro en el catálogo. Simplemente preocúpese por responder la forma de `Solicitud de Gastos <#solicitud-de-gastos>`_ :octicon:`report;1em;sd-text-info` y Linkaform se encargará de sincronizar el mismo registro en este catálogo.

Formularios del Módulo Viáticos
===============================

Los formularios que componen al módulo de viáticos son los siguientes:

- **Solicitud de Viáticos**: Gestiona la información de las solicitudes de viáticos por parte de los empleados.
- **Autorización de Viáticos**: Administra el proceso de autorización de las solicitudes.
- **Registros de Gastos de Viaje**: Permite registrar los gastos realizados durante los viajes.

Solicitud de Viáticos
---------------------

Esta forma permite registrar y gestionar las solicitudes de viáticos por parte de los empleados.

.. warning:: Cuando crea un nuevo registro en esta forma, este debe sincronizarse con el catálogo `Solicitud de Gastos <#solicitud-de-gastos>`_ :octicon:`report;1em;sd-text-info`. Asegúrese de que la configuración de sincronización esté correctamente definida.

Autorización de Viáticos
------------------------

Esta forma permite administrar el proceso de autorización de las solicitudes de viáticos.

.. caution:: Asegúrese de aplicar las reglas de campo necesarias para la correcta autorización de las solicitudes.

Registros de Gastos de Viaje
----------------------------

Esta forma permite registrar los gastos realizados durante los viajes.

.. attention:: Esta forma actualiza los registros en el catálogo `Solicitud de Gastos <#solicitud-de-gastos>`_ :octicon:`report;1em;sd-text-info`. Asegúrese de que los montos actualizados correspondan a los gastos reales.

.. note:: Recuerde que un catálogo actúa como una base de datos donde se puede tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

Ha completado con éxito el proceso de configuración y utilización del módulo de viáticos. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.