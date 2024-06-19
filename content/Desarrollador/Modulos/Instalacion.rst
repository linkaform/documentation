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

Antes de comenzar a explicar a cerca del desarrollo de Módulos, considere los requisitos del perfil técnico para esta tarea. Este perfil debe contar con experiencia básica en:

- Git
- GitHub
- Python
- MongoDB
- Docker
- XML

A lo largo de la documentación, podrá encontrar orientación sobre los aspectos necesarios para la creación de su propio reporte personalizado.

Configuración del entorno
=========================

Antes de comenzar el desarrollo de módulos, asegúrese de que su entorno de trabajo esté correctamente configurado. A continuación, encontrará la documentación oficial de las herramientas necesarias para configurar su entorno:

- Si no cuenta con experiencia en **Mongodb** revise el curso de |mongodb| :octicon:`report;1em;sd-text-info` y posteriormente, continue con el curso de |mongodb-python| :octicon:`report;1em;sd-text-info`.

- También se sugiere revisar la documentación oficial de |Docker| :octicon:`report;1em;sd-text-info` e instalar la herramienta según sea necesario. Además, revise e instale |Docker-compose| :octicon:`report;1em;sd-text-info`.

- Si es necesario, revise la documentación de |GitHub| :octicon:`report;1em;sd-text-info` y |Git| :octicon:`report;1em;sd-text-info`.

Continue clonando los repositorios necesarios. Siga los pasos a continuación:

.. tip:: Se recomienda crear una carpeta que contenga los repositorios necesarios. En este caso, la carpeta ``lkf`` contendrá los repositorios ``linkaform_api`` y ``addons``.

Repositorio linkaform_api
-------------------------

1. Solicite acceso al repositorio de ``linkaform_api`` en GitHub a través del soporte técnico. 
2. Ingrese al siguiente enlace |linkaform_api| :octicon:`report;1em;sd-text-info` y clone el repositorio.

.. code-block::
    :linenos:

    git@github.com:linkaform/linkaform_api.git

Repositorio addons
------------------

1. Solicite acceso al repositorio de ``addons`` en GitHub a través del soporte técnico. 
2. Ingrese al siguiente enlace |linkaform_api| :octicon:`report;1em;sd-text-info` y clone el repositorio.

.. code-block::
    :linenos:

    git@github.com:linkaform/addons.git

.. note:: Observe que **addons** hace referencia al repositorio **modules**

   .. image:: /imgs/Modules/Modules1.png

Configuración de archivos
-------------------------

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

.. code-block:: python
    :linenos:

    # coding: utf-8
    from  settings import * 
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

   <a href="https://github.com/linkaform/linkaform_api" target="_blank">linkaform_api</a>

.. |addons| raw:: html

   <a href="https://github.com/linkaform/addons" target="_blank">addons</a>
