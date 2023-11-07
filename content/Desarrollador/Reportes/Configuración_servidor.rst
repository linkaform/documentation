==============
Vista general
==============

Servido es una plataforma de código abierto donde los clientes de Linkaform tienen la capacidad de desarrollar informes utilizando herramientas como APIs o scripts.

La estructura de Servido se divide en dos partes.

**Servido**: Representa el frontend. Este directorio general abarca todo el entorno del sistema y se ejecuta en un servidor Docker, consta de la siguiente estructura de directorios y archivos.

- apps: Contiene carpetas corresponde a cada cliente.

Cada carpeta contiene mínimo tres archivos por reporte, estos archivos corresponden al front.

**Infosyn_scripts**: Correspondiente al backend, en este directorio se encuentran un conjunto de carpetas correspondiente a cada cliente que hace uso de scripts para sus reportes. Cada carpeta debe contener un conjunto de scripts, los cuales se encuentran estandarizados de la siguiente forma:
    
- account_settings.py: Contiene la configuración de la base de datos, como las credenciales de acceso del cliente. 

.. danger::
    Debe tener cuidado en la configuración de account_settings.py, contiene información sensible. 
    
- report_nombre_scripts.py: Estos archivos, por ejemplo: ***reporte_visitas.py*** corresponden al backend del reporte.
    
Los reportes usan la arquitectura client-API-backend.

Configuración de servido
------------------------
   
.. important:: Antes de comenzar con la configuración es necesario
   contar con el entorno de **docker-compose** instalado y configurado
   en su entorno local, si aun no lo tiene instalado puede consultar la
   `instalación de docker-compose  <https://docs.docker.com/compose/install/linux/#install-using-the-repository/>`__. 


.. note:: Si usa una distribución de Linux como Ubuntu, debian o algún
   otro; se recomienda configurar el usuario local para darle permisos
   de administrador. Se recomienda crear un directorio llamada **lkf**
   dentro de su entorno **home**, ya que dentro de este entorno se
   configurarán todos los proyectos de linkaform.

A continuación, se detalla la configuración necesaria para la instalación de **servido** y el inicio del desarrollo de reportes.

1. Diríjase al enlace de `servido <https://github.com/linkaform/servido/>`__.
2. Clone el repositorio de servido en la carpeta lkf dentro de su entorno local.
3. Siga las instrucciones del documento README.md.
4. Una vez que el proyecto esté en ejecución podrá acceder a:
    - API en el puerto 5000 `<http://127.0.0.1:5000/>`__.
    - Páginas web en el puerto 8011 en https

.. image:: /imgs/Reportes/ConfServido/9.png
.. seealso::

    Para conectarse en su local utilice el siguiente enlace: 

    `http://127.0.0.1:8011/carpeta_cliente/nombre_archivo.html?script_id=123`.


    Por ejemplo:

    `http://srv.linkaform.com/visitas/resporte_visitas.html?script_id=94392`.


Configuración del backend de reportes
-------------------------------------

1. Ingrese a su cuenta (utilice las credenciales proporcionadas por Linkaform).
2. Seleccione el ícono de Formas seguido de la opción ``Scripts``. 

.. image:: /imgs/Reportes/ConfServido/3.png

3. Seleccione la opción de cargar ``Script``.

.. image:: /imgs/Reportes/ConfServido/4.png

4. Cargue el archivo ``.py`` para que el nombre del script se autocomplete con el nombre del archivo. 

Seleccione una imagen; en este caso, hace referencia a la versión que utiliza Python, se recomienda ingresar el número "3", y automáticamente aparecerá el nombre completo de la imagen.

Finalmente, presione ``cargar``.

.. image:: /imgs/Reportes/ConfServido/6.png

Configuración de frontend de reportes
-------------------------------------

1. Acceda a la carpeta de apps.

2. Cree una carpeta unica para su reporte. Se recomienda utilizar el nombre del cliente.

3. Cree los archivos correspondientes.

Cada carpeta tiene el siguiente estándar:

- styles.css: Contiene los estilos del frontend.

- reporte_nombreReporte.html: Contiene la estructura del reporte.

- reporte_nombreReporte.js: Contiene la lógica para gestionar las peticiones con la API y mostrarlas en la estructura.

- reporte_nombreReporte_data.js: Contiene configuraciones de librerías que se utiliza, estas pueden ser para gráficos, tablas, entre otros. estas bibliotecas se pueden consultar en la sección bibliotecas. (HIPERVINCULO)

.. image:: /imgs/Reportes/ConfServido/8.png

4. Suba los archivos al repositorio.

5. Haga build del proyecto (solicite ayuda a soporte de Linkaform).

6. Configure el reporte en Linkaform, diríjase a la barra lateral izquierda y seleccionar la opción de ``Reporte``, la interfaz debe ser similar a la siguiente:

.. image:: /imgs/Reportes/ConfServido/2.png

.. note:: Los reportes que se hacen en linkaform son embebidos, esto significa que existe un enlace de servido que contiene todo el reporte perce.

7. Cree un reporte. Seleccione el ícono de documento en la sección de la barra superior derecha, al seleccionar el ícono, Linkaform mostrará una ventana emergente con tres ventanas, la ventana por defecto es **General** esta cuenta con tres campos: 

- **Nombre de reporte**: Nombre descriptivo que diferenciará al reporte.

- **URL**: Dirección de la demo que generó en servido.

- **Scripts**: Nombre del script que cargó anteriormente.

.. image:: /imgs/Reportes/ConfServido/10.png

En esta sección, ha aprendido a configurar el entorno de scripts y reportes. En las secciones posteriores, se proporcionará una explicación más detallada sobre el código que compone los archivos.