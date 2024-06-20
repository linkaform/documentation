.. _config-modules:

=======
Módulos
=======

En Linkaform, el término **módulo** hace referencia a un conjunto de formas y catálogos que se centran en ofrecer una funcionalidad específica. En este apartado, encontrará documentación sobre las funcionalidades que ofrece una forma, entre las que se incluyen:

- Configuración del entorno
- Instalación del módulo
- Plantillas
- Estructura de archivos

.. importante:: Tenga en cuenta que el desarrollo de módulos se basa en las estructuras de formas (formularios digitales) y catálogos, por lo que es importante que comprenda su funcionamiento. Consulte el siguiente enlace para revisar la documentación sobre :ref:`section-forms` :octicon:`report;1em;sd-text-info` y :ref:`catalogo` :octicon:`report;1em;sd-text-info`.

Antes de comenzar a explicar a cerca del desarrollo de módulos, considere los requisitos del perfil técnico para esta tarea. Este perfil debe contar con experiencia básica en:

- Git
- GitHub
- Python
- MongoDB
- Docker
- XML

.. seealso::

   - Si no cuenta con experiencia en **Mongodb** revise el curso de |mongodb| :octicon:`report;1em;sd-text-info` y posteriormente, continue con el curso de |mongodb-python| :octicon:`report;1em;sd-text-info`.
   - También se sugiere revisar la documentación oficial de |Docker| :octicon:`report;1em;sd-text-info` e instalar la herramienta según sea necesario. Además, revise e instale |Docker-compose| :octicon:`report;1em;sd-text-info`.
   - Si es necesario, revise la documentación de |GitHub| :octicon:`report;1em;sd-text-info` y |Git| :octicon:`report;1em;sd-text-info`.
   
   A lo largo de la documentación, podrá encontrar orientación sobre los aspectos necesarios para la creación e instalación de módulos.

Configuración del entorno
=========================

Repositorio linkaform api
-------------------------

1. Solicite acceso al repositorio de ``linkaform_api`` en GitHub a través del soporte técnico. 
2. Ingrese al siguiente |linkaform_api| :octicon:`report;1em;sd-text-info` y clone el repositorio.

.. code-block::
   :linenos:

   git clone git@github.com:linkaform/linkaform_api.git

.. note:: Lea detenidamente el archivo README del repositorio, cumpla con los requisitos y clone el repositorio.

Repositorio addons
------------------

1. Solicite acceso al repositorio de ``addons`` en GitHub a través del soporte técnico. 
2. Ingrese al siguiente |addons| :octicon:`report;1em;sd-text-info`. Observe que el repositorio **addons** hace referencia al submódulo **modules**.

.. image:: /imgs/Modules/Modules1.png

Cuando clona un repositorio con submódulos, de forma predeterminada obtiene los directorios que contienen los submódulos, pero ninguno de estos directorios contiene archivos. Para extraer el contenido de los submódulos, debe ejecutar dos comandos.

Para inicializar el archivo de configuración local de los submódulos:

.. code-block::
   :linenos:

   git submodule init

Para buscar todos los datos del proyecto y verificar el *commit* adecuado que figura en el proyecto:

.. code-block::
   :linenos:

   git submodule update

De manera simplificada, también puede ejecutar el siguiente comando para inicializar y actualizar automáticamente cada submódulo en el repositorio al clonar:

.. code-block::
   :linenos:

   git clone --recursive git@github.com:linkaform/addons.git

.. seealso:: Consulte la documentación de Git sobre |submodules| :octicon:`report;1em;sd-text-info` para más detalles.

.. tip:: Se recomienda crear una carpeta que contenga los repositorios necesarios. En este caso, la carpeta ``lkf`` contendrá los repositorios ``linkaform_api`` y ``addons``. Observe la estructura. 

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
         <a>lkf</a><br>
         ├── <a>addons</a><br>
         │   ├── <a>config</a><br>
         │   │   └── <a>__pycache__</a><br>
         │   ├── <a">docker</a><br>
         │   ├── <a">lkf_addons</a><br>
         │   │   ├── <a>addons</a><br>
         │   │   ├── <a>bin</a><br>
         │   │   └── <a>items</a><br>
         │   ├── <a>modules</a><br>
         │   │   ├── <a>accesos</a><br>
         │   │   ├── <a>employee</a><br>
         │   │   ├── <a>expenses</a><br>
         │   │   ├── <a>_module_template</a><br>
         │   │   ├── <a>product</a><br>
         │   │   ├── <a>stock</a><br>
         │   │   ├── <a>stock_greenhouse</a><br>
         │   │   └── <a>stock_lab</a><br>
         │   └── <a>test</a><br>
         │   &nbsp;&nbsp;&nbsp; ├── <a>conf</a><br>
         │   &nbsp;&nbsp;&nbsp; └── <a>docker</a><br>
         ├── <a>linkaform_api</a><br>
         │   └── <a>linkaform_api</a><br>
         │   &nbsp;&nbsp;&nbsp; ├── <a>config</a><br>
         │   &nbsp;&nbsp;&nbsp; ├── <a>lkf_base</a><br>
         │   &nbsp;&nbsp;&nbsp; ├── <a>models</a><br>
         │   &nbsp;&nbsp;&nbsp; └── <a>__pycache__</a><br>
      </body>
      </html>

Configuración de archivos
=========================

Concéntrese en el repositorio **addons** y ubique la carpeta **config**, la cual contiene archivos sobre configuraciones y todo lo necesario para ejecutar operaciones de creación y descarga de módulos. Siga las siguientes secciones para conocer más a detalle lo que compone cada archivo.

.. raw:: html

   <!DOCTYPE html>
   <html>
   <head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
   <meta name="Author" content="Made by 'tree'">
   <meta name="GENERATOR" content="$Version: $ tree v2.0.2 (c) 1996 - 2022 by Steve Baker, Thomas Moore, Francesc Rocher, Florian Sesser, Kyosuke Tokoro $">
   </head>
   <body>
      <a href=".">.</a><br>
      ├── <a>addons</a><br>
      │   ├── <a>config</a><br>
      │   │   ├── <a>account_settings.py</a><br>
      │   │   ├── <a>enviorment.py</a><br>
      │   │   ├── <a>local_settings.py</a><br>
      │   │   ├── <a>settings.py</a><br>
      │   │   └── <a>uts.py</a><br>
   <br><br><p>
   </body>
   </html>

Archivo account settings
------------------------

Este archivo importa todo lo definido en `settings <#arch-settings>`_ :octicon:`report;1em;sd-text-info` (variables, funciones, clases, etc.), lo cual es útil para acceder fácilmente a las configuraciones definidas en ese archivo y usarlas en tu script principal.

.. code-block:: python
   :linenos:

   # coding: utf-8
   #!/usr/bin/python
   from settings import *

.. _arch-settings:

Archivo settings
----------------

Las **settings** proporcionan la configuración inicial y la carga de ajustes para una aplicación Python, importando configuraciones desde el módulo ``api.settings`` y definiendo rutas de directorio importantes. 

Inicializa un diccionario ``config`` con valores predeterminados para configuraciones de base de datos, autenticación JWT y entornos COUCH, y luego lo actualiza con credenciales específicas. 

Posteriormente, actualiza las configuraciones en el módulo ``settings``, para el uso global en la aplicación, y ajusta el objeto ``settings`` llamando a una función ``update_settings``. 

Además, intenta cargar configuraciones adicionales desde ``local_settings.py``, proporcionando una advertencia si el archivo no se encuentra. 

Este archivo facilita la centralización y configuración inicial de variables clave y configuraciones específicas del entorno para la aplicación Python.

.. warning:: Por ningun motivo modifique este archivo.

.. code-block:: python
   :linenos:
      
   # coding: utf-8
   # print('=================== LODING SETTINGS FOR ENVIOIRMENT: {} ==================='.format(ENV))
   from linkaform_api import settings

   MODULES_PATH = '/srv/scripts/addons/modules'
   ADDONS_PATH = '/usr/local/lib/python3.10/site-packages/lkf_addons/addons'

   config = {
      'COLLECTION' : 'form_answer',
      # 'MONGODB_REPLICASET': 'linkaform_replica',
      # 'MONGO_READPREFERENCE': 'secondaryPreferred',
      'MONGODB_MAX_IDLE_TIME': 12000,
      'MONGODB_MAX_POOL_SIZE': 1000,
      'USER_ID' : '',
      'JWT_KEY': False,
      'USE_JWT': True,
      'COUCH_ENV':'prod',
      'COUCH_PROTOCOL':'http',
      'COUCH_USER':'',
      'COUCH_PASSWORD':'',
      'COUCH_HOST':'',
      'COUCH_PORT':'',
      'COUCH_DEV_PROTOCOL':'http',
      'COUCH_DEV_USER':'',
      'COUCH_DEV_PASSWORD':'',
      'COUCH_DEV_HOST':'',
      'COUCH_DEV_PORT':'',
   }

   config.update({
               'USERNAME' : 'your_likaform_username@here.com',
               'APIKEY': 'your_APIKEY_HERE',
   })

   settings.config.update(config)

   from enviorment import *

   settings = update_settings(settings)

   try:
      from local_settings import *
      # print('loaidng local_settings')
   except Exception as e:
      print('local_settings... NOT FOUND!!!', e)
      print('create a file with you own local_settings, just import this file with from  settings import * ')
      print('Then update your config with your own keys')

Archivo uts
-----------

El archivo ``utils.py`` facilita la integración y configuración de la aplicación con los módulos y modelos de API de Linkaform.

La función ``update_settings(settings)`` actualiza las configuraciones de ``settings`` utilizando la API de ``utils.Cache`` para obtener y configurar claves JWT y otras variables importantes como ``USER_ID`` y ``ACCOUNT_ID``. 

La función ``get_lkf_api()`` proporciona una instancia de ``utils.Cache`` configurada con las credenciales y configuraciones actuales, verificando la existencia y validez del usuario a través de la clave API proporcionada en ``settings.config['APIKEY']``. 

Finalmente, ``get_lkf_module()`` utiliza ``get_lkf_api()`` para obtener la configuración necesaria y luego instancia un objeto ``LKFModules`` de ``linkaform_api.lkf_models``, que proporciona funcionalidad adicional basada en las configuraciones y credenciales del usuario obtenidas. Este archivo es crucial para la interacción fluida y segura con los módulos y modelos específicos de ``linkaform_api`` dentro del entorno de la aplicación Python.

.. code-block:: python
   :linenos:

   # coding: utf-8

   #Utils for using LinkaFrom modules...
   from linkaform_api import utils, lkf_models
   import settings 

   def update_settings(settings):
      lkf_api = utils.Cache(settings)
      user = lkf_api.get_jwt(api_key=settings.config['APIKEY'], get_user=True)
      settings.config["JWT_KEY"] = user.get('jwt')
      settings.config["APIKEY_JWT_KEY"] = user.get('jwt')
      account_id = user['user']['parent_info']['id']
      settings.config["USER_ID"] = user['user']['id']
      settings.config["ACCOUNT_ID"] = account_id
      settings.config["USER"] = user['user']
      settings.config["MONGODB_USER"] = 'account_{}'.format(account_id)
      return settings

   def get_lkf_api():
      lkf_api = utils.Cache(settings)
      user = lkf_api.get_jwt(api_key=settings.config['APIKEY'], get_user=True)
      if not user:
         raise ('User not found or incorrecto APIKEY ')
      settings.config["JWT_KEY"] = user.get('jwt')
      settings.config["ACCOUNT_ID"] = user['user']['parent_info']['id']
      settings.config["USER"] = user['user']
      lkf_api = utils.Cache(settings)
      return lkf_api

   def get_lkf_module():
      lkf_api = get_lkf_api()
      settings = lkf_api.settings
      lkf_modules = lkf_models.LKFModules(settings)
      user = lkf_api.get_jwt(api_key=settings.config['APIKEY'], get_user=True)
      settings.config["JWT_KEY"] = user.get('jwt')
      settings.config["ACCOUNT_ID"] = user['user']['parent_info']['id']
      settings.config["USER"] = user['user']
      lkf_modules = lkf_models.LKFModules(settings)
      return lkf_modules
    
Archivo enviorment
------------------

Archivo local settings
------------------------

.. caution:: El archivo ``local_settings`` desarrollado en ``python`` contiene información y configuraciones sensibles de la cuenta del cliente. 

.. code-block:: python
    :linenos:

    # coding: utf-8
    from settings import * # Configuraciones de la api
    from uts import update_settings

    config.update({
                #account_id = 20
                'USERNAME' : 'correo.electronico@linkaform.com',
                'APIKEY': '123456789101234567891012345678910'

    })

    settings.config.update(config)

    if ENV == 'local':
        mongo_hosts = '192.168.0.25:27017'
        
    if ENV == 'local':
        config.update({
                'MONGODB_HOST':mongo_hosts,
                #'MONGODB_URI' : 'mongodb://%s/'%(mongo_hosts),
                'PROTOCOL' : 'http', #http or https
                'HOST' : '192.168.0.25:8000',
                'AIRFLOW_PROTOCOL' : 'https', #http or https
                'AIRFLOW_PORT' : 5000, #http or https
                'AIRFLOW_HOST' : 'af.linkaform.com',
                #'AIRFLOW_HOST' : 'airflow.linkaform.com',
            })

    settings.config.update(config)

    settings = update_settings(settings)

1. Crear archivo local_settings y colocar correo, apikey 

.. seealso:: Consulte el siguiente apartado :ref:`generar-api-key` :octicon:`report;1em;sd-text-info` para consultar la API Key.

2. Configurar el entorno de preprod en el archivo enverioment
3. Correr el contenedor de addons con 

.. code-block:: 
    :linenos:

    cd lkf/addons/

    ./lkf -ar start addons

4. Crear archivo local_settings y colocar correo, apikey 

.. seealso:: Consulte el siguiente apartado :ref:`generar-api-key` :octicon:`report;1em;sd-text-info` para consultar la API Key.

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

   <a href="https://docs.github.com/es" target="_blank">GitHub</a>

.. |Git| raw:: html

   <a href="https://git-scm.com/doc" target="_blank">Git</a>

.. |linkaform_api| raw:: html

   <a href="https://github.com/linkaform/linkaform_api" target="_blank">enlace</a>

.. |addons| raw:: html

   <a href="https://github.com/linkaform/addons" target="_blank">enlace</a>

.. |submodules| raw:: html

   <a href="https://git-scm.com/book/es/v2/Herramientas-de-Git-Subm%C3%B3dulos" target="_blank">submódulos</a>
