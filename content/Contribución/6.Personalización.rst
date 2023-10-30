===============================
Personalización con extensiones
===============================

En esta sección, aprenderá acerca de algunas de las extensiones que Sphinx proporciona para crear una documentación más atractiva.

Sphinx proporciona extensiones que no solo enriquecen la documentación técnica, sino que también hacen que el proceso de documentación sea más eficiente y efectivo. Al permitir la personalización y la automatización obtendrá documentación de alta calidad. Desde correcciones ortográficas, gráficos y ecuaciones complejas, cada extensión tiene su propia documentación detallada que proporciona instrucciones sobre cómo usarla y configurarla.

Las extensiones que se mostrarán a continuación ya se encuentran instaladas y listas para usar. No obstante, si necesita una extensión nueva, se proporcionarán los pasos de configuración dentro del entorno del proyecto.

.. _etiqueta_mermaind:

Sphinxcontrib-mermaid
=====================

Esta extensión le permite incrustar gráficos Mermaid en su documentación, incluidos diagramas de flujo, diagramas de secuencia, diagramas de Gantt y más. 

Para hacer uso de mermaid, utilice la directiva ``.. mermaid::``. Al crear diagramas, debe tener en cuenta las siguientes opciones de directivas.

+------------+--------------------------------------------------+
| Propiedad  | Descripción                                      |
+============+==================================================+
| alt        | Texto alternativo para la salida HTML.           |
+------------+--------------------------------------------------+
| align      | Posición de la imagen. Opciones válidas:         |
|            | ``left``, ``center``, ``right``.                 |
+------------+--------------------------------------------------+
| caption    | Título al diagrama.                              |
+------------+--------------------------------------------------+
| zoom       | Se utiliza para habilitar el zoom del diagrama   |
|            | (en caso de que sea muy grande).                 |
+------------+--------------------------------------------------+


En cuanto a los elementos que debe incluir un diagrama Mermaid, generalmente se utilizan:

- Nodos: Representan elementos como procesos, decisiones, objetos, etc. Debe definir los nodos con un nombre único.

- Conexiones: Las conexiones, se crean con :bdg-success-line:`-->, ==> o <--`, indican la dirección en la que fluye la información o el proceso de un nodo a otro.

- Etiquetas y Texto: Puede agregar etiquetas o texto a los nodos o conexiones para proporcionar información adicional o aclaraciones.

- Estilos: Opcionalmente, puede aplicar estilos a los nodos y conexiones para personalizar la apariencia del diagrama, como colores, bordes y anchos de línea.

A continuación, se presentan algunos ejemplos que podrá utilizar. Tenga en cuenta que Mermaid es una herramienta muy flexible que le permitirá crear una amplia variedad de diagramas. Puede personalizar los diagramas según sus necesidades y documentar procesos, estructuras y relaciones de manera efectiva.

Diagrama de Flujo
-----------------

Los diagramas de flujo utilizan ``graph TD`` y ``graph TB``. Puede usar graph TD para un flujo de arriba hacia abajo (Top-Down) y graph TB para un flujo de izquierda a derecha (Left-Right). Estos diagramas son ideales para representar flujos de trabajo, procesos y estructuras.

El siguiente ejemplo es un diagrama de flujo que representa un proceso con decisiones y ramificaciones.

.. tab-set::

    .. tab-item:: Ejemplo 1

        .. mermaid::
            :alt: Ejemplo de diagrama de flujo
            :align: center
            :zoom:

            graph TB

                A(Inicio) --> B(Proceso 1)
                B --> C(Subproceso 1)
                B --> D(Subproceso 2)
                C --> E(Decisión 1)
                D --> F(Resultado 1)
                E --> G(Opción 1)
                E --> H(Opción 2)
                G --> I(Resultado 2)
                H --> I
                I --> J(Fin)

    .. tab-item:: Estructura

        .. code-block::

            .. mermaid::
                :alt: Ejemplo de diagrama de flujo
                :align: center
                :zoom:

                graph TB

                    A(Inicio) --> B(Proceso 1)
                    B --> C(Subproceso 1)
                    B --> D(Subproceso 2)
                    C --> E(Decisión 1)
                    D --> F(Resultado 1)
                    E --> G(Opción 1)
                    E --> H(Opción 2)
                    G --> I(Resultado 2)
                    H --> I
                    I --> J(Fin)

Otra forma de crear diagramas de flujo es a través de texto simple. De manera similar, utilice ``graph TD`` o ``graph TB``. La principal diferencia entre el ejemplo anterior y este radica en la forma en que está organizado. En este caso, se emplea una especie de clases para aplicar nodos y conexiones, además de la posibilidad de aplicar estilos personalizados.

.. tab-set::

    .. tab-item:: Ejemplo 2

        .. mermaid::
            :alt: Ejemplo de diagrama de flujo
            :align: center
            :zoom:

            graph TD
            
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

    .. tab-item:: Estructura
        
        .. code-block::

            .. mermaid::
                :alt: Ejemplo de diagrama de flujo
                :align: center
                :zoom:

                graph TD
                
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


Diagrama de Gantt
-----------------

Los diagramas de gantt hacen uso de ``gantt``.

Este es un diagrama de Gantt, muestra una programación de tareas a lo largo del tiempo.

.. tab-set::

    .. tab-item:: Ejemplo 3

        .. mermaid::
            :alt: Ejemplo de diagrama de Gantt
            :align: center
            :zoom:

            gantt

                title Diagrama de Gantt
                dateFormat YYYY-MM-DD
                section Sección 1
                Tarea 1 :a1, 2023-01-01, 7d
                Tarea 2 :after a1, 3d
                section Sección 2
                Tarea 3 :2023-01-10, 2d
                Tarea 4 : 2d

    .. tab-item:: Estructura

        .. code-block::

            .. mermaid::
                :alt: Ejemplo de diagrama de Gantt
                :align: center
                :zoom:

                gantt

                    title Diagrama de Gantt
                    dateFormat YYYY-MM-DD
                    section Sección 1
                    Tarea 1 :a1, 2023-01-01, 7d
                    Tarea 2 :after a1, 3d
                    section Sección 2
                    Tarea 3 :2023-01-10, 2d
                    Tarea 4 : 2d

Diagrama de Clases
------------------

Los diagramas de clase utilizan ``classDiagram`` para inciar.

Este es un diagrama de clases que muestra la herencia y las propiedades de las clases "Perro" y "Gato" en relación con la clase base "Animal".

.. tab-set::

    .. tab-item:: Ejemplo 4

        .. mermaid::
            :alt: Ejemplo de diagrama de Clases
            :align: center
            :zoom:

            classDiagram

                class Animal {
                    - nombre: string
                    + obtenerNombre(): string
                }
                class Perro {
                    + ladrar(): void
                }
                class Gato {
                    + maullar(): void
                }
                Animal <|-- Perro
                Animal <|-- Gato

    .. tab-item:: Estructura

        .. code-block::

            .. mermaid::
                :alt: Ejemplo de diagrama de Clases
                :align: center
                :zoom:
                
                classDiagram

                    class Animal {
                        - nombre: string
                        + obtenerNombre(): string
                    }
                    class Perro {
                        + ladrar(): void
                    }
                    class Gato {
                        + maullar(): void
                    }
                    Animal <|-- Perro
                    Animal <|-- Gato

Diagrama de Secuencia
---------------------

Los diagramas de secuencia empiezan por ``sequenceDiagram``.
Se utiliza para crear representar interacciones entre objetos o actores a lo largo del tiempo. 

.. tab-set::

    .. tab-item:: Ejemplo 5

        .. mermaid::
            :alt: Ejemplo de diagrama de Secuencia
            :align: center
            :zoom:

            sequenceDiagram
                participant dotcom
                participant iframe
                participant viewscreen
                dotcom->>iframe: Carga html con URL de iframe
                iframe->>viewscreen: Plantilla de solicitud
                viewscreen->>iframe: html & javascript
                iframe->>dotcom: iframe listo
                dotcom->>iframe: Establecer datos mermaid en iframe
                iframe->>iframe: Render mermaid

    .. tab-item:: Estructura

        .. code-block::

            .. mermaid::
                :alt: Ejemplo de diagrama de Secuencia
                :align: center
                :zoom:

                sequenceDiagram
                    participant dotcom
                    participant iframe
                    participant viewscreen
                    dotcom->>iframe: Carga html con URL de iframe
                    iframe->>viewscreen: Plantilla de solicitud
                    viewscreen->>iframe: html & javascript
                    iframe->>dotcom: iframe listo
                    dotcom->>iframe: Establecer datos mermaid en iframe
                    iframe->>iframe: Render mermaid

Si necesita conocer más acerca de mermaid puede consultar la documentación `Sphinxcontrib-mermaid  <https://github.com/mgaitan/sphinxcontrib-mermaid/>`_ :octicon:`report;1em;sd-text-info`.  

Sphinx.ext.graphviz
===================

Esta extensión le permite representar información estructural como diagramas de redes y gráficos abstractos. Graphviz tiene muchas funciones útiles para diagramas concretos, como opciones de colores, fuentes, diseños de nodos tabulares, estilos de línea, hipervínculos y formas personalizadas.

A diferencia de :ref:`etiqueta_mermaind`, Graphviz utiliza un lenguaje de descripción llamado ``DOT``, que es un lenguaje declarativo para describir gráficos y diagramas.  Es más estructurado y complejo que el formato de texto plano de Mermaid. Una de las ventajas de utilizar graphviz, es la flexibilidad de controlar el formato de salida utilizando ``graphviz_output_format = 'png'`` en el :ref:`conf`.

Para hacer uso de graphviz, debe utilizar la directiva ``.. graphviz::``. De la misma manera, tenga en cuenta las siguientes directivas.

+--------------+---------------------------------------------------------------------------------------------+
| Propiedad    | Descripción                                                                                 |
+==============+=============================================================================================+
| alt          | Texto alternativo.                                                                          |
+--------------+---------------------------------------------------------------------------------------------+
| align        | Alineación del gráfico (``left``, ``center``, ``right``).                                   |  
+--------------+---------------------------------------------------------------------------------------------+
| caption      | Título del gráfico.                                                                         |
+--------------+---------------------------------------------------------------------------------------------+
| name         | Etiqueta.                                                                                   |
+--------------+---------------------------------------------------------------------------------------------+
| class        | Nombres de clase (una lista de clases separados por espacios)                               |
|              | `ver más <https://graphviz.org/docs/attrs/class/>`_ :octicon:`report;1em;sd-text-info`.     |
+--------------+---------------------------------------------------------------------------------------------+
| layout       | Tipo de gráfico. Especifica el nombre del                                                   |
|              | `motor de diseño  <https://graphviz.org/docs/layouts/>`_ :octicon:`report;1em;sd-text-info`.|
+--------------+---------------------------------------------------------------------------------------------+

Graphviz utiliza atributos para darle un aspecto visual a sus nodos, conexiones, fondos, etc., de manera similar a aplicar estilos CSS en línea. Puede consultar la lista completa de atributos `aquí  <https://graphviz.org/docs/graph/>`_ :octicon:`report;1em;sd-text-info`.

A continuación, se presentan algunos ejemplos de Graphviz.

Clústeres
---------

Este pequeño ejemplo ilustra la característica de usar el punto para dibujar nodos y bordes en grupos o regiones de diseño rectangulares separadas. Los grupos están codificados como subgrafos cuyos nombres tienen el prefijo `clúster  <https://graphviz.org/Gallery/directed/cluster.html/>`_ :octicon:`report;1em;sd-text-info`.

.. tab-set::

    .. tab-item:: Ejemplo 1

        .. graphviz::
            :align: center

            digraph G {
                fontname="Helvetica,Arial,sans-serif"
                node [fontname="Helvetica,Arial,sans-serif"]
                edge [fontname="Helvetica,Arial,sans-serif"]

                subgraph cluster_0 {
                    style=filled;
                    color=lightgrey;
                    node [style=filled,color=white];
                    a0 -> a1 -> a2 -> a3;
                    label = "process #1";
                }

                subgraph cluster_1 {
                    node [style=filled];
                    b0 -> b1 -> b2 -> b3;
                    label = "process #2";
                    color=blue
                }
                start -> a0;
                start -> b0;
                a1 -> b3;
                b2 -> a3;
                a3 -> a0;
                a3 -> end;
                b3 -> end;

                start [shape=Mdiamond];
                end [shape=Msquare];
            }

    .. tab-item:: Estructura

        .. code-block::

            .. graphviz::
                :align: center

                digraph G {
                    fontname="Helvetica,Arial,sans-serif"
                    node [fontname="Helvetica,Arial,sans-serif"]
                    edge [fontname="Helvetica,Arial,sans-serif"]

                    subgraph cluster_0 {
                        style=filled;
                        color=lightgrey;
                        node [style=filled,color=white];
                        a0 -> a1 -> a2 -> a3;
                        label = "process #1";
                    }

                    subgraph cluster_1 {
                        node [style=filled];
                        b0 -> b1 -> b2 -> b3;
                        label = "process #2";
                        color=blue
                    }
                    start -> a0;
                    start -> b0;
                    a1 -> b3;
                    b2 -> a3;
                    a3 -> a0;
                    a3 -> end;
                    b3 -> end;

                    start [shape=Mdiamond];
                    end [shape=Msquare];
                }

Colores parcialmente transparentes
----------------------------------

Este ejemplo ilustra el uso de `colores <https://graphviz.org/Gallery/neato/transparency.html/>`_ :octicon:`report;1em;sd-text-info` parcialmente transparentes para nodo ``fillcolor`` y  para graficar  ``bgcolor``. 

.. tab-set::

    .. tab-item:: Ejemplo 2

        .. graphviz::
            :align: center

            graph Transparency {
                layout=neato
                start=11 // empiric value to set orientation
                bgcolor="#0000ff11"
                node [shape=circle width=2.22 label="" style=filled]
                5 [color="#0000ff80"]
                6 [color="#ee00ee80"]
                1 [color="#ff000080"]
                2 [color="#eeee0080"]
                3 [color="#00ff0080"]
                4 [color="#00eeee80"]
                1 -- 2 -- 3 -- 4 -- 5 -- 6 -- 1
            }

    .. tab-item:: Estructura

        .. code-block::

            .. graphviz::
                :align: center

                graph Transparency {
                    layout=neato
                    start=11 // empiric value to set orientation
                    bgcolor="#0000ff11"
                    node [shape=circle width=2.22 label="" style=filled]
                    5 [color="#0000ff80"]
                    6 [color="#ee00ee80"]
                    1 [color="#ff000080"]
                    2 [color="#eeee0080"]
                    3 [color="#00ff0080"]
                    4 [color="#00eeee80"]
                    1 -- 2 -- 3 -- 4 -- 5 -- 6 -- 1
                }

Gradient aplicados a una estructura de datos
--------------------------------------------

Demuestra una aplicación de gradientes para registrar `nodos <https://graphviz.org/Gallery/gradient/datastruct.html/>`_ :octicon:`report;1em;sd-text-info`. 

.. tab-set::

    .. tab-item:: Ejemplo 3

        .. graphviz::
            :align: center

            digraph g {
                fontname="Helvetica,Arial,sans-serif"
                node [fontname="Helvetica,Arial,sans-serif"]
                edge [fontname="Helvetica,Arial,sans-serif"]
                graph [
                rankdir = "LR"
                bgcolor = "white:lightblue"
                style="filled"
                gradientangle = 270];
                node [
                fontsize = "16"
                shape = "ellipse"
                style="filled"
                gradientangle=90
                ];
                edge [
                ];
                "node0" [
                label = "<f0> 0x10ba8| <f1>"
                shape = "record"
                gradientangle="90"
                fillcolor = "yellow:blue"
                ];
                "node1" [
                label = "<f0> 0xf7fc4380| <f1> | <f2> |-1"
                shape = "record"
                fillcolor = "blue:red"
                gradientangle = 0
                ];
                "node2" [
                label = "<f0> 0xf7fc44b8| | |2"
                shape = "record"
                fillcolor = "brown:yellow"
                gradientangle = 90
                ];
                "node3" [
                label = "<f0> 3.43322790286038071e-06|44.79998779296875|0 | <f1>"
                shape = "record"
                fillcolor = "green:red"
                gradientangle = 90
                ];
                "node4" [
                label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
                shape = "record"
                fillcolor = "red:green"
                gradientangle = 0
                ];
                "node5" [
                label = "<f0> (nil)| | |-1"
                shape = "record"
                fillcolor = "red:red"
                gradientangle = 90
                ];
                "node6" [
                label = "<f0> 0xf7fc4380| <f1> | <f2> |1"
                shape = "record"
                fillcolor = "orange:green"
                ];
                "node7" [
                label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
                shape = "record"
                fillcolor = "cyan:green"
                ];
                "node8" [
                label = "<f0> (nil)| | |-1"
                shape = "record"
                fillcolor = "cyan:cyan"
                ];
                "node9" [
                label = "<f0> (nil)| | |-1"
                shape = "record"
                fillcolor = "orange:orange"
                gradientangle = 90
                ];
                "node10" [
                label = "<f0> (nil)| <f1> | <f2> |-1"
                shape = "record"
                fillcolor = "magenta:green"
                ];
                "node11" [
                label = "<f0> (nil)| <f1> | <f2> |-1"
                shape = "record"
                fillcolor = "red:green"
                ];
                "node12" [
                label = "<f0> 0xf7fc43e0| | |1"
                shape = "record"
                fillcolor = "magenta:magenta"
                ];
                "node0":f0 -> "node1":f0 [
                id = 0
                ];
                "node0":f1 -> "node2":f0 [
                id = 1
                ];
                "node1":f0 -> "node3":f0 [
                id = 2
                ];
                "node1":f1 -> "node4":f0 [
                id = 3
                ];
                "node1":f2 -> "node5":f0 [
                id = 4
                ];
                "node4":f0 -> "node3":f1 [
                id = 5
                ];
                "node4":f1 -> "node6":f0 [
                id = 6
                ];
                "node4":f2 -> "node10":f0 [
                id = 7
                ];
                "node6":f0 -> "node3":f1 [
                id = 8
                ];
                "node6":f1 -> "node7":f0 [
                id = 9
                ];
                "node6":f2 -> "node9":f0 [
                id = 10
                ];
                "node7":f0 -> "node3":f1 [
                id = 11
                ];
                "node7":f1 -> "node1":f0 [
                id = 12
                ];
                "node7":f2 -> "node8":f0 [
                id = 13
                ];
                "node10":f1 -> "node11":f0 [
                id = 14
                ];
                "node10":f2 -> "node12":f0 [
                id = 15
                ];
                "node11":f2 -> "node1":f0 [
                id = 16
                ];
            }

    .. tab-item:: Estructura

        .. code-block::

            .. graphviz::
                :align: center

                digraph g {
                    fontname="Helvetica,Arial,sans-serif"
                    node [fontname="Helvetica,Arial,sans-serif"]
                    edge [fontname="Helvetica,Arial,sans-serif"]
                    graph [
                    rankdir = "LR"
                    bgcolor = "white:lightblue"
                    style="filled"
                    gradientangle = 270];
                    node [
                    fontsize = "16"
                    shape = "ellipse"
                    style="filled"
                    gradientangle=90
                    ];
                    edge [
                    ];
                    "node0" [
                    label = "<f0> 0x10ba8| <f1>"
                    shape = "record"
                    gradientangle="90"
                    fillcolor = "yellow:blue"
                    ];
                    "node1" [
                    label = "<f0> 0xf7fc4380| <f1> | <f2> |-1"
                    shape = "record"
                    fillcolor = "blue:red"
                    gradientangle = 0
                    ];
                    "node2" [
                    label = "<f0> 0xf7fc44b8| | |2"
                    shape = "record"
                    fillcolor = "brown:yellow"
                    gradientangle = 90
                    ];
                    "node3" [
                    label = "<f0> 3.43322790286038071e-06|44.79998779296875|0 | <f1>"
                    shape = "record"
                    fillcolor = "green:red"
                    gradientangle = 90
                    ];
                    "node4" [
                    label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
                    shape = "record"
                    fillcolor = "red:green"
                    gradientangle = 0
                    ];
                    "node5" [
                    label = "<f0> (nil)| | |-1"
                    shape = "record"
                    fillcolor = "red:red"
                    gradientangle = 90
                    ];
                    "node6" [
                    label = "<f0> 0xf7fc4380| <f1> | <f2> |1"
                    shape = "record"
                    fillcolor = "orange:green"
                    ];
                    "node7" [
                    label = "<f0> 0xf7fc4380| <f1> | <f2> |2"
                    shape = "record"
                    fillcolor = "cyan:green"
                    ];
                    "node8" [
                    label = "<f0> (nil)| | |-1"
                    shape = "record"
                    fillcolor = "cyan:cyan"
                    ];
                    "node9" [
                    label = "<f0> (nil)| | |-1"
                    shape = "record"
                    fillcolor = "orange:orange"
                    gradientangle = 90
                    ];
                    "node10" [
                    label = "<f0> (nil)| <f1> | <f2> |-1"
                    shape = "record"
                    fillcolor = "magenta:green"
                    ];
                    "node11" [
                    label = "<f0> (nil)| <f1> | <f2> |-1"
                    shape = "record"
                    fillcolor = "red:green"
                    ];
                    "node12" [
                    label = "<f0> 0xf7fc43e0| | |1"
                    shape = "record"
                    fillcolor = "magenta:magenta"
                    ];
                    "node0":f0 -> "node1":f0 [
                    id = 0
                    ];
                    "node0":f1 -> "node2":f0 [
                    id = 1
                    ];
                    "node1":f0 -> "node3":f0 [
                    id = 2
                    ];
                    "node1":f1 -> "node4":f0 [
                    id = 3
                    ];
                    "node1":f2 -> "node5":f0 [
                    id = 4
                    ];
                    "node4":f0 -> "node3":f1 [
                    id = 5
                    ];
                    "node4":f1 -> "node6":f0 [
                    id = 6
                    ];
                    "node4":f2 -> "node10":f0 [
                    id = 7
                    ];
                    "node6":f0 -> "node3":f1 [
                    id = 8
                    ];
                    "node6":f1 -> "node7":f0 [
                    id = 9
                    ];
                    "node6":f2 -> "node9":f0 [
                    id = 10
                    ];
                    "node7":f0 -> "node3":f1 [
                    id = 11
                    ];
                    "node7":f1 -> "node1":f0 [
                    id = 12
                    ];
                    "node7":f2 -> "node8":f0 [
                    id = 13
                    ];
                    "node10":f1 -> "node11":f0 [
                    id = 14
                    ];
                    "node10":f2 -> "node12":f0 [
                    id = 15
                    ];
                    "node11":f2 -> "node1":f0 [
                    id = 16
                    ];
                }

Hay mucho más contenido que puede explorar y probar. Consulte este `enlace <https://graphviz.org//>`_ :octicon:`report;1em;sd-text-info` para obtener más información.

Sphinx_design
=============

Es una extensión para diseñar componentes web responsivos. Surgió como una mejora de sphinx-panels, con la intención de hacerlo más flexible, más fácil de usar y minimizar los conflictos de CSS con los temas de sphinx. 

Con Sphinx Design, puede trabajar con grids, tarjetas, pestañas, listas desplegables, insignias, botones e iconos. Ofrece CSS libre de conflictos (utiliza prefijos en las clases para evitar conflictos con otros frameworks), funciona sin JavaScript, es bastante flexible y configurable (todos los colores se pueden configurar utilizando variables CSS).

Grids
-----

Los Grids (cuadrillas) se basan en un sistema de 12 columnas, que se pueden adaptar al tamaño de la pantalla de visualización. Para utilizar grids utilice la directiva ``.. grid::``.

Grids utiliza tres opciones de `directivas <https://sphinx-design.readthedocs.io/en/furo-theme/grids.html#grid-options/>`_ :octicon:`report;1em;sd-text-info`. A continuación, se presenta un ejemplo de grids anidadas para crear diseños complejos y adaptables.

.. tab-set::

    .. tab-item:: Ejemplo

        .. grid:: 1 1 2 2
            :gutter: 1

            .. grid-item::

                .. grid:: 1 1 1 1
                    :gutter: 1

                    .. grid-item-card:: Item 1.1

                        Multi-línea

                        Contenido

                    .. grid-item-card:: Item 1.2

                        Contenido

            .. grid-item::

                .. grid:: 1 1 1 1
                    :gutter: 1

                    .. grid-item-card:: Item 2.1

                        Contenido

                    .. grid-item-card:: Item 2.2

                        Contenido

                    .. grid-item-card:: Item 2.3

                        Contenido

    .. tab-item:: Estructura

        .. code-block::

            .. grid:: 1 1 2 2
                :gutter: 1

                .. grid-item::

                    .. grid:: 1 1 1 1
                        :gutter: 1

                        .. grid-item-card:: Item 1.1

                            Multi-línea

                            Contenido

                        .. grid-item-card:: Item 1.2

                            Contenido

                .. grid-item::

                    .. grid:: 1 1 1 1
                        :gutter: 1

                        .. grid-item-card:: Item 2.1

                            Contenido

                        .. grid-item-card:: Item 2.2

                            Contenido

                        .. grid-item-card:: Item 2.3

                            Contenido

Si necesita más información a cerca de grids puede revisar el siguiente `enlace <https://sphinx-design.readthedocs.io/en/furo-theme/grids.html/>`_ :octicon:`report;1em;sd-text-info`. 

Cards
-----

Las cards (tarjetas) son contenedores de información de un solo tema. Son flexibles y extensibles; se puede formatear con componentes que incluyen encabezados y pies de página, hipervínculos, títulos e imágenes. 

Una Card básica utiliza la directiva ``.. card::``. De la misma manera, Cards proporciona opciones para personalizar sus tarjetas. Puede consultarlas `aquí <https://sphinx-design.readthedocs.io/en/furo-theme/cards.html#card-options/>`_ :octicon:`report;1em;sd-text-info`. 

El siguiente ejemplo es una tarjeta con un encabezado, título, contenido y pie de página.

Todo el contenido antes del simbolo ``^^^`` se considera encabezado, y todo el contenido después de ``+++`` se considera pie de página.

.. tab-set::

    .. tab-item:: Ejemplo

        .. card:: Título de la tarjeta

            Encabezado
            ^^^
            Contenido
            +++
            Pie de página

    .. tab-item:: Estructura

        .. code-block::

            .. card:: Título de la tarjeta

                Encabezado
                ^^^
                Contenido
                +++
                Pie de página

Dropdowns
---------

Los Dropdowns (menús desplegables) se utilizan para alternar contenido (generalmente no esencial), y mostrarlo solo cuando un usuario haga clic en el panel de encabezado. 

Un dropdown utiliza la directiva ``.. dropdown::``. Las opciones para personalizar sus listas desplegables puede encontrarlas en `dropdown-options <https://sphinx-design.readthedocs.io/en/furo-theme/dropdowns.html#dropdown-options/>`_ :octicon:`report;1em;sd-text-info`. 

El menú desplegable puede tener un título, como argumento directivo, y ``open`` (para inicializar el menú desplegable en el estado abierto). 

.. tab-set::

    .. tab-item:: Ejemplo

        .. dropdown::

            Contenido

        .. dropdown:: Título

            Contenido

        .. dropdown:: Dropdown abierto por default
            :open:

            Contenido

    .. tab-item:: Estructura

        .. code-block::

            .. dropdown::

                Contenido

            .. dropdown:: Título

                Contenido

            .. dropdown:: Dropdown abierto por default
                :open:

                Contenido

Tabs
----

Las Tabs (pestañas) organizan y permiten la navegación entre grupos de contenidos que están relacionados y en el mismo nivel de jerarquía. 

Para utilizar un tab necesita la directiva ``.. tab-set::``. Las opciones para personalizar pestañas las puede encontrar en `tab-set-options <https://sphinx-design.readthedocs.io/en/furo-theme/tabs.html#tab-set-options/>`_ :octicon:`report;1em;sd-text-info`. 

El siguiente ejemplo básico le resultará familiar, ya que es el que se utiliza para explicar otros aspectos.

.. tab-set::

    .. tab-item:: Label1

        Contenido 1

    .. tab-item:: Label2

        Contenido 2

La estructura es la siguiente: ::

    .. tab-set::

        .. tab-item:: Label1

            Contenido 1

        .. tab-item:: Label2

            Contenido 2

.. _badges:

Badges
------

Badges (insignias) se utilizan como componentes de etiquetado. Las insignias están disponibles en cada color semántico, con variantes en relleno y contorno. Puede utilizar las siguientes:

.. tab-set::

    .. tab-item:: Ejemplo

        :bdg:`plain badge`

        :bdg-primary:`primary`, :bdg-primary-line:`primary-line`

        :bdg-secondary:`secondary`, :bdg-secondary-line:`secondary-line`

        :bdg-success:`success`, :bdg-success-line:`success-line`

        :bdg-info:`info`, :bdg-info-line:`info-line`

        :bdg-warning:`warning`, :bdg-warning-line:`warning-line`

        :bdg-danger:`danger`, :bdg-danger-line:`danger-line`

        :bdg-light:`light`, :bdg-light-line:`light-line`

        :bdg-dark:`dark`, :bdg-dark-line:`dark-line`

    .. tab-item:: Estructura

        .. code-block::
            
            :bdg:`plain badge`

            :bdg-primary:`primary`, :bdg-primary-line:`primary-line`

            :bdg-secondary:`secondary`, :bdg-secondary-line:`secondary-line`

            :bdg-success:`success`, :bdg-success-line:`success-line`

            :bdg-info:`info`, :bdg-info-line:`info-line`

            :bdg-warning:`warning`, :bdg-warning-line:`warning-line`

            :bdg-danger:`danger`, :bdg-danger-line:`danger-line`

            :bdg-light:`light`, :bdg-light-line:`light-line`

            :bdg-dark:`dark`, :bdg-dark-line:`dark-line`

Existen badges especiales para referencias y enlaces, como las que se muestran a continuación:

.. tab-set::

    .. tab-item:: Ejemplo

        :bdg-link-primary:`https://example.com`

        :bdg-link-primary-line:`explicit title <https://example.com>`

    .. tab-item:: Estructura

        .. code-block::

            :bdg-link-primary:`https://example.com`

            :bdg-link-primary-line:`explicit title <https://example.com>`

Puede consultar `insignias <https://getbootstrap.com/docs/5.0/components/badge/>`_ :octicon:`report;1em;sd-text-info` para obtener más información.  

Buttons
-------

Los botones permiten a los usuarios navegar a sitios externos ( button-link) / interno ( button-ref), además de que permite mayor personalización. 

Los buttons son muy diferentes a los badges con referencia. Inician con la directiva ``.. button-link::``. Revise las `directivas <https://sphinx-design.readthedocs.io/en/furo-theme/badges_buttons.html#button-link-and-button-ref-optionsque/>`_ :octicon:`report;1em;sd-text-info` que ofrece.

Estos son algunos ejemplos:

.. tab-set::

    .. tab-item:: Ejemplo

        .. button-link:: https://example.com

        .. button-link:: https://example.com

            Button text

        .. button-link:: https://example.com
            :color: primary
            :shadow:

        .. button-link:: https://example.com
            :color: primary
            :outline:

        .. button-link:: https://example.com
            :color: secondary
            :expand:

    .. tab-item:: Estructura

        .. code-block::

            .. button-link:: https://example.com

            .. button-link:: https://example.com

                Button text

            .. button-link:: https://example.com
                :color: primary
                :shadow:

            .. button-link:: https://example.com
                :color: primary
                :outline:

            .. button-link:: https://example.com
                :color: secondary
                :expand:

Consulte `Bootstrap <https://getbootstrap.com/docs/5.0/components/buttons/>`_ :octicon:`report;1em;sd-text-info` para más detlles.

Icons
-----

Los iconos se utilizan para facilitar la navegación y la identificación de elementos, se agregan como SVG directamente en la página. Para utilizar un icono inicie con ``:octicon:``.

Por defecto el icono será de altura 1em (la altura de la fuente). Se puede establecer una altura específica después de un punto y coma (``;``) con unidades ``px``, ``em`` o ``rem``. 

Los colores son ajustables y son los que utiliza :ref:`badges`.

A continuación, se muestran algunos ejemplos:

.. tab-set::

    .. tab-item:: Ejemplo

        Un icono se ve así :octicon:`bell-fill;1em;sd-text-warning`, puede incluir más texto después.

        Magna sunt magna laborum mollit occaecat aliqua sunt velit eu nisi est :octicon:`alert-fill;1em;sd-text-danger`.

        Eiusmod elit pariatur occaecat laborum id nostrud :octicon:`check-circle-fill;1em;sd-text-success`.

    .. tab-item:: Estructura

        .. code-block::

            Un icono se ve así :octicon:`bell-fill;1em;sd-text-warning`, puede incluir más texto después.

            Magna sunt magna laborum mollit occaecat aliqua sunt velit eu nisi est :octicon:`alert-fill;1em;sd-text-danger`.

            Eiusmod elit pariatur occaecat laborum id nostrud :octicon:`check-circle-fill;1em;sd-text-success`.

.. NO ABRIR dropdown (Contiene lista de iconos)

.. dropdown:: Ver iconos admitidos

    .. tab-set::

        .. tab-item:: Ejemplo

            alert: :octicon:`alert` 

            alert-fill: :octicon:`alert-fill` 

            archive: :octicon:`archive` 

            arrow-both: :octicon:`arrow-both` 

            arrow-down: :octicon:`arrow-down` 

            arrow-down-left: :octicon:`arrow-down-left` 

            arrow-down-right: :octicon:`arrow-down-right` 

            arrow-left: :octicon:`arrow-left` 

            arrow-right: :octicon:`arrow-right` 

            arrow-switch: :octicon:`arrow-switch` 

            arrow-up: :octicon:`arrow-up` 

            arrow-up-left: :octicon:`arrow-up-left` 

            arrow-up-right: :octicon:`arrow-up-right` 

            beaker: :octicon:`beaker` 

            bell: :octicon:`bell` 

            bell-fill: :octicon:`bell-fill` 

            bell-slash: :octicon:`bell-slash` 

            blocked: :octicon:`blocked` 

            bold: :octicon:`bold` 

            book: :octicon:`book` 

            bookmark: :octicon:`bookmark` 

            bookmark-fill: :octicon:`bookmark-fill` 

            bookmark-slash: :octicon:`bookmark-slash` 

            bookmark-slash-fill: :octicon:`bookmark-slash-fill` 

            briefcase: :octicon:`briefcase` 

            broadcast: :octicon:`broadcast` 

            browser: :octicon:`browser` 

            bug: :octicon:`bug` 

            calendar: :octicon:`calendar` 

            check: :octicon:`check` 

            check-circle: :octicon:`check-circle` 

            check-circle-fill: :octicon:`check-circle-fill` 

            checklist: :octicon:`checklist` 

            chevron-down: :octicon:`chevron-down` 

            chevron-left: :octicon:`chevron-left` 

            chevron-right: :octicon:`chevron-right` 

            chevron-up: :octicon:`chevron-up` 

            circle: :octicon:`circle` 

            circle-slash: :octicon:`circle-slash` 

            clock: :octicon:`clock` 

            code: :octicon:`code` 

            code-review: :octicon:`code-review` 

            code-square: :octicon:`code-square` 

            codescan: :octicon:`codescan` 

            codescan-checkmark: :octicon:`codescan-checkmark` 

            codespaces: :octicon:`codespaces` 

            columns: :octicon:`columns` 

            comment: :octicon:`comment` 

            comment-discussion: :octicon:`comment-discussion` 

            commit: :octicon:`commit` 

            container: :octicon:`container` 

            copy: :octicon:`copy` 

            cpu: :octicon:`cpu` 

            credit-card: :octicon:`credit-card` 

            cross-reference: :octicon:`cross-reference` 

            dash: :octicon:`dash` 

            database: :octicon:`database` 

            dependabot: :octicon:`dependabot` 

            desktop-download: :octicon:`desktop-download` 

            device-camera: :octicon:`device-camera` 

            device-camera-video: :octicon:`device-camera-video` 

            device-desktop: :octicon:`device-desktop` 

            device-mobile: :octicon:`device-mobile` 

            diamond: :octicon:`diamond` 

            diff: :octicon:`diff` 

            diff-added: :octicon:`diff-added` 

            diff-ignored: :octicon:`diff-ignored` 

            diff-modified: :octicon:`diff-modified` 

            diff-removed: :octicon:`diff-removed` 

            diff-renamed: :octicon:`diff-renamed` 

            dot: :octicon:`dot` 

            dot-fill: :octicon:`dot-fill` 

            download: :octicon:`download` 

            duplicate: :octicon:`duplicate` 

            ellipsis: :octicon:`ellipsis` 

            eye: :octicon:`eye` 

            eye-closed: :octicon:`eye-closed` 

            file: :octicon:`file` 

            file-badge: :octicon:`file-badge` 

            file-binary: :octicon:`file-binary` 

            file-code: :octicon:`file-code` 

            file-diff: :octicon:`file-diff` 

            file-directory: :octicon:`file-directory` 

            file-directory-fill: :octicon:`file-directory-fill` 

            file-media: :octicon:`file-media` 

            file-submodule: :octicon:`file-submodule` 

            file-symlink-file: :octicon:`file-symlink-file` 

            file-zip: :octicon:`file-zip` 

            filter: :octicon:`filter` 

            flame: :octicon:`flame` 

            fold: :octicon:`fold` 

            fold-down: :octicon:`fold-down` 

            fold-up: :octicon:`fold-up` 

            gear: :octicon:`gear` 

            gift: :octicon:`gift` 

            git-branch: :octicon:`git-branch` 

            git-commit: :octicon:`git-commit` 

            git-compare: :octicon:`git-compare` 

            git-merge: :octicon:`git-merge` 

            git-pull-request: :octicon:`git-pull-request` 

            git-pull-request-closed: :octicon:`git-pull-request-closed` 

            git-pull-request-draft: :octicon:`git-pull-request-draft` 

            globe: :octicon:`globe` 

            grabber: :octicon:`grabber` 

            graph: :octicon:`graph` 

            hash: :octicon:`hash` 

            heading: :octicon:`heading` 

            heart: :octicon:`heart` 

            heart-fill: :octicon:`heart-fill` 

            history: :octicon:`history` 

            home: :octicon:`home` 

            home-fill: :octicon:`home-fill` 

            horizontal-rule: :octicon:`horizontal-rule` 

            hourglass: :octicon:`hourglass` 

            hubot: :octicon:`hubot` 

            image: :octicon:`image` 

            inbox: :octicon:`inbox` 

            infinity: :octicon:`infinity` 

            info: :octicon:`info` 

            issue-closed: :octicon:`issue-closed` 

            issue-draft: :octicon:`issue-draft` 

            issue-opened: :octicon:`issue-opened` 

            issue-reopened: :octicon:`issue-reopened` 

            italic: :octicon:`italic` 

            iterations: :octicon:`iterations` 

            kebab-horizontal: :octicon:`kebab-horizontal` 

            key: :octicon:`key` 

            key-asterisk: :octicon:`key-asterisk` 

            law: :octicon:`law` 

            light-bulb: :octicon:`light-bulb` 

            link: :octicon:`link` 

            link-external: :octicon:`link-external` 

            list-ordered: :octicon:`list-ordered` 

            list-unordered: :octicon:`list-unordered` 

            location: :octicon:`location` 

            lock: :octicon:`lock` 

            logo-gist: :octicon:`logo-gist` 

            logo-github: :octicon:`logo-github` 

            mail: :octicon:`mail` 

            mark-github: :octicon:`mark-github` 

            markdown: :octicon:`markdown` 

            megaphone: :octicon:`megaphone` 

            mention: :octicon:`mention` 

            meter: :octicon:`meter` 

            milestone: :octicon:`milestone` 

            mirror: :octicon:`mirror` 

            moon: :octicon:`moon` 

            mortar-board: :octicon:`mortar-board` 

            multi-select: :octicon:`multi-select` 

            mute: :octicon:`mute` 

            no-entry: :octicon:`no-entry` 

            no-entry-fill: :octicon:`no-entry-fill` 

            north-star: :octicon:`north-star` 

            note: :octicon:`note` 

            number: :octicon:`number` 

            organization: :octicon:`organization` 

            package: :octicon:`package` 

            package-dependencies: :octicon:`package-dependencies` 

            package-dependents: :octicon:`package-dependents` 

            paintbrush: :octicon:`paintbrush` 

            paper-airplane: :octicon:`paper-airplane` 

            paste: :octicon:`paste` 

            pencil: :octicon:`pencil` 

            people: :octicon:`people` 

            person: :octicon:`person` 

            person-add: :octicon:`person-add` 

            person-fill: :octicon:`person-fill` 

            pin: :octicon:`pin` 

            play: :octicon:`play` 

            plug: :octicon:`plug` 

            plus: :octicon:`plus` 

            plus-circle: :octicon:`plus-circle` 

            project: :octicon:`project` 

            pulse: :octicon:`pulse` 

            question: :octicon:`question` 

            quote: :octicon:`quote` 

            reply: :octicon:`reply` 

            repo: :octicon:`repo` 

            repo-clone: :octicon:`repo-clone` 

            repo-forked: :octicon:`repo-forked` 

            repo-pull: :octicon:`repo-pull` 

            repo-push: :octicon:`repo-push` 

            repo-template: :octicon:`repo-template` 

            report: :octicon:`report` 

            rocket: :octicon:`rocket` 

            rows: :octicon:`rows` 

            rss: :octicon:`rss` 

            ruby: :octicon:`ruby` 

            screen-full: :octicon:`screen-full` 

            screen-normal: :octicon:`screen-normal` 

            search: :octicon:`search` 

            server: :octicon:`server` 

            share: :octicon:`share` 

            share-android: :octicon:`share-android` 

            shield: :octicon:`shield` 

            shield-check: :octicon:`shield-check` 

            shield-lock: :octicon:`shield-lock` 

            shield-x: :octicon:`shield-x` 

            sidebar-collapse: :octicon:`sidebar-collapse` 

            sidebar-expand: :octicon:`sidebar-expand` 

            sign-in: :octicon:`sign-in` 

            sign-out: :octicon:`sign-out` 

            single-select: :octicon:`single-select` 

            skip: :octicon:`skip` 

            smiley: :octicon:`smiley` 

            sort-asc: :octicon:`sort-asc` 

            sort-desc: :octicon:`sort-desc` 

            square: :octicon:`square` 

            square-fill: :octicon:`square-fill` 

            squirrel: :octicon:`squirrel` 

            stack: :octicon:`stack` 

            star: :octicon:`star` 

            star-fill: :octicon:`star-fill` 

            stop: :octicon:`stop` 

            stopwatch: :octicon:`stopwatch` 

            strikethrough: :octicon:`strikethrough` 

            sun: :octicon:`sun` 

            sync: :octicon:`sync` 

            tab: :octicon:`tab` 

            table: :octicon:`table` 

            tag: :octicon:`tag` 

            tasklist: :octicon:`tasklist` 

            telescope: :octicon:`telescope` 

            telescope-fill: :octicon:`telescope-fill` 

            terminal: :octicon:`terminal` 

            three-bars: :octicon:`three-bars` 

            thumbsdown: :octicon:`thumbsdown` 

            thumbsup: :octicon:`thumbsup` 

            tools: :octicon:`tools` 

            trash: :octicon:`trash` 

            triangle-down: :octicon:`triangle-down` 

            triangle-left: :octicon:`triangle-left` 

            triangle-right: :octicon:`triangle-right` 

            triangle-up: :octicon:`triangle-up` 

            typography: :octicon:`typography` 

            unfold: :octicon:`unfold` 

            unlock: :octicon:`unlock` 

            unmute: :octicon:`unmute` 

            unverified: :octicon:`unverified` 

            upload: :octicon:`upload` 

            verified: :octicon:`verified` 

            versions: :octicon:`versions` 

            video: :octicon:`video` 

            workflow: :octicon:`workflow` 

            x: :octicon:`x` 

            x-circle: :octicon:`x-circle` 

            x-circle-fill: :octicon:`x-circle-fill` 

            zap: :octicon:`zap`



        .. tab-item:: Estructura
    
            .. code-block::

                alert: :octicon:`alert`
                alert-fill: :octicon:`alert-fill`
                archive: :octicon:`archive`
                arrow-both: :octicon:`arrow-both`
                arrow-down: :octicon:`arrow-down`
                arrow-down-left: :octicon:`arrow-down-left`
                arrow-down-right: :octicon:`arrow-down-right`
                arrow-left: :octicon:`arrow-left`
                arrow-right: :octicon:`arrow-right`
                arrow-switch: :octicon:`arrow-switch`
                arrow-up: :octicon:`arrow-up`
                arrow-up-left: :octicon:`arrow-up-left`
                arrow-up-right: :octicon:`arrow-up-right`
                beaker: :octicon:`beaker`
                bell: :octicon:`bell`
                bell-fill: :octicon:`bell-fill`
                bell-slash: :octicon:`bell-slash`
                blocked: :octicon:`blocked`
                bold: :octicon:`bold`
                book: :octicon:`book`
                bookmark: :octicon:`bookmark`
                bookmark-fill: :octicon:`bookmark-fill`
                bookmark-slash: :octicon:`bookmark-slash`
                bookmark-slash-fill: :octicon:`bookmark-slash-fill`
                briefcase: :octicon:`briefcase`
                broadcast: :octicon:`broadcast`
                browser: :octicon:`browser`
                bug: :octicon:`bug`
                calendar: :octicon:`calendar`
                check: :octicon:`check`
                check-circle: :octicon:`check-circle`
                check-circle-fill: :octicon:`check-circle-fill`
                checklist: :octicon:`checklist`
                chevron-down: :octicon:`chevron-down`
                chevron-left: :octicon:`chevron-left`
                chevron-right: :octicon:`chevron-right`
                chevron-up: :octicon:`chevron-up`
                circle: :octicon:`circle`
                circle-slash: :octicon:`circle-slash`
                clock: :octicon:`clock`
                code: :octicon:`code`
                code-review: :octicon:`code-review`
                code-square: :octicon:`code-square`
                codescan: :octicon:`codescan`
                codescan-checkmark: :octicon:`codescan-checkmark`
                codespaces: :octicon:`codespaces`
                columns: :octicon:`columns`
                comment: :octicon:`comment`
                comment-discussion: :octicon:`comment-discussion`
                commit: :octicon:`commit`
                container: :octicon:`container`
                copy: :octicon:`copy`
                cpu: :octicon:`cpu`
                credit-card: :octicon:`credit-card`
                cross-reference: :octicon:`cross-reference`
                dash: :octicon:`dash`
                database: :octicon:`database`
                dependabot: :octicon:`dependabot`
                desktop-download: :octicon:`desktop-download`
                device-camera: :octicon:`device-camera`
                device-camera-video: :octicon:`device-camera-video`
                device-desktop: :octicon:`device-desktop`
                device-mobile: :octicon:`device-mobile`
                diamond: :octicon:`diamond`
                diff: :octicon:`diff`
                diff-added: :octicon:`diff-added`
                diff-ignored: :octicon:`diff-ignored`
                diff-modified: :octicon:`diff-modified`
                diff-removed: :octicon:`diff-removed`
                diff-renamed: :octicon:`diff-renamed`
                dot: :octicon:`dot`
                dot-fill: :octicon:`dot-fill`
                download: :octicon:`download`
                duplicate: :octicon:`duplicate`
                ellipsis: :octicon:`ellipsis`
                eye: :octicon:`eye`
                eye-closed: :octicon:`eye-closed`
                file: :octicon:`file`
                file-badge: :octicon:`file-badge`
                file-binary: :octicon:`file-binary`
                file-code: :octicon:`file-code`
                file-diff: :octicon:`file-diff`
                file-directory: :octicon:`file-directory`
                file-directory-fill: :octicon:`file-directory-fill`
                file-media: :octicon:`file-media`
                file-submodule: :octicon:`file-submodule`
                file-symlink-file: :octicon:`file-symlink-file`
                file-zip: :octicon:`file-zip`
                filter: :octicon:`filter`
                flame: :octicon:`flame`
                fold: :octicon:`fold`
                fold-down: :octicon:`fold-down`
                fold-up: :octicon:`fold-up`
                gear: :octicon:`gear`
                gift: :octicon:`gift`
                git-branch: :octicon:`git-branch`
                git-commit: :octicon:`git-commit`
                git-compare: :octicon:`git-compare`
                git-merge: :octicon:`git-merge`
                git-pull-request: :octicon:`git-pull-request`
                git-pull-request-closed: :octicon:`git-pull-request-closed`
                git-pull-request-draft: :octicon:`git-pull-request-draft`
                globe: :octicon:`globe`
                grabber: :octicon:`grabber`
                graph: :octicon:`graph`
                hash: :octicon:`hash`
                heading: :octicon:`heading`
                heart: :octicon:`heart`
                heart-fill: :octicon:`heart-fill`
                history: :octicon:`history`
                home: :octicon:`home`
                home-fill: :octicon:`home-fill`
                horizontal-rule: :octicon:`horizontal-rule`
                hourglass: :octicon:`hourglass`
                hubot: :octicon:`hubot`
                image: :octicon:`image`
                inbox: :octicon:`inbox`
                infinity: :octicon:`infinity`
                info: :octicon:`info`
                issue-closed: :octicon:`issue-closed`
                issue-draft: :octicon:`issue-draft`
                issue-opened: :octicon:`issue-opened`
                issue-reopened: :octicon:`issue-reopened`
                italic: :octicon:`italic`
                iterations: :octicon:`iterations`
                kebab-horizontal: :octicon:`kebab-horizontal`
                key: :octicon:`key`
                key-asterisk: :octicon:`key-asterisk`
                law: :octicon:`law`
                light-bulb: :octicon:`light-bulb`
                link: :octicon:`link`
                link-external: :octicon:`link-external`
                list-ordered: :octicon:`list-ordered`
                list-unordered: :octicon:`list-unordered`
                location: :octicon:`location`
                lock: :octicon:`lock`
                logo-gist: :octicon:`logo-gist`
                logo-github: :octicon:`logo-github`
                mail: :octicon:`mail`
                mark-github: :octicon:`mark-github`
                markdown: :octicon:`markdown`
                megaphone: :octicon:`megaphone`
                mention: :octicon:`mention`
                meter: :octicon:`meter`
                milestone: :octicon:`milestone`
                mirror: :octicon:`mirror`
                moon: :octicon:`moon`
                mortar-board: :octicon:`mortar-board`
                multi-select: :octicon:`multi-select`
                mute: :octicon:`mute`
                no-entry: :octicon:`no-entry`
                no-entry-fill: :octicon:`no-entry-fill`
                north-star: :octicon:`north-star`
                note: :octicon:`note`
                number: :octicon:`number`
                organization: :octicon:`organization`
                package: :octicon:`package`
                package-dependencies: :octicon:`package-dependencies`
                package-dependents: :octicon:`package-dependents`
                paintbrush: :octicon:`paintbrush`
                paper-airplane: :octicon:`paper-airplane`
                paste: :octicon:`paste`
                pencil: :octicon:`pencil`
                people: :octicon:`people`
                person: :octicon:`person`
                person-add: :octicon:`person-add`
                person-fill: :octicon:`person-fill`
                pin: :octicon:`pin`
                play: :octicon:`play`
                plug: :octicon:`plug`
                plus: :octicon:`plus`
                plus-circle: :octicon:`plus-circle`
                project: :octicon:`project`
                pulse: :octicon:`pulse`
                question: :octicon:`question`
                quote: :octicon:`quote`
                reply: :octicon:`reply`
                repo: :octicon:`repo`
                repo-clone: :octicon:`repo-clone`
                repo-forked: :octicon:`repo-forked`
                repo-pull: :octicon:`repo-pull`
                repo-push: :octicon:`repo-push`
                repo-template: :octicon:`repo-template`
                report: :octicon:`report`
                rocket: :octicon:`rocket`
                rows: :octicon:`rows`
                rss: :octicon:`rss`
                ruby: :octicon:`ruby`
                screen-full: :octicon:`screen-full`
                screen-normal: :octicon:`screen-normal`
                search: :octicon:`search`
                server: :octicon:`server`
                share: :octicon:`share`
                share-android: :octicon:`share-android`
                shield: :octicon:`shield`
                shield-check: :octicon:`shield-check`
                shield-lock: :octicon:`shield-lock`
                shield-x: :octicon:`shield-x`
                sidebar-collapse: :octicon:`sidebar-collapse`
                sidebar-expand: :octicon:`sidebar-expand`
                sign-in: :octicon:`sign-in`
                sign-out: :octicon:`sign-out`
                single-select: :octicon:`single-select`
                skip: :octicon:`skip`
                smiley: :octicon:`smiley`
                sort-asc: :octicon:`sort-asc`
                sort-desc: :octicon:`sort-desc`
                square: :octicon:`square`
                square-fill: :octicon:`square-fill`
                squirrel: :octicon:`squirrel`
                stack: :octicon:`stack`
                star: :octicon:`star`
                star-fill: :octicon:`star-fill`
                stop: :octicon:`stop`
                stopwatch: :octicon:`stopwatch`
                strikethrough: :octicon:`strikethrough`
                sun: :octicon:`sun`
                sync: :octicon:`sync`
                tab: :octicon:`tab`
                table: :octicon:`table`
                tag: :octicon:`tag`
                tasklist: :octicon:`tasklist`
                telescope: :octicon:`telescope`
                telescope-fill: :octicon:`telescope-fill`
                terminal: :octicon:`terminal`
                three-bars: :octicon:`three-bars`
                thumbsdown: :octicon:`thumbsdown`
                thumbsup: :octicon:`thumbsup`
                tools: :octicon:`tools`
                trash: :octicon:`trash`
                triangle-down: :octicon:`triangle-down`
                triangle-left: :octicon:`triangle-left`
                triangle-right: :octicon:`triangle-right`
                triangle-up: :octicon:`triangle-up`
                typography: :octicon:`typography`
                unfold: :octicon:`unfold`
                unlock: :octicon:`unlock`
                unmute: :octicon:`unmute`
                unverified: :octicon:`unverified`
                upload: :octicon:`upload`
                verified: :octicon:`verified`
                versions: :octicon:`versions`
                video: :octicon:`video`
                workflow: :octicon:`workflow`
                x: :octicon:`x`
                x-circle: :octicon:`x-circle`
                x-circle-fill: :octicon:`x-circle-fill`
                zap: :octicon:`zap`


.. _conf:

Puede consultar el siguiente enlace sobre `iconos en linea <https://sphinx-design.readthedocs.io/en/furo-theme/badges_buttons.html#inline-icons/>`_ :octicon:`report;1em;sd-text-info` para más información.

sphinxcontrib.youtube
=====================

Esta extensión facilita la incorporación de videos de YouTube y Vimeo en su documentación. Toman un argumento único y obligatorio, que es la identificación del video: ::

    .. youtube:: dQw4w9WgXcQ
    
    .. vimeo:: 148751763

De forma predeterminada, el vídeo incrustado tiene un tamaño de contenido de 720p. Para configurar esto modifique los parámetros:

+-------------------+---------------------------------------------------------------+
| Propiedad         | Descripción                                                   |
+===================+===============================================================+
| URL               | ID del video de YouTube (obligatorio).                        |
+-------------------+---------------------------------------------------------------+
| aspect            | Relación proporcional de un elemento entre su ancho y alto,   |
|                   | por ejemplo (4:3).                                            |
+-------------------+---------------------------------------------------------------+
| width             | Ancho.                                                        |
+-------------------+---------------------------------------------------------------+
| height            | Altura.                                                       |
+-------------------+---------------------------------------------------------------+
| align             | Alineación (puede ser "center", "left", "right").             |
+-------------------+---------------------------------------------------------------+
| privacy_mode      | Modo de privacidad.                                           |
+-------------------+---------------------------------------------------------------+
| url_parameters    | Inicia el video en un momento específico (por ejemplo,        |
|                   | "?start=43").                                                 |
+-------------------+---------------------------------------------------------------+

.. tab-set::

    .. tab-item:: Ejemplo

        .. youtube:: dQw4w9WgXcQ
            :aspect: 16:9
            :width: 640
            :height: 360
            :align: center
            :privacy_mode: enable_privacy_mode
            :url_parameters: ?start=30

    .. tab-item:: Estructura

        .. code-block::

            .. youtube:: dQw4w9WgXcQ
                :aspect: 16:9
                :width: 640
                :height: 360
                :align: center
                :privacy_mode: enable_privacy_mode
                :url_parameters: ?start=30

Para obtener más información, consulte el enlace sobre `sphinxcontrib-youtube <https://sphinxcontrib-youtube.readthedocs.io/en/latest/usage.html/>`_ :octicon:`report;1em;sd-text-info`.

.. _conf:

Archivo conf.py
===============

El archivo ``conf.py`` es el archivo de configuración principal en Sphinx, contiene las configuraciones y ajustes específicos que controlan cómo se genera y se presenta la documentación. 

Podrá encontrar el archivo en el primer nivel del repositorio. A continuación, se explicarán algunos aspectos importantes a tener en cuenta.

- **templates_path** define la ubicación de la carpeta que contiene las plantillas (archivos de estilo que controlan la apariencia de la documentación).

- **exclude_patterns** se utiliza para especificar patrones de exclusión, es decir, evita que ciertos archivos o carpetas se incluyan en la generación de la documentación. 

- **language** establece el idioma predeterminado de la documentación.

- **languages_names** es utilizado para proporcionar al usuario la posibilidad de seleccionar el idioma de la documentación (aunque esta opción se encuentra deshabilitada y está en proceso).

.. caution:: No modificar.

.. code-block:: python
    :caption: Idioma y otras configuraciones
    :linenos:
    :emphasize-lines: 1,2,4,5

    templates_path = ['_templates']
    exclude_patterns = []

    language = 'es'
    languages_names = {
        'en': 'EN',
        'es': 'ES',
        'fr': 'FR',
    }

- **extension_dir** define la ubicación del directorio ``extensions`` para contener extensiones de Sphinx personalizadas o de terceros.

- **sys.path.insert(0, str(extension_dir.absolute()))**  agrega la ruta al directorio ``extensions`` al principio de la lista de rutas del sistema (sys.path). Es útil si desea utilizar extensiones personalizadas o que no están instaladas de forma global.

- **extensions** se utiliza para habilitar las extensiones en el proyecto. Si necesita instalar una extensión nueva, consulte la documentación de instalación de su extensión de preferencia y posteriormente colóquela aquí.

- **source_suffix** especifica las extensiones de archivo que Sphinx debe considerar como fuentes de documentación. En este caso, Sphinx procesará archivos con las extensiones .rst y .md, lo que significa que puedes escribir documentos de Sphinx en formato reStructuredText (.rst) o en formato Markdown (.md).

.. note:: Aunque ``markdown`` es más simple y fácil de usar, se recomienda utilizar ``restructuredtext`` , ya que Sphinx fue originalmente diseñado para funcionar con ``rst`` y proporciona una mayor sopoerte y estabilidad con funciones, extensiones y directivas.

.. code-block:: python
    :caption: Extensiones
    :linenos:
    :emphasize-lines: 1,2,3,12

    extension_dir = Path('extensions')
    sys.path.insert(0, str(extension_dir.absolute()))
    extensions = [
        'sphinx_design', #Extensión para componentes responsivos.
        'sphinxcontrib.youtube', #Extensión para incrustar videos youtube.
        'sphinxcontrib.mermaid', #Extensión que permite hacer uso de Mermaind (diagramas).
        'sphinx_copybutton', #Extensión que hace posible personalizar .. code-block::
        'sphinx.ext.graphviz', #Extensión sobre gráficos.
        'myst_parser',  #Extensión que permite a Sphinx leer MySt(Markedly Structured Text).
        'sphinx.ext.autodoc', #Automatizar la generación de documentación a partir de los comentarios y docstrings.
    ]
    source_suffix = ['.rst', '.md']

- **html_theme** es la configuración para especificar a Sphinx que se necesita utilizar el tema `furo <https://sphinx-themes.org/sample-sites/furo/>`_ :octicon:`report;1em;sd-text-info`.

- **templates_path** establece la ubicación del directorio de plantillas personalizadas que desea utilizar.

- **html_static_path** es la ubicación de la carpeta ``static`` que contiene archivos estáticos, como imágenes y hojas de estilo, que se utilizarán en la documentación. 

.. important:: La carpeta ``static`` se encuentra en el primer nivel y está destinada a ser modificada. No debe confundirse con la que se encuentra en ``build``.

- **html_css_files** es la ubicacion del archivo ``custom.css`` para agregar CSS personalizado.

- **html_theme_options** esta instrucción es muy importante, se utiliza para personalizar diferentes aspectos del tema ``furo``, como la visibilidad del nombre en la barra lateral, los logotipos, colores, fuentes y otros detalles de estilo.

.. caution:: Cualquier cambio en ``html_theme_options`` afectará a todas las páginas de la documentación. No se recomienda modificarlo a menos que sea necesario.

- **pygments_style** y **pygments_dark_style** establecen el estilo de resaltado de sintaxis para los bloques de código.

- **graphviz_output_format** especifica el formato de salida para los gráficos generados con Graphviz. En este caso, los gráficos se generan en formato PNG.

.. code-block:: python
    :caption: Personalización y otras configuraciones
    :linenos:
    :emphasize-lines: 1,2,3,4,5,24,25,26

    html_theme = 'furo'
    templates_path = ['./extensions/']
    html_static_path = ['static']
    html_css_files = ['css/custom.css']
    html_theme_options = {
        'sidebar_hide_name': True,
        'light_logo': '/img/Linkaform_light.png',
        'dark_logo': '/img/Linkaform_dark_new.png',
        'light_css_variables': {
            "color-brand-primary": "#0c1c49",
            "color-brand-content": "#2c3e50",
            "color-background-hover": "#e1e2e6",
        },
        'dark_css_variables': {
            "color-background-primary": "#1c262d", 
            "color-background-secondary": "#141b1f",
            "color-background-hover": "#27343e",
            "color-brand-primary": "#FFFFFF",
            "color-brand-content": "#E0E0E0",
            "color-header-text": "#FFFFFF",
        },
        'font-stack': "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu",
    }
    pygments_style = "lightbulb"
    pygments_dark_style = "zenburn"
    graphviz_output_format = 'png' 

