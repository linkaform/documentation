================================
Desarrollo de Demo Frontend (JS)
================================

Antes de comenzar a explicar el código perce, debe considerar algunos estándares y buenas prácticas al momento de programar.

Una de esas es usar comentarios que describan en pocas palabras y de forma coherente el código que se está realizando, esto permitirá a usted y a otros desarrolladores comprender el código. 

Una buena práctica es usar un estándar con el nombre de las variables, estas deben ser descriptivas y estar en el formato camelCase para javascript o snake_case para python.

Otra buena práctica es considerar que se está usando el lenguaje Python 3, por lo que se recomienda eseguir la versión mencionada. 

El archivo JS que se analiza a continuación, se encarga principalmente de gestionar los eventos que ocurren en la vista, alguna de estas corresponden a solicitudes que se realizan al backend, por ejemplo a los catálogos en la mayoria de de los casos (no en todos), estas formas son:

1. Utilizar una función API que se encuentrán el front para realizar peticiones a catálogos que se encuentran asociadas a una forma. Esta manera de realizar la petición es poco práctica, ya que devuelve solo los datos de catálogos en un primer nivel, recordemos que los catálogos pueden ser anidados, esto devuelve resultados incompletos, por lo que no se considera práctico.

2. Hacer una petición a los scripts: los scripts realizan la petición a una misma API de los scripts y esta API realiza las peticiones a los catálogos. Es un método recomendado, ya que puede formatear la data o inclusive puede realizar consultas a la misma base de datos y devolver la data.

La creación de Script comienza declarando las variables a utilizar y a instanciarlas con un valor inicial **null**.

.. code-block:: javascript

  let us = null; 
  let usTy = null;
  let jw = null;
  let userId = null;
  let userJwt = null; // token del usuario
  let userName = null; // 
  let userParentId = null; // id de la cuenta padre
  let scriptId = null; // argumento get

Cuando un reporte se renderiza, se aplican ciertas funciones automáticamente, a continuación se muestran las siguientes:

.. code-block:: javascript

  // Oculta el elemento con el ID "divOptions" en la página.
  $('#divOptions').hide();
  // Oculta el elemento con el ID "title_report" en la página.
  $('#title_report').hide();
  // Oculta todos los elementos con la clase CSS "title_tables" en la página.
  $('.title_tables').hide();
  // Llama a una función personalizada "hideElement" para ocultar un elemento con el ID "title_demo".
  hideElement("title_demo");
  // Llama a la función "hideElement" para ocultar un elemento con el ID "firstParameters".
  hideElement("firstParameters");
  // Llama a la función "hideElement" para ocultar un elemento con el ID "firstElement".
  hideElement("firstElement");
  // Llama a la función "hideElement" para ocultar un elemento con el ID "secondElement".
  hideElement("secondElement");
  // Llama a la función "hideElement" para ocultar un elemento con el ID "thirdElement".
  hideElement("thirdElement");


Estos son métodos de jQuery, los argumentos que recibe son los ids de las etiquetas en el archivo HTML, estos métodos ocultan estos elementos al cargar el reporte.

Las siguientes funciones son las siguientes:

.. code-block:: javascript

  // Esta función se ejecutará cuando la ventana haya cargado completamente.
  window.onload = function(){
    // Obtiene los parámetros de la URL y los convierte en un objeto JavaScript.
    var qs = urlParamstoJson();
    // Obtiene un elemento del DOM con el ID "appCont".
    var formNode = document.getElementById("appCont");
    // Inicializa una variable para almacenar el ID del script.
    var scriptId;
    // Recorre los parámetros de la URL.
    for (var key in qs) {
      // Verifica si el parámetro es "script_id" y lo convierte en un entero.
      if (key === 'script_id') {
        console.log('script id', key);
        scriptId = parseInt(qs[key]);
      }
      // Verifica si el parámetro es "env" y establece la URL en función del valor.
      if (key === 'env') {
        if (qs[key] === 'test') {
          url = "https://preprod.linkaform.com/api/"; // Establece la URL de la API en modo de prueba.
        }
      }
      // Verifica si el parámetro es "title" y establece el texto de un elemento con el ID "title_report".
      if (key === 'title') {
        $("#title_report").text(qs[key]);
      }
      // Obtiene todos los elementos con el atributo 'data-infosync-id' igual a 'key'.
      var elements = getAllElementsWithAttribute(formNode, 'data-infosync-id', key);
      // Decodifica el valor del parámetro.
      var value = decodeURI(qs[key]);
      // Si el parámetro es 'infosyncRecordID', establece su valor en un elemento con el mismo ID.
      if (key === 'infosyncRecordID') {
        var recId = document.getElementById("infosyncRecordID");
        recId.value = value;
      }
      else if (elements.length > 0) {
        // Si existen elementos con el atributo 'data-infosync-id', actualiza sus valores según el tipo de elemento.
        switch (elements[0].type) {
          case 'text':
          case 'textarea':
          case 'select-one':
            elements[0].value = value;
            break;
          case 'radio':
            for (var idx in elements) {
              if (elements[idx].value === value) {
                elements[idx].checked = true;
              }
            }
            break;
          case 'checkbox':
            // Divide el valor en partes y verifica si coincide con los elementos.
            var values = value.split(';');
            for (var idx in elements) {
              if (values.indexOf(elements[idx].value) !== -1) {
                elements[idx].checked = true;
              }
            }
            break;
        }
      }
    }
  }

El propósito del código anterior es comprobar el entorno de ejecución. Esta se ejecuta cuando la página se carga por completo y procesa los parámetros de la URL para actualizar los elementos del formulario en función de esos parámetros. También se encarga de establecer la URL de la API y manipular el texto de un elemento con el ID 

Además, esta función se compone de otras funciones y condicionales, tales como:

.. code-block:: javascript

  // Obtiene valores de cookies y almacena en variables.
  us = getCookie("userId");
  jw = getCookie("userJwt");
  userParentId = getCookie("userParentId");

  // Oculta elementos con los IDs "close_sesion" y "firstParameters".
  hideElement("close_sesion");
  hideElement("firstParameters");

Si la condición se cumple, se ejecutan las siguientes funciones, donde la primera condición se encarga de verificar si un usuario ha iniciado sesión. 
Los parámetros ``us`` corresponden al ID del usuario, ``jw`` al token del usuario y ``scriptId`` al parámetro. 

.. important::
  Si ``scriptId`` es nulo, el entorno se configura para la demo.
 
.. code-block:: javascript

  // Verifica si las cookies "userId" y "userJwt" no están vacías o si "scriptId" es nulo.
  if (us != "" && jw != "" || scriptId === null) {
    // Oculta el elemento con el ID "inicio_ses" porque ya hay una sesión activa.
    hideElement("inicio_ses");

    // Muestra el elemento con el ID "close_sesion" correspondiente al botón cerrar sesión.
    unhideElement("close_sesion");

    // Obtiene el logo de la empresa según el "userParentId".
    getCompanyLogo(userParentId);

    // Asigna valores a variables globales.
    userId = us;
    userJwt = jw;
    userName = getCookie("userName"); //Obtiene el nombre del usuario a través de una cookie.

    // Restablece la propiedad "display" del elemento con el ID "firstParameters" (lo muestra).
    document.getElementById("firstParameters").style.removeProperty('display');

    // Muestra elementos del reporte (llama a una función "unHideReportElements").
    unHideReportElements();

    // Si "scriptId" es nulo, carga datos de la demo y ejecuta la función correspondiente de loadDemoData.
    if (scriptId == null) {
      loadDemoData();
    }

    // Carga la animación de spinner cuando se carga la data.
    setSpinner();
    $('#divOptions').show();
    $('#title_report').show();
    document.getElementById("firstParameters").style.removeProperty('display');
  } else {
    // Si las condiciones anteriores no se cumplen, muestra el elemento con el ID "inicio_ses".
    unhideElement("inicio_ses");

    // Oculta varios elementos, incluyendo "divContent", "divOptions", "title_report" y elementos con la clase "title_tables".
    $('#divContent').hide();
    $('#divOptions').hide();
    $('#title_report').hide();
    $('.title_tables').hide();

    // Oculta el elemento con el ID "firstElement-Buttons".
    hideElement("firstElement-Buttons");
  }

  // Recorre los parámetros de la URL.
  for (var key in qs) {
    // Si el parámetro es "embed" y tiene un valor, oculta los elementos con los IDs "close_sesion" y "image_log".
    if (key === 'embed' && qs[key]) {
      $("#close_sesion").hide();
      $("#image_log").hide();
    }
  }
  // Definición de la función "unHideReportElements".
  function unHideReportElements(){
    // Muestra los elementos específicos en la página que son necesarios para el reporte al iniciar sesión.
    // Muestra el elemento con el ID "firstElement-Buttons".
    unhideElement("firstElement-Buttons");
    // Muestra el elemento con el ID "firstParameters".
    unhideElement("firstParameters");
    // Muestra el elemento con el ID "close_sesion".
    unhideElement("close_sesion");
    // Muestra el elemento con el ID "firstElement".
    unhideElement("firstElement");
  }

El siguiente bloque de código está diseñado para cargar datos de demostración y mostrar gráficos y elementos en la página.

.. code-block:: javascript

  //detecta si el entorno es la demo, en caso de serlo muestra ciertos elementos pertenecientes a la demo.
  function loadDemoData(){
    // Muestra el elemento con el ID "title_demo".
    unhideElement("title_demo");
    // Muestra todos los elementos con la clase "title_tables".
    $('.title_tables').show();
    // Restablece la propiedad "display" del elemento con el ID "firstParameters" (lo muestra).
    document.getElementById("firstParameters").style.removeProperty('display');
    // Llama a la función "getDrawGraphicFirst" para obtener y mostrar un gráfico utilizando "data1" y "setOptions1".
    getDrawGraphicFirst(data1, setOptions1);
    // Restablece la propiedad "display" del elemento con el ID "firstElement" (lo muestra).
    document.getElementById("firstElement").style.removeProperty('display');
    // Llama a funciones similares para obtener y mostrar otros gráficos y elementos.
    // Esto se repite para "secondElement", "thirdElement", "fourthElement", "fivethElement", "sixthElement", "seventhElement", y "eigthElement".
    getDrawGraphicSecond(data2, setOptions2);
    document.getElementById("secondElement").style.removeProperty('display');

    getDrawGraphicThird(data3, setOptions3);
    document.getElementById("thirdElement").style.removeProperty('display');

    getDrawGraphicFourth(data4, setOptions4);
    document.getElementById("fourthElement").style.removeProperty('display');

    getDrawGraphicFiveth(data5, setOptions5);
    document.getElementById("fivethElement").style.removeProperty('display');

    getDrawGraphicSixth(data6, setOptions6);
    document.getElementById("sixthElement").style.removeProperty('display');

    getDrawGraphicSeventh(data7, setOptions7);
    document.getElementById("seventhElement").style.removeProperty('display');

    getDrawGraphicEigth(data8, setOptions8);
    document.getElementById("eigthElement").style.removeProperty('display');
  }

Posteriormente el siguiente código se utiliza para la visibilidad de elementos en la página. 
Cuando se llama a la función runFirstElement, oculta "divContent", muestra "load-wrapp" y oculta "title_tables". 
La visibilidad de estos elementos se ajusta mediante la modificación de las propiedades de estilo.

.. code-block:: javascript

  // Obtiene una referencia al elemento HTML con la clase "loading-container".
  const loading = document.querySelector('.loading-container');
  // Oculta el elemento con la clase "loading-container" estableciendo su propiedad "display" en 'none'.
  loading.style.display = 'none';
  // se encarga de gestionar los filtros existentes, toma los valores de «date_to» (de esta fecha) y «date_from» (a esta fecha) y las almacena en las variables.
  function runFirstElement() {
    // Obtiene referencias a los elementos HTML con los IDs "date_from" y "date_to".
    let date_from = document.getElementById("date_from");
    let date_to = document.getElementById("date_to");
    let promotor = document.getElementById("promotor");
    
    //Llama a la función "getFirstElement". La propiedad value de las fechas no deben tener un valor nulo (no existencia) y que no deben estar vacías, si la condición se cumple se ejecuta la función getFirstElement esta recibe tres argumentos. 
    getFirstElement(date_to.value, date_from.value,  promotor.value );
  }

  // Esta función recibe los tres argumentos y se encarga de solicitar la data y de otras funciones
  function getFirstElement(dateTo, dateFrom, promotor) {
    // Oculta el elemento con el ID "divContent".
    $("#divContent").hide();
    // Muestra elementos con la clase "load-wrapp".
    $('.load-wrapp').show();
    // Oculta elementos con la clase "title_tables".
    $('.title_tables').hide();
  }

La función `fetch` recibe la URL (puede ser a prod o a preprod dependiendo de los parámetros en la URL, esta se le añade una ruta estandarizada). 
Posteriormente se define el cuerpo de la función con el método HTTP POST, el cuerpo de la petición se formatea a JSON, la cuál recibe dos atributos, el primero corresponde al ``ID`` del script y el ``option``. El `option` puede valer 0 o 1, estos definen el tipo de petición, donde `option 0` define la búsqueda a catálogos y `option 1` define una petición normal.

Posteriormente se define el encabezado de la petición: este recibe el tipo con contenido de la petición y el token del usuario.



El siguiente bloque de código consiste en realizar la petición al backen a través de una función fetch, esta recibe una serie de argumentos, como son, la url y el complemento de la ruta como estandar, la petición se ejecuta con el método POST y el cuerpo de la petición envía los argumentos de script_id, los rangos de fechas el id del promotor y el option: 1 correspondiente al tipo de petición.

.. code-block:: javascript

  // Realiza una solicitud HTTP POST a la URL formada por la concatenación de 'url' y 'infosync/scripts/run/'.
  fetch(url + 'infosync/scripts/run/', {
    method: 'POST',
    body: JSON.stringify({
      script_id: scriptId, // Envia un objeto JSON en el cuerpo de la solicitud con una propiedad "script_id".
      date_to: dateTo,
      date_from: dateFrom,
      promotor: promotor,
      option: 1 // o 0, reemplaza con el valor deseado
    }),
    headers: {
      'Content-Type': 'application/json', // Establece el tipo de contenido del cuerpo de la solicitud como JSON.
      'Authorization': 'Bearer ' + userJwt // Incluye la autorización en el encabezado de la solicitud, probablemente un token JWT.
    },
  })


Posteriormente se encuentra el bloque de código que verifica que los datos se devuelvan con éxito, en caso de tener éxito, se oculta el elemento de carga y se muestra el contenido, en teste caso demo en particular se hace uso de la función getDrawTable, responsable de dibujar la tabla.

.. code-block:: javascript

      .then(res => res.json()) // Convierte la respuesta HTTP en un objeto JSON.
      .then(res => {
        if (res.success) { // Verifica si la propiedad "success" en la respuesta es verdadera.
          //----Hide and show Muestra y oculta según sea necesario.
          // Oculta el elemento con la clase "load-wrapp".
          $('.load-wrapp').hide();
          // Muestra el elemento con el ID "divContent".
          $("#divContent").show();
          // Muestra elementos con la clase "title_tables".
          $('.title_tables').show();
          console.log(res.response);

          if (res.response.firstElement.tabledata) {
            // Si existe "tabledata" en la propiedad "firstElement" de "response," llama a la función "getDrawTable" para mostrar una tabla.
            getDrawTable('firstElement', columsTable1, res.response.firstElement.tabledata, 450);

            // Restablece la propiedad "display" del elemento con el ID "firstElement" (lo muestra).
            document.getElementById("firstElement").style.removeProperty('display');
          }
        }
      });


El resultado del código anterior se visualiza de la siguiente forma:

.. image:: /imgs/Reportes/DatosPrueba/1.png

El cuerpo de la función que se presenta a continuación, presenta un formato definido por la librería Tabulator <https://tabulator.info/>. Esta estructura es un estándar para la gestión de tablas, puede ser a justada a las necesidades de los clientes. Se inicializa un objeto de Tabulator esta recibe como primer argumento «#»+ id y un objeto javascript que define el formato de la tabla.

.. code-block:: javascript

  // Crea una instancia de Tabulator y la asigna a la variable "table".
  var table = new Tabulator("#" + id, {
    height: height + "px", // Establece la altura de la tabla en píxeles.
    layout: "fitDataTable", // Configura el diseño de la tabla para ajustarse automáticamente al contenido.
    data: tableData, // Establece los datos que se mostrarán en la tabla.
    resizableRows: false, // Desactiva la capacidad de redimensionar filas.
    dataTree: true, // Habilita la funcionalidad de árbol de datos para la tabla.
    dataTreeStartExpanded: false, // Inicia todos los nodos del árbol de datos como no expandidos.
    clipboard: true, // Habilita la funcionalidad de portapapeles en la tabla.
    clipboardPasteAction: "replace", // Define la acción a realizar al pegar datos en la tabla (en este caso, reemplazar).
    textDirection: "ltr", // Establece la dirección del texto como de izquierda a derecha.
    columns: columnsData, // Define las columnas de la tabla utilizando los datos proporcionados en "columnsData".
  });

El resto del cuerpo de la función consiste en las condicionales que se muestran a continuación. Las condicionales comprueban si existen los botones de descarga de la tabla en distintos formatos (xlsx, csv, pdf). Se realiza esta condición porque en ciertos casos estos botones no se colocan por requerimientos del cliente.

.. code-block:: javascript

  // Verifica si existe un elemento con el ID "download_xlsx_" seguido de "id".
  if (document.getElementById("download_xlsx_" + id)) {
    // Reemplaza el elemento actual con una copia clonada del mismo elemento.
    document.getElementById("download_xlsx_" + id).replaceWith(document.getElementById("download_xlsx_" + id).cloneNode(true));

    // Agrega un evento de escucha al elemento clonado para la descarga del archivo XLSX.
    document.getElementById("download_xlsx_" + id).addEventListener("click", function () {
      // Utiliza la función "table.download" para descargar el contenido de la tabla en formato XLSX con el nombre de archivo "data.xlsx".
      table.download("xlsx", "data.xlsx", { sheetName: "data" });
    });
  }

  // Verifica si existe un elemento con el ID "download_csv_" seguido de "id".
  if (document.getElementById("download_csv_" + id)) {
    // Reemplaza el elemento actual con una copia clonada del mismo elemento.
    document.getElementById("download_csv_" + id).replaceWith(document.getElementById("download_csv_" + id).cloneNode(true));

    // Agrega un evento de escucha al elemento clonado para la descarga del archivo CSV.
    document.getElementById("download_csv_" + id).addEventListener("click", function () {
      // Utiliza la función "table.download" para descargar el contenido de la tabla en formato CSV con el nombre de archivo "data.csv".
      table.download("csv", "data.csv");
    });
  }

Los botones de descarga son los siguientes:

.. image:: /imgs/Reportes/DatosPrueba/2.png
