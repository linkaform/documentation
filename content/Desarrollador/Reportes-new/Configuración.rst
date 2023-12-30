======================
Desarrollo de reportes
======================

La creación de reportes es una funcionalidad que brinda a los clientes de **Linkaform** una perspectiva visual, resumida y agradable de los datos recopilados de las formas. Un reporte se construye siguiendo un conjunto de estándares y librerías establecidas por Linkaform.

.. important:: Tenga en cuenta que el desarrollo de reportes se basa en la información recopilada de las formas (formularios digitales), por lo que es importante comprender su funcionamiento. Consulte el siguiente enlace para revisar la documentación oficial de las :ref:`section-forms` :octicon:`report;1em;sd-text-info`.

Antes de comenzar a explicar el desarrollo de reportes, considere los requisitos del perfil técnico para esta tarea. Este perfil debe contar con experiencia básica en:

- HTML, CSS, Bootstrap
- Git
- GitHub
- Python
- JavaScript
- MongoDB
- Docker

A lo largo de esta sección, podrá encontrar orientación detallada sobre los aspectos necesarios para la creación de su propio reporte personalizado.

Configuración del entorno
=========================

Para comenzar el desarrollo de reportes en Linkaform, es importante asegurarse de que su entorno de trabajo esté correctamente configurado. A continuación, encontrará la documentación oficial de las herramientas necesarias para configurar su entorno:

.. seealso::

    Revise el curso de |mongodb| :octicon:`report;1em;sd-text-info` y posteriormente, continue con el curso de |mongodb-python| :octicon:`report;1em;sd-text-info`.

    También se sugiere revisar la documentación oficial de |Docker| :octicon:`report;1em;sd-text-info` e instalar la herramienta según sea necesario. Además, revise e instale |Docker-compose|.

    Si es necesario, revise la documentación de |GitHub| :octicon:`report;1em;sd-text-info` y |Git| :octicon:`report;1em;sd-text-info`.

Ahora, el segundo paso es clonar los repositorios necesarios para el desarrollo de reportes. Linkaform tiene repositorios específicos en GitHub y GitLab. Siga los pasos a continuación:

Repositorio servido
-------------------

1. Solicite acceso al repositorio de ``Servido`` a través del soporte técnico. 
2. Ingrese al siguiente enlace |Servido| :octicon:`report;1em;sd-text-info` y clone el repositorio.

.. code-block::
    :linenos:

    git@github.com:linkaform/servido.git

.. _run-docker:

3. Abra una terminal y navegue al directorio del repositorio de ``Servido`` y ``docker``, por ejemplo:

.. code-block::
    :linenos:

    cd lkf/servido/docker

.. note:: En este caso, tenga en cuenta que el repositorio de ``Servido`` está dentro de otra carpeta llamada ``lkf``.

4. Ejecute el siguiente comando para correr ``Servido`` localmente:

.. code-block::
    :linenos:
    
    docker-compose up -d  
    
En caso de contar con una versión actualizada de Docker:

.. code-block::
    :linenos:
    
    docker compose up -d

5. Compruebe que ``Servido`` esté en ejecución accediendo a:

.. code-block::
    :linenos:
    :caption: API en el puerto 5000
    
    http://127.0.0.1:5000

.. code-block::
    :linenos:
    :caption: Páginas web en el puerto 8011 

    http://127.0.0.1:8011/

.. note:: Consulte el archivo ``reedme.md`` del repositorio para más información.

Repositorio infosync_scripts
----------------------------

1. Solicite acceso al repositorio de ``infosync_scripts`` en GitLab a través del soporte técnico.
2. Ingrese al repositorio y clone el repositorio.

.. note:: Consulte el archivo ``reedme.md`` del repositorio para más información.

.. tip:: Se recomienda crear una carpeta que contenga ambos repositorios. En este caso, la carpeta ``lkf`` contendrá los repositorios ``Servido`` e ``infosync_scripts``. Esta organización facilitará la gestión y el acceso a ambos conjuntos de archivos. 

Bases de Servido
================

``Servido`` es una plataforma *Open Source* que facilita el desarrollo de reportes mediante el uso de diversas herramientas, como *bibliotecas*, *scripts* y *APIs*. Estas herramientas se utilizan para procesar información y generar resultados que se presentan a través de *dashboards*, *tablas*, *gráficos*, y otras representaciones visuales.

Las dos partes principales que complementan a ``Servido`` son las siguientes:

.. grid:: 2
   :gutter: 0

   .. grid-item-card:: Directory Tree
      :columns: 5

      .. raw:: html

         <!DOCTYPE html>
         <html>
         <head>
         <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
         <meta name="Author" content="Made by 'tree'">
         <meta name="GENERATOR" content="$Version: $ tree v2.0.2 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro $">
         </head>
         <style>
            .print{
               background-color: #E36414
            }
            .printf{
               background-color: #88AB8E
            }
         </style>
         <body>
            <a href=".">.</a><br>
            ├── <a>infosync_scripts</a><br>
            │   ├── <a>Nombre_carpeta</a><br>
            │   │   ├── <a>reporte_nombre.py</a><br>
            └── <a class="print">servido</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a  class="printf">apps</a><br>
            &nbsp;&nbsp;&nbsp; │   ├── <a>Nombre_carpeta</a><br>
            &nbsp;&nbsp;&nbsp; │   │   ├── <a>reporte_nombre_data.js</a><br>
            &nbsp;&nbsp;&nbsp; │   │   ├── <a>reporte_nombre.html</a><br>
            &nbsp;&nbsp;&nbsp; │   │   ├── <a>reporte_nombre.js</a><br>
            &nbsp;&nbsp;&nbsp; │   │   └── <a>style.css</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>docker</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>Dockerfile</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>libs</a><br>
            &nbsp;&nbsp;&nbsp; │   └── <a>tabulator</a><br>
            &nbsp;&nbsp;&nbsp; │   &nbsp;&nbsp;&nbsp; ├── <a">css</a><br>
            &nbsp;&nbsp;&nbsp; │   &nbsp;&nbsp;&nbsp; └── <a>js</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>README.md</a><br>
         </body>
         </html>

   .. grid-item-card:: Apps
      :columns: 7

      La carpeta ``Apps`` contenida en el repositorio de ``Servido`` alberga la totalidad del *front-end* (HTML, CSS, JavaScript vanilla y jQuery) del reporte. 
      
      .. note:: Cada carpeta está asignada a cada cliente, las cuales contienen sus propios reportes. 

      Dentro de ``Apps`` cree su propia carpeta exclusiva para sus reportes.
      
      .. important:: En caso de que ya cuente con una carpeta, asegúrese de crear los archivos correspondientes para el desarrollo de su nuevo reporte.

      Cada carpeta contiene los siguientes archivos:

      - **style.css**: Contiene estilos generales del reporte (un archivo por carpeta).

- **reporte_nombre.html**: Contiene la estructura del reporte.      
- **reporte_nombre.js**: Contiene la lógica encargada de gestionar las solicitudes a la *API*, así como de procesar y presentar la información correspondiente en la estructura establecida.
- **reporte_nombre_data.js**: Contiene configuraciones de librerías que se utilizan.

.. seealso:: Consulte la siguiente sección para obtener información detallada sobre la :ref:`estructura-archivos` :octicon:`report;1em;sd-text-info` que conforman a Servido.

.. grid:: 2
   :gutter: 0

   .. grid-item-card:: Infosync_scripts
      :columns: 7

      El contenido de ``infosync_scripts``, ubicado en el repositorio ``infosync_scripts``, contiene información correspondiente al *backend* del reporte. Cada carpeta alberga *scripts* utilizados por los clientes.

      Para nombrar un script específico para un reporte, siga el siguiente estándar de nomenclatura:

      .. code-block::
         :linenos:
         
         reporte_nombre_script.py

      .. caution:: Bajo ninguna circunstancia modifique los archivos que NO inicien con ``report``. Estos archivos son scripts que desempeñan funciones importantes para el cliente, aunque no estén directamente relacionados con reportes.

      .. important:: Tenga cuidado con el archivo ``account_settings.py``, ya que contiene información sensible de la cuenta del cliente.

   .. grid-item-card:: Directory Tree
      :columns: 5

      .. raw:: html

         <!DOCTYPE html>
         <html>
         <head>
         <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
         <meta name="Author" content="Made by 'tree'">
         <meta name="GENERATOR" content="$Version: $ tree v2.0.2 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro $">
         </head>
         <style>
            .print{
               background-color: #E36414
            }
         </style>
         <body>
            <a href=".">.</a><br>
            ├── <a class="print">infosync_scripts</a><br>
            │   ├── <a>Nombre_carpeta</a><br>
            │   │   ├── <a>reporte_nombre.py</a><br>
            └── <a>servido</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>apps</a><br>
            &nbsp;&nbsp;&nbsp; │   ├── <a>Nombre_carpeta</a><br>
            &nbsp;&nbsp;&nbsp; │   │   ├── <a>reporte_nombre_data.js</a><br>
            &nbsp;&nbsp;&nbsp; │   │   ├── <a>reporte_nombre.html</a><br>
            &nbsp;&nbsp;&nbsp; │   │   ├── <a>reporte_nombre.js</a><br>
            &nbsp;&nbsp;&nbsp; │   │   └── <a>style.css</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>docker</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>Dockerfile</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>libs</a><br>
            &nbsp;&nbsp;&nbsp; │   └── <a>tabulator</a><br>
            &nbsp;&nbsp;&nbsp; │   &nbsp;&nbsp;&nbsp; ├── <a">css</a><br>
            &nbsp;&nbsp;&nbsp; │   &nbsp;&nbsp;&nbsp; └── <a>js</a><br>
            &nbsp;&nbsp;&nbsp; ├── <a>README.md</a><br>
         </body>
         </html>

.. _url-acceso:

URLs de acceso
--------------

Una vez que haya configurado su entorno y desarrollado un reporte, es importante que comprenda las diversas formas de acceder a los reportes en Linkaform. La accesibilidad a los reportes se facilita mediante ``URLs`` específicas, brindando opciones como la visualización local con datos demo, la integración de un script, el acceso a través de servido y la posibilidad de trabajar en un entorno de prueba.

.. note:: Asegúrese de ejecutar previamente su contenedor `Docker <#run-docker>`_ :octicon:`report;1em;sd-text-info` e ingresar al enlace según lo requiera.
 
 .. _link-demo:

Local con datos demo
^^^^^^^^^^^^^^^^^^^^

Si desea obtener una vista previa del reporte antes de realizar la integración completa del script, considere y modifique la siguiente URL:

.. code-block::
   :linenos:
   
   http://127.0.0.1:8011/nombre_carpeta/reporte_nombre.html

Al modificar esta ``URL`` según su estructura de carpetas y el nombre del reporte específico, podrá visualizar una versión demo del reporte. Esto le brinda la oportunidad de recibir retroalimentación importante antes de la implementación final del script. 

.. _link-script:

Local con script integrado
^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta opción le brinda la posibilidad de integrar el script directamente en la ``URL``, indicando al reporte qué script debe utilizar.

.. code-block::
   :linenos:

   http://127.0.0.1:8011/nombre_carpeta/reporte_nombre.html?script_id=123456

Simplemente, añada el parámetro ``script_id`` a la ``URL`` seguido del valor correspondiente al script. Esto le indicará al script de JavaScript a dónde debe realizar la petición.

.. _link-servido:

Servido
^^^^^^^

Al acceder a través de ``Servido``, se solicitarán credenciales de autenticación debido a que la cookie utilizada para la autenticación no fue encontrada. Este proceso difiere de iniciar sesión en Linkaform y abrir reportes desde allí, donde la autenticación se realiza de manera automática gracias a las cookies.

.. note:: El usuario (correo) y la contraseña son los que se utilizan en producción.

.. code-block::
   :linenos:

   https://srv.linkaform.com/nombre_carpeta/reporte_nombre.html?script_id=123456

.. _link-env:

Entorno de prueba (Test Environment)
************************************

Si necesita acceder al entorno de prueba del reporte, asigne un argumento adicional a la ``URL``. Básicamente, se genera una cookie de autenticación, facilitando el desarrollo en un entorno controlado antes de realizar peticiones a producción. Esto es útil para aquellos que no cuentan con la contraseña de producción.

.. code-block::
   :linenos:

   http://127.0.0.1:8011/nombre_carpeta/reporte_nombre.html?script_id=123456&env=test 

Este enlace incluye un argumento adicional, ``&env=test``, que genera una cookie de autenticación al realizar la petición en el entorno de preproducción. 

.. note:: Solicite la contraseña de preproducción a soporte técnico.

Una vez dentro del entorno de prueba, puede proceder con normalidad sin la necesidad de incluir ``&env=test`` en futuras peticiones a producción. La contraseña de preproducción actúa como una llave maestra que puede utilizar en cualquier reporte que desarrolle y desee emplear en el entorno de preproducción.


















.. LIGAS EXTERNAS

.. |mongodb| raw:: html

   <a href="https://learn.mongodb.com/learning-paths/introduction-to-mongodb" target="_blank">MongoDB University</a>

.. |mongodb-python| raw:: html

   <a href="https://learn.mongodb.com/learning-paths/using-mongodb-with-python" target="_blank">MongoDB con Python</a>

.. |Docker| raw:: html

   <a href="https://docs.docker.com/" target="_blank">Docker</a>

.. |Docker-compose| raw:: html

   <a href="https://docs.docker.com/compose/install/" target="_blank">Docker compose</a>

.. |GitHub| raw:: html

   <a href="https://docs.github.com/es" target="_blank">Docker compose</a>

.. |Git| raw:: html

   <a href="https://git-scm.com/doc" target="_blank">Docker compose</a>

.. |Servido| raw:: html

   <a href="https://github.com/linkaform/servido" target="_blank">servido</a>

.. |Scripts| raw:: html

   <a href="https://gitlab.linkaform.com/develop/infosync_scripts" target="_blank">servido</a>


    