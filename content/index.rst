.. LinkaForm documentation master file, created by
   sphinx-quickstart on Thu Sep 14 23:15:23 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

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
   Contribución/Index


..  youtube:: v=N_yuPf1ITjE
   :align: center
   :aspect: 16:9

.. graphviz:: extructura.dot

.. graphviz::

   digraph example {
       A -> B
       B -> C
   }

.. graph:: foo

   "bar" -- "baz";


.. digraph:: foo

   "bar" -> "baz" -> "quux";

.. graphviz::

     digraph example {
         a [label="sphinx", href="https://www.sphinx-doc.org/", target="_top"];
         b [label="other"];
         a -> b;
     }


.. graphviz::

   digraph proyecto {
      rankdir=TB;  // Dirección del flujo de arriba a abajo

      // Nodos del proyecto y carpetas
      node [shape=plaintext];  // Cambiar la forma a "plaintext"
      proyecto [label="miproyecto"];
      docs [label="docs"];
      build [label="build"];
      html [label="html"];
      index_html [label="index.html"];
      source [label="source"];
      conf_py [label="conf.py"];
      index_rst [label="index.rst"];
      README [label="README"];
      miproyecto_dir [label="miproyecto"];
      init_py [label="__init__.py"];
      main_py [label="main.py"];

      // Conexiones entre nodos
      proyecto -> docs;
      docs -> build;
      build -> html;
      build -> Makefile;
      html -> index_html;
      docs -> source;
      source -> conf_py;
      source -> index_rst;
      proyecto -> README;
      proyecto -> miproyecto_dir;
      miproyecto_dir -> init_py;
      miproyecto_dir -> main_py;
   }

.. graphviz::

   digraph proyecto {
      rankdir=TB;  // Dirección del flujo de arriba a abajo
   
      // Nodos del proyecto y carpetas
      node [shape=box];
      proyecto [label="miproyecto"];
      docs [label="docs"];
      build [label="build"];
      html [label="html"];
      index_html [label="index.html"];
      source [label="source"];
      conf_py [label="conf.py"];
      index_rst [label="index.rst"];
      README [label="README"];
      miproyecto_dir [label="miproyecto"];
      init_py [label="__init__.py"];
      main_py [label="main.py"];
   
      // Conexiones entre nodos
      proyecto -> docs;
      docs -> build;
      build -> html;
      build -> Makefile;
      html -> index_html;
      docs -> source;
      source -> conf_py;
      source -> index_rst;
      proyecto -> README;
      proyecto -> miproyecto_dir;
      miproyecto_dir -> init_py;
      miproyecto_dir -> main_py;
   }
   


.. raw:: html
   
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
      │   ├── <a href="./build/1.Introducci%C3%B3n/">1.Introducción</a><br>
      │   ├── <a href="./build/2.M%C3%B3dulos/">2.Módulos</a><br>
      │   ├── <a href="./build/3.PDF/">3.PDF</a><br>
      │   ├── <a href="./build/4.Reportes/">4.Reportes</a><br>
      │   ├── <a href="./build/Contribuci%C3%B3n/">Contribución</a><br>
      │   ├── <a href="./build/genindex.html">genindex.html</a><br>
      │   ├── <a href="./build/_images/">_images</a><br>
      │   ├── <a href="./build/index.html">index.html</a><br>
      │   ├── <a href="./build/objects.inv">objects.inv</a><br>
      │   ├── <a href="./build/search.html">search.html</a><br>
      │   ├── <a href="./build/searchindex.js">searchindex.js</a><br>
      │   ├── <a href="./build/_sources/">_sources</a><br>
      │   ├── <a href="./build/_sphinx_design_static/">_sphinx_design_static</a><br>
      │   ├── <a href="./build/_static/">_static</a><br>
      │   └── <a href="./build/_video_thumbnail/">_video_thumbnail</a><br>
      ├── <a href="./conf.py">conf.py</a><br>
      ├── <a href="./content/">content</a><br>
      │   ├── <a href="./content/1.Introducci%C3%B3n/">1.Introducción</a><br>
      │   ├── <a href="./content/2.M%C3%B3dulos/">2.Módulos</a><br>
      │   ├── <a href="./content/3.PDF/">3.PDF</a><br>
      │   ├── <a href="./content/4.Reportes/">4.Reportes</a><br>
      │   ├── <a href="./content/Contribuci%C3%B3n/">Contribución</a><br>
      │   ├── <a href="./content/imgs/">imgs</a><br>
      │   ├── <a href="./content/index.rst">index.rst</a><br>
      │   └── <a href="./content/locale/">locale</a><br>
      ├── <a href="./docker-compose.yml">docker-compose.yml</a><br>
      ├── <a href="./Dockerfile">Dockerfile</a><br>
      ├── <a href="./estruc.html">estruc.html</a><br>
      ├── <a href="./estructura.html">estructura.html</a><br>
      ├── <a href="./extensions/">extensions</a><br>
      │   └── <a href="./extensions/cards/">cards</a><br>
      ├── <a href="./LICENSE">LICENSE</a><br>
      ├── <a href="./local_build">local_build</a><br>
      ├── <a href="./locale/">locale</a><br>
      │   └── <a href="./locale/en/">en</a><br>
      ├── <a href="./Makefile">Makefile</a><br>
      ├── <a href="./README.md">README.md</a><br>
      ├── <a href="./requirements.txt">requirements.txt</a><br>
      └── <a href="./static/">static</a><br>
      &nbsp;&nbsp;&nbsp; ├── <a href="./static/css/">css</a><br>
      &nbsp;&nbsp;&nbsp; └── <a href="./static/img/">img</a><br>
   <br><br><p>
   </body>
   </html>
