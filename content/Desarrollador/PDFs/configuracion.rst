==================
Desarrollo de PDFs
==================

En esta sección, encontrará plantillas disponibles, la estructura de archivos necesaria y la configuración requerida para crear sus propios documentos en formato pdf. 

Configuración del entorno
=========================

Para comenzar el desarrollo de PDFs en Linkaform, es importante que prepare y configure su entorno de trabajo. Siga los siguientes apartados para más información.

.. _conf-django:

Administración de Django
------------------------

La administración de Django es la interfaz que permite realizar operaciones CRUD (crear, leer, actualizar, borrar) con los registros de las formas. Para configurar la administración de Django, siga los siguientes pasos:

1. Inicie sesión en |prodDjango| :octicon:`report;1em;sd-text-info` o desde |preprodDjango| :octicon:`report;1em;sd-text-info`.

.. note:: Solicite a soporte técnico el acceso y las credenciales necesarias de la administración de Django. 
    
    El proceso de configuración en producción y preproducción es idéntico. Sin embargo, se recomienda iniciar la configuración en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

.. image:: /imgs/PDF/pdf16.png

Una vez autenticado, se muestra la interfaz principal de la administración de Django. Observe que tiene acceso a una variedad de recursos, sin embargo, con el propósito de abordar el desarrollo de archivos PDF, la explicación se centra en la sección ``Pdfdocuments``, que consta de dos elementos clave: 

.. list-table::
   :widths: 20 80
   :header-rows: 1
   :align: left

   * - Opción
     - Descripción
   * - Plantillas
     - Contiene todas las plantillas creadas en la plataforma.
   * - Widgets
     - Proporciona plantillas adaptadas a los diferentes tipos de datos utilizados.

.. image:: /imgs/PDF/pdf15.png

En cuanto a las plantillas, encontrará la siguientes opciones:

.. tab-set::

    .. tab-item:: Agregar
        
        La opción ``Agregar`` permite configurar una nueva plantilla. Siga los siguientes pasos:

        .. grid:: 2
            :gutter: 0
            :padding: 0
            :margin: 0

            .. grid-item-card::
                :columns: 6
                :padding: 0
                :margin: 0
                
                **Name**: Nombre de la plantilla.

                .. note:: Para el nombre de una plantilla se sigue el siguiente estándar: ::
                    
                    [nombre_cliente] [-] [nombre_PDF]

                .. _type:

                **Type**:

                - Single Record (registro único): Plantilla que se centra en un solo conjunto de datos. Es decir, presenta información de un solo registro del formulario.

                - Multiple Records (múltiples registros): Plantilla para presentar información de múltiples registros pertenecientes al mismo formulario

                .. important:: Es obligatorio que seleccione el tipo de PDF. Aunque el proceso de configuración es el mismo, la programación difiere según el tipo seleccionado.
                
                **Paginate:** Permite agregar paginación al documento. Es opcional ya que se puede personalizar en la programación.

            .. grid-item-card::  
                :columns: 6
                :padding: 0
                :margin: 0

                .. image:: /imgs/PDF/4.png
                    :align: center

            .. grid-item-card::
                :columns: 12
                :padding: 0
                :margin: 0

                **Description**: Descripción breve que ayuda a diferenciar entre documentos.

                .. note:: La descripción de un documento está estandarizada con la siguiente notación: ::
                    
                    [Template] [de] [nombre_PDF] [para] [nombre_cliente]

                **Default**: Define la plantilla por defecto para la forma cuando no se ha seleccionado ninguna en la :ref:`vincular` :octicon:`report;1em;sd-text-info`.

                .. attention:: Este campo suele estar establecido en *falso* de manera predeterminada.

                **Header**: Código del encabezado del documento en formato ``XML`` (requerido).

                **Body**: Código del cuerpo del documento en formato ``XML`` (requerido).

                **Footer**: Código del pie de página del documento en formato ``XML`` (requerido).

                **Style**: Código de los estilos usados en formato ``XML`` (requerido).

                .. note:: Los campos relacionados al ``XML`` son archivos que se desarrollan según el requerimiento del boceto del cliente o el diseño realizado.
                    
                **Owner**: Nombre de la cuenta padre a la que se va asignar la plantilla.

                .. dropdown:: Tip selector **Owner**

                    Debido a que el selector ``Owner`` contiene muchas opciones de cuentas de usuarios actuales, puede llevar tiempo buscar la cuenta de su interés entre tantas opciones. Para simplificar la búsqueda, siga estos pasos:

                    1. Inspeccione la pagina haciendo ``clic derecho > Inspeccionar`` o presionando directamente ``F12``.
                    2. Presione la opción de seleccionar y ubíquese en la pestaña de ``Elements`` de la página para inspeccionar los elementos del DOM en la parte superior izquierda o presione directamente ``Ctrl + Shift + C``.

                    .. image:: /imgs/PDF/pdf22.png

                    3. Haga clic en el selector de ``Owner``.

                    .. image:: /imgs/PDF/pdf19.png
                    
                    4. Abra el elemento que contiene a las opciones del selector.
                        
                    .. image:: /imgs/PDF/pdf20.png
                        :width: 500px
                        :height: 150px

                    5. Presione ``Ctrl + F`` e ingrese el nombre o Valor del ``ID`` de la cuenta de su interés para buscar entre las opciones.
                    6. Haga doble clic en la opción de su interés e ingrese la palabra ``selected`` y presione ``Enter``. Automáticamente la opción sera seleccionada.

                    .. important:: Revise que el ``ID`` de la opción corresponda a la cuenta de su interés.

                    .. image:: /imgs/PDF/pdf21.png

    .. tab-item:: Modificar

        La opción ``Modificar`` presenta una lista de plantillas existentes actualmente utilizadas por clientes de Linkaform. Para editar una plantilla, simplemente seleccione el nombre de la plantilla de su preferencia.

        Para agregar y configurar una nueva plantilla presione la opción ``Agregar plantilla``.

        .. image:: /imgs/PDF/pdf17.png

    .. tab-item:: Eliminar

        Para eliminar una plantilla, seleccione la casilla o casillas correspondientes y elija la opción en el selector, seguido del botón ``Ejecutar``.

        .. warning:: Tenga cuidado y verifique que haya seleccionado la plantilla correcta. Una vez ejecutada la acción, no podrá deshacerse.

        .. image:: /imgs/PDF/pdf18.png

Repositorio de PDFs
-------------------

El repositorio que contiene los PDFs actuales se encuentra en un repositorio de |github| :octicon:`report;1em;sd-text-info`. Este repositorio es exclusivo para usuarios de Linkaform, utilice git para realizar cambios y contribuciones locales. 

.. seealso:: Si aún no está familiarizado con Git, se recomienda que revise la |git| :octicon:`report;1em;sd-text-info` para obtener más detalles.

Siga las siguientes instrucciones para clonar el repositorio:

1. Solicite acceso al repositorio de PDFs a través de soporte técnico.
2. Ingrese al siguiente |gitPDF| :octicon:`report;1em;sd-text-info` y clone el repositorio.
3. Clone directamente utilizando: ::

    git@github.com:linkaform/PDFTemplates.git

.. tip:: Se recomienda tener una carpeta exclusiva para repositorios pertenecientes a Linkaform.

Plantillas
==========

Para el desarrollo de un PDF, se requieren cuatro archivos: un **encabezado**, **cuerpo**, **pie de página** y un archivo de **estilos**.

Aunque es posible insertar el encabezado, pie de página y estilos directamente en el cuerpo del PDF, así como tener un único archivo de estilos para todos los PDFs de un cliente en específico, se recomienda separar los archivos para mantener un orden y cumplir con los requisitos del `administrador de Django <#conf-django>`_ :octicon:`report;1em;sd-text-info`.

.. mermaid::

   graph TB
     
   A(PDF)
   A --> B[header.xml]
   A --> C[body.xml]
   A --> D[footer.xml]
   A --> E[style.xml]

En el repositorio **PDFTemplates**, identifique la carpeta ``Básico``, aquí podrá encontrar plantillas que servirán como base para la creación de nuevos PDFs.

.. grid:: 1
    :gutter: 0

    .. grid-item-card:: Directory Tree
        :columns: 12

        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style type="text/css">
            </style>
            </head>
            <style>
                .print{
                background-color: #627254
                }
            </style>
            <body>
                <a>.</a><br>
                ├── <a class="print">Básico</a><br>
                │   └── <a class="printf">example_body.xml</a><br>
                │   └── <a class="printf">example_footer.xml</a><br>
                │   └── <a class="printf">example_header.xml</a><br>
                │   └── <a class="printf">example_style.xml</a><br>                
            </body>
            </html>

.. caution:: El repositorio **PDFTemplates** contiene plantillas e información perteneciente a clientes de Linkaform. Si tiene acceso, es importante que considere que la información contenida es de suma importancia y confidencial. Por lo tanto, se solicita que tenga discreción con la información.

Si ya dispone con una carpeta, agregue los archivos necesarios para el nuevo PDF. De lo contrario, cree una nueva carpeta utilizando el nombre de la empresa o cliente como identificador y agregue los archivos necesarios dentro de ella.

.. note:: Para nombrar a los archivos utilice la convención |snake_case| :octicon:`report;1em;sd-text-info`.

Si dentro de su carpeta solo tiene un proyecto, utilice el nombre de la empresa o cliente seguido del tipo de archivo. Por ejemplo: 

.. code:: html

    [nombre_cliente] [_] [tipo_archivo] [.xml]

    pintasco_header.xml

.. grid:: 2
    :gutter: 0  

    .. grid-item-card:: 
        :columns: 6

        Si dentro de su carpeta tiene más de un PDF, utilice el nombre del PDF como identificador. Por ejemplo: ::

            [nombre_pdf] [_] [tipo_archivo] [.xml]

            gastos_semanales_body.xml

    .. grid-item-card:: Directory Tree
        :columns: 6

        .. raw:: html

            <!DOCTYPE html>
            <html>
            <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <style type="text/css">
            </style>
            </head>
            <style>
                .print{
                background-color: #E36414
                }
            </style>
            <body>
                <a href=>.</a><br>
                ├── <a class="print">Pintasco</a><br>
                │   └── <a class="printf">gastos_semanales_body.xml</a><br>
                │   └── <a class="printf">gastos_semanales_footer.xml</a><br>
                │   └── <a class="printf">gastos_semanales_header.xml</a><br>
                │   └── <a class="printf">gastos__semanales_style.xml</a><br>                
            </body>
            </html>  

.. _estructura:

Estructura de archivos
----------------------

Revise las siguientes secciones sobre la estructura de los archivos que componen un PDF. El código es genérico y puede ser utilizado para proyectos futuros según sea necesario.

.. important::

    En los siguientes ejemplos, observe que se utilizan etiquetas similares a HTML, estas pertenecen a RML. Consulte :ref:`report_markup_language` :octicon:`report;1em;sd-text-info` en la documentación para obtener más detalles.

    También encontrará líneas que contienen ``{% %}`` o ``{{ }}``, las cuales representan etiquetas y variables del lenguaje de plantillas de Django. Para obtener más información consulte la sección :ref:`rml_django` :octicon:`report;1em;sd-text-info` en la documentación.

Estructura body
^^^^^^^^^^^^^^^

El cuerpo del documento es la parte más importante. Similar a HTML, aquí se especifica la estructura de los elementos que compondrán al PDF, tales como tablas, imágenes, texto, etc.

El siguiente bloque de código solamente representa la configuración del documento, que incluyen propiedades como el tamaño de la página, márgenes, tipografía, etc. Sin embargo, para estructurar los elementos del PDF, deberá insertar su propio código entre las etiquetas ``<story>`` (líneas 40, 43).

.. hint:: Dentro del bloque de código, asegúrese de revisar los comentarios para obtener más contexto sobre cómo se estructura y configura el documento PDF.

.. code-block:: xml
    :linenos:
    :emphasize-lines: 40, 43

    <?xml version="1.0"?>
    <!-- Variables de Django - No se mueve-->
    {% load PrintFields %}
    {% load set_var %}
    {% load custom_tags %}
    <!-- Configuración del documento -->
    <document filename="Example" xmlns:doc="http://namespaces.zope.org/rml/doc">
        <!-- Propiedades informativas del documento -->
        <pageInfo pageSize="(21cm,27.5cm)" doc:example="" />
        <!-- Tipografía del documento -->
        <docinit>
            <registerTTFont faceName="Montserrat-Regular" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Regular.ttf" />
            <registerTTFont faceName="Montserrat-Bold" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Bold.ttf" />
            <registerTTFont faceName="Montserrat-BoldItalic" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-BoldItalic.ttf" />
        </docinit>
        <!-- En Template se define el tamaño (pageSize) y margen de la página (frame y sus atributos) -->
        <template pageSize="(22cm,28cm)" title="Examples" author="LinkaForm">
            <pageTemplate id="first">
                <frame id="first"    x1="1.5cm"   y1="1.5cm" width="19cm"   height="25cm"/>
                <pageGraphics>
                    <setFont name="Montserrat-Regular" size="7.5"/>
                    <setFont name="Montserrat-Regular" size="8"/>
                    <!-- drawCenteredString - No se mueve -->
                    <drawCenteredString x="10.5cm" y="27.8cm">
                    {{direccion}}
                    </drawCenteredString>
                    <!-- Cabecera de documento (opcional) -->
                    {% Header company_logo parent user form Template meta %}
                    <!-- Pie del documento (opcional) -->
                    {% Footer user form Template meta %}
                </pageGraphics>
            </pageTemplate>
        </template>
        <!-- stylesheet - No se mueve -->
        <stylesheet>
            {% autoescape on %}
            {{ Template.style|safe }}
            {% endautoescape %}
        </stylesheet>
        <story>
            <!-- Aquí va el código de los elementos del pdf -->
            <para>Hello world</para>
        </story>
    </document>

Estructura header y footer
^^^^^^^^^^^^^^^^^^^^^^^^^^

El encabezado del documento suele contener información como el logotipo, títulos y datos de identificación del cliente o del registro. Para rellenar el campo en el `administrador de Django <#conf-django>`_ :octicon:`report;1em;sd-text-info`, utilice el siguiente código base:

.. code-block:: xml
    :linenos:

    <drawRightString x="12cm" y="25cm"></drawRightString>

El pie de página del documento puede incluir información adicional, como datos de contacto, notas importantes o número de páginas. Aunque regularmente los documentos PDF no cuentan con un pie de página, es importante adjuntar algo en el `administrador de Django <#conf-django>`_ :octicon:`report;1em;sd-text-info`. Para ello, puede utilizar la siguiente etiqueta:

.. code-block:: xml
    :linenos:

    <drawRightString x="19.5cm" y="0.85cm">Página <pageNumber/> de <getName id="LASTPAGENO"/></drawRightString>

Para incluir elementos del ``header`` y ``footer`` en el cuerpo del documento, utilice **etiquetas** y **custom tags** especiales de Django y Linkaform dentro de ``<pageGraphics>``. 

En la sección :ref:`report_markup_language` :octicon:`report;1em;sd-text-info` se habla más a cerca de las etiquetas.

.. code-block:: xml
    :linenos:

    <pageGraphics>

    <!-- Cabecera de documento -->
    {% Header company_logo parent user form Template meta %}

    <!-- Pie del documento -->
    {% Footer user form Template meta %}

    </pageGraphics>

Estructura style
^^^^^^^^^^^^^^^^

El archivo ``style`` establece los parámetros estéticos necesarios para cada elemento de la plantilla, definiendo aspectos como colores, dimensiones y otras características estéticas. Del mismo modo, es importante adjuntar código en el `administrador de Django <#conf-django>`_ :octicon:`report;1em;sd-text-info`.  El siguiente bloque de código muestra un estilo para una tabla básica.

.. code-block:: xml
    :linenos:

    <!-- Ejemplo de estilos básicos de una tabla -->
    <blockTableStyle id="general">
    <lineStyle thickness="0.5" kind="GRID" colorName="#cfd8dc" start="0,0" stop="-1,-1" />
    <blockAlignment value="center" start="0,0" stop="-1,-1"/>
    <blockValign value="middle"/>
    </blockTableStyle>

.. LIGAS DE INTERÉS

.. |github| raw:: html

   <a href="https://docs.github.com/es" target="_blank">GitHub</a>

.. |git| raw:: html

   <a href="https://git-scm.com/doc" target="_blank">documentación de git</a>

.. |djangoproject| raw:: html

   <a href="https://www.djangoproject.com/" target="_blank">Django</a>
   
.. |gitPDF| raw:: html

   <a href="https://github.com/linkaform/PDFTemplates" target="_blank">enlace</a>

.. |prodDjango| raw:: html

   <a href="https://app.linkaform.com/admin" target="_blank">prod Administración de Django</a>

.. |preprodDjango| raw:: html

   <a href="https://preprod.linkaform.com/admin/" target="_blank">preprod Administración de Django</a>

.. |snake_case| raw:: html

   <a href="https://developer.mozilla.org/en-US/docs/Glossary/Snake_case" target="_blank">snake_case</a>


.. - **Django**: No es necesario instalar Django, sin embargo, se recomienda revisar la documentación de |djangoproject| :octicon:`report;1em;sd-text-info` para obtener más información.
.. - **Python**: Instale Python según sea necesario. Revise la |python| :octicon:`report;1em;sd-text-info` para obtener más información. En la mayoría de los sistemas operativos Linux, Python ya viene preinstalado, sin embargo, se recomienda verificar y actualizar la versión.
