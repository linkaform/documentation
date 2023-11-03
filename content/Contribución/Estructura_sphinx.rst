===========================
Estructura de documentación
===========================

Tras la instalación y configuración del entorno, es importante conocer la estructura que utiliza **Linkaform** para mantener su contenido.

Carpetas 
========

En su repositorio podrá encontrar las siguientes carpetas donde:

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
                <p>
                <a href=".">.</a><br>
                ├── <a>build</a><br>
                ├── <a>conf.py</a><br>
                ├── <a>content</a><br>
                ├── <a>docker-compose.yml</a><br>
                ├── <a>Dockerfile</a><br>
                ├── <a>extensions</a><br>
                ├── <a>LICENSE</a><br>
                ├── <a>local_build</a><br>
                ├── <a>locale</a><br>
                ├── <a>Makefile</a><br>
                ├── <a>README.md</a><br>
                ├── <a>requirements.txt</a><br>
                └── <a>static</a><br>
            <p>
            </body>
            </html>

    .. grid-item-card:: Carpetas de interés
        :columns: 8

        +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
        | Nombre                               | Descripción                                                                                                                                        |
        +======================================+====================================================================================================================================================+
        | Build                                | Carpeta que se genera al hacer build de su proyecto.                                                                                               |
        +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
        | Content                              | Carpeta dónde podrá almacenar su documentación escrita en rst.                                                                                     |
        +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
        | Extensions                           | Carpeta que se genera al instalar una extensión nueva.                                                                                             |
        +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
        | Locale                               | Carpeta que contiene archivos .po útiles para traducciones de las páginas.                                                                         |
        +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
        | Static                               | Carpeta que almacena archivos sobre personalización.                                                                                               |
        +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
        | Conf.py                              | Archivo que contiene la configuración principal de Sphinx. :ref:`conf` :octicon:`report;1em;sd-text-info`                                          |
        +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Carpeta build
=============

Esta carpeta contiene los archivos generados por Sphinx, como la documentación en formato HTML, PDF, etc. Los archivos en esta carpeta son los que se pueden distribuir o publicar para que otros los consulten.

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
                <p>
                <a href=".">.</a><br>
                ├── <a>Introducción</a><br>
                ├── <a>Módulos</a><br>
                ├── <a>PDF</a><br>
                ├── <a>Reportes</a><br>
                ├── <a>Desarrolladores</a><br>
                ├── <a>Contribución</a><br>
                ├── <a>genindex.html</a><br>
                ├── <a>_images</a><br>
                ├── <a>index.html</a><br>
                ├── <a>objects.inv</a><br>
                ├── <a>search.html</a><br>
                ├── <a>searchindex.js</a><br>
                ├── <a>_sources</a><br>
                ├── <a>_sphinx_design_static</a><br>
                ├── <a>_static</a><br>
                └── <a>_video_thumbnail</a><br>
            </body>
            </html>
            
    .. grid-item-card::  Carpetas de interés
        :columns: 8

        +-------------+-------------------------------------------------------------------------------------------------------------------------+
        | **Nombre**  | **Descripción**                                                                                                         |
        +=============+=========================================================================================================================+
        | _images     | En esta carpeta, se almacena todas las imágenes que se utilizan en la documentación (gráficos o imágenes).              |
        +-------------+-------------------------------------------------------------------------------------------------------------------------+
        | _static     | Almacena archivos estáticos utilizados por los temas en la documentación (archivos CSS, imágenes o archivos JavaScript).|
        +-------------+-------------------------------------------------------------------------------------------------------------------------+
        | .doctrees   | Contiene archivos temporales utilizados para agilizar la generación de la documentación.                                |
        +-------------+-------------------------------------------------------------------------------------------------------------------------+
        +-------------+-------------------------------------------------------------------------------------------------------------------------+
        | objects.inv | Se utiliza para generar un índice de objetos en la documentación. Ayuda a vincular y buscar  elementos específicos.     |
        +-------------+-------------------------------------------------------------------------------------------------------------------------+
        | arch.html   | Los archivos que llevan la terminación .html son archivos rst convertidos a html para presentarse en formato web.       |
        +-------------+-------------------------------------------------------------------------------------------------------------------------+

Carpeta content
===============

La carpeta ``content`` alberga archivos fuente de la documentación en formato ReStructuredText. Sphinx utiliza estos archivos como base para generar la documentación final.

.. grid:: 2
    :gutter: 0

    .. grid-item-card::  Directory Tree
        :columns: 3

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
                ├── <a>Introducción</a><br>
                ├── <a>Módulos</a><br>
                ├── <a>PDF</a><br>
                ├── <a>Reportes</a><br>
                ├── <a>Desarrolladores</a><br>
                ├── <a>Contribución</a><br>
                ├── <a>imgs</a><br>
                ├── <a>index.rst</a><br>
                └── <a>locale</a><br>
            </body>
            </html>
            
    .. grid-item-card::  
        :columns: 9

        Al comenzar con su proyecto cree una carpeta con un nombre descriptivo.

        .. seealso:: Introducción, Módulos, PDF, Reportes, Desarrolladores y Contribución son carpetas que pertenecen a una sección de la documentación.

        En caso de utilizar imágenes, cree una nueva carpeta con el nombre de su proyecto dentro de la carpeta ``imgs``. Dentro de esta carpeta, puede organizar las imágenes de la manera que le resulte más cómoda.

        .. important:: index.rst es el archivo principal que debe ejecutar en su navegador (:ref:`generar_HTML` :octicon:`report;1em;sd-text-info`). Si se encuentra trabajando en una sección nueva asegurese de incluir su indice en el :ref:`toc` :octicon:`report;1em;sd-text-info` del index principal.

Carpeta static
==============

Carpeta que almacena archivos sobre personalización como hojas de estilo (CSS), imágenes o archivos JavaScript.

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
                <a href=".">.</a><br>
                ├── <a href="./css/">css</a><br>
                │   └── <a href="./css/custom.css">custom.css</a><br>
                ├── <a href="./directorio4.html">directorio4.html</a><br>
                └── <a href="./img/">img</a><br>
                &nbsp;&nbsp;&nbsp; ├── <a href="./img/Linkaform_dark.png">Linkaform_dark.png</a><br>
                &nbsp;&nbsp;&nbsp; └── <a href="./img/Linkaform_light.png">Linkaform_light.png</a><br>
            </body>
            </html>    

    .. grid-item-card:: 
        :columns: 8

        .. important:: Esta carpeta solo se utiliza para modificaciones que afectan a toda la documentación.

        En caso de aplicar estilos CSS, puede hacerlo en el archivo ``custom.css``, solamente asegúrese de agregar comentarios que identifiquen su propósito.

        Dentro de la carpeta ``img``, se almacenan imágenes que se desean mostrar en todas las páginas, como los logotipos de Linkaform.

Carpetas extra
==============

Otras carpetas importantes que son generadas al momento de instalar alguna extensión, son las siguientes:

:bdg-secondary:`_sphinx_design_static`: Esta carpeta contiene archivos estáticos derivados de la extensión Sphinx design para diseñar componentes web responsivos.

:bdg-secondary:`Cards`: Carpeta dentro de extensions, derivada de la extensión Cards para el uso de tarjetas personalizadas.

:bdg-secondary:`_video_thumbnail`: Carpeta generada por la extensión sphinxcontrib.youtube, útil para incluir videos. En esta carpeta se almacenan miniaturas o recursos relacionados con los videos.

En esta sección, se han explicado las carpetas principales que se utilizarán para crear la documentación. En secciones posteriores, se presentarán ejemplos de cómo escribir documentación con reStructuredText y cómo añadirlos al índice principal.

