=====================================
Diagrama de flujo del módulo viáticos
=====================================

Este diagrama representa el flujo de acciones que ocurren al realizar
una solicitud de viáticos.

1. El proceso inicia con el registro de una solicitud de viáticos.

.. mermaid::

    graph TD;
        A[Django] -->|Cada PDF es una plantilla| B(LinkaForm);
        B -->|Plantillas genéricas| D[No tienen dueño, disponibles para todos];
        B -->|Plantillas hechas a la medida| E[Es exclusivo y personalizado];

.. code:: mermaid

   ---
   title: FLUJO MÓDULO DE VIÁTICOS
   ---

   flowchart TB
       %% Formularios
       form_solicitud_viaticos(#1 Solicitud de viáticos);
       form_autorizacion_viaticos(#3 Autorización de viáticos);
       form_entrega_anticipo_efectivo(#1.1 Entrega de anticipo efectivo)
       form_registros_gastos_viajes(#2 Registro de gastos de viaje);
       %% form_reserva_viajes(Reserva de viajes);
       
      %% Catalogos
       catalogo_solicitud_gastos([Solicitud de gastos]);


       %% Conexiones
       form_solicitud_viaticos == status = pendiente autorización <br> ó gasto = 0 ==> form_autorizacion_viaticos;
       form_solicitud_viaticos -- status = autorizado --> form_entrega_anticipo_efectivo;
       form_entrega_anticipo_efectivo == status = autorizado <br> Actualiza ==> catalogo_solicitud_gastos;
       %% form_solicitud_viaticos == status = autorizado  ==> catalogo_solicitud_gastos;

       form_registros_gastos_viajes == Actualiza sets de gasto ==> form_solicitud_viaticos;
       form_registros_gastos_viajes == Monto actualizado - gasto ==> catalogo_solicitud_gastos;
     
       %% Estilos

       style form_solicitud_viaticos fill:#40c057,stroke:#333,stroke-width:1px;
       style form_autorizacion_viaticos fill:#40c057,stroke:#333,stroke-width:1px;
       style form_entrega_anticipo_efectivo fill:#40c057,stroke:#333,stroke-width:1px; 
       style form_registros_gastos_viajes fill:#40c057,stroke:#333,stroke-width:1px;
       style catalogo_solicitud_gastos fill:#228be6,stroke:#333,stroke-width:1px;

.. code:: mermaid

   flowchart  BT
       %% Catalogos
       catalogo_solicitud_gastos([Solicitud de gastos]); catalogo_empleados([Empleados]);
       catalogo_moneda([Moneda]);
       catalogo_responsables_gastos([Responsables de gastos]);
    
       style catalogo_solicitud_gastos fill:#228be6,stroke:#333,stroke-width:1px; 
       style catalogo_empleados fill:#228be6,stroke:#333,stroke-width:1px;
       style catalogo_moneda fill:#228be6,stroke:#333,stroke-width:1px;
       style catalogo_responsables_gastos fill:#228be6,stroke:#333,stroke-width:1px;

..

.. note::
  Los rectángulos en color azul representan los **módulos** y los de color verde representan los **formularios**.

Formularios
-----------

Formularios que componen al **módulo de viáticos**: - Registro de gastos
de viaje - Solicitud de viáticos - Entrega de anticipo - Autorización de
viáticos

.. figure:: /imgs/Modulos/Viaticos/formasModViaticos.png
   :alt: Formas del módulo viáticos

   Formas del módulo viáticos

Catálogos
---------

Los **catálogos** que componen al módulo son: - Empleados - Moneda -
Responsables de autorizar gastos - Solicitud de gastos
