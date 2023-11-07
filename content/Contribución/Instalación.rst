===========
Instalación
===========

En esta sección se presentan los pasos necesarios para instalar Sphinx en su sistema, ya sea que esté trabajando en un sistema operativo Windows o Linux.

.. important:: Como requisito previo, es importante tener conocimientos básicos sobre Git.

Configuración del entorno
=========================

Linkaform utiliza ``GitHub``, que se basa en ``Git``, para administrar sus repositorios y Git para el control de versiones, lo que permite gestionar y rastrear cambios en el código o el proyecto.

Si ya dispone de una cuenta en GitHub y tiene Git instalado, puede omitir los primeros pasos y continuar con el paso 6 en :ref:`git`, comenzando así a realizar cambios locales en la documentación. De lo contrario, siga las siguientes instrucciones para preparar su entorno.

GitHub
------

A continuación, se presentan configuraciones básicas sobre GitHub. 

.. _GitHub:

1. Cree una cuenta en `GitHub <https://github.com/join/>`_ :octicon:`report;1em;sd-text-info`. 

.. _git:

Git
---

Siga los siguientes pasos para la instalación de Git en Windows o Linux:

.. tab-set::

    .. tab-item:: Windows

        1. Descargue el instalador de Git desde el sitio web oficial: `gitforwindows.org <https://gitforwindows.org/>`_ :octicon:`report;1em;sd-text-info`.

        2. Ejecute el instalador y siga las instrucciones. Puede aceptar las configuraciones por defecto o personalizarlas según sus preferencias.

        3. Elija si desea usar Git desde la línea de comandos o con Git Bash durante la instalación.

        .. tip:: Se recomienda usar Git Bash.

        4. Verifique que Git se instaló correctamente abriendo Git Bash o la línea de comandos de Windows y ejecute:
        
        .. code-block::
            
            git --version

        Siga el siguiente video si tiene dudas.

        .. youtube:: wHh3IgJvXcE
            :aspect: 16:9
            :width: 640
            :height: 360
            :align: center
            :privacy_mode: enable_privacy_mode
            :url_parameters: ?start=100

    .. tab-item:: Linux

        Git no viene preinstalado en la mayoría de las distribuciones de Linux por defecto, pero está ampliamente disponible.

        1. Abra una terminal en su sistema Linux.

        2. Actualice la lista de paquetes con el comando:

        .. code-block::

            sudo apt update

        3. Instale Git con el siguiente comando:

        .. code-block::

            sudo apt install git

        4. Verifique la instalación usando:

        .. code-block::

            git --version

Después de la instalación, las configuraciones básicas de Git son las mismas en Windows y Linux.

5. Configure Git para su identificacion como autor de futuras contrubuciones.

.. code-block::
    :caption: Nombre de usuario

    git config --global user.name "Su Nombre"

.. code-block::
    :caption: Dirección de correo electrónico:

    git config --global user.email "su@email.com"

.. important:: Utilice el mismo correo electrónico que utilizó para registrarse en :ref:`GitHub`.

.. youtube:: wHh3IgJvXcE
    :aspect: 16:9
    :width: 640
    :height: 360
    :align: center
    :privacy_mode: enable_privacy_mode
    :url_parameters: ?start=311

6. Genere una `clave SSH <https://docs.github.com/es/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/>`_ :octicon:`report;1em;sd-text-info` y registrela en su cuenta GitHub. Si tiene dudas puede seguir el siguiente video tutorial.

.. youtube:: wHh3IgJvXcE
    :aspect: 16:9
    :width: 640
    :height: 360
    :align: center
    :privacy_mode: enable_privacy_mode
    :url_parameters: ?start=496

7. Dirijase al repositorio de la documentación en `github.com/linkaform/documentation <https://github.com/linkaform/documentation/>`_ :octicon:`report;1em;sd-text-info`.

8. Clone el repositorio.

.. image:: /imgs/Contribución/22.png

.. code-block::

    git clone git@github.com:linkaform/documentation.git

El contenido principal se encuentra en la rama ``develop``. Por defecto, usted se encontrará en la rama ``main``. Para cambiar de rama puede usar ``checkout`` o ``switch``:

.. code-block:: 

    git checkout develop

.. code-block::

    git switch develop


Una vez que comience sus modificaciones y esté seguro de sus cambios haga ``push`` en la rama ``develop``.

.. code-block::

    git push origin develop

.. important:: Es importante hacer `git pull <https://git-scm.com/docs/git-pull/>`_ :octicon:`report;1em;sd-text-info` antes de `git push <https://git-scm.com/docs/git-push/>`_ :octicon:`report;1em;sd-text-info`.


Python
------

Si ya cuenta con la instalación de ``Python`` y ``pip``,  continúe con la configuración de :ref:`docker`. Si aún no los tiene, siga los siguientes pasos para la instalación.

.. tab-set::

    .. tab-item:: Windows

        1. Descargue ``Python`` en el sitio web oficial `python.org <https://www.python.org/downloads/windows/>`_ :octicon:`report;1em;sd-text-info` (seleccione la versión estable y adecuada para su sistema).

        2. Ejecute el instalador y siga las instrucciones del instalador. Marque la opción "Add python.exe to PATH". Esto agregará Python al PATH del sistema, lo que te permitirá ejecutar ``Python`` y ``pip`` desde la línea de comandos.

        3. Siga los pasos y verifique la instalación abriendo una ventana de comandos y ejecute:

        .. code-block::

            python --version
            pip --version

        Puede consultar el siguiente video.

        .. youtube:: nXgxe3JM7Rc
            :aspect: 16:9
            :width: 640
            :height: 360
            :align: center
            :privacy_mode: enable_privacy_mode
            :url_parameters: ?start=7

    .. tab-item:: Linux

        En sistemas basados en Linux, ``Python 3`` suele venir preinstalado. Sin embargo, para asegurarse de tener la última versión de y ``Python`` y ``pip``, siga los siguientes pasos:

        1. Actualice la lista de paquetes:

        .. code-block::

            sudo apt update

        2. Instale ``Python 3`` y ``pip``.

        .. code-block::

            sudo apt install python3 python3-pip

        3. Verifique la instalación:

        .. code-block::

            python3 --version
            pip3 --version

.. _docker:

Docker
------

.. tab-set::

    .. tab-item:: Windows

        Esto es una guía breve de como instalar Docker, sin embargo, para màs detalles consulte la documentación oficial de `Docker Desktop en Windows <https://docs.docker.com/desktop/install/windows-install/>`_ :octicon:`report;1em;sd-text-info`. 
                    
        1. Descargue `Docker Desktop <https://docs.docker.com/desktop/install/windows-install/>`_ :octicon:`report;1em;sd-text-info` en el sitio web oficial de Docker.

        2. Ejecuta el instalador y siga las instrucciones.

        3. Inicie Docker Desktop.

        4. Verifique la instalación:

        .. code-block::

            docker --version

        Puede consultar el siguiente video en caso de tener dudas con las configuraciones.

        .. youtube:: vP3DlhXmsBU
            :aspect: 16:9
            :width: 640
            :height: 360
            :align: center
            :privacy_mode: enable_privacy_mode
            :url_parameters: ?start=5

La instalación de Docker en Linux es más compleja y puede variar según la distribución y sus dependencias. Para una instalación exitosa, consulte la `documentación oficial de Docker Desktop en Linux <https://docs.docker.com/desktop/install/linux-install/>`_ :octicon:`report;1em;sd-text-info` y siga los pasos específicos de su distribución. Cada distribución puede requerir pasos diferentes.

.. tab-set::

    .. tab-item:: Ubuntu

        Para la instalación de docker en la distribución Ubuntu de Linux puede seguir el siguiente video tutorial:

        .. youtube:: mVVepIzpypQ
            :aspect: 16:9
            :width: 640
            :height: 360
            :align: center
            :privacy_mode: enable_privacy_mode
            :url_parameters: ?start=150

.. _generar_HTML:

Generación de documentación
---------------------------

Al tener su entorno listo y configurado correctamente, pruebe el contenido que se encuentra en el repositorio.

Sphinx (herramienta de software utilizada para generar documentación) lleva a cabo el proceso de conversión de documentos en formato reStructuredText (rst) a HTML. Este proceso solo es posible cuando se tienen documentos escritos y estructurados en ``rst`` y después de haber configurado el proyecto de Sphinx en archivo ``conf.py``.

.. important:: Al trabajar en un contenedor de Docker, el proceso de build difiere del que se muestra en la documentación principal de Sphinx.

Para llevar a cabo el `build` de su documentación, siga los siguientes pasos.

1. En su terminal, navegue a la carpeta que corresponde a la documentación.

.. code-block::

    cd documentation
    
3. Ejecute el siguiente comando.

.. code-block::

    docker-compose up -d

O si tiene la versión más reciente de docker, ejecute el siguiente comando.

.. code-block::

    docker compose up -d

La instrucción anterior se utiliza para iniciar y ejecutar el contenedor de la aplicación sin bloquear la terminal y permitir que los contenedores sigan ejecutandose en segundo plano.

4. Después de ejecutar su contenedor Docker, ejecute el siguiente comando.

.. code-block::

    docker exec -it lkf-documentation bash

La instrucción se utiliza para abrir una sesión dentro del contenedor ``lkf-documentation`` utilizando el shell Bash. Esto permite ejecutar comandos dentro del contenedor como si estuviera en una terminal dentro de ese entorno.

5. Como último paso, ejecute el siguiente comando según su SO.

.. tab-set::

    .. tab-item:: Windows

        .. code-block::

            bash local_build
            
    .. tab-item:: Linux
        
        .. code-block::

            local_build
        
        .. image:: /imgs/Contribución/16.png


El comando anterior es la que se encarga de hacer build (generar el contenido). En caso de cometer algún error, podrá verlo en la terminal.

Para poder ver el resultado, diríjase a la carpeta ``build`` y abra el archivo ``index.html`` en su navegador de preferencia.

.. code-block::

    cd documentation/build/index.html

¡Felicidades! 🎉 Ha logrado configurar su entorno y ejecutar la documentación disponible. Si tiene alguna duda, puede regresar al contenido o consultar la documentación de la sección de su preferencia. También puede comenzar a crear sus primeras secciones personalizadas con la ayuda de la siguiente sección.
