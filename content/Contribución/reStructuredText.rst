.. _escribiendo:

===============================
Escribiendo en reStructuredText
===============================

reStructuredText es el lenguaje de marcado de texto sin formato predeterminado utilizado por Sphinx. Esta sección es una breve introducción a los conceptos y la sintaxis de reStructuredText (reST) que comúnmente se utiliza para crear documentación.

Creación de archivo
===================

Antes de iniciar con la explicación de reStructuredText, siga estos pasos para crear su primer proyecto.

1. Cree la carpeta de su proyecto en la :ref:`content` :octicon:`report;1em;sd-text-info`.

.. caution:: Asegúrese de que el nombre de su carpeta no contenga espacios, en caso de tener más de dos palabras use ``snake_case``.

2. Cree su archivo ``.rst`` dentro de la carpeta de su proyecto.

.. grid:: 2
    :gutter: 0

    .. grid-item-card::  Directory Tree
        :columns: 4

        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style type="text/css">
                A:visited { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:link    { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:active  { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                .VERSION { font-size: small; font-family : arial, sans-serif; }
                .NORM  { color: black;  }
                .FIFO  { color: purple; }
                .CHAR  { color: yellow; }
                .DIR   { color: blue;   }
                .BLOCK { color: yellow; }
                .LINK  { color: aqua;   }
                .SOCK  { color: fuchsia;}
                .EXEC  { color: green;  }
            </style>
            </head>
                <body>
                <a>.</a><br>
                ├── <a>carpeta_ejemplo</a><br>
                │   ├── <a>archivo1.rst</a><br>
                ├── <a>index.rst</a><br>
                ├── <a>Módulos</a><br>
                ├── <a>PDF</a><br>
                └── <a>Reportes</a><br>
                </body>
            </html>

    .. grid-item-card::   
        :columns: 8

        .. caution:: De la misma manera, asegúrese de que el nombre de su archivo no contenga espacios.

Si dentro de la carpeta de su proyecto tiene más de un archivo, cree un archivo ``index.rst``, y los archivos que necesite, por ejemplo:

.. grid:: 2
    :gutter: 0

    .. grid-item-card::  Directory Tree
        :columns: 4
                
        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style type="text/css">
                A:visited { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:link    { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:active  { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                .VERSION { font-size: small; font-family : arial, sans-serif; }
                .NORM  { color: black;  }
                .FIFO  { color: purple; }
                .CHAR  { color: yellow; }
                .DIR   { color: blue;   }
                .BLOCK { color: yellow; }
                .LINK  { color: aqua;   }
                .SOCK  { color: fuchsia;}
                .EXEC  { color: green;  }
            </style>
            </head>
                <body>
                <a>.</a><br>
                ├── <a>carpeta_ejemplo</a><br>
                │   ├── <a>archivo1.rst</a><br>
                │   ├── <a>archivo2.rst</a><br>
                │   ├── <a>archivo3.rst</a><br>
                │   ├── <a>index.rst</a><br>
                ├── <a>index.rst</a><br>
                ├── <a>Módulos</a><br>
                ├── <a>PDF</a><br>
                └── <a>Reportes</a><br>
                </body>
            </html>

    .. grid-item-card::   
        :columns: 8

        .. note:: El archivo ``index.rst`` se crea únicamente cuando se tiene más de un archivo ``.rst``. Este archivo permite agrupar todos los archivos de su carpeta en uno solo y tratarlo como un enlace hacia el contenido principal. (Consulte :ref:`preparar_toctree` :octicon:`report;1em;sd-text-info` para más detalles).

Si necesita otras secciones dentro de su proyecto, cree una subcarpeta y dentro de ella los archivos que necesite.

.. grid:: 2
    :gutter: 0

    .. grid-item-card::  Directory Tree
        :columns: 12

        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style type="text/css">
                A:visited { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:link    { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:active  { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                .VERSION { font-size: small; font-family : arial, sans-serif; }
                .NORM  { color: black;  }
                .FIFO  { color: purple; }
                .CHAR  { color: yellow; }
                .DIR   { color: blue;   }
                .BLOCK { color: yellow; }
                .LINK  { color: aqua;   }
                .SOCK  { color: fuchsia;}
                .EXEC  { color: green;  }
            </style>
            </head>
                <body>
                <a>.</a><br>
                ├── <a>carpeta_ejemplo</a><br>
                │   ├── <a>archivo1.rst</a><br>
                │   ├── <a>archivo2.rst</a><br>
                │   ├── <a>archivo3.rst</a><br>
                │   ├── <a>index.rst</a><br>
                │   └── <a>subcarpeta</a><br>
                │   &nbsp;&nbsp;&nbsp; ├── <a>archivo1.rst</a><br>
                │   &nbsp;&nbsp;&nbsp; ├── <a>archivo2.rst</a><br>
                │   &nbsp;&nbsp;&nbsp; ├── <a>archivo3.rst</a><br>
                │   &nbsp;&nbsp;&nbsp; └── <a>archivo4.rst</a><br>
                ├── <a>index.rst</a><br>
                ├── <a>Módulos</a><br>
                ├── <a>PDF</a><br>
                └── <a>Reportes</a><br>
                </body>
            </html>

Secciones
=========

Las secciones resultan útiles para organizar y estructurar su documentación, ya que permiten dividir el contenido en partes más pequeñas y establecer una jerarquía clara.

En lugar de imponer un número y un orden fijos para el título de la sección, el orden aplicado será el orden encontrado. El primer estilo hallado se considerará como un título principal (similar al HTML H1), el segundo estilo será un subtítulo, el tercero será otro subtítulo, y así sucesivamente.

A continuación, se muestran ejemplos de títulos y subelementos ::

    ====================
    Título de la Sección
    ====================

    Introducción
    ============

    Sección 1
    ---------
            
    Subsección 1.1
    ^^^^^^^^^^^^^^
    Subsección 1.2
    ^^^^^^^^^^^^^^

    Sección 2
    ---------

.. importante:: La longitud de la cadena de texto debe ser igual a la longitud del símbolo que se va a utilizar, por ejemplo:

    .. code-block::
        :caption: Correcto

        Título con la longitud correcta
        ===============================

    .. code-block::
        :caption: Incorrecto

        Título con la longitud incorrecta
        ===========

Párrafos
========

El párrafo es el bloque más básico en un documento ``reST``. Los párrafos son simplemente fragmentos de texto separados por uno o más espacios en blanco. 

.. important:: Como en Python, la sangría es significativa en reST, por lo que todas las líneas del mismo párrafo debe estar alineado a la izquierda con el mismo nivel de sangría. 

Resaltos
========

El marcado en línea estándar de reST es muy sencilla.

Utilice un asterisco para un *énfasis* (cursiva)::

    *text*

Utilice dos asteriscos para un **fuerte énfasis** (negrita)::

    **text**

Utilice comillas inversas para un ejemplo de tipo ``código en línea``::


    ``text``

.. caution:: Al utilizar alguno de los resaltos anteriores, debe tener cuidado con los espacios. Si existe un espacio entre el caracter y la palabra, la instrucción no será reconocida.
    
Listas 
======

Listas ordenadas y no ordenadas
-------------------------------

Para crear una lista no ordenada, simplemente coloque un asterisco ``*`` al principio del texto y aplique la sangría adecuada. 

Del mismo modo, las listas numeradas se pueden generar automáticamente utilizando el signo ``#`` al principio de cada elemento o enumerarlas manualmente (1, 2, 3...).

.. tab-set::

    .. tab-item:: Ejemplo

        * Esta es una lista con viñetas.
        * Tiene dos ítems, el segundo item
          utiliza dos líneas.

        1. Esta es una lista numerada.
        2. También tiene dos elementos.

        #. Esta es una lista numerada.
        #. Tiene dos artículos también.

    .. tab-item:: Estructura

        .. code-block::

            * Esta es una lista con viñetas.
            * Tiene dos ítems, el segundo item
              utiliza dos líneas.

            1. Esta es una lista numerada.
            2. También tiene dos elementos.

            #. Esta es una lista numerada.
            #. Tiene dos artículos también.

Listas anidadas
---------------

Es posible anidar listas, pero es importante tener en cuenta que deben separarse de los elementos de la lista principal mediante líneas en blanco.

.. tab-set::

    .. tab-item:: Ejemplo

        * Esto es
            * una lista
            * con una lista anidada
            * y algunos subelementos
        * y aquí continúa la lista padre

    .. tab-item:: Estructura

        .. code-block::

            * Esto es
                * una lista
                * con una lista anidada
                * y algunos subelementos
            * y aquí continúa la lista padre

Tablas 
======

Las tablas en reStructuredText se crean utilizando caracteres como la barra vertical ``|``, guiones ``-``, ``+``, e incluso el signo igual ``=`` para definir las celdas y encabezados de la tabla.

Si desea mostrar tablas con bordes, deberá agregar la cuadrícula manualmente, por ejemplo:

.. tab-set::

    .. tab-item:: Ejemplo

        +-----------+--------------+------------+
        | Fruta     | Color        | Sabor      |
        +===========+==============+============+
        | Manzana   | Roja         | Dulce      |
        +-----------+--------------+------------+
        | Plátano   | Amarillo     | Dulce      |
        +-----------+--------------+------------+
        | Fresa     | Roja         | Dulce      |
        +-----------+--------------+------------+



    .. tab-item:: Estructura

        .. code-block::

            +-----------+--------------+------------+
            | Fruta     | Color        | Sabor      |
            +===========+==============+============+
            | Manzana   | Roja         | Dulce      |
            +-----------+--------------+------------+
            | Plátano   | Amarillo     | Dulce      |
            +-----------+--------------+------------+
            | Fresa     | Roja         | Dulce      |
            +-----------+--------------+------------+

Las tablas simples son más fáciles de escribir, pero tienen limitaciones. Deben tener más de una fila y las celdas de la primera columna no pueden contener múltiples líneas, por ejemplo:

.. tab-set::

    .. tab-item:: Ejemplo

        ================  ==========  ==========
        Fruta             Color       Sabor
        ================  ==========  ==========
        Manzana           Roja        Dulce
        Plátano           Amarillo    Dulce
        Fresa             Roja        Dulce
        ================  ==========  ==========

    .. tab-item:: Estructura

        .. code-block::

            ================  ==========  ==========
            Fruta             Color       Sabor
            ================  ==========  ==========
            Manzana           Roja        Dulce
            Plátano           Amarillo    Dulce
            Fresa             Roja        Dulce
            ================  ==========  ==========

Si necesita información más detallada acerca de las tablas, puede consultar la documentación disponible en `Tables <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables/>`_ :octicon:`report;1em;sd-text-info`.

.. _etiqueta:

Hipervínculos
=============

Enlaces externos
----------------

Puede crear hipervínculos a sitios externos de dos maneras sencillas, utilizando una función especial de reST o empleando código HTML.

Para utilizar la función que ofrece reST, puede hacerlo de la siguiente manera:

.. tab-set::

    .. tab-item:: Ejemplo

        `Documentación oficial de Sphinx <https://www.sphinx-doc.org/en/master/>`_ :octicon:`report;1em;sd-text-info`.

    .. tab-item:: Estructura

        .. code-block::

            `Documentación oficial de Sphinx <https://www.sphinx-doc.org/en/master/>`_.

.. important:: Tenga en cuenta que debe existir un espacio entre el texto del enlace y la apertura ``<`` de la URL.

.. note:: Se recomienda el uso del :ref:`icons` para destacar al usuario que se trata de un enlace.

La función que ofrece reST está está limitada y no hay un atributo que permita abrir el enlace en una nueva página por defecto. Si necesita esta funcionalidad, considere el uso de HTML de la siguiente manera:

.. tab-set::

    .. tab-item:: Ejemplo

        |nombre_etiqueta| :octicon:`report;1em;sd-text-info`.

    .. tab-item:: Estructura

        .. code-block::
            :caption: Establezca la etiqueta

            .. |nombre_etiqueta| raw:: html

                <a href="https://www.sphinx-doc.org/en/master" target="_blank">Documentación oficial de Sphinx</a>

        .. code-block::
            :caption: Haga referencia a la etiqueta

            |nombre_etiqueta| :octicon:`report;1em;sd-text-info`.

Observe que simplemente debe crear una etiqueta HTML con el atributo target seguido del nombre que necesita, para después llamarla entre símbolos de barra.

.. note:: Si utiliza enlaces externos con ayuda de HTML, se recomienda colocar las ligas al final de su documento ``rst`` y especificar que se trata de ligas externas mediante un comentario. Esto facilita una mejor organización y permite un mantenimiento más efectivo en posteriores ocasiones.

.. _mi-etiqueta-de-referencia:

Enlaces internos
----------------

Si desea enlazar a otra parte de su propia documentación, puede hacerlo utilizando dos funciones especiales de reST proporcionada por Sphinx.

Para que la función de reST opere correctamente, los nombres de las etiquetas deben ser únicos. Si coloca una etiqueta directamente antes del título de una sección, esta función tomará ese nombre por defecto y lo mostrará; es decir, no podrá modificar el nombre que quiera presentar. Por ejemplo:

.. tab-set::

    .. tab-item:: Ejemplo

        Se refiere a la sección misma, ver :ref:`mi-etiqueta-de-referencia` :octicon:`report;1em;sd-text-info`.

    .. tab-item:: Estructura

        .. code-block::
            :caption: Establezca la etiqueta

            .. _mi-etiqueta-de-referencia:

            Enlaces internos
            ----------------

        .. code-block::
            :caption: Haga referencia a la etiqueta

            Se refiere a la sección misma :ref:`mi-etiqueta-de-referencia` :octicon:`report;1em;sd-text-info`.

.. important:: 
    Las etiquetas de referencia deben comenzar con un guion bajo. 
    
    Al hacer referencia a una etiqueta, se debe omitir el guion bajo.

    Si necesita información más detallada acerca de hipervínculos, puede consultar la documentación disponible en `reStructuredText  <https://www.sphinx-doc.org/en/master/usage/referencing.html#ref-role/>`_ :octicon:`report;1em;sd-text-info`.

La otra opción de hipervínculo interno es utilizando etiquetas personalizadas, como se muestra a continuación:

.. tab-set::

    .. tab-item:: Ejemplo

        Se refiere a la sección misma, ver `Personaliza <#etiqueta>`_ :octicon:`report;1em;sd-text-info`

    .. tab-item:: Estructura

        .. code-block::
            :caption: Establezca la etiqueta

            .. _etiqueta:

            Enlaces internos
            ----------------

        .. code-block::
            :caption: Haga referencia a la etiqueta

            Se refiere a la sección misma, ver `Personaliza <#etiqueta>`_ :octicon:`report;1em;sd-text-info`

.. important:: Esta función es más cómoda y permite personalizar el mensaje del hipervínculo. El nombre de la etiqueta debe ser una sola palabra; no puede incluir espacios, por ejemplo, ``nombre_etiqueta`` debe ser ``etiqueta``.

Directivas
==========

Las directivas son comandos especiales de marcado que permiten incorporar elementos interactivos, como tablas, imágenes, notas y otros elementos, en su documentación.

Básicamente, una directiva consta de un nombre, argumentos, opciones y contenido. Una directiva es uno de los mecanismos de extensión de reStructuredText (reST), y Sphinx la emplea de manera frecuente en su funcionamiento.

Tabla de contenidos
-------------------

Dado que reST no proporciona facilidades para interconectar varios documentos o dividir documentos en múltiples archivos de salida, Sphinx utiliza una directiva personalizada para agregar relaciones entre los distintos archivos que componen la documentación, así como tablas de contenidos. La directiva ``toctree`` es el elemento central en este proceso.

.. _toc:

toctree
^^^^^^^

La directiva toctree en reStructuredText (reST) se utiliza para crear una tabla de contenidos en su documentación. Permite especificar qué documentos o secciones se incluirán en la tabla de contenidos y la profundidad máxima de la jerarquía de secciones que se mostrará.

**Inicio de la directiva toctree**

Para comenzar a usar la directiva toctree, debe insertar ``.. toctree::`` en su documento. Esta línea inicia la directiva y le dice a reST que se creará una tabla de contenidos en ese punto.

**Parámetros**

:bdg-secondary:`:caption:`: Se utiliza para agregar un título o una leyenda a la tabla de contenidos generada por esa directiva. 

Esto es útil cuando necesita proporcionar una breve descripción o contexto para la tabla de contenidos que está creando, por ejemplo: ::

    .. toctree::
        :caption: Documentación de Python

        introduccion.rst
        variables.rst
        funciones.rst
        ...


:bdg-secondary:`:maxdepth:`: Es un parámetro opcional, se utiliza para limitar la profundidad de la tabla de contenidos. Esto es útil si desea mostrar solo ciertos niveles de secciones. 

Por ejemplo, ``:maxdepth: 2`` mostrará solo las dos primeras capas de secciones en la tabla de contenidos::

    .. toctree::
        :maxdepth: 2

        archivo1.rst
        archivo2.rst

:bdg-secondary:`:titlesonly:`: Este parámetro resulta útil cuando se desea mostrar únicamente los títulos de las secciones en la tabla de contenidos, sin incluir enlaces. 

Por ejemplo: ::

    .. toctree::
        :titlesonly:

        archivo1.rst
        archivo2.rst

:bdg-secondary:`:hidden:`: Si necesita que la tabla de contenidos se genere, pero no se muestre en la documentación final, puede utilizar hidden. Esto es útil para mantener la tabla de contenidos en segundo plano.

Observe el siguiente ejemplo: ::

    .. toctree::
        :hidden:

        archivo1.rst
        archivo2.rst

:bdg-secondary:`:numbered:`: Este parámetro es opcional y se utiliza para numerar automáticamente las entradas de la tabla de contenidos.

Por ejemplo, para que las entradas se numeren utilice el siguiente ejemplo: ::

    .. toctree::
        :numbered:

        archivo1.rst
        archivo2.rst


Antes de continuar, asegúrese de tener en cuenta la ubicación de sus archivos. En este ejemplo, tenemos dos archivos en nuestro proyecto y dos archivos en carpetas diferentes. ::
    
    .. toctree::

        Capitulo1.rst
        Capitulo2.rst
        Subcarpeta/Subcapitulo1.rst
        Subcarpeta/Subcapitulo2.rst

.. important:: Asegúrese de aplicar la sangría de manera adecuada.

    .. code-block::
        :caption: Correcto

        .. toctree::
            :maxdepth: 2
            :titlesonly:
            :numbered:

            Capitulo1.rst
            Capitulo2.rst
            Subcarpeta/Subcapitulo1.rst
            Subcarpeta/Subcapitulo2.rst
            
    .. code-block::
        :caption: Incorrecto

        .. toctree::
        :maxdepth: 2
        :titlesonly:
        :numbered:

        Capitulo1.rst
        Capitulo2.rst
        Subcarpeta/Subcapitulo1.rst
        Subcarpeta/Subcapitulo2.rst

Observe el siguiente ejemplo. Con fines prácticos, en la siguiente figura se muestra la tabla de contenido del proyecto principal, la cual incluye ``:maxdepth: 2`` y ``:titlesonly:``.

.. tab-set::

    .. tab-item:: Ejemplo

        .. image:: /imgs/Contribución/11.1.png

    .. tab-item:: Estructura

        .. code-block::

            ==========================
            Documentación de Linkaform
            ==========================

            .. toctree::
                :maxdepth: 2
                :titlesonly:

                1.Introducción/Introducción
                2.Módulos/Módulos
                3.PDF/PDF
                4.Reportes/Reportes
                5.Desarrolladores/Index
                Contribución/Index

En este ejemplo, hemos utilizado ``:maxdepth: 4`` para mostrar las secciones hasta una profundidad de 4, ``:titlesonly:`` para visualizar solo los títulos, y ``:numbered:`` para numerar automáticamente el contenido.

.. tab-set::

    .. tab-item:: Ejemplo

        .. image:: /imgs/Contribución/11.2.png
            
    .. tab-item:: Estructura

        .. code-block::

            ==========================
            Documentación de Linkaform
            ==========================

            .. toctree::
                :maxdepth: 4
                :titlesonly:
                :numbered:

                1.Introducción/Introducción
                2.Módulos/Módulos
                3.PDF/PDF
                4.Reportes/Reportes
                5.Desarrolladores/Index
                Contribución/Index

Si requiere información adicional, conocer otros parámetros o necesita otros ejemplos puede consultar la documentación de `Sphinx  <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree/>`_ :octicon:`report;1em;sd-text-info`. 

.. _preparar_toctree:

Preparar toctree
^^^^^^^^^^^^^^^^

Cuando tenga su contenido organizado y escrito en archivos ``.rst``, debe indicarle a Sphinx dónde debe buscar los documentos. A continuación, siga los siguientes pasos para agregar su contenido al índice.

.. note:: Para el siguiente ejemplo, tenga en cuenta que se está presentando un proyecto almacenado en la carpeta ``Desarrollador``. En consecuencia, este ya se encuentra en el índice principal, por lo tanto, se mostrará como *llamarla* en el índice de dicha carpeta. Sin embargo, en caso de tener un proyecto independiente, los mismos pasos aplican.
    
1. Anteriormente, se mostró cómo y dónde crear sus archivos ``.rst``. Ahora deberá agregar un título a sus archivos. Esto es fundamental, ya que la directiva busca el título principal para incluirlo en el índice.

2. Una vez que haya añadido el título, deberá incluir la ruta de sus archivos en el ``index.rst`` de su proyecto.

.. grid:: 2
    :gutter: 0

    .. grid-item-card::  Directory Tree
        :columns: 5

        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style type="text/css">
                A:visited { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:link    { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:active  { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                .VERSION { font-size: small; font-family : arial, sans-serif; }
                .NORM  { color: black;  }
                .FIFO  { color: purple; }
                .CHAR  { color: yellow; }
                .DIR   { color: blue;   }
                .BLOCK { color: yellow; }
                .LINK  { color: aqua;   }
                .SOCK  { color: fuchsia;}
                .EXEC  { color: green;  }
                .HIP   { background-color: red; color: white; text-decoration: none; }
            </style>
            </head>
                <body>
                <a>.</a><br>
                ├── <a>carpeta_ejemplo</a><br>
                   ├── <a>archivo1.rst</a><br>
                   ├── <a>archivo2.rst</a><br>
                   ├── <a>archivo3.rst</a><br>
                   ├── <a class="HIP">index.rst</a><br>
                   └── <a>subcarpeta</a><br>
                   &nbsp;&nbsp;&nbsp; ├── <a>archivo1.rst</a><br>
                   &nbsp;&nbsp;&nbsp; ├── <a>archivo2.rst</a><br>
                   &nbsp;&nbsp;&nbsp; ├── <a>archivo3.rst</a><br>
                   &nbsp;&nbsp;&nbsp; └── <a>archivo4.rst</a><br>
                </body>
            </html>

    .. grid-item-card::  toctree en index.rst
        :columns: 7

        .. code-block::

            ==============
            Título ejemplo
            ==============

            .. toctree::
               
                archivo1
                archivo2
                archivo3
                subcarpeta/archivo1
                subcarpeta/archivo2
                subcarpeta/archivo3
                subcarpeta/archivo4

3. Ahora inserte la ruta del ``index`` de su proyecto en la carpeta padre del mismo, en este caso, el ``index`` de la carpeta ``Desarrollador``.

.. grid:: 2
    :gutter: 0

    .. grid-item-card::  Directory Tree
        :columns: 5

        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style type="text/css">
                A:visited { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:link    { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                A:active  { text-decoration : none; line-height: 1; margin : 0px; padding : 0px;}
                .VERSION { font-size: small; font-family : arial, sans-serif; }
                .NORM  { color: black;  }
                .FIFO  { color: purple; }
                .CHAR  { color: yellow; }
                .DIR   { color: blue;   }
                .BLOCK { color: yellow; }
                .LINK  { color: aqua;   }
                .SOCK  { color: fuchsia;}
                .EXEC  { color: green;  }
                .HIP   { background-color: red; color: white; text-decoration: none; }
            </style>
            </head>
                <body>
                <a>.</a><br>
                ├── <a>carpeta_ejemplo</a><br>
                │   ├── <a>archivo1.rst</a><br>
                │   ├── <a>archivo2.rst</a><br>
                │   ├── <a>archivo3.rst</a><br>
                │   ├── <a>index.rst</a><br>
                │   └── <a>subcarpeta</a><br>
                │   &nbsp;&nbsp;&nbsp; ├── <a>archivo1.rst</a><br>
                │   &nbsp;&nbsp;&nbsp; ├── <a>archivo2.rst</a><br>
                │   &nbsp;&nbsp;&nbsp; ├── <a>archivo3.rst</a><br>
                │   &nbsp;&nbsp;&nbsp; └── <a>archivo4.rst</a><br>
                ├── <a class="HIP">index.rst</a><br>
                ├── <a>Módulos</a><br>
                ├── <a>PDF</a><br>
                └── <a>Reportes</a><br>
                </body>
            </html>

    .. grid-item-card::  toctree en index.rst
        :columns: 7

        .. code-block::

            ==================================
            Documentación para desarrolladores
            ==================================

            .. toctree::
                :maxdepth: 1
                :titlesonly:

                Módulos/index
                PDF/index
                Reportes/index
                carpeta_ejemplo/index

Con esto, ha logrado insertar satisfactoriamente su contenido. Puede probar sus cambios siguiendo :ref:`generar_HTML` :octicon:`report;1em;sd-text-info` o continuar leyendo acerca de cómo escribir en reST.

Advertencias
------------

Las advertencias son útiles para incorporar contenido adicional en su documentación sin interrumpir significativamente el flujo del documento. Sphinx ofrece varios tipos de advertencias diferentes y permite la inclusión y anidación de contenido arbitrario.

.. important:: Recuerde respetar la indentación.

Nota
^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. note:: Esta es una nota básica.

        .. note:: 
            Esta es otra advertencia básica con varios párrafos.

            Puede incluir listas, código, tablas o imágenes.

    .. tab-item:: Estructura

        .. code-block::
            
            .. note:: Esta es una nota básica.

            .. note:: 
                Esta es otra advertencia básica con varios párrafos.

                Puede incluir listas, código, tablas o imágenes.
            
            Para finalizar un bloque de advertencia, simplemente colóquese a la misma altura donde comenzó la instrucción.
                
Peligro
^^^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. danger:: Tocar esto sin saber lo que está haciendo es como tratar de domar un león mientras lleva una hamburguesa en el bolso.

    .. tab-item:: Estructura

        .. code-block::
            
            .. danger:: Tocar esto sin saber lo que está haciendo es como tratar de domar un león mientras lleva una hamburguesa en el bolso.

Error
^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. error:: Parece que cometiste un error de dedo. 

    .. tab-item:: Estructura

        .. code-block::
            
            .. error:: Parece que cometiste un error de dedo. 

Atención
^^^^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. attention:: El cambio climático es real.

    .. tab-item:: Estructura

        .. code-block::
            
            .. attention:: El cambio climático es real.

Advertencia
^^^^^^^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. warning:: Si su código funciona, no lo toque más.

    .. tab-item:: Estructura

        .. code-block::
            
            .. warning:: Si su código funciona, no lo toque más.

Precaución
^^^^^^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. caution:: No sobrepase el horario de comida.

    .. tab-item:: Estructura

        .. code-block::
            
            .. caution:: No sobrepase el horario de comida.

Importante
^^^^^^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. important:: Esta biblioteca es compatible con las versiones de Python 3.6 o superiores.


    .. tab-item:: Estructura

        .. code-block::
            
            .. important:: Esta biblioteca es compatible con las versiones de Python 3.6 o superiores.

Pista
^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. hint:: Aquí tienes una pequeña pista, si el código no funciona, ¡probablemente necesite algún arreglo! Mágico.

    .. tab-item:: Estructura

        .. code-block::
            
            .. hint:: Aquí tienes una pequeña pista, si el código no funciona, ¡probablemente necesite algún arreglo! Mágico.

Consejo
^^^^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. tip:: Intente reiniciar su equipo.

    .. tab-item:: Estructura

        .. code-block::
            
            .. tip:: Intente reiniciar su equipo.

Ver también
^^^^^^^^^^^

.. tab-set::

    .. tab-item:: Ejemplo

        .. seealso:: Otra información relevante. 

    .. tab-item:: Estructura

        .. code-block::
            
            .. seealso:: Otra información relevante. 

Si necesita más información a cerca de las tarjetas de advertencia, o en su caso requiere advertencias personalizadas puede consultar la documentación que ofrece el tema furo respecto a las `advertencias  <https://pradyunsg.me/furo/reference/admonitions/#admonition/>`_ :octicon:`report;1em;sd-text-info`.

Imágenes
--------

Las imágenes en línea se pueden definir utilizando la directiva ``image``. El argumento obligatorio de esta directiva es la URI del archivo de imagen.

Opcionalmente, el bloque de la directiva de imagen puede contener una lista de campos clave y valor, que definen las opciones de la imagen, por ejemplo:

.. tab-set::

    .. tab-item:: Ejemplo

        .. image:: /imgs/Contribución/gato.jpg
            :height: 650px
            :width: 550px
            :scale: 50%
            :alt: texto alternativo
            :align: center

    .. tab-item:: Estructura

        .. code-block::
            
            .. image:: /imgs/Contribución/gato.jpg
                :height: 650px
                :width: 550px
                :scale: 50%
                :alt: texto alternativo
                :align: center

Se reconocen las siguientes opciones: 

+------------+-------------------------------------------------+
| Propiedad  | Descripción                                     |
+============+=================================================+
| height     | La altura deseada de la imagen en píxeles o     |
|            | porcentaje.                                     | 
+------------+-------------------------------------------------+
| width      | El ancho de la imagen en píxeles o porcentaje.  |
+------------+-------------------------------------------------+
| scale      | El factor de escala uniforme de la imagen,      |
|            | expresado en porcentaje (el símbolo ``%`` es    |
|            | opcional).                                      |
+------------+-------------------------------------------------+
| alt        | Texto alternativo.                              |
+------------+-------------------------------------------------+
| align      | La alineación de la imagen (``top``, ``middle``,|
|            | ``bottom``, ``left``, ``center`` o ``right``).  |
+------------+-------------------------------------------------+

.. attention:: Al utilizar la directiva ``image``, debe tener en cuenta lo siguiente:

    Es correcto que exista un espacio entre los dos puntos y la ruta de la imagen, así como también una sangría para las propiedades.

    .. code-block::
        :caption: Correcto

        .. image:: /imgs/Contribución/gato.jpg
            :height: 300px
            :width: 550px
            :scale: 50%
            :alt: texto alternativo
            :align: center

    .. code-block::
        :caption: Incorrecto

        .. image::/imgs/Contribución/gato.jpg
        :height: 300px
        :width: 550px
        :scale: 50%
        :alt: texto alternativo
        :align: center

Si necesita más información sobre imágenes, puede consultar el siguiente `enlace <https://docutils.sourceforge.io/docs/ref/rst/directives.html#image/>`_ :octicon:`report;1em;sd-text-info`.

Bloques de código
-----------------

Los bloques de código son una herramienta valiosa que permite ver ejemplos de código, comprender su funcionamiento y en última instancia, aplicarlo a su propio proyecto. Sphinx proporciona una forma flexible de incluir bloques de código en su documentación a través de la directiva bloque de código.

Para mostrar un código de ejemplo, utilice `code-block` bajo la siguiente estructura: ::

    .. code-block:: language

        code ...
  
Al especificar el lenguaje, se habilitarán los colores correspondientes a la sintaxis, como se muestra a continuación.

.. tab-set::

    .. tab-item:: Código python

        .. code-block:: python

            # Esto es un ejemplo de código en Python
            def saludar(nombre):
                print("Hola, {nombre}!")

    .. tab-item:: Código JS

        .. code-block:: javascript

            // Esto es un ejemplo de código en JavaScript
            function saludar(nombre) {
                console.log(`Hola, ${nombre}!`);
            }
            saludar("Pedrito");

    .. tab-item:: Código HTML 

        .. code-block:: HTML

            <!-- Esto es un ejemplo de código HTML -->
            <!DOCTYPE html>
            <html>
            <head>
                <title>Mi Página Web</title>
            </head>
            <body>
                <h1>Bienvenido a mi página web</h1>
                <p>Esta es una página de ejemplo.</p>
            </body>
            </html>

    .. tab-item:: Código CSS

        .. code-block:: CSS

            /*Esto es un ejemplo de código CSS*/
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }

            .header {
                background-color: #333;
                color: #fff;
                text-align: center;
                padding: 10px;
            }

            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }

Títulos dentro del bloque
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Puede agregar títulos dentro del bloque de código utilizando el parámetro ``:caption:``` ::

    .. code-block:: language
        :caption: Example

        code ...


Mostrar números de línea
^^^^^^^^^^^^^^^^^^^^^^^^

Puede agregar números de línea a bloques de código con el parámetro ``:linenos:``: ::

    .. code-block:: language
        :linenos:

        code ...

Resaltar líneas
^^^^^^^^^^^^^^^

Puede resaltar ciertas líneas utilizando el parámetro ``:emphasize-lines:``: ::

    .. code-block:: language
        :emphasize-lines: 6,12,15

        code ...

Los parámetros mencionados anteriormente se reflejan de la siguiente manera, con un título, números de línea y líneas resaltadas:

.. code-block:: XML
    :caption: Ejemplo de código XML
    :linenos:
    :emphasize-lines: 6,12,15

    <library>
    <book>
        <title>El Gran Gatsby</title>
        <author>F. Scott Fitzgerald</author>
        <genre>Novela</genre>
        <published>1925</published>
    </book>
    <book>
        <title>1984</title>
        <author>George Orwell</author>
        <genre>Distopía</genre>
        <published>1949</published>
    </book>
    <book>
        <title>Matar a un ruiseñor</title>
        <author>Harper Lee</author>
        <genre>Novela</genre>
        <published>1960</published>
    </book>
    </library>

Si necesita explicar un fragmento de código en múltiples partes de la documentación o si el código es muy extenso, puede guardarlo en un archivo independiente y luego incluirlo de la siguiente manera: ::
    
    .. include:: mi_codigo.txt

.. note:: Para guardar su archivos, deberá ubicarlos en la carpeta ``codi`` dentro de la carpeta ``content``.

Los parámetros mencionados anteriormente son los más utilizados. Si tiene alguna duda o necesita información adicional, consulte la documentación sobre `code-block <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#showing-code-examples/>`_ :octicon:`report;1em;sd-text-info`.

.. _codigo-crudo:

Código en crudo
^^^^^^^^^^^^^^^

El código en crudo es un tipo de marcado sin formato. Se utiliza la directiva ``raw`` junto al lenguaje que va a ejecutar. Esta directiva funciona como una medida provisional que permite omitir el marcado de reStructuredText. 

El siguiente ejemplo permite incrustar código HTML en crudo, es decir, se ejecutará como un HTML normal en un navegador. 

.. tab-set::

    .. tab-item:: HTML en crudo

        .. raw:: html

            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <style>
                    .ghost{
                    block-size: 25rem;
                    inline-size: 17.5rem;
                    background-color: #de95d6;
                    border-radius: 10rem 10rem 0 0;
                    position: relative;
                    }
                    .ghost::before{
                    content: '';
                    position: absolute;
                    inset-block-end: -3.5rem;
                    background-color: transparent;
                    color: transparent;
                    inline-size: 5.9rem;
                    block-size: 6rem;
                    border-radius: 50%;
                    box-shadow: 5.9rem 0, 11.6rem 0;
                    }
                    .eye{
                    background-color: white;
                    color: white;
                    position: absolute;
                    inset-inline-end: 1.5rem;
                    inset-block-start: 5rem;
                    inline-size: 5rem;
                    block-size: 5rem;
                    border-radius: 50%;
                    box-shadow: -7rem 0;
                    }
                    .eye::before{
                    content: '';
                    inline-size: 2rem;
                    block-size: 2rem;
                    border-radius: 50%;
                    inset-block-start: 1.5rem;
                    inset-inline-end: .8rem;
                    background-color: #0c63bf;
                    color: #0c63bf;
                    box-shadow: -7rem 0;
                    position: absolute;
                    }
                </style>
                <h2>Fantasma</h2>
                <div class="ghost">
                    <div class="eye"></div>
                </div>
            </body>
            </html>

    .. tab-item:: Estructura raw

        .. code-block::

            .. raw:: html
            
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                </head>
                <body>
                    <style>
                        .ghost{
                        block-size: 25rem;
                        inline-size: 17.5rem;
                        background-color: #de95d6;
                        border-radius: 10rem 10rem 0 0;
                        position: relative;
                        }
                        .ghost::before{
                        content: '';
                        position: absolute;
                        inset-block-end: -3.5rem;
                        background-color: transparent;
                        color: transparent;
                        inline-size: 5.9rem;
                        block-size: 6rem;
                        border-radius: 50%;
                        box-shadow: 5.9rem 0, 11.6rem 0;
                        }
                        .eye{
                        background-color: white;
                        color: white;
                        position: absolute;
                        inset-inline-end: 1.5rem;
                        inset-block-start: 5rem;
                        inline-size: 5rem;
                        block-size: 5rem;
                        border-radius: 50%;
                        box-shadow: -7rem 0;
                        }
                        .eye::before{
                        content: '';
                        inline-size: 2rem;
                        block-size: 2rem;
                        border-radius: 50%;
                        inset-block-start: 1.5rem;
                        inset-inline-end: .8rem;
                        background-color: #0c63bf;
                        color: #0c63bf;
                        box-shadow: -7rem 0;
                        position: absolute;
                        }
                    </style>
                    <h2>Fantasma</h2>
                    <div class="ghost">
                        <div class="eye"></div>
                    </div>
                </body>
                </html>

En caso de tener un archivo extenso puede utilizar la directiva file y adjuntar la URL de su archivo. Por ejemplo: ::

    .. raw:: html
        :file: /cod/archivo.html

.. note:: Para guardar su archivo HTML, deberá ubicarlo en la carpeta ``codi`` dentro de la carpeta ``content``.

.. caution:: Tenga cuidado con el uso excesivo de la directiva en crudo. Al permitir la omisión del marcado de reStructuredText hace que su página sea menos portátil, afectando el formato y además, representa un potencial agujero de seguridad.

Para más detalles consulte la documentación sobre `transferencia de datos sin procesar <https://docutils.sourceforge.io/docs/ref/rst/directives.html#raw-data-pass-through/>`_ :octicon:`report;1em;sd-text-info`.

Comentarios
-----------

En reStructuredText, los comentarios se crean utilizando el carácter de dos puntos ``..``. Los comentarios son útiles para incluir notas, aclaraciones o información que no debe aparecer en la documentación final, pero que puede ser útil para los autores o colaboradores del documento.

Aquí hay un ejemplo de como crear comentarios en reST:

.. tab-set::

    .. tab-item:: Ejemplo

        Este es un párrafo normal.

        .. Este es un comentario que no se mostrará en la documentación final.
            Puede escribir cualquier cosa aquí, y se ignorará al generar la salida.


    .. tab-item:: Estructura

        .. code-block::
            
            Este es un párrafo normal.

            .. Este es un comentario que no se mostrará en la documentación final.
                Puede escribir cualquier cosa aquí, y se ignorará al generar la salida.

.. attention:: La correcta aplicación de la sangría es esencial para que los comentarios sean interpretados adecuadamente. Los comentarios deben tener la misma sangría que el texto.

Directorios
===========

.. note:: El siguiente contenido no es propio de restructuredtext ni de una extensión de Sphinx. 

Para ilustrar de forma gráfica la estructura de su proyecto, utilice la herramienta ``tree`` basada exclusivamente en sistemas Unix y Linux. Este comando muestra la organización de directorios y archivos en forma de árbol, lo que facilita la navegación y la comprensión de la estructura de datos en el sistema.

Por lo general, ya se encuentra instalado en la mayoría de las distribuciones de Linux. Para verificar si ``tree`` está instalado en su sistema, simplemente abra una terminal y ejecute: ::

    tree --version

Si ``tree`` está instalado, verá la versión del programa. Si no está instalado, puede seguir estos pasos para instalarlo en Debian/Ubuntu:

1. Abra una terminal y ejecute: ::

    sudo apt-get update
    sudo apt-get install tree

En el caso de tener una distribución de Linux diferente, puede consultar la siguiente `página <https://itslinuxfoss.com/install-tree-linux/>`_ :octicon:`report;1em;sd-text-info` para instalar la herramienta de acuerdo a su sistema operativo.

.. note:: Si está utilizando un sistema operativo Windows y tiene instalado Git Bash, puede utilizar la terminal, ya que básicamente es una emulación del entorno Unix.

Comandos de tree
----------------

Los comandos de ``tree`` permiten limitar la profundidad de visualización de los directorios. Hay variedad de comandos que puede consultar directamente en la terminal ejecutando: ::

    man tree

Algunos de los comandos más usados son los siguientes.

+------------------------------------+----------------------------------------------------------------------------------------------------------+
| Comando                            | Descripción                                                                                              |
+====================================+==========================================================================================================+
| $ tree                             | Muestra directorios y ficheros.                                                                          |
+------------------------------------+----------------------------------------------------------------------------------------------------------+
| $ tree -d                          | Muestra solo directorios.                                                                                |
+------------------------------------+----------------------------------------------------------------------------------------------------------+
| $ tree -L X                        | Muestra hasta X directorios de profundidad.                                                              |
+------------------------------------+----------------------------------------------------------------------------------------------------------+
| $ tree -f                          | Muestra los archivos con su respectiva ruta.                                                             |
+------------------------------------+----------------------------------------------------------------------------------------------------------+
| $ tree -a                          | Muestra todos los archivos, incluidos los ocultos.                                                       |
+------------------------------------+----------------------------------------------------------------------------------------------------------+
| $ tree /                           | Muestra un árbol de todo nuestro sistema.                                                                |
+------------------------------------+----------------------------------------------------------------------------------------------------------+
| $ tree -ugh                        | Muestra los ficheros con su respectivo propietario (-u), el grupo (-g) y el tamaño de cada archivo (-h). |
+------------------------------------+----------------------------------------------------------------------------------------------------------+
| $ tree -H . -o nombre_archivo.html | Exporta el árbol del directorio a un archivo HTML.                                                       |
+------------------------------------+----------------------------------------------------------------------------------------------------------+

Para crear un directorio siga los siguientes pasos.

1. Ubique la carpeta deseada, por ejemplo: ::

    cd lkf/documentation

2. Ejecute el comando que necesite. En el siguiente ejemplo solo se muestran los directorios hasta el nivel 2.

.. image:: /imgs/Contribución/5.png

3. Una vez confirmado su directorio exporte el archivo a html. Para ello ejecute: :: 

    -H . -o nombre_archivo.html

.. image:: /imgs/Contribución/6.png

.. important:: Al exportar su archivo HTML, por defecto se ubicará en la carpeta desde la cual esté consultando el directorio. Para evitar tener archivos HTML sueltos, deberá moverlo a la carpeta ``directorios``. Asegúrese de darle un nombre descriptivo a su archivo.

4. Cuando tenga su directorio listo y desee colocarlo en un lugar específico, deberá hacer uso de :ref:`codigo-crudo` y realizar algunas modificaciones necesarias.

El código html que se genera al exportar su directorio es el siguiente: 

.. code-block:: html
    :emphasize-lines: 8-24, 27, 49 - 60
    :linenos:

    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="Author" content="Made by 'tree'">
    <meta name="GENERATOR" content="$Version: $ tree v2.0.2 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro $">
    <title>Directory Tree</title>
    <style type="text/css">
    BODY { font-family : monospace, sans-serif;  color: black;}
    P { font-family : monospace, sans-serif; color: black; margin:0px; padding: 0px;}
    A:visited { text-decoration : none; margin : 0px; padding : 0px;}
    A:link    { text-decoration : none; margin : 0px; padding : 0px;}
    A:hover   { text-decoration: underline; background-color : yellow; margin : 0px; padding : 0px;}
    A:active  { margin : 0px; padding : 0px;}
    .VERSION { font-size: small; font-family : arial, sans-serif; }
    .NORM  { color: black;  }
    .FIFO  { color: purple; }
    .CHAR  { color: yellow; }
    .DIR   { color: blue;   }
    .BLOCK { color: yellow; }
    .LINK  { color: aqua;   }
    .SOCK  { color: fuchsia;}
    .EXEC  { color: green;  }
    </style>
    </head>
    <body>
        <h1>Directory Tree</h1><p>
        <a href=".">.</a><br>
        ├── <a href="./build/">build</a><br>
        │   ├── <a href="./build/Contribuci%C3%B3n/">Contribución</a><br>
        │   ├── <a href="./build/Desarrollador/">Desarrollador</a><br>
        │   ├── <a href="./build/_images/">_images</a><br>
        │   ├── <a href="./build/_sources/">_sources</a><br>
        │   ├── <a href="./build/_sphinx_design_static/">_sphinx_design_static</a><br>
        │   ├── <a href="./build/_static/">_static</a><br>
        │   └── <a href="./build/_video_thumbnail/">_video_thumbnail</a><br>
        ├── <a href="./content/">content</a><br>
        │   ├── <a href="./content/Contribuci%C3%B3n/">Contribución</a><br>
        │   ├── <a href="./content/Desarrollador/">Desarrollador</a><br>
        │   └── <a href="./content/imgs/">imgs</a><br>
        ├── <a href="./directorios/">directorios</a><br>
        ├── <a href="./extensions/">extensions</a><br>
        │   └── <a href="./extensions/cards/">cards</a><br>
        ├── <a href="./locale/">locale</a><br>
        │   └── <a href="./locale/en/">en</a><br>
        └── <a href="./static/">static</a><br>
        &nbsp;&nbsp;&nbsp; ├── <a href="./static/css/">css</a><br>
        &nbsp;&nbsp;&nbsp; └── <a href="./static/img/">img</a><br>
    <br><br><p>

    20 directories

    </p>
        <hr>
        <p class="VERSION">
            tree v2.0.2 © 1996 - 2022 by Steve Baker and Thomas Moore <br>
            HTML output hacked and copyleft © 1998 by Francesc Rocher <br>
            JSON output hacked and copyleft © 2014 by Florian Sesser <br>
            Charsets / OS/2 support © 2001 by Kyosuke Tokoro
        </p>
    </body>
    </html>


Deberá realizar las siguientes modificaciones:

- Elimine los estilos (líneas 8-24).
- Elimine el H1 (línea 27).
- Elimine los créditos (líneas 49-60).
- En las etiquetas ``a`` elimine la URL de referencia.

Sus modificaciones se verán de la siguiente manera:

.. tab-set::

    .. tab-item:: Directory Tree

        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <meta name="Author" content="Made by 'tree'">
            <meta name="GENERATOR" content="$Version: $ tree v2.0.2 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro $">
            <title>Directory Tree</title>
            </head>
            <body>
                <a>.</a><br>
                ├── <a>build</a><br>
                │   ├── <a>Contribución</a><br>
                │   ├── <a>Desarrollador</a><br>
                │   ├── <a>_images</a><br>
                │   ├── <a>_sources</a><br>
                │   ├── <a>_sphinx_design_static</a><br>
                │   ├── <a>_static</a><br>
                │   └── <a>_video_thumbnail</a><br>
                ├── <a>content</a><br>
                │   ├── <a>Contribución</a><br>
                │   ├── <a>Desarrollador</a><br>
                │   └── <a>imgs</a><br>
                ├── <a>directorios</a><br>
                ├── <a>extensions</a><br>
                │   └── <a>cards</a><br>
                ├── <a>locale</a><br>
                │   └── <a>en</a><br>
                └── <a>static</a><br>
                &nbsp;&nbsp;&nbsp; ├── <a>css</a><br>
                &nbsp;&nbsp;&nbsp; └── <a>img</a><br>
            </body>
            </html>

    .. tab-item:: Estructura

        .. code-block::

            .. raw:: html

                <!DOCTYPE html>
                <html>
                <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <meta name="Author" content="Made by 'tree'">
                <meta name="GENERATOR" content="$Version: $ tree v2.0.2 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro $">
                <title>Directory Tree</title>
                </head>
                <body>
                    <a>.</a><br>
                    ├── <a>build</a><br>
                    │   ├── <a>Contribución</a><br>
                    │   ├── <a>Desarrollador</a><br>
                    │   ├── <a>_images</a><br>
                    │   ├── <a>_sources</a><br>
                    │   ├── <a>_sphinx_design_static</a><br>
                    │   ├── <a>_static</a><br>
                    │   └── <a>_video_thumbnail</a><br>
                    ├── <a>content</a><br>
                    │   ├── <a>Contribución</a><br>
                    │   ├── <a>Desarrollador</a><br>
                    │   └── <a>imgs</a><br>
                    ├── <a>directorios</a><br>
                    ├── <a>extensions</a><br>
                    │   └── <a>cards</a><br>
                    ├── <a>locale</a><br>
                    │   └── <a>en</a><br>
                    └── <a>static</a><br>
                    &nbsp;&nbsp;&nbsp; ├── <a>css</a><br>
                    &nbsp;&nbsp;&nbsp; └── <a>img</a><br>
                </body>
                </html>

Para obtener más información sobre los comandos de ``tree``, puede ejecutar el siguiente comando en su terminal: ::

    man tree

En esta sección, ha aprendido a crear sus archivos con la estructura y contenido básico de restructuredtext. En la próxima sección, aprenderá a mejorar su contenido con la ayuda de extensiones que le proporcionarán un valor potencial más atractivo y funcional.


.. LIGAS EXTERNAS

.. |nombre_etiqueta| raw:: html

    <a href="https://www.sphinx-doc.org/en/master" target="_blank">Documentación oficial de Sphinx</a>