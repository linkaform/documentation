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

Configuración de archivos addons
================================

Concéntrese en el repositorio **addons** y ubique la carpeta **config**, la cual contiene archivos sobre configuraciones y todo lo necesario para ejecutar operaciones de creación y descarga de módulos. Siga las siguientes secciones para conocer más a detalle lo que compone cada archivo.

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
      <a>lkf</a><br>
      ├── <a>addons</a><br>
      │   ├── <a class="print">config</a><br>
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

Este archivo importa todo lo definido en `settings <#arch-settings>`_ :octicon:`report;1em;sd-text-info` (variables, funciones, clases, etc.), lo cual es útil para acceder fácilmente a las configuraciones definidas en ese archivo y usarlas en el script principal.

.. code-block:: python
   :linenos:

   # coding: utf-8
   #!/usr/bin/python
   from settings import *

.. _arch-settings:

Archivo settings
----------------

Las **settings** inicializan y cargan configuraciones generales y específicas desde diferentes archivos (settings.py, environment.py, local_settings.py) para configurar y ajustar el entorno de ejecución. Observe que utiliza configuraciones de la API de Linkaform.

Observe el bloque de código correspondiente al diccionario ``config`` (líneas 10-28). Este diccionario inicializa varias configuraciones con valores predeterminados. Incluye configuraciones relacionadas con:

- Bases de datos (``MONGODB_MAX_IDLE_TIME``, ``MONGODB_MAX_POOL_SIZE``)
- Autenticación (``USER_ID``, ``JWT_KEY``), uso de JWT (``USE_JWT``)
- Configuraciones para el servicio ``COUCH``.

Identifique las líneas 40 y 43, donde se importa todo lo definido en `environment <#arch-environment>`_:octicon:`report;1em;sd-text-info`. Estas son configuraciones del entorno de ejecución y actualizan las configuraciones en ``settings`` llamando a la función ``update_settings``.

El último bloque importa todo lo definido en `local settings <#arch-local-settings>`_:octicon:`report;1em;sd-text-info`, donde se define la configuración con las autenticaciones propias.

.. tip:: Lea los comentarios dentro del bloque de código para más detalles.
   
.. warning:: Por ningún motivo modifique este archivo.

.. code-block:: python
   :linenos:
   :emphasize-lines: 10-28, 40, 43, 46-52
      
   # coding: utf-8
   # print('=================== LODING SETTINGS FOR ENVIOIRMENT: {} ==================='.format(ENV))
   from linkaform_api import settings #Importa configuraciones de la API de Linkaform

   # Define rutas de los directorios
   MODULES_PATH = '/srv/scripts/addons/modules'
   ADDONS_PATH = '/usr/local/lib/python3.10/site-packages/lkf_addons/addons'

   # Diccionario con configuraciones predeterminadas
   config = {
      'COLLECTION' : 'form_answer',
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

   # Actualiza el diccionario 'config' utilizando credenciales del usuario.
   config.update({
               'USERNAME' : 'your_likaform_username@here.com',
               'APIKEY': 'your_APIKEY_HERE',
   })

   # Actualiza las configuraciones de 'settings' (API de Linkaform) con el diccionario 'config'
   settings.config.update(config)

   # Importa todas las definiciones desde 'environment.py'
   from enviorment import *

   # Actualiza las configuraciones en 'settings' llamando a la función 'update_settings'
   settings = update_settings(settings)

   # Intenta importar configuraciones adicionales desde 'local_settings.py'
   try:
      from local_settings import *
   # Si no se encuentra 'local_settings.py' o hay un error al importarlo
   except Exception as e:
      print('local_settings... NOT FOUND!!!', e)
      print('create a file with you own local_settings, just import this file with from  settings import * ')
      print('Then update your config with your own keys')
    
.. _arch-environment:

Archivo environment
-------------------

El siguiente código permite configurar y actualizar las variables clave y configuraciones específicas del entorno de ejecución. Asegúrese de ajustar el entorno de acuerdo a sus necesidades.
Para eso:

1. Identifique el bloque de entorno actual (líneas 6-8).
2. Descomente la línea de su elección y asegúrese de que las demás se encuentren comentadas.
3. Guarde los cambios del archivo.

.. tip:: Lea los comentarios dentro del bloque de código para más detalles.

.. warning:: No modifique otro contenido del bloque.

.. code-block:: python
   :linenos: 
   :emphasize-lines: 6-8
   
   # coding: utf-8
   # Importa el diccionario 'config' desde el módulo 'settings'
   from settings import config

   # Define el entorno actual
   ENV = 'preprod' 
   #ENV = 'local' 
   #ENV = 'prod' 
   
   # print('=================== LODING SETTINGS FOR ENVIOIRMENT: {} ==================='.format(ENV))
   # Obtiene las configuraciones actuales de 'mongo_hosts', 'PROTOCOL' y 'HOST' desde el diccionario 'config'
   mongo_hosts = config.get('mongo_hosts')
   PROTOCOL = config.get('PROTOCOL')
   HOST = config.get('HOST')

   # Configura valores específicos dependiendo del entorno
   if ENV == 'prod':
      mongo_hosts = 'db2.linkaform.com:27017,db3.linkaform.com:27017,db4.linkaform.com:27017'
      HOST = 'app.linkaform.com'
      PROTOCOL = 'https'

   elif ENV == 'preprod':
      mongo_hosts = 'dbs2.lkf.cloud:27918'
      HOST = 'preprod.linkaform.com'
      PROTOCOL = 'https'

   # Define el tamaño máximo del pool y el tiempo de espera de la cola para MongoDB
   MAX_POOL_SIZE = 1000
   WAIT_QUEUE_TIMEOUT = 1000
   # Construye la URI de MongoDB usando los 'mongo_hosts' configurados
   MONGODB_URI = 'mongodb://%s/'%(mongo_hosts)

   # Actualiza el diccionario 'config' con las nuevas configuraciones
   config.update({
         'PROTOCOL' : PROTOCOL,
         'HOST' : HOST,
         'MONGODB_PORT':27017,
         'MONGODB_HOST': mongo_hosts,
         #'MONGODB_URI': MONGODB_URI,
         'AIRFLOW_PROTOCOL' : 'https', #http or https
         'AIRFLOW_PORT' : 5000, #http or https
         'AIRFLOW_HOST' : 'airflow.linkaform.com',
         #'AIRFLOW_HOST' : 'airflow.linkaform.com',
      })

   # Función para actualizar las configuraciones en el objeto 'settings'
   def update_settings(settings):
      global config
      settings.config.update(config)
      return settings

.. _arch-uts:

Archivo uts
-----------

Las ``uts.py`` contienen funciones utiles que facilitan la integración y configuración con los módulos y modelos de la API de Linkaform.

- La función ``update_settings(settings)`` actualiza las configuraciones de ``settings`` utilizando la API de ``utils.Cache`` para obtener y configurar claves JWT y otras variables importantes como ``USER_ID`` y ``ACCOUNT_ID``. 

- La función ``get_lkf_api()`` verifica y valida la existencia del usuario a través de la API Key proporcionada en ``settings.config['APIKEY']`` (`archivo local settings <#arch-local-settings>`_:octicon:`report;1em;sd-text-info`).

- La función ``get_lkf_module()`` garantiza que la instancia de ``LKFModules`` esté completamente configurada con las credenciales y datos del usuario más recientes.

.. warning:: Por ningún motivo modifique este archivo.

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

.. _arch-local-settings:

Archivo local settings
----------------------

.. caution:: El archivo ``local_settings`` contiene información y configuraciones sensibles de la cuenta del cliente. 

El siguiente código permite configurar sus propias claves para su autenticación y asegurar que las configuraciones sean correctas y específicas para el entorno en el que se estará ejecutando.

1. Coloque el correo de la cuenta donde se instalará el módulo (linea 8).
2. Coloque el código alfanumérico de la APIKEY (linea 9)

.. seealso:: Consulte el siguiente apartado :ref:`generar-api-key` :octicon:`report;1em;sd-text-info` para consultar la API Key.

.. tip:: Lea los comentarios dentro del bloque de código para más detalles.

.. code-block:: python
   :linenos:
   :emphasize-lines: 8,9

   # coding: utf-8
   from settings import * # Importa todas las configuraciones desde 'settings'
   from uts import update_settings # Importa la función 'update_settings' desde 'uts'

   # Actualiza el diccionario 'config' con las credenciales del usuario
   config.update({
               #account_id = 20
               'USERNAME' : 'correo.electronico@linkaform.com',
               'APIKEY': '123456789101234567891012345678910'
   })

   # Actualiza las configuraciones en 'settings' con el diccionario 'config'
   settings.config.update(config)

   # Configura valores específicos dependiendo del entorno
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

   # Actualiza las configuraciones en 'settings' con el diccionario 'config'
   settings.config.update(config)

   # Llama a la función 'update_settings' para actualizar las configuraciones y las devuelve
   settings = update_settings(settings)

Configuración archivos API Key
==============================

Concéntrese en el repositorio **linkaform_api** y ubique el archivo **base.py** dentro de la carpeta **lkf_base** y el archivo **lkf_object.py** los cuales contienen configuraciones y funciones útiles al momento de instalar o crear nuevos módulos. Siga las siguientes secciones para conocer más a detalle lo que compone cada archivo.

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
         background-color: #E36414
      }
   </style>
   <body>
      <a>lkf</a><br>
      ├── <a>linkaform_api</a><br>
      │   ├── <a>__pycache__</a><br>
      │   ├── <a>lkf_base</a><br>
      │   │   ├── <a>__pycache__</a><br>
      │   │   ├── <a>__init__.py</a><br>
      │   │   ├── <a class="printf">base.py</a><br>
      │   ├── <a>models</a><br>
      │   ├── <a class="printf">lkf_object.py</a><br>
   <br><br><p>
   </body>
   </html>

Archivo lkf Object
------------------

En el siguiente bloque de código podrá encontrar una vista general del código completo del archivo. De los detalles más importantes que debe considerar:

La clase ``LKFBaseObject`` (linea 19), utilizada en `base <#arch-base>`_:octicon:`report;1em;sd-text-info`, contiene métodos para crear, leer, actualizar, editar, buscar y eliminar objetos en la base de datos de MongoDB.

.. tip:: Lea los comentarios dentro del bloque de código para más detalles.

.. code-block:: python
   :linenos:
   :emphasize-lines: 19

   # coding: utf-8
   #!/usr/bin/python

   # Bibliotecas de Python
   from bson import ObjectId
   from hashlib import sha1, md5
   import subprocess, jwt

   from .models.base_models import UserData
   from .mongo_util import connect_mongodb

   ##### LKF Object

   # Clase base para la búsqueda de módulos
   class LKFBase:
      def search_modules(self, path): ...

   # Clase que extiende LKFBase y agrega funcionalidades específicas
   class LKFBaseObject(LKFBase):
      
      def __init__(self, *, id: str, created_by: UserData, settings: dict,  object: str = None ):
         self.id = id
         self.created_by = created_by
         self.object = object
         self.cr_con = {}
         self.settings = settings
         self.config = settings.config

      # Método para manejar excepciones específicas de LKF
      def LKFException(self, msg): ...

      # Método para decodificar un JSON Web Token
      def decode_jwt(self): ...

      # Método para obtener datos del usuario
      def get_user_data(self): ...

      # Método para obtener la URI de MongoDB para una cuenta específica
      def get_mongo_uri(self, account_id): ...

      # Método privado para conectar a la base de datos
      def __conect_db(self): ...

      # Método para obtener un cursor de la base de datos
      def get_db_cr(self, _object=None, db_name=False, collection=False): ...

      # Método para editar un registro en la base de datos
      def _edit_record(self, cr, data): ...
        
      # Método para insertar un registro en la base de datos
      def _insert_record(self, cr, data): ...

      # Método para obtener datos del cursor
      def get_cr_data(self, _object=None, is_json=False, collection=False): ...

      # Método para crear un nuevo registro
      def create(self, _object, is_json=True, collection=False): ...

      # Método para actualizar un registro existente
      def update(self, query, data, replace=False): ...

      # Método para buscar registros en la base de datos
      def search(self, query): ...

      # Método para buscar un elemento del módulo
      def serach_module_item(self, item_info): ...
      
      # Método para eliminar un registro
      def delete(self, _object=None, query=False, is_json=False ): ...

.. _arch-base:

Archivo base
------------

En este archivo tenemos a la clase ``LKF_Base`` esta clase contiene varios métodos útiles al momento de programar nuevos módulos. Dentro de las más interesantes podrá encontrar:

- cache_get
- cache_read
- cache_set (crea o actualiza dependiendo. Simplemente hago el self.create y solo se le pasa el id y lo va  a crear)
- cache_update 

.. tip:: Consulte todos los métodos en el repositorio correspondiente.

.. code-block:: python
   :linenos:
   :emphasize-lines: 12

   # -*- coding: utf-8 -*-
   import sys, simplejson, arrow, time
   from datetime import datetime, date
   from bson import ObjectId
   import importlib
   from datetime import datetime
   from pytz import timezone

   from ..lkf_object import LKFBaseObject

   from linkaform_api import settings, network, utils, lkf_models

   class LKF_Base(LKFBaseObject):

      def __init__(self, settings, sys_argv=None, use_api=False): ...

      def _set_connections(self, settings):
         self.lkf_api = utils.Cache(settings)
         self.net = network.Network(settings)
         self.cr = self.net.get_collections()
         self.cr_wkf = self.net.get_collections('workflow_log')
         self.lkm = lkf_models.LKFModules(settings)
         return True

      def cache_get(self, values, **kwargs): ...

      def cache_read(self, values, **kwargs): ...

      def cache_set(self, values, **kwargs): ...
      
      def cache_update(self, values): ...

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
