.. _crear-reporte-demo:

================
Creación de Demo
================

La creación de un reporte comienza con el desarrollo de un **reporte demo** (prototipo). Este prototipo tiene como objetivo mostrar la idea de funcionamiento y demostrar las funcionalidades del reporte al cliente. Esto permite recibir retroalimentación y realizar mejoras en el aspecto visual del reporte y la forma de presentar la información. 

Una vez que se cuenta con la demo, la integración del script se simplifica, ya que resulta más fácil comprender qué datos se van a utilizar y cómo deben presentarse.

.. note:: Recuerde que para el desarrollo de un reporte puede realizar el proceso de configuración en |Producción| :octicon:`report;1em;sd-text-info` o en |Preproducción| :octicon:`report;1em;sd-text-info`, ya que el proceso es idéntico. Sin embargo, se recomienda iniciar el proceso de creación de reportes en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

.. _estructura-archivos:

Estructura de archivos
======================

Dentro del :ref:`repositorio-servido` :octicon:`report;1em;sd-text-info` encontrará los archivos correspondientes al front-end del reporte. Por favor, sigan los siguientes pasos para crear los archivos necesarios y continúe revisando cada sección correspondiente a la explicación sobre su contenido.

1. Cree una carpeta exclusiva dentro de la carpeta ``Apps`` para sus reportes en caso de no contar con una.

.. note:: Identifique a la carpeta con el nombre de su empresa o el cliente que lo requiera.

2. Cree los cuatro archivos correspondientes al front-end del reporte, las cuales incluyen:

- **reporte_nombre.html**: Estructura del reporte.    
- **reporte_nombre.js**: Lógica encargada de gestionar las solicitudes a la *API*, así como de procesar y presentar la información correspondiente en la estructura establecida.
- **reporte_nombre_data.js**: Configuraciones de librerías que se utilizan.
- **style.css**: Estilos generales del reporte (un archivo por carpeta).

.. important:: En las siguientes secciones se explicará el contenido de cada archivo. Sin embargo, considere que NO se tiene un estándar establecido para el contenido. No obstante, utilice los ejemplos como base para sus proyectos futuros.

Estructura html
---------------

El archivo ``html`` se encarga de establecer la estructura del reporte y facilitar la inclusión de archivos y bibliotecas externas que son necesarias. El archivo ``HTML`` se divide en tres partes: el ``head``, el ``body`` y las ``librerías``. 

A continuación, se presentan fragmentos de código HTML con explicaciones detalladas sobre cada parte, destacando los elementos que se pueden personalizar.

.. note:: El código completo se encuentra al final de la sección.

head
^^^^

El encabezado (``head``) contiene información y metadatos que influyen en la interpretación del navegador. También incluye enlaces a CDNs para bibliotecas de estilos como Bootstrap y Font Awesome (íconos), además de estilos propios de Linkaform.

.. code-block:: html
    :caption: head
    :linenos:
    :emphasize-lines: 7

    <!DOCTYPE html>
        <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title>Servido</title>
            <meta name="title" content="Servido">
            <meta name="description" content="Reporte Visitas">
            <link type="image/x-icon" rel="shortcut icon" href="../styles/img/favicon.ico">
            <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1, maximum-scale=1">
            <link type="image/x-icon" rel="shortcut icon" href="../styles/img/favicon.ico">
            <!--Bootstrap -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <!--Font Awesome -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <!--Utils -->        
            <link rel="stylesheet" href="../styles/css/sweetalert2.min.css">
            <link rel="stylesheet" href="../styles/css/styles.css">
            <link rel="stylesheet" href="style.css">
        </head>

Asegúrese de ajustar el contenido ubicado en la línea 7 según sus requerimientos. Más allá de eso, evite realizar cambios adicionales en esta sección. 

.. note:: Analice el código y lea los comentarios para comprender su funcionalidad.

body
^^^^

En el cuerpo (``body``) se establece la estructura visible del reporte, donde se definen elementos como cabeceras, títulos, gráficas, tablas, cards, entre otros. Se incluye todo lo necesario para establecer la estructura correspondiente a filtros y elementos donde la información se presentará. 

En el siguiente dropdown, encontrará el código del cuerpo de un reporte.  

.. dropdown:: Código body

    .. code-block:: html
        :linenos:

        <body>
            <!-- Header -->
            <nav class="navbar header">
                <div class="navbar-brand">
                    <div class="row">
                        <div class="col-md-6">
                            <a href="index.html">
                                <div class="logo_marca">
                                    <img src="https://app.linkaform.com/img/login-linkaform-logo.png" alt="LinkaForm" id="image_log">
                                </div>
                            </a>
                        </div>
                        <div class="col-md-6">
                            <div class="container">
                                <div class="back"  id="atras"><i class="fa fa-solid fa-arrow-left"></i>Atras</div>
                                <div class="close" id="close_sesion"><a onclick="closeSession();"><i class="fa-solid fa-lock"></i>Cerrar Sesión</a></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-12">
                        <h1 id="title_report">Reporte Visitas</h1>
                    </div>
                </div> 
            </nav>

            <!-- Loading style -->
            <div class="loading-container">
                <div class="spinner-border text-primary" role="status">
                    <span class="sr-only">Loading...</span>
                </div>
            </div>

            <!-- Content -->
            <div style="width:100%">
                <div class="app" id="appCont" style="padding-top: 0px;">
                
                    <!--Session -->
                    <div class="row inicio_ses" id="inicio_ses">
                        <div class="errorLogin" id="errorLog"></div>
                        <div class="control">
                            <div class="renglon">
                                <h3>Usuario: </h3>
                                <input class="form-control ds-input" id="user" name="user" value="">
                            </div>
                            <div class="renglon">
                                <h3>Contraseña: </h3>
                                <input class="form-control ds-input" type="password" id="pass" name="pass" value="">
                            </div>
                            <div class="controlBtn">
                            <div class="btn btn-primary" onclick="login()">Login</div>
                            <div class="btn btn-primary" onclick="reset()">Reset</div>
                            </div>
                        </div>
                    </div>

                    <!--Title Demo -->
                    <div id="title_demo" style="margin-bottom: 20px;">
                        <center>
                            <h1><span>Demo data</span>&nbsp;&nbsp;</h1>
                        </center>
                    </div>

                    <!--Options FIlter -->
                    <div class="col-sm-12 col-md-12 col-lg-12 row" id="divOptions">
                        <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#firstParameters" aria-expanded="false" aria-controls="collapseExample" id="buttonFilter">
                            <i class="fa-solid fa-filter"></i>
                        </button >  &nbsp;  &nbsp;
                        <div class="btn btn-primary" onclick="runFirstElement()" >Run</div>
                    </div>

                    <!--Filters -->
                    <div id="firstParameters" class="collapse row show">
                        <div class="col-sm-12 col-md-3 col-lg-3">
                            <h5>Fecha Desde: </h5>
                            <input class="form-control ds-input" type="date" id="date_from" name="date_from">
                        </div>
                        <div class="col-sm-12 col-md-3 col-lg-3">
                            <h5>Fecha Hasta: </h5>
                            <input class="form-control ds-input" type="date" id="date_to" name="date_to">
                        </div>

                        <div class="col-sm-12 col-md-3 col-lg-3" >
                            <h5>Promotor: </h5>
                            <select class="form-control mdb-select md-form" id="promotor">
                                <option value="">--Seleccione--</option>
                            </select>
                        </div>
                    </div>

                    <!--Content -->
                    <div class="row" style="margin-top:20px;"  id="divContent">

                        <!--Primer Elemento -->
                        <div class="col-sm-12 col-md-12 col-lg-12" style="align-items: center;overflow-y: scroll;">
                            <section class="title_tables">
                                <h3><span>Recepción Visitas</span>&nbsp;&nbsp;
                                    <button class="btn btn-primary" id="download_csv_firstElement"><i class="fa-solid fa-file-csv"></i></button>
                                    <button class="btn btn-success" id="download_xlsx_firstElement"><i class="fa-regular fa-file-excel"></i></button>
                                </h3>
                                <hr class="hrFirstElement">
                            </section>
                            <div id="firstElement" ></div>
                        </div>  
                    </div>
                </div>
            </div>
        </body>

.. caution:: En los elementos, no se recomienda el uso de estilos en línea. En su lugar, se sugiere asignar clases a los elementos y colocar el código CSS correspondiente en la sección de estilos (style) de su proyecto.

A continuación, se detallan por bloques de código el cuerpo del reporte para indicar qué elementos se pueden personalizar.

Header del reporte
******************

El primer bloque corresponde al encabezado del reporte. Su función principal es mostrar las siguientes opciones:
 
- Opción para cerrar sesión. 
- Mostrar logo de la empresa.

.. seealso:: Consulte la :ref:`funcion-window-onload` :octicon:`report;1em;sd-text-info` donde se detallan los eventos utilizados.
    
- Mostrar nombre del reporte.

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: html
            :caption: Header
            :linenos:
            :emphasize-lines: 9, 18, 25

            <!-- Header -->
            <nav class="navbar header">
                <div class="navbar-brand">
                    <div class="row">
                        <!-- Logo -->
                        <div class="col-md-6">
                            <a href="index.html">
                                <div class="logo_marca">
                                    <img src="https://app.linkaform.com/img/login-linkaform-logo.png" alt="LinkaForm" id="image_log">
                                </div>
                            </a>
                        </div>

                        <!-- Opción para cerrar sesión -->
                        <div class="col-md-6">
                            <div class="container">
                                <div class="back"  id="atras"><i class="fa fa-solid fa-arrow-left"></i>Atras</div>
                                <div class="close" id="close_sesion"><a onclick="closeSession();"><i class="fa-solid fa-lock"></i>Cerrar Sesión</a></div>
                            </div>
                        </div>
                    </div>

                    <!-- Nombre del reporte (cambiar) -->
                    <div class="col-md-12">
                        <h1 id="title_report">Nombre del reporte</h1>
                    </div>
                </div> 
            </nav>

        .. caution:: Regularmente, la estructura no cambia. Sin embargo, asegúrese de cambiar el nombre del reporte (línea 25). Lea los comentarios en el código. 

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes11.png

.. _estructura-elementos:

Content del reporte
*******************

El contenido (``content``) es la parte más importante de la estructura html; aquí se establecen los elementos que se utilizan para filtrar y representar la data. Dentro de ``content``, se encuentran bloques de código estandarizados que se explican a continuación.

.. note:: Al final, podrá encontrar el bloque completo del contenido.

El bloque ``Session`` contiene el inicio de sesión del reporte, es decir, cuando se intenta abrir desde :ref:`link-servido` :octicon:`report;1em;sd-text-info`.

.. seealso:: Revise la estructura del archivo js, en la función `window.onload <#mostrar-filtro>`_ :octicon:`report;1em;sd-text-info` y lea los comentarios de la línea 36.

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: html
            :linenos:
            :emphasize-lines: 2

            <!-- Session -->
            <div class="row inicio_ses" id="inicio_ses">
                <div class="errorLogin" id="errorLog"></div>
                <!-- Login -->
                <div class="control">
                    <div class="renglon">
                        <h3>Usuario: </h3>
                        <input class="form-control ds-input" id="user" name="user" value="">
                    </div>
                    <div class="renglon">
                        <h3>Contraseña: </h3>
                        <input class="form-control ds-input" type="password" id="pass" name="pass" value="">
                    </div>
                    <!-- Botones -->
                    <div class="controlBtn">
                        <div class="btn btn-primary" onclick="login()">Login</div>
                        <div class="btn btn-primary" onclick="reset()">Reset</div>
                    </div>
                </div>
            </div>

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes14.png

El bloque ``title Demo``, es simplemente el título que diferencia al reporte, indicando que es solo un ``reporte demo``. 

.. seealso:: Consulte :ref:`link-demo` :octicon:`report;1em;sd-text-info`.

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: html
            :linenos:
            :emphasize-lines: 4

            <!--Title Demo -->
            <div id="title_demo" style="margin-bottom: 20px;">
                <center>
                    <h1><span>Demo data</span>&nbsp;&nbsp;</h1>
                </center>
            </div>

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes30.png

``Options Filter`` es el botón que permite habilitar u ocultar los filtros disponibles, así como la opción ``Run`` para ejecutar la consulta.

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: html
            :linenos:
            :emphasize-lines: 3, 4, 5, 6

            <!--Options FIlter -->
            <div class="col-sm-12 col-md-12 col-lg-12 row" id="divOptions">
                <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#firstParameters" aria-expanded="false" aria-controls="collapseExample" id="buttonFilter">
                    <i class="fa-solid fa-filter"></i>
                </button >  &nbsp;  &nbsp;
                <div class="btn btn-primary" onclick="runFirstElement()">Run</div>
            </div>

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes15.png

.. attention:: Tenga en cuenta que este botón NO funciona si está accediendo con la ``URL local con datos demo``, para ello debe complementar la ``URL`` con el ``id_script``. Consulte :ref:`url-acceso` :octicon:`report;1em;sd-text-info`.

El contenido ``Filters`` son las opciones de filtros para tratar la información, siendo las más comunes las ``Fechas Desde`` y ``Fecha Hasta``. 

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: html
            :linenos:
            :emphasize-lines: 16-21

            <!-- Filters -->
            <div id="firstParameters" class="collapse row show">
                <!-- Filtro uno -->
                <div class="col-sm-12 col-md-3 col-lg-3">
                    <h5>Fecha Desde: </h5>
                    <input class="form-control ds-input" type="date" id="date_from" name="date_from">
                </div>

                <!-- Filtro dos -->
                <div class="col-sm-12 col-md-3 col-lg-3">
                    <h5>Fecha Hasta: </h5>
                    <input class="form-control ds-input" type="date" id="date_to" name="date_to">
                </div>

                <!-- Filtro tres -->
                <div class="col-sm-12 col-md-3 col-lg-3" >
                    <h5>Promotor: </h5>
                    <select class="form-control mdb-select md-form" id="promotor">
                        <option value="">--Seleccione--</option>
                    </select>
                </div>
            </div>

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes12.png

Modifique los filtros según sus necesidades. Añada o elimine filtros según sea necesario; estos pueden ser filtros de fecha, rango, opciones, etc.

.. note:: En el ejemplo anterior, hay una tercera opción de filtro llamada ``Promotor`` (líneas 16-21). Solamente asegúrese de asignar un ``id`` descriptivo al elemento. El ``id firstParameters`` es utilizado para mostrar todos los filtros. Consulte la función `window.load <#mostrar-filtro>`_ :octicon:`report;1em;sd-text-info` para conocer más detalles. 

En el bloque ``Content``, se incluyen elementos del reporte como tablas, gráficos, cards, o cualquier otro elemento donde se representará la data.

.. note:: Todo elemento que se incluya debe estar dentro del contenedor ``div`` con la clase ``row`` (Líneas 2-14). 

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: html
            :linenos:
            :emphasize-lines: 2, 7-8, 10, 12, 14

            <!--Content -->
            <div class="row" style="margin-top:20px;"  id="divContent">
                <!--Primer Elemento -->
                <div class="col-sm-12 col-md-12 col-lg-12" style="align-items: center;overflow-y: scroll;">
                    <section class="title_tables">
                        <h3><span>Recepción Visitas</span>&nbsp;&nbsp;
                            <button class="btn btn-primary" id="download_csv_firstElement"><i class="fa-solid fa-file-csv"></i></button>
                            <button class="btn btn-success" id="download_xlsx_firstElement"><i class="fa-regular fa-file-excel"></i></button>
                        </h3>
                        <hr class="hrFirstElement">
                    </section>
                    <div id="firstElement" ></div>
                </div>
            </div>

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes13.png

El bloque de código anterior corresponde a las opciones de descarga (``csv`` y ``xls``) de la información de una tabla. Estas funcionalidades son proporcionadas por la biblioteca |Tabulator| :octicon:`report;1em;sd-text-info`.

.. seealso:: Consulte la documentación oficial de |Tabulator-doc| :octicon:`report;1em;sd-text-info`. 

Puede modificar o añadir otras funcionalidades según su necesidad. Sin embargo, identifique y tenga precaución con el uso del atributo ``id`` (Líneas 7-8), ya que son utilizados por la biblioteca ``Tabulator`` para poblar con datos.

.. warning:: El  código anterior para una tabla ya se encuentra estandarizada. Si necesita otra tabla, simplemente copie y pegue. Solo asegúrese de cambiar el ``id`` (Líneas 7, 8, 10, 12) por ``firstElement``, ``secondElement`` y así sucesivamente.
  
.. dropdown:: Código content

    .. code-block:: html
        :caption: Header
        :linenos:
        :emphasize-lines: 20

        <!-- Content -->
        <div style="width:100%">
            <div class="app" id="appCont" style="padding-top: 0px;">

                <!--Session -->
                <div class="row inicio_ses" id="inicio_ses">
                    <div class="errorLogin" id="errorLog"></div>
                    <div class="control">
                        <div class="renglon">
                            <h3>Usuario: </h3>
                            <input class="form-control ds-input" id="user" name="user" value="">
                        </div>
                        <div class="renglon">
                            <h3>Contraseña: </h3>
                            <input class="form-control ds-input" type="password" id="pass" name="pass" value="">
                        </div>
                        <div class="controlBtn">
                        <div class="btn btn-primary" onclick="login()">Login</div>
                        <div class="btn btn-primary" onclick="reset()">Reset</div>
                        </div>
                    </div>
                </div>

                <!--Title Demo -->
                <div id="title_demo" style="margin-bottom: 20px;">
                    <center>
                        <h1><span>Demo data</span>&nbsp;&nbsp;</h1>
                    </center>
                </div>

                <!--Options FIlter -->
                <div class="col-sm-12 col-md-12 col-lg-12 row" id="divOptions">
                    <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#firstParameters" aria-expanded="false" aria-controls="collapseExample" id="buttonFilter">
                        <i class="fa-solid fa-filter"></i>
                    </button >  &nbsp;  &nbsp;
                    <div class="btn btn-primary" onclick="runFirstElement()" >Run</div>
                </div>

                <!--Filters -->
                <div id="firstParameters" class="collapse row show">
                    <div class="col-sm-12 col-md-3 col-lg-3">
                        <h5>Fecha Desde: </h5>
                        <input class="form-control ds-input" type="date" id="date_from" name="date_from">
                    </div>
                    <div class="col-sm-12 col-md-3 col-lg-3">
                        <h5>Fecha Hasta: </h5>
                        <input class="form-control ds-input" type="date" id="date_to" name="date_to">
                    </div>

                    <div class="col-sm-12 col-md-3 col-lg-3" >
                        <h5>Promotor: </h5>
                        <select class="form-control mdb-select md-form" id="promotor">
                            <option value="">--Seleccione--</option>
                        </select>
                    </div>
                </div>

                <!--Content -->
                <div class="row" style="margin-top:20px;"  id="divContent">
                    <!--Primer Elemento -->
                    <div class="col-sm-12 col-md-12 col-lg-12" style="align-items: center;overflow-y: scroll;">
                        <section class="title_tables">
                            <h3><span>Recepción Visitas</span>&nbsp;&nbsp;
                                <button class="btn btn-primary" id="download_csv_firstElement"><i class="fa-solid fa-file-csv"></i></button>
                                <button class="btn btn-success" id="download_xlsx_firstElement"><i class="fa-regular fa-file-excel"></i></button>
                            </h3>
                            <hr class="hrFirstElement">
                        </section>
                        <div id="firstElement" ></div>
                    </div>
                </div>
            </div>
        </div>

Librerías
^^^^^^^^^

Este bloque se localiza en la sección final de la etiqueta ``body``, donde se especifican las rutas de los archivos JavaScript para las bibliotecas utilizadas en las funcionalidades del reporte. Entre estas bibliotecas se incluyen ``Tabulator``, ``Chart.js``, ``jQuery``, ``Bootstrap``, ``Select2``, así como los ``Utils`` de Linkaform y ``Servido``. Además, se especifica la ubicación de los archivos JavaScript encargados de procesar y mostrar la información. 

.. note:: Los ``Utils`` son funciones propias de Linkaform, que se emplean para ciertas tareas como descargas de gráficos, imágenes, enviar peticiones al backend, entre otras.

Para acceder a las bibliotecas, se utiliza tanto la opción del ``CDN`` como la ``URL`` correspondiente. Dado que ``Servido`` se encuentra alojado en un contenedor ``Docker``, se opta por referenciar las versiones alojadas en los servidores del ``CDN`` en lugar de descargar los recursos directamente desde el servidor local. Esta elección se debe a que realizar *builds* cada vez que se actualizan las bibliotecas y ejecutar las versiones |minificadas| :octicon:`report;1em;sd-text-info` resultaría más pesado en comparación con mantener enlaces directos a las versiones actuales de las bibliotecas.

.. warning:: Una desventaja al hacer referencia a bibliotecas almacenadas en ``CDNs`` es la posibilidad de que dichas bibliotecas experimenten fallas debido a interrupciones en el servicio del ``CDN`` provocando acciones inesperadas en los reportes.

Regularmente, los *links* no cambian, a excepción de la llamada de sus ``archivos JS`` ubicados al final del documento.

.. code-block:: html
    :linenos:

    <!-- TABULATOR -->
    <script type="text/javascript" src="https://oss.sheetjs.com/sheetjs/xlsx.full.min.js"></script>

    <!-- tabulator : PDF Downlowd-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.20/jspdf.plugin.autotable.min.js"></script>
    <link href="https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css" rel="stylesheet">
    <script type="text/javascript" src="https://unpkg.com/tabulator-tables/dist/js/tabulator.min.js"></script>
    
    <!-- chartjs -->
    <script type="text/javascript" src=" https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-datalabels/2.0.0/chartjs-plugin-datalabels.min.js" integrity="sha512-R/QOHLpV1Ggq22vfDAWYOaMd5RopHrJNMxi8/lJu8Oihwi4Ho4BRFeiMiCefn9rasajKjnx9/fTQ/xkWnkDACg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script type="text/javascript" src="https://unpkg.com/chart.js-plugin-labels-dv/dist/chartjs-plugin-labels.min.js"></script>

    <!-- Jquery -->
    <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>

    <!-- Bootstrap -->
    <script src="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap4-toggle@3.6.1/js/bootstrap4-toggle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>

A excepción de ``utils``, aquí se encuentran algunas librerías minificadas, como ``chroma``, que permite crear paletas de colores automáticamente, útil cuando se necesitan ciertos colores para gráficos. Además, la librería ``sweetalert2`` permite crear alertas atractivas y personalizadas.

.. code-block:: html
    :linenos:

    <script type="text/javascript" src="../styles/js/chroma.min.js"></script>
    <script type="text/javascript" src="../styles/js/sweetalert2.all.min.js"></script>

También se encuentran archivos propios de ``Servido``, correspondientes a las funciones API.

.. code-block:: html
    :linenos:

    <script type="text/javascript" src="../utils/lkf_utils.js"></script>
    <script type="text/javascript" src="../utils/servido_utils.js"></script>

El bloque de código anterior importa el archivo ``servido_utils.js``, que se encarga de configurar el inicio de sesión, gestionar usuarios, contraseñas y configurar las cookies con información sensible como ``sessionId``, ``userId``, ``userJwt``, ``userName`` y ``userParentId``. Además, proporciona funciones útiles como ``getPalleteColors``, ``setSpinner``, ``getChartDownload``, ``getDownload``, ``setDateFilterMonth``.

En el último bloque, se llaman a los archivos encargados de gestionar el reporte y el archivo con la *data ficticia* que se verá reflejada en las gráficas, tablas, u algún otro elemento que haya asignado.

.. code-block:: html
    :linenos:

    <script type="text/javascript" src="./reporte_visitas.js"></script>
    <script type="text/javascript" src="./reporte_visitas_data.js"></script>

En la siguiente pestaña desplegable, encontrará el código de un archivo HTML.  

.. note:: Por favor, considere leer los comentarios dentro del código para comprender los elementos.

.. dropdown:: Código completo archivo HTML

    .. code-block:: html
        :linenos:

        <!DOCTYPE html>
        <html lang="en" dir="ltr">
        <head>
            <!-- Metadatos y configuraciones iniciales -->
            <meta charset="utf-8">
            <title>Servido</title>
            <meta name="title" content="Servido">
            <meta name="description" content="Reporte Visitas">
            <!-- Icono de la página -->
            <link type="image/x-icon" rel="shortcut icon" href="../styles/img/favicon.ico">
            <!-- Configuración de la vista en dispositivos -->
            <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1, maximum-scale=1">

            <!-- Enlaces a bibliotecas externas (CDN) -->
            <link type="image/x-icon" rel="shortcut icon" href="../styles/img/favicon.ico">
            <!--Bootstrap -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <!--Font Awesome -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <!-- Utils -->        
            <link rel="stylesheet" href="../styles/css/sweetalert2.min.css">
            <link rel="stylesheet" href="../styles/css/styles.css">
            <link rel="stylesheet" href="style.css">
        </head>
        <body>
            <!-- Header (Barra de navegación) -->
            <nav class="navbar header">
                <div class="navbar-brand">
                    <div class="row">
                        <!-- Logo -->
                        <div class="col-md-6">
                            <a href="index.html">
                                <div class="logo_marca">
                                    <img src="https://app.linkaform.com/img/login-linkaform-logo.png" alt="LinkaForm" id="image_log">
                                </div>
                            </a>
                        </div>
                        <!-- Opción para cerrar sesión -->
                        <div class="col-md-6">
                            <div class="container">
                                <div class="back"  id="atras"><i class="fa fa-solid fa-arrow-left"></i>Atrás</div>
                                <div class="close" id="close_sesion"><a onclick="closeSession();"><i class="fa-solid fa-lock"></i>Cerrar Sesión</a></div>
                            </div>
                        </div>
                    </div>
                    <!-- Nombre del reporte (cambiar) -->
                    <div class="col-md-12">
                        <h1 id="title_report">Reporte Visitas</h1>
                    </div>
                </div> 
            </nav>

            <!-- Estilo de carga (Loading) -->
            <div class="loading-container">
                <div class="spinner-border text-primary" role="status">
                    <span class="sr-only">Loading...</span>
                </div>
            </div>

            <!-- Contenido principal -->
            <div style="width:100%">
                <div class="app" id="appCont" style="padding-top: 0px;">
                    <!-- Inicio de sesión -->
                    <div class="row inicio_ses" id="inicio_ses">
                        <!-- Formulario de inicio de sesión -->
                        <div class="errorLogin" id="errorLog"></div>
                        <div class="control">
                            <div class="renglon">
                                <h3>Usuario: </h3>
                                <input class="form-control ds-input" id="user" name="user" value="">
                            </div>
                            <div class="renglon">
                                <h3>Contraseña: </h3>
                                <input class="form-control ds-input" type="password" id="pass" name="pass" value="">
                            </div>
                            <!-- Botones -->
                            <div class="controlBtn">
                                <div class="btn btn-primary" onclick="login()">Login</div>
                                <div class="btn btn-primary" onclick="reset()">Reset</div>
                            </div>
                        </div>
                    </div>

                    <!-- Título de demo -->
                    <div id="title_demo" style="margin-bottom: 20px;">
                        <center>
                            <h1><span>Demo data</span>&nbsp;&nbsp;</h1>
                        </center>
                    </div>

                    <!-- Opciones de filtro -->
                    <div class="col-sm-12 col-md-12 col-lg-12 row" id="divOptions">
                        <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#firstParameters" aria-expanded="false" aria-controls="collapseExample" id="buttonFilter">
                            <i class="fa-solid fa-filter"></i>
                        </button >  &nbsp;  &nbsp;
                        <div class="btn btn-primary" onclick="runFirstElement()" >Run</div>
                    </div>

                    <!-- Filtros -->
                    <div id="firstParameters" class="collapse row show">
                        <div class="col-sm-12 col-md-3 col-lg-3">
                            <h5>Fecha Desde: </h5>
                            <input class="form-control ds-input" type="date" id="date_from" name="date_from">
                        </div>
                        <div class="col-sm-12 col-md-3 col-lg-3">
                            <h5>Fecha Hasta: </h5>
                            <input class="form-control ds-input" type="date" id="date_to" name="date_to">
                        </div>

                        <div class="col-sm-12 col-md-3 col-lg-3" >
                            <h5>Promotor: </h5>
                            <select class="form-control mdb-select md-form" id="promotor">
                                <option value="">--Seleccione--</option>
                            </select>
                        </div>
                    </div>

                    <!-- Elementos del contenido (Tablas, gráficas, etc.) -->
                    <div class="row" style="margin-top:20px;"  id="divContent">
                        <!--Primer Elemento -->
                        <div class="col-sm-12 col-md-12 col-lg-12" style="align-items: center;overflow-y: scroll;">
                            <section class="title_tables">
                                <h3><span>Recepción Visitas</span>&nbsp;&nbsp;
                                    <button class="btn btn-primary" id="download_csv_firstElement"><i class="fa-solid fa-file-csv"></i></button>
                                    <button class="btn btn-success" id="download_xlsx_firstElement"><i class="fa-regular fa-file-excel"></i></button>
                                </h3>
                                <hr class="hrFirstElement">
                            </section>
                            <div id="firstElement" ></div>
                        </div>
                    </div>
                </div>
            </div>
        </body>

        <!-- Bibliotecas JavaScript -->

        <!-- TABULATOR -->
        <script type="text/javascript" src="https://oss.sheetjs.com/sheetjs/xlsx.full.min.js"></script>

        <!-- PDF Download para Tabulator -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.4.0/jspdf.umd.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.5.20/jspdf.plugin.autotable.min.js"></script>
        <link href="https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css" rel="stylesheet">
        <script type="text/javascript" src="https://unpkg.com/tabulator-tables/dist/js/tabulator.min.js"></script>
        
        <!-- chartjs -->
        <script type="text/javascript" src=" https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.1/chart.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/chartjs-plugin-datalabels/2.0.0/chartjs-plugin-datalabels.min.js" integrity="sha512-R/QOHLpV1Ggq22vfDAWYOaMd5RopHrJNMxi8/lJu8Oihwi4Ho4BRFeiMiCefn9rasajKjnx9/fTQ/xkWnkDACg==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script type="text/javascript" src="https://unpkg.com/chart.js-plugin-labels-dv/dist/chartjs-plugin-labels.min.js"></script>

        <!-- Jquery -->
        <script src="https://code.jquery.com/jquery-3.6.0.js" integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk=" crossorigin="anonymous"></script>

        <!-- Bootstrap -->
        <script src="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap4-toggle@3.6.1/js/bootstrap4-toggle.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>

        <!-- Bibliotecas y utilidades personalizadas -->
        <script type="text/javascript" src="../styles/js/chroma.min.js"></script>
        <script type="text/javascript" src="../styles/js/sweetalert2.all.min.js"></script>

        <script type="text/javascript" src="../utils/lkf_utils.js"></script>
        <script type="text/javascript" src="../utils/servido_utils.js"></script>

        <!-- Template -->
        <script type="text/javascript" src="./reporte_visitas.js"></script>
        <script type="text/javascript" src="./reporte_visitas_data.js"></script>
        </html>


.. _estructura-js:

Estructura js
-------------

El archivo ``js`` en ``Servido`` contiene la lógica encargada de gestionar las solicitudes a la *API de Linkaform*, así como de procesar y presentar la información correspondiente en la estructura establecida.

Observe el siguiente bloque de código, el cual representa de manera general las variables y funciones principales que componen al archivo ``js``. Sin embargo, en contenido posterior podrá encontrar detalles sobre las funciones más relevantes, resaltando los elementos que puede personalizar. Por favor, vaya comparando los ``IDs`` y ``clases`` usadas con el archivo HTML para comprender el funcionamiento.

.. note:: Regularmente, las variables y funciones que no tienen ningún comentario como título contienen código genérico que rara vez se modifica; por lo tanto, se mantienen sin cambios.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 19, 22, 30, 34, 38, 41, 45, 49

    let us = null;
    let usTy = null;
    let jw = null;
    let userId = null;
    let userJwt = null;
    let userName = null;
    let userParentId = null;
    let scriptId = null;

    $('#divOptions').hide();
    $('#title_report').hide();
    $('.title_tables').hide();
    hideElement("title_demo");
    hideElement("firstParameters");
    hideElement("firstElement");
    hideElement("secondElement");
    hideElement("thirdElement");

    window.onload = function(){ ...
    }

    function unHideReportElements(){ ...
    }

    const loading = document.querySelector('.loading-container');
    loading.style.display = 'none';

    //-----DEMO 
    function loadDemoData(){ ...
    }

    //-----DATE
    function setDate(){ ...
    }

    //-----EXCUTION
    function runFirstElement(){ ...
    }

    function getFirstElement(dateTo, dateFrom, promotor){ ...
    }

    //-----TABLES
    function getDrawTable(id, columnsData, tableData, height = 500){ ...
    }

    //-----CATALOG
    function get_catalog(){ ...
    };

Las siguientes variables globales, pertenecientes a la cuenta que ingrese al reporte y que son parte de la *cookie*, se utilizan en el archivo ``servido_utils``.

.. caution:: Las variables no se modifican. 

.. code-block:: javascript
    :linenos:

    let us = null;
    let usTy = null;
    let jw = null;
    let userId = null;
    let userJwt = null; //Token del usuario
    let userName = null;
    let userParentId = null; //Id de la cuenta padre
    let scriptId = null; //Script del reporte

El siguiente bloque de código corresponde a métodos de ``jQuery``,  se utiliza para manipular el *DOM* de la página. Específicamente, oculta varios elementos visuales antes de cualquier interacción con el reporte. Lo hace tanto por su identificador único (ID) como por su clase. Por favor, revise los comentarios dentro del código.

.. code-block:: javascript
    :linenos:

    $('#divOptions').hide(); // Oculta el elemento con ID "divOptions"
    $('#title_report').hide(); // Oculta el elemento con ID "title_report"
    $('.title_tables').hide(); // Oculta todos los elementos con la clase "title_tables"

    // Llama a la función para ocultar elementos con IDs específicos
    hideElement("title_demo");
    hideElement("firstParameters");
    hideElement("firstElement");
    hideElement("secondElement");
    hideElement("thirdElement");

.. _funcion-window-onload:

Función ``window.onload``
^^^^^^^^^^^^^^^^^^^^^^^^^

La función ``window.onload()`` se activa siempre que la pantalla se carga por completo. Además, procesa los parámetros de la ``URL`` para actualizar los elementos del reporte en función a esos parámetros. También se encarga de manipular el contenido de los filtros mediante el ``ID`` de los elementos.

En las líneas 6-8, verifica si la ``clave (key)`` recibida es igual a ``script_id``, es decir, lo que se recibe como parámetro de la ``URL``. 

.. seealso::

    Consulte la sección **URLs de acceso**, específicamente en la de :ref:`link-servido` :octicon:`report;1em;sd-text-info`.
    
    Revise la configuración del reporte en la sección :ref:`config-reporte` :octicon:`report;1em;sd-text-info`.

De manera similar, en las líneas 10-13, verifica si se está accediendo al entorno de pruebas para apuntar y acceder a los valores de preproducción. 

.. seealso::

    Consulte: :ref:`link-env` :octicon:`report;1em;sd-text-info`.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 6-8, 10-13
        
    window.onload = function(){ // Esta función se ejecutará cuando la ventana haya cargado completamente.
    var qs = urlParamstoJson(); // Obtiene los parámetros de la URL y los convierte en un objeto.
    var formNode = document.getElementById("appCont"); // Obtiene el elemento del DOM del contenido de "inicio de sesión".
        for(var key in qs){ // Recorre los parámetros de la URL.
        // Verifica si el parámetro es "script_id" y lo convierte en un entero.
        if (key === 'script_id' ){
        scriptId = parseInt(qs[key]);
        }
         // Verifica si el parámetro es "env" y establece la URL en función del valor.
        if (key === 'env') {
        if (qs[key] === 'test'){
            url = "https://preprod.linkaform.com/api/"; // Establece la URL de la API en modo de prueba. 
        }
        }
        // Verifica si el parámetro es "title" y establece el texto del elemento con el ID "title_report" que es el título del reporte.
        if (key ==='title'){
        $("#title_report").text(qs[key]);
        }
            var elements = getAllElementsWithAttribute(formNode, 'data-infosync-id', key); // Obtiene todos los elementos con el atributo 'data-infosync-id' igual a 'key'.
            var value = decodeURI(qs[key]); // Decodifica el valor del parámetro.
         // Si el parámetro es 'infosyncRecordID', establece su valor en un elemento con el mismo ID.
        if (key === 'infosyncRecordID'){
        var recId = document.getElementById("infosyncRecordID");
        recId.value = value;
        }
            else if(elements.length > 0){
                // Si existen elementos con el atributo 'data-infosync-id', actualiza sus valores según el tipo de elemento del filtro.
                switch(elements[0].type){
                    case 'text':
                        elements[0].value = value;
                        break;
                    case 'textarea':
                        elements[0].value = value;
                        break;
                    case 'select-one':
                        elements[0].value = value;
                        break;
                    case 'radio':
                        for(var idx in elements){
                            if(elements[idx].value === value){
                                elements[idx].checked = true;
                            }
                        }
                        break;
                    case 'checkbox':
                        var values = value.split(';');
                        for(var idx in elements){
                            if(values.indexOf(elements[idx].value) !== -1){
                                elements[idx].checked = true;
                            }
                        }
                        break;
                }
            }
        }

.. _mostrar-filtro:

Continuando con la función ``window.onload`` de forma general, la condicional (línea 11) verifica si se ha iniciado sesión. El parámetro ``us`` corresponde al ``ID del usuario`` (línea 2), el parámetro ``jw`` al ``token del usuario`` (línea 3). 

Si el parámetro ``scriptId`` es *nulo*, el entorno se configurará como ``demo``. Si la condición se cumple, se ejecutan otras acciones. Revise los comentarios dentro del código para comprender el flujo.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 2, 3, 11

    // Obtiene valores de cookies y almacena en variables.
    us = getCookie("userId");
    jw = getCookie("userJwt");
    userParentId = getCookie("userParentId");

    // Oculta elementos con los IDs "close_sesion" y "firstParameters".
    hideElement("close_sesion");
    hideElement("firstParameters");

    // Verifica si las cookies "userId" y "userJwt" no están vacías o si "scriptId" es nulo.
    if(us != "" && jw != "" || scriptId===null){
        hideElement("inicio_ses"); // Oculta el inicio de sesión porque ya hay una sesión activa.
        unhideElement("close_sesion"); // Muestra el botón "cerrar sesión" que aparece en la parte superior derecha.
        getCompanyLogo(userParentId); // Obtiene el logo de la empresa según el "userParentId".

        // Asigna valores a variables globales.
        userId = us;
        userJwt = jw;
        userName = getCookie("userName"); //Obtiene el nombre del usuario a través de la cookie.
        document.getElementById("firstParameters").style.removeProperty('display');  // Restablece la propiedad "display" del elemento con los filtros del reporte "id firstParameters" (lo muestra).
        unHideReportElements() // Muestra elementos del reporte (llama a una función "unHideReportElements" ubicada en código posterior).

        // Si "scriptId" es nulo, carga datos de la demo y ejecuta la función correspondiente de loadDemoData.
        if (scriptId == null) {
        loadDemoData(); // Ejecuta la función "loadDemoData()". Podrá encontrar la explicación en contenido posterior.
        }
        //--Styles
        setSpinner(); // Carga la animación de spinner cuando se carga la data.
        setDate(); // Ejecuta la función "setDate()". Podrá encontrar la explicación en contenido posterior.
        get_catalog(); // Ejecuta la función "get_catalog()". Podrá encontrar la explicación en contenido posterior.
        $('#divOptions').show(); // Muestra las opciones de filtro.
        $('#title_report').show(); // Muestra el título del reporte.
        document.getElementById("firstParameters").style.removeProperty('display');
        
    } else {
        // Si las condiciones anteriores no se cumplen, muestra el elemento con el ID "inicio_ses" que es el formulario para la autenticación.
        unhideElement("inicio_ses");

        // Oculta varios elementos, incluyendo "divContent", "divOptions", "title_report" y elementos con la clase "title_tables".
        $('#divContent').hide(); // Elementos que se utilizan para representar la data de las formas (Tablas, gráficos, etc.).
        $('#divOptions').hide(); // Botones opciones de filtro.
        $('#title_report').hide(); // Título del reporte.
        $('.title_tables').hide(); // Títulos de las tablas (NOTA: Este elemento corresponde a una tabla, en caso de algún otro elemento deberá colocarlo aquí).
        hideElement("firstElement-Buttons");
    }
    ///-----HIDE AND SHOW
    for(var key in qs){ // Recorre los parámetros de la URL.
        // Si el parámetro es "embed" y tiene un valor, oculta los elementos con los IDs "close_sesion" (opción para cerrar sesión, ubicada en la parte superior derecha) y "image_log".
        if (key === 'embed'){
        if (qs[key]){
            $("#close_sesion").hide();
            $("#image_log").hide();
        }
        }
    }
    }

Función ``unHideReportElements``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La siguiente función ``unHideReportElements()`` se encarga de mostrar los elementos específicos en la página que son necesarios para el reporte al iniciar sesión. Lea los comentarios.

.. attention:: Configure aquí todos los elementos del reporte que deben mostrarse al iniciar sesión.

.. code-block:: javascript
    :linenos:

    function unHideReportElements(){

    unhideElement("firstElement-Buttons"); // Botones opciones de filtro. 
    unhideElement("firstParameters"); // Filtros.
    unhideElement("close_sesion"); // Opción para cerrar sesión.
    }

    // La variable "loading" almacena el primer elemento con la clase "loading-container" (spinner).
    const loading = document.querySelector('.loading-container');

    // Oculta visualmente el elemento seleccionado estableciendo su propiedad de estilo 'display' en 'none'.
    loading.style.display = 'none';

Función ``loadDemoData``
^^^^^^^^^^^^^^^^^^^^^^^^

La función ``loadDemoData()`` está diseñada para cargar datos de demostración y otros elementos como tablas y gráficos en el reporte.

.. attention:: Esta es una de las funciones más importantes que debe adaptar. Continuando con el ejemplo del reporte que hemos seguido desde el principio, encontrará únicamente el código correspondiente a una tabla dentro del siguiente bloque de código. Sin embargo, después de este bloque, verá un ejemplo en caso de incluir algún otro elemento como gráficos.

Observe que en la línea 11 se llama a la función ``getDrawTable``, la cual se utiliza para para obtener datos y elementos de una tabla, enviando los siguientes cuatro parámetros:

- **firstElement**: Es el ``ID`` del div donde se necesita colocar la tabla.
- **columsTable1**: Variable que contiene un array de objetos que representan las columnas de la tabla (biblioteca de tablas Tabulator).

.. seealso:: Consulte el archivo data.js, donde está ubicada la variable mencionada anteriormente.

- **dataTable1**: Variable que contiene un array de objetos que representan los datos de la tabla. Recuerde que, dado que es un reporte demo, se llena con información ficticia que no se extrae de la base de datos con registros reales.

.. seealso:: Consulte el archivo data.js, donde está ubicada la variable que se mencionó anteriormente. 

- **350**: Es la altura máxima en píxeles que medirá la tabla.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 11

    //-----DEMO 
    // Detecta si el entorno es la demo, en caso de serlo muestra ciertos elementos pertenecientes al mismo.
    function loadDemoData(){ 
    $('.title_tables').show();// Muestra todos los elementos con la clase "title_tables". En este caso, el titulo de la o las tablas (dependiendo de cuantas tablas haya establecido).
    unhideElement("title_demo")// Muestra el elemento con la clase "title_demo". En este caso, coloca "Demo data" debajo del titulo del reporte para indicar que es un reporte de demostración.
    
    // Restablece la propiedad "display" (eliminar la propiedad display del estilo del elemento) para mostrar y permitir que el elemento con el ID "firstParameters" (opciones y botones de filtros) force a la regla de estilo predeterminada o hojas de estilo externas a abarcar todo el espacio de la página.
    document.getElementById("firstParameters").style.removeProperty('display');

    // Llama a la función "getDrawTable" para obtener y mostrar una tabla.
    getDrawTable('firstElement', columsTable1, dataTable1, 350);
    // Restablece la propiedad "display" (eliminar la propiedad display del estilo del elemento) para mostrar y permitir que el elemento con el ID "firstElement" (tabla) force a abarcar todo el espacio de la página.
    document.getElementById("firstElement").style.removeProperty('display');
    }

Función ``setDate``
^^^^^^^^^^^^^^^^^^^

La función ``setDate()`` está diseñada para establecer valores iniciales en los filtros de tipo fecha del reporte. Estos son los inputs con los IDs ``date_to`` y ``date_from`` que existen en la estructura de los filtros establecidos en el archivo HTML. Lea los comentarios del código. 

.. code-block:: javascript
    :linenos:

    //-----DATE
    function setDate(){ // Función para establecer valores predeterminados en campos de fecha
    // Array de representaciones de dos dígitos de los 12 meses del año
    array_month = ['01','02','03','04','05','06','07','08','09','10','11','12']; 

    //---DATE TO
    // Obtiene fecha actual como fecha final del filtro hasta (date_to)
    date_to = new Date();
    year = date_to.getFullYear();
    month = array_month[date_to.getMonth()];
    day = date_to.getDate();
    date_to = year +'-'+ month +'-'+ day;
    $('#date_to').val(date_to); // Establece el valor en el campo de fecha final

    //---DATE FROM
    // Obtiene fecha actual menos 30 días como fecha de inicio (date_from)
    date_from = new Date();
    date_from.setDate(date_from.getDate() - 30)

    year = date_from.getFullYear();
    month = array_month[date_from.getMonth()];
    day = date_from.getDate();
    date_from = year +'-'+ month +'-'+ day;
    $('#date_from').val(date_from);// Establece el valor en el campo de fecha de inicio
    }

Función ``get_catalog``
^^^^^^^^^^^^^^^^^^^^^^^

La función ``get_catalog()`` se encarga de realizar una petición (puede ser a producción o a preproducción dependiendo del parámetro que contenga en la ``URL``, línea 5) para traer la data única de un catálogo. Por favor, lea detenidamente los comentarios.

.. caution:: La siguiente función está diseñada para realizar una petición para el selector ``Promotor`` (filtro) correspondiente a un catálogo. Puede usarla como referencia en caso de que necesite extraer información para un filtro de un catalogo. Consulte la sección :ref:`catalogo` :octicon:`report;1em;sd-text-info` para más detalles.

.. seealso:: Revise el código del script en ``infosync_scripts`` que detalla más a cerca del ``option: 0`` ubicado en la línea 9. (FALTA REFERENCIAA)

Cada usuario que inicia sesión en su cuenta tiene un token (``Jwt``) línea 13, el cual se envía en la petición del ``script``. Si el usuario tiene acceso al ``script``, ya sea porque se le compartió o pertenece al grupo de la cuenta padre, podrá ejecutarlo. En caso contrario, se le indicará a través de un mensaje que no tiene acceso y se le sugerirá iniciar sesión.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 5, 9, 13

    //-----CATALOG
    // Función para obtener datos de un catálogo a través de una solicitud fetch
    function get_catalog(){ 
    // Realiza una solicitud fetch usando el método POST
    fetch(url + 'infosync/scripts/run/', {
        method: 'POST',
        body: JSON.stringify({ // Convierte a un JSON
            script_id: 95556, // Id del script al que debe apuntar
            option: 0, // Determina que consulta debe realizar, en este caso 0 le indica que debe realizar una consulta a un catalogo, en el caso de que fuera 1 seria una petición normal a la forma. 
        }),
        headers:{
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+userJwt
        },
        })
        // Procesa la respuesta en formato JSON
        .then(res => res.json())
        .then(res => {
        // Verifica si la petición fue exitosa (success = true)
        if (res.success) {
            // Verifica si hay elementos en el catálogo devuelto
            if (res.response.catalog.length){
            array_value = []
            // Itera sobre los elementos del catálogo para extraer valores únicos
            for (i = 0; i < res.response.catalog.length; i++) {
                if (!array_value.includes(res.response.catalog[i]['63dc0f1ec29b8336b7b72615'])) {
                array_value.push(res.response.catalog[i]['63dc0f1ec29b8336b7b72615'])
                }
            }
            // Ordena los valores únicos en el array
            array_value.sort();
            // Limpia y actualiza un elemento del DOM (select con ID "promotor" (filtro))
            $("#promotor").empty();
            $('#promotor').append('<option value="--">--Seleccione--</option>');
            // Itera sobre los valores únicos y agregar opciones al elemento "promotor"
            for (i = 0; i <array_value.length; i++) {
                $('#promotor').append('<option value="'+ array_value[i] +'">'+array_value[i]+'</option>');
            }
        }
    }

Función ``runFirstElement``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

La función ``runFirstElement()`` se ejecuta cuando se presiona el botón ``Run`` de los filtros. Obtiene las referencias de los filtros para validar que no estén vacíos (línea 10) y poder traer la data correspondiente (línea 12). Por favor, continue leyendo los comentarios dentro del código.

.. attention:: Ajuste esta función de acuerdo a los filtros que necesite. En este caso, los campos (filtros) son de fechas y promotores. Si no están vacíos y están completos, llama a la función `getFirstElement <#funcion-getFirstElement>`_ :octicon:`report;1em;sd-text-info` con los valores de fecha y promotor. Si los campos de fecha están vacíos, muestra una alerta visual utilizando la biblioteca Swal (|sweetalert2| :octicon:`report;1em;sd-text-info`), solicitando al usuario que ingrese un rango de fechas antes de continuar.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 10, 12

    //-----EXCUTION
    // Se encarga de gestionar los filtros existentes, toma los valores de "date_to" (de esta fecha) y "date_from" (a esta fecha) y las almacena en las variables.
    function runFirstElement(){
    // Obtiene referencias a los elementos HTML con los IDs "date_from" y "date_to".
    let date_from = document.getElementById("date_from");
    let date_to = document.getElementById("date_to");  
    let promotor = document.getElementById("promotor");  

    // Verifica si los campos de fecha no están vacíos.
    if (date_from.value != null && date_to.value != null && date_from.value != "" && date_to.value != ""){
        // Si los campos no están vacíos, llama a la función getFirstElement con los valores de fecha y promotor
        getFirstElement(date_to.value, date_from.value, promotor.value);
    }
    else
    {
        // Muestra un mensaje de alerta si los campos de fecha están vacíos
        Swal.fire({
        title: 'Rango de Fechas Requerido',
        });
    }
    }

.. _funcion-getFirstElement:

Función ``getFirstElement``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

En términos generales, la función ``getFirstElement()`` obtiene los parámetros de los filtros y presenta datos dinámicos del servidor en los elementos del reporte.

La función se encarga de recibir las validaciones de los filtros para realiza una solicitud al servidor (puede ser a producción o a preproducción dependiendo del parámetro que contenga en la ``URL``, línea 9) utilizando el método ``POST``.

.. seealso:: El ``scriptId`` es lo que se recibe como parámetro en la ``URL``, línea 12 (Regrese y consulte la :ref:`funcion-window-onload` :octicon:`report;1em;sd-text-info`, específicamente las líneas 6-8, y lea los comentarios).

Después de procesar la respuesta del servidor, muestra u oculta elementos en la interfaz según el resultado. Si la respuesta es exitosa, se actualiza el elemento (tabla) con los datos recibidos. En caso de error se muestra un mensaje utilizando la biblioteca Swal (|sweetalert2| :octicon:`report;1em;sd-text-info`) líneas 46-60. Lea detenidamente los comentarios dentro del código para comprender el flujo.

.. note:: Los errores más comunes que pueden presentarse al hacer la solicitud pueden incluir:

    - No tener acceso a la información.
    - La sesión caducó (el token ha expirado).

Observe la línea de código número 40, llama a la `función getDrawTable <#funcion-getDrawTable>`_ :octicon:`report;1em;sd-text-info`. Desglosando los parámetros que envía:

- **firstElement**: Es el ``ID`` del ``div`` donde se necesita colocar la tabla.

- **columsTable1**: Variable que contiene un array de objetos que representan las columnas de la tabla (biblioteca de tablas |Tabulator| :octicon:`report;1em;sd-text-info`).

.. caution:: ``columsTable1`` es la única variable que funciona tanto en el ``reporte demo`` como en el ``reporte operativo final``. Las columnas pueden ser dinámicas o estáticas, sin embargo, al utilizar funciones propias de JavaScript es difícil usar el dinamismo a menos de que todas las columnas lleven la misma estructura. Consulte el archivo `data.js <#archivo-data>`_ :octicon:`report;1em;sd-text-info` para más detalles.

- **res.response.firstElement.tabledata**: Son las filas extraídas del valor, es decir, toda la data real.

- **450**: Es la altura máxima en píxeles que medirá la tabla.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 9, 12, 40, 46-60

    // Función para obtener datos de los elementos a través de una solicitud fetch
    function getFirstElement(dateTo, dateFrom, promotor){
    //----Hide Css
    $("#divContent").hide(); // Oculta todos los elementos (tablas, gráficos, etc.) para que, al aplicar un filtro, los elementos se recarguen y no permanezcan visibles hasta que se complete la carga del nuevo filtro.
    $('.load-wrapp').show(); // Muestra la animación del spinner para cargar la data.
    $('.title_tables').hide(); // Asegura que el título de la o las tablas esté oculto para que cada vez que se aplique un filtro, los elementos vuelvan a cargarse.

    // Realiza una solicitud fetch usando el método POST para obtener datos del servidor
    fetch(url + 'infosync/scripts/run/', {
        method: 'POST',
        body: JSON.stringify({ // Convierte a un JSON
        script_id: scriptId,
        // Parámetros (filtros) que recibirá el script
        date_to: dateTo,
        date_from: dateFrom,
        promotor: promotor,
        option: 1, // Determina que consulta debe realizar, en este caso 1 le indica que debe realizar una consulta normal es decir, a la forma
        }),
        headers:{
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+userJwt
        },
    })
     // Procesa la respuesta en formato JSON
    .then(res => res.json())
    .then(res => {
        // Verifica si la petición fue exitosa (success = true)
        if (res.success) {
        //----Hide and show
        $('.load-wrapp').hide(); // Oculta la animación del spinner para cargar la data
        $("#divContent").show(); // Ahora ya muestra todos los elementos (tablas, gráficos, etc.)
        $('.title_tables').show(); // Se habilitan títulos de la o las tablas que estaban ocultas

        // Observe en la consola del navegador la data extraída, almacenada en un objeto
        console.log(res.response)
        
        // Verificar si hay datos en la respuesta
        if (res.response.firstElement.tabledata) {
            // Llama a la función "getDrawTable()" para actualizar la tabla con los datos recibidos. NOTA: Consulte la función para más detalles ubicada posteriormente.
            getDrawTable('firstElement', columsTable1, res.response.firstElement.tabledata, 450);
            // Restablecer la propiedad 'display' para mostrar el elemento 'firstElement'
            document.getElementById("firstElement").style.removeProperty('display');
        }
        } else {
        // En caso de error, oculta el indicador de carga y muestra un mensaje de error
        hideLoading();
        if(res.code == 11){
            Swal.fire({
            title: 'Error',
            html: res.error
            });
            $('.load-wrapp').hide();
        } else {
            Swal.fire({
            title: 'Error',
            html: res.error
            });
            $('.load-wrapp').hide();
        }
        }
    })
    }

.. _funcion-getDrawTable:

Función ``getDrawTable``
^^^^^^^^^^^^^^^^^^^^^^^^

La función ``getDrawTable()`` se utiliza para dibujar y configurar la tabla interactiva utilizando la biblioteca |Tabulator-doc| :octicon:`report;1em;sd-text-info`. Proporciona opciones para descargar los datos de la tabla en formatos ``XLSX`` y ``CSV``. A continuación, se describe el flujo de la función de manera general:

.. caution:: Esta función NO está estandarizada, pero si está preparada para funcionar con ``n`` cantidad de tablas que se requieran de un mismo reporte. 

Observe la línea 4, donde el ``ID`` es el indicador de HTML que toma el valor de la variable ``id`` y lo concatena con el símbolo de almohadilla (``#``), creando así un selector de identificador completo para seleccionar un elemento específico en el documento HTML basado en su identificador (tabla).

.. admonition:: Ejemplo
    :class: pied-piper
    
    Si ``id`` tiene el valor ``firstElement``, entonces ``#`` + ``id`` se convierte en ``#firstElement`` y eso se utilizará para seleccionar el elemento con el ``ID firstElement`` en el HTML. Es decir, no tendrá que repetir la función por cada tabla y colocar ``firstElement``, ``secondElement`` y así sucesivamente.

Identifique las líneas de código de la 4-15, aquí se crea una instancia de |Tabulator| :octicon:`report;1em;sd-text-info` y se configuran aspectos de la tabla, como la altura, el diseño, los datos, la capacidad de redimensionar filas, la estructura de árbol de datos, la capacidad de copiar al portapapeles, la dirección del texto y las columnas.

.. seealso:: Sin embargo, para funciones mas especificas considere revisar las |Tabulator-proprieties| :octicon:`report;1em;sd-text-info`  y ajuste las propiedades según sus necesidades. Revise la documentación correspondiente a la tabla.

En los bloques de código (18-27, 29-38) verifica si existe un elemento del DOM para la descarga de datos en formato ``XLSX`` y ``CSV`` (botones para descarga). Si existe, se reemplaza con una copia para evitar duplicados y se agrega un evento de clic para activar la descarga de datos en formato ``XLSX`` y ``CSV`` cuando se haga clic en el elemento.

.. code-block:: javascript
    :linenos:
    :emphasize-lines: 4-15, 18-27, 29-38

    //-----TABLES
    function getDrawTable(id, columnsData, tableData, height = 500){
    // Crear una instancia de Tabulator y configurar la tabla
    var  table = new Tabulator("#" + id, {
        height:height +"px",
        layout:"fitDataTable",
        data:tableData,
        resizableRows:false,
        dataTree:true,
        dataTreeStartExpanded:false,
        clipboard:true,
        clipboardPasteAction:"replace",
        textDirection:"ltr",
        columns:columnsData,
    });

    // Configuración para descargar datos en formato XLSX (Excel)
    if (document.getElementById("download_xlsx_"+id)){
        // trigger download of data.xlsx file
        // Reemplaza el elemento actual con una copia clonada del mismo elemento
        document.getElementById("download_xlsx_"+id).replaceWith(document.getElementById("download_xlsx_"+id).cloneNode(true));
        // Agrega un evento al elemento clonado para la descarga del archivo XLSX
        document.getElementById("download_xlsx_"+id).addEventListener("click", function (){
        // Utiliza la función "table.download" para descargar el contenido de la tabla en formato XLSX con el nombre de archivo "data.xlsx"
        table.download("xlsx", "data.xlsx", {sheetName:"data"});
        });
    }
    // Configuración para descargar datos en formato CSV
    if (document.getElementById("download_csv_"+id)){
        //trigger download of data.csv file
        // Reemplaza el elemento actual con una copia clonada del mismo elemento
        document.getElementById("download_csv_"+id).replaceWith(document.getElementById("download_csv_"+id).cloneNode(true));
        // Agrega un evento al elemento clonado para la descarga del archivo CSV
        document.getElementById("download_csv_"+id).addEventListener("click", function (){
        // Utiliza la función "table.download" para descargar el contenido de la tabla en formato CSV con el nombre de archivo "data.csv"
        table.download("csv", "data.csv");
        });
    }
    }

.. _archivo-data:

Estructura data.js
------------------

La estructura de un archivo ``data.js`` en ``Servido`` tiene el propósito de albergar configuraciones de las librerías utilizadas en el reporte. Es utilizado para proporcionar datos de relleno de tablas, gráficos y otros elementos y visualizar cómo se verá el reporte cuando se complete con datos reales. A continuación, se detalla más acerca de la estructura de un archivo ``data.js``. Al final, encontrará el código completo:

El siguiente bloque de código contiene un array de objetos que representan las columnas de la tabla, continue:

- Ubique la líneas de código 2-4, es una funcion propia de JavaScript diseñada para generar dinámicamente una ``URL`` para un enlace en función del valor del campo ``record_id`` en la fila actual de la tabla. Cada celda en la columna ``Folio`` tendrá un enlace único que apunta a la **página de detalles del registro** (Consulte: :ref:`visualizar-registro` :octicon:`report;1em;sd-text-info`) correspondiente en la aplicación de **Linkaform**. Es decir, la función ``url`` se utiliza como parte del *formateador* para la columna ``Folio`` en Tabulator.

+-------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Método/Instrucción                                                      | Descripción                                                                                                                                                                                     |
+=========================================================================+=================================================================================================================================================================================================+
| ``cell.getData()``                                                      | Se utiliza para obtener los datos asociados con esa celda en la fila actual de la tabla. Asumiendo que la celda está asociada al conjunto de datos que incluye un campo llamado ``record_id``.  |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``record_id``                                                           | Después de obtener los datos de la celda con ``getData()``, se accede al valor específico del campo ``record_id`` y se extrae su valor.                                                         |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``formatter``                                                           | Formateador de la celda por columna.                                                                                                                                                            |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``formateadorParams``                                                   | Parámetros adicionales con el formateador, que debe contener un objeto con información adicional para configurar el formateador.                                                                |
+-------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. seealso:: Consulte |Tabulator-format-link| :octicon:`report;1em;sd-text-info` para más detalles o revise otras opciones para |Tabulator-format| :octicon:`report;1em;sd-text-info`.

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: javascript
            :linenos:
            :emphasize-lines: 2-4, 6

            var columsTable1 = [
            {title:"Folio", field:'folio', hozAlign:"right", formatter:"link", formatterParams:{
            url:function(cell){return "https://app.linkaform.com/#/records/detail/" + cell.getData().record_id}, 
            target:"_blank",}, headerFilter:"input",width:100},
            { title:"Store ID", field:'store_id',hozAlign:"right",width:200},
            { title:"Merchant", field:'merchant',hozAlign:"left",width:300},
            { title:"Store", field:'store',hozAlign:"left",width:300},
            { title:"Promotor", field:'promotor',hozAlign:"left",width:300},
            { title:"City", field:'city',hozAlign:"left",width:250},
            { title:"State", field:'state',hozAlign:"left",width:250},
            { title:"Fecha Inicio de Captura", field:'fecha_captura',hozAlign:"right",width:250},
            { title:"Coordenadas Latitud", field:'cordenada_latitud',hozAlign:"right",formatter: "money",
            "formatterParams": {"symbol": "", "symbolAfter": "", "thousand": "",  precision:false},width:250},
            { title:"Coordenadas Longitud", field:'cordenada_longitud',hozAlign:"right",formatter: "money",
            "formatterParams": {"symbol": "", "symbolAfter": "", "thousand": "",  precision:1},width:250},
            { title:"Check In", field:'checkin',hozAlign:"right",width:250},
            { title:"Check Out", field:'checkout',hozAlign:"right",width:250},
            { title:"Tiempo Visita", field:'tiempo_visita',hozAlign:"right",width:250},
            ];

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes16.png

        - **title**: Texto de la columna.
        - **field**: Atributo key que permitirá enlzar las columnas con las filas.
        - **hozAlign**: Alineación de la data, puede ser ``righth``, ``center`` o ``left``, pero no ``justify``.
        - **width**: Ancho de la columna en ``px``.

.. caution:: Las columnas pueden ser dinámicas solamente si no se utilizan formateos específicos para la tabla. Es decir, si todas las columnas de la tabla son estáticas y usan la misma estructura (title, field, hozAlign y width), como se muestra en la línea 6.

El siguiente bloque de código representa un array de objetos de la data de la tabla.

.. note:: Cada objeto dentro del arreglo representa una fila de datos con propiedades específicas.

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: javascript
            :linenos:

            var dataTable1 = [
            {
                "folio": "850-11702", 
                "record_id": "63eaed385a3ef7414d4899da", 
                "store_id": "1209250816961081402", 
                "merchant": "Calvin Klein Instore", 
                "store": "Ck Parque Lindavista", 
                "centro_comercial": "Parque Lindavista", 
                "promotor": "Alberto Torres", 
                "city": "Gustavo A. Madero", 
                "fecha_creacion": "2023-02-14 08:08:56", 
                "checkin": "2023-02-14 08:03:49", 
                "checkout": "2023-02-14 08:08:45", 
                "tz_offset": -360.0, 
                "tiempo_visita": 296.0
            },
            {
                "folio": "850-11702", 
                "record_id": "63eaed385a3ef7414d4899da", 
                "store_id": "1209250816961081402", 
                "merchant": "Calvin Klein Instore", 
                "store": "Ck Parque Lindavista", 
                "centro_comercial": "Parque Lindavista", 
                "promotor": "Alberto Torres", 
                "city": "Gustavo A. Madero", 
                "fecha_creacion": "2023-02-14 08:08:56", 
                "checkin": "2023-02-14 08:03:49", 
                "checkout": "2023-02-14 08:08:45", 
                "tz_offset": -360.0, 
                "tiempo_visita": 296.0
            },
            ];

    .. tab-item:: Resultado

        .. image:: /imgs/Reportes/Reportes17.png

Estructura CSS
==============

La estructura de un archivo ``CSS`` es simple y básica, son estilos generales aplicados especialmente a los títulos de los elementos. Utilice el siguiente código como base para sus reportes futuros.

.. note:: La mayoría de los estilos del reporte dependen de la herramienta que se esté utilizando, ya que estas contienen sus propios estilos. 

.. code-block:: css
    :linenos:

    .title_tables h3 {
    color: black;
    font: 33px gothambook;
    margin-top: 30px;
    text-align: left;
    }


    .hrFirstElement {
    border-top: 1px solid #707b7c;
    width: 500px;
    margin-left: 0%;
    }

    .hrSecondElement {
    border-top: 1px solid #707b7c;
    width: 550px;
    margin-left: 0%;
    }

    body{
    font-family: gothambook;
    }

En esta sección ha aprendido lo necesario para desarrollar sus reportes demo. Por favor, continúe con la siguiente parte para desarrollar el script necesario y construir las consultas a la base de datos y poblar sus elementos con datos reales.

.. LIGAS EXTERNAS

.. |Producción| raw:: html

   <a href="https://app.linkaform.com/" target="_blank">Producción</a>

.. |Preproducción| raw:: html

   <a href="https://preprod.linkaform.com/" target="_blank">Preproducción</a>

.. |Tabulator| raw:: html

   <a href="https://tabulator.info/docs/5.5/download" target="_blank">Tabulator</a>

.. |Tabulator-doc| raw:: html

   <a href="https://tabulator.info/" target="_blank">Tabulator</a>

.. |Tabulator-proprieties| raw:: html

   <a href="https://tabulator.info/examples/5.5" target="_blank">opciones de tablas</a>

.. |Tabulator-format-link| raw:: html

   <a href="https://tabulator.info/docs/5.5/format#formatter-link" target="_blank">formateador de tabla con url</a>

.. |Tabulator-format| raw:: html

   <a href="https://tabulator.info/docs/5.5/format" target="_blank">formatear tablas</a>

.. |minificadas| raw:: html

   <a href="https://kinsta.com/es/blog/minificar-javascript/#qu-es-la-minificacin-de-cdig" target="_blank">minificadas</a>

.. |sweetalert2| raw:: html

   <a href="https://sweetalert2.github.io/" target="_blank">SweetAlert2</a>
