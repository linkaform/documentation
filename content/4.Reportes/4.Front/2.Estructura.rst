==========
Estructura
==========

En esta sección se describen con más detalle la estructura que componen a los archivos que hacen posible la visualización del reporte.  

Estructura de un archivo html
=============================

En esta sección, procederemos a describir la estructura que compone un archivo HTML.

+--------------------------------+-------------------------------------+
| Estructura                     | Descripción                         |
+================================+=====================================+
| HEAD                           | Contiene ciertos requerimientos     |
|                                | que considera el navegador al       |
|                                | momento de renderizar la página. En |
|                                | esta sección se deben colocar los   |
|                                | CDN para los estilos, estos son     |
|                                | bootstrap, Font Awesome y estilos   |
|                                | propios de Linkaform.               |
+--------------------------------+-------------------------------------+
| BODY                           | Contiene el cuerpo del reporte, es  |
|                                | lo que verá el usuario, dentro de   |
|                                | esta se mostraran gráficas, tablas, |
|                                | tarjetas, entre otros elementos.    |
+--------------------------------+-------------------------------------+
| Librerías                      | Este apartado se ubica en la última |
|                                | sección de la etiqueta body, en     |
|                                | donde se encuentran las rutas de:   |
|                                | Tabulator, Chartjs, Jquery,         |
|                                | Bootstrap, utilidades de linkaform  |
|                                | y servido, la ubicación del         |
|                                | manejador js, y del manejador de la |
|                                | estructura de los datos.            |
+--------------------------------+-------------------------------------+

En el siguiente bloque de código se muestra la estructura de un archivo html.

.. code:: html

    <!DOCTYPE html>
        <html lang="en" dir="ltr">
        <head>
            <meta charset="utf-8">
            <title>Servido</title>
            <meta name="title" content="Servido">
            <meta name="description" content="Reporte Encuestas">
            <link type="image/x-icon" rel="shortcut icon" href="../styles/img/favicon.ico">
            <meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1, maximum-scale=1">
            <link type="image/x-icon" rel="shortcut icon" href="../styles/img/favicon.ico">
            <!--Bootstrap -->
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
            <!--Font Awesome -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
            <!--LIBRARY CHECK -->
            <link href="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap4-toggle@3.6.1/css/bootstrap4-toggle.min.css" rel="stylesheet">
            <!--Utils -->        
            <link rel="stylesheet" href="../styles/css/sweetalert2.min.css">
            <link rel="stylesheet" href="../styles/css/styles.css">
            <link rel="stylesheet" href="style.css">
        </head>
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
                        <h1 id="title_report">Reporte de preguntas</h1>
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



                    <!--OPtions FIlter -->
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
                        <div class="col-sm-12 col-md-2 col-lg-2">
                            <h5>Resumen por: </h5>
                            <input type="checkbox"  data-toggle="toggle" data-width="130" data-on="Operativo" data-off="Visita" id="input_check" data-onstyle="success" data-offstyle="primary">
                        </div>
                    </div>

                    <!--Content -->
                    <div class="row" style="margin-top:20px;"  id="divContent">
                        <!--Primer Elemento -->
                        <div class="col-sm-12 col-md-12 col-lg-12" style="align-items: center;overflow-y: scroll;">
                            <section class="title_tables">
                                <h3><span>Recepción Preguntas</span>&nbsp;&nbsp;
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
        <script
        src="https://code.jquery.com/jquery-3.6.0.js"
        integrity="sha256-H+K7U5CnXl1h5ywQfKtSj8PCmoN9aaq30gDh27Xc0jk="
        crossorigin="anonymous"></script>

        <!-- Bootstrap -->
        <script src="https://cdn.jsdelivr.net/gh/gitbrent/bootstrap4-toggle@3.6.1/js/bootstrap4-toggle.min.js"></script>

        <script 
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" 
        integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" 
        crossorigin="anonymous"></script>

        <script 
        src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" 
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" 
        crossorigin="anonymous"></script>


        <!-- Utils -->
        <script type="text/javascript" src="../styles/js/chroma.min.js"></script>
        <script type="text/javascript" src="../styles/js/sweetalert2.all.min.js"></script>

        <script type="text/javascript" src="../utils/lkf_utils.js"></script>
        <script type="text/javascript" src="../utils/servido_utils.js"></script>

        <!-- Template -->
        <script type="text/javascript" src="./reporte_preguntas.js"></script>
        <script type="text/javascript" src="./reporte_preguntas_data.js"></script>
        </body>
    </html>

Estructura de un archivo js
===========================

La mayoría del código presentado está estandarizado; sin embargo, para llevar a cabo acciones más específicas, es necesario actualizarlo de acuerdo a sus necesidades particulares. 

.. important::
    El archivo JavaScript está preparado para procesar la lógica del reporte, tenga en cuenta la personalización de formas, la asignación de identificadores a los campos, la gestión de catálogos, entre otros aspectos.

.. code:: javascript

    // Reporte Production Forscast
    // Librerias: Chart.js


    let us = null;
    let usTy = null;
    let jw = null;
    let userId = null;
    let userJwt = null;
    let userName = null;
    let userParentId = null;
    let scriptId = null;
    let nuevo = null

    $('#divOptions').hide();
    $('#title_report').hide();
    $('.title_tables').hide();
    hideElement("title_demo");
    hideElement("firstParameters");
    hideElement("firstElement");
    hideElement("secondElement");
    hideElement("thirdElement");




    window.onload = function(){
    var qs = urlParamstoJson();
    var formNode = document.getElementById("appCont");
        for(var key in qs){
        if (key === 'script_id' ){
        console.log('script_id', key)
        scriptId = parseInt(qs[key]);
        }
        if (key === 'env') {
        if (qs[key] === 'test'){
            url = "https://preprod.linkaform.com/api/";
        }
        }
        if (key ==='title'){
        $("#title_report").text(qs[key]);
        }
            var elements = getAllElementsWithAttribute(formNode, 'data-infosync-id', key);
            var value = decodeURI(qs[key]);
        if (key === 'infosyncRecordID'){
        var recId = document.getElementById("infosyncRecordID");
        recId.value = value;
        }
            else if(elements.length > 0){
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

    us = getCookie("userId");
    jw = getCookie("userJwt");
    userParentId = getCookie("userParentId");
    hideElement("close_sesion");
    hideElement("firstParameters");


    if(us != "" && jw != "" || scriptId===null){
        hideElement("inicio_ses");
        unhideElement("close_sesion");
        getCompanyLogo(userParentId);
        userId = us;
        userJwt = jw;
        userName = getCookie("userName");
        document.getElementById("firstParameters").style.removeProperty('display');
        unHideReportElements()
        if (scriptId == null) {
        loadDemoData();
        }
        //--Styles
        setSpinner();
        setDate();
        get_catalog();
        $('#divOptions').show();
        $('#title_report').show();
        document.getElementById("firstParameters").style.removeProperty('display');
        
    } else {
        unhideElement("inicio_ses");
        $('#divContent').hide();
        $('#divOptions').hide();
        $('#title_report').hide();
        $('.title_tables').hide();
        hideElement("firstElement-Buttons");
    }
    ///-----HIDE AND SHOW
    for(var key in qs){
        if (key === 'embed'){
        if (qs[key]){
            $("#close_sesion").hide();
            $("#image_log").hide();
        }
        }
    }
    }


    function unHideReportElements(){
    //Set here all report elements that need to be unHiden on a loggin
    unhideElement("firstElement-Buttons");
    unhideElement("firstParameters");
    unhideElement("close_sesion");
    unhideElement("firstElement");
    }

    const loading = document.querySelector('.loading-container');
    loading.style.display = 'none';


    //-----DEMO 
    function loadDemoData(){
    $('.title_tables').show();
    unhideElement("title_demo")
    document.getElementById("firstParameters").style.removeProperty('display');


    getDrawTable('firstElement', columsTable3, dataTable1, 350);
    document.getElementById("firstElement").style.removeProperty('display');
    }

    //-----DATEE
    function setDate(){
    array_month = ['01','02','03','04','05','06','07','08','09','10','11','12'];
    //---DATE TO
    date_to = new Date();
    year = date_to.getFullYear();
    month = array_month[date_to.getMonth()];
    day = date_to.getDate();
    date_to = year +'-'+ month +'-'+ day;
    $('#date_to').val(date_to);
    $('#date_from').val(date_to);
    //---DATE FROM IN CASE 30 DAYS
    /*
    date_from = new Date();
    date_from.setDate(date_from.getDate() - 30)

    year = date_from.getFullYear();
    month = array_month[date_from.getMonth()];
    day = date_from.getDate();
    date_from = year +'-'+ month +'-'+ day;
    $('#date_from').val(date_from);
    */
    }



    //-----EXCUTION
    function runFirstElement(){
    let date_from = document.getElementById("date_from");
    let date_to = document.getElementById("date_to");  

    option = 0;
    if (document.getElementById('input_check').checked)
    {
        option = 1;
    }
    getFirstElement(date_to.value, date_from.value, option);
    }


    function getFirstElement(dateTo, dateFrom, option){
    //----Hide Css
    $("#divContent").hide();
    $('.load-wrapp').show();
    $('.title_tables').hide();


    fetch(url + 'infosync/scripts/run/', {
        method: 'POST',
        body: JSON.stringify({
        script_id: scriptId,
        date_to: dateTo,
        date_from: dateFrom,
        option: option,
        }),
        headers:{
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+userJwt
        },
    })
    .then(res => res.json())
    .then(res => {
        if (res.success) {
        //----Hide and show
        $('.load-wrapp').hide();
        $("#divContent").show();
        $('.title_tables').show();
        console.log(res.response.firstElement.tabledata)
        if (res.response.firstElement.tabledata) {
            
            if(option == 0){

            getDrawTable('firstElement', columsTable3, res.response.firstElement.tabledata, 450);
            }else if(option == 1){
            getDrawTable('firstElement', columsTable2, res.response.firstElement.tabledata, 450);
            }
            document.getElementById("firstElement").style.removeProperty('display');
        }
        } else {
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

    //-----TABLES
    function getDrawTable(id, columnsData, tableData, height = 500){
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

    if (document.getElementById("download_xlsx_"+id)){
        //trigger download of data.xlsx file
        document.getElementById("download_xlsx_"+id).replaceWith(document.getElementById("download_xlsx_"+id).cloneNode(true));
        document.getElementById("download_xlsx_"+id).addEventListener("click", function (){
        table.download("xlsx", "data.xlsx", {sheetName:"data"});
        });
    }

    if (document.getElementById("download_csv_"+id)){
        //trigger download of data.csv file
        document.getElementById("download_csv_"+id).replaceWith(document.getElementById("download_csv_"+id).cloneNode(true));
        document.getElementById("download_csv_"+id).addEventListener("click", function (){
        table.download("csv", "data.csv");
        });
    }
    }


    //-----CATALOG
    function get_catalog() 
    {
    fetch(url + 'infosync/scripts/run/', {
        method: 'POST',
        body: JSON.stringify({
            script_id: 95556,
            option: 0,
        }),
        headers:{
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+userJwt
        },
        })
        .then(res => res.json())
        .then(res => {
        if (res.success) {
        if (res.response.catalog.length){
            array_value = []
            for (i = 0; i < res.response.catalog.length; i++) {
            if (!array_value.includes(res.response.catalog[i]['63dc0f1ec29b8336b7b72615'])) {
                array_value.push(res.response.catalog[i]['63dc0f1ec29b8336b7b72615'])
            }
            }
            array_value.sort();  
            $("#promotor").empty();
            $('#promotor').append('<option value="--">--Seleccione--</option>');
            for (i = 0; i <array_value.length; i++) {
            $('#promotor').append('<option value="'+ array_value[i] +'">'+array_value[i]+'</option>');
            }

            console.log(array_value);
        }
        } 
    })
    };



Estructura de un archivo data.js
================================

La estructura de un archivo "data.js" tiene el propósito de albergar configuraciones de las librerías utilizadas en el reporte. Puede incluir gráficos, tablas y otros elementos. Incluso es posible proporcionar datos de relleno para visualizar cómo se verá el reporte cuando se complete con datos reales.

A continuación, se presenta el bloque de código que muestra la estructura de un archivo "data.js":

.. code:: javascript

    var columsTable2 = [
    {title:"Folio", field:'folio', hozAlign:"right", formatter:"link", formatterParams:{
    url:function(cell){return "https://app.linkaform.com/#/records/detail/" + cell.getData().record_id}, 
    target:"_blank",},  headerTooltip:true,width:100},
    { title:"Store ID", field:'store_id',hozAlign:"right", headerTooltip:true,width:200},
    { title:"Merchant", field:'merchant',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Store", field:'store',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Promotor", field:'promotor',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Fecha", field:'fecha',hozAlign:"center", headerTooltip:true,width:150},
    { title:"Hora", field:'hora',hozAlign:"center", headerTooltip:true,width:150},

    { title:"¿La tienda cuenta con usuario y contraseña ?", field:'pregunta_1',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda ya cuenta con los datos de soporte telefónico servicio al cliente y tienda?", field:'pregunta_2',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Describe las fallas u optunidades de mejora que te comentaron los vendedores, y cómo se resolvieron.", field:'pregunta_3',hozAlign:"left", headerTooltip:true,width:300},
    {
        title:"En tu visita, ¿Qué obstáculos y/o retos tiene la tienda?",
        columns:[
        { title:"Clientes no les interesa Kueski Pay", field:'pregunta_4A',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Vendedores no cuentan con capacitación", field:'pregunta_4B',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Vendedores no ofrecen Kueski Pay", field:'pregunta_4C',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Dar Beneficios de Kuesky Pay a Vendedores", field:'pregunta_4D',hozAlign:"left", headerTooltip:true,width:300},
        { title:"No tienen autorización de corporativo para ofrecer Kueski", field:'pregunta_4F',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Otro", field:'pregunta_4G',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    { title:"¿Compartiste las ventas que tiene con Kueski Pay actualmente la tienda?", field:'pregunta_5',hozAlign:"left", headerTooltip:true,width:300},
    {
        title:"¿La tienda cuenta con publicidad de Kueski?",
        columns:[
        { title:"No", field:'pregunta_6A',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Sticker", field:'pregunta_6B',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Carta Informativa ( mini banner )", field:'pregunta_6C',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Video Pantalla", field:'pregunta_6D',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    { title:"¿Numero telefonico de sucursal?", field:'pregunta_8',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Cuál es el nombre del gerente de sucursal o encargado?", field:'pregunta_9',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Cuál es el mail del gerente o encargado de sucursal?", field:'pregunta_10',hozAlign:"left", headerTooltip:true,width:300},
    {
        title:"¿La tienda tiene promociones vigentes de Kueski?",
        columns:[
        { title:"Respuesta", field:'pregunta_11',hozAlign:"left", headerTooltip:true,width:300},
        { title:"¿Cuál?", field:'pregunta_12',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    {
        title:"¿ Tuvo alguna  promoción de Kueski el mes pasado ?",
        columns:[
        { title:"Respuesta", field:'pregunta_13',hozAlign:"left", headerTooltip:true,width:300},
        { title:"¿Cuál?", field:'pregunta_14',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    {
        title:"¿La tienda tiene promociones vigentes de la marca?",
        columns:[
        { title:"Respuesta", field:'pregunta_15',hozAlign:"left", headerTooltip:true,width:300},
        { title:"¿Cuál?", field:'pregunta_16',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    {
        title:"¿La tienda tuvo alguna  promoción de la marca el mes pasado?",
        columns:[
        { title:"Respuesta", field:'pregunta_17',hozAlign:"left", headerTooltip:true,width:300},
        { title:"¿Cuál?", field:'pregunta_18',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    { title:"Comentarios Adicionales", field:'pregunta_19',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda cuenta con cobro de Aplazo?", field:'pregunta_20',hozAlign:"left", headerTooltip:true,width:300},
    {
        title:"¿La tienda cuenta con publicidad de Aplazo?",
        columns:[
        { title:"No", field:'pregunta_21A',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Banner", field:'pregunta_21B',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Sticker", field:'pregunta_21C',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Video Pantalla", field:'pregunta_21D',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Carta Informativa", field:'pregunta_21E',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Cenefa", field:'pregunta_21F',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Stopper", field:'pregunta_21G',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Otro", field:'pregunta_21H',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    {
        title:"¿Tiene algún incentivo de Aplazo?",
        columns:[
        { title:"Respuesta", field:'pregunta_22',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Desarrollar Respuesta", field:'pregunta_23',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    {
        title:"¿Tiene alguna promoción la tienda con Aplazo?",
        columns:[
        { title:"Respuesta", field:'pregunta_24',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Desarrollar Respuesta", field:'pregunta_25',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    ];
    
    var columsTable3 = [
    {title:"Folio", field:'folio', hozAlign:"right", formatter:"link", formatterParams:{
    url:function(cell){return "https://app.linkaform.com/#/records/detail/" + cell.getData().record_id}, 
    target:"_blank",},  headerTooltip:true,width:100},
    { title:"Store ID", field:'store_id',hozAlign:"right", headerTooltip:true,width:200},
    { title:"Merchant", field:'merchant',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Store", field:'store',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Promotor", field:'promotor',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Fecha", field:'fecha',hozAlign:"center", headerTooltip:true,width:150},
    { title:"Hora", field:'hora',hozAlign:"center", headerTooltip:true,width:150},

    { title:"¿La tienda cuenta con usuario y contraseña?", field:'pregunta_1',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda cuenta con el portal de cobro activo?", field:'pregunta_2',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿El personal de tienda esta debidamente enterado y capacitado de Código de pago?", field:'pregunta_3',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda ya cuenta con los datos de soporte telefónico servicio al cliente y tienda?", field:'pregunta_4',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Vendedores están capacitados en proceso de cobro y qué es Kueski Pay?", field:'pregunta_5',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Cajeros están capacitados en proceso de cobro y qué es Kueski Pay?", field:'pregunta_6',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Gerente, subgerente, jefe de piso están capacitados en proceso de cobro y qué es Kueski Pay?", field:'pregunta_7',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿El personal de tienda esta debidamente enterado y capacitado de Downpayment?", field:'pregunta_8',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿El personal de tienda esta debidamente enterado y capacitado de cupón 10% de descuento para nuevos clientes?", field:'pregunta_9',hozAlign:"left", headerTooltip:true,width:300},
    {
        title:"¿En tu visita, ¿Qué obstáculos y/o retos tiene la tienda?",
        columns:[
        { title:"Clientes no les interesa Kueski Pay", field:'pregunta_10A',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Vendedores no cuentan con capacitación", field:'pregunta_10B',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Vendedores no ofrecen Kueski Pay", field:'pregunta_10C',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Dar Beneficios de Kuesky Pay a Vendedores", field:'pregunta_10D',hozAlign:"left", headerTooltip:true,width:300},
        { title:"No tienen autorización de corporativo para ofrecer Kueski", field:'pregunta_10E',hozAlign:"left", headerTooltip:true,width:300},
        { title:"Otro", field:'pregunta_10F',hozAlign:"left", headerTooltip:true,width:300},
        ],
    },
    { title:"¿Numero telefonico de sucursal?", field:'pregunta_11',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Cuál es el nombre del gerente de sucursal o encargado?", field:'pregunta_12',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Cuál es el mail del gerente o encargado de sucursal?", field:'pregunta_13',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Tuvo alguna promoción de Kueski el mes pasado?", field:'pregunta_14',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda cuenta con publicidad de Kueski?", field:'pregunta_15',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Banner mini acrílico 4", field:'pregunta_16',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker para piso de venta negro", field:'pregunta_17',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker para piso de venta blanco QR", field:'pregunta_18',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker para piso de venta blanco", field:'pregunta_19',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker para piso de venta negro QR", field:'pregunta_20',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Banner Mini Blanco", field:'pregunta_21',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Banner Mini Negro", field:'pregunta_22',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Banner Mini Generico", field:'pregunta_23',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker ventana 1", field:'pregunta_24',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker ventana piso de venta 1 QR", field:'pregunta_25',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker ventana piso de venta 2", field:'pregunta_26',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Tentcard genérico 2023", field:'pregunta_27',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Sticker genérico 2023", field:'pregunta_28',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Tentcard 10% negro", field:'pregunta_29',hozAlign:"left", headerTooltip:true,width:300},
    { title:"Tentcard 10% azul", field:'pregunta_30',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda tiene promociones vigentes de la marca?", field:'pregunta_31',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda tuvo alguna promoción de la marca el mes pasado?", field:'pregunta_32',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda cuenta con cobro de Aplazo?", field:'pregunta_33',hozAlign:"left", headerTooltip:true,width:300},
    {
        title:"¿La tienda cuenta con publicidad de Aplazo?",
        columns:[
        { title:"No", field:'pregunta_34A',hozAlign:"left", headerTooltip:true,width:70},
        { title:"Banner", field:'pregunta_34B',hozAlign:"left", headerTooltip:true,width:100},
        { title:"Sticker", field:'pregunta_34C',hozAlign:"left", headerTooltip:true,width:100},
        { title:"Video Pantalla", field:'pregunta_34D',hozAlign:"left", headerTooltip:true,width:150},
        { title:"Carta Informativa", field:'pregunta_34E',hozAlign:"left", headerTooltip:true,width:200},
        { title:"Cenefa", field:'pregunta_34F',hozAlign:"left", headerTooltip:true,width:100},
        { title:"Stopper", field:'pregunta_34G',hozAlign:"left", headerTooltip:true,width:100},
        { title:"Otro", field:'pregunta_34H',hozAlign:"left", headerTooltip:true,width:70},
        ],
    },
    { title:"¿Tiene algún incentivo de Aplazo?", field:'pregunta_35',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿Tiene alguna promoción la tienda con Aplazo?", field:'pregunta_36',hozAlign:"left", headerTooltip:true,width:300},
    { title:"¿La tienda cuenta con publicidad de Aplazo?", field:'pregunta_37',hozAlign:"left", headerTooltip:true,width:300},
    ];

Archivo de estilos CSS
======================

El archivo de estilos está estandarizado. La mayor parte de los estilos se aplica a los títulos y a pequeñas partes que no afectan significativamente el contenido. Esto se debe a que la mayor parte de la personalización se realiza de acuerdo a las bibliotecas utilizadas y las necesidades específicas del diseño.

.. code-block:: css

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
