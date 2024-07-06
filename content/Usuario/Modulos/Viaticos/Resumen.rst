=======
Resumen
=======

Este diagrama representa el flujo de acciones que ocurren al realizar una solicitud de viáticos.

1. El proceso inicia con el registro de una solicitud de viáticos.

.. mermaid::

    graph TB
    
        %% Formularios
        form_solicitud_viaticos(#1 Solicitud de viáticos);
        form_autorizacion_viaticos(#3 Autorización de viáticos);
        form_entrega_anticipo_efectivo(#1.1 Entrega de anticipo efectivo);
        form_registros_gastos_viajes(#2 Registro de gastos de viaje);
        
        %% Catalogos
        catalogo_solicitud_gastos([Solicitud de gastos]);
        
        %% Conexiones
        form_solicitud_viaticos == status = pendiente autorización <br> ó gasto = 0 ==> form_autorizacion_viaticos;
        form_solicitud_viaticos == status = autorizado ==> form_entrega_anticipo_efectivo;
        form_entrega_anticipo_efectivo == status = autorizado <br> Actualiza ==> catalogo_solicitud_gastos;
        form_registros_gastos_viajes == Actualiza sets de gasto ==> form_solicitud_viaticos;
        form_registros_gastos_viajes == Monto actualizado - gasto ==> catalogo_solicitud_gastos;
        
        %% Estilos
        style form_solicitud_viaticos fill:#40c057,stroke:#333,stroke-width:1px;
        style form_autorizacion_viaticos fill:#40c057,stroke:#333,stroke-width:1px;
        style form_entrega_anticipo_efectivo fill:#40c057,stroke:#333,stroke-width:1px;
        style form_registros_gastos_viajes fill:#40c057,stroke:#333,stroke-width:1px;
        style catalogo_solicitud_gastos fill:#228be6,stroke:#333,stroke-width:1px;

Formularios
===========

Formularios que componen el módulo de viáticos:

- Registro de gastos
- Solicitud de viáticos
- Entrega de anticipo
- Autorización de viáticos

.. image:: /imgs/Modulos/Viaticosss/Resumen/formasModViaticos.png
    :alt: Formas del módulo viáticos
    :align: center

Figura 1. Formas del módulo viáticos

Catálogos
=========

Los catálogos que componen el módulo son:

- Empleados
- Moneda
- Responsables de autorizar gastos
- Solicitud de gastos.

