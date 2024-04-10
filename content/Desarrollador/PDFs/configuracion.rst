==================
Desarrollo de PDFs
==================

En esta sección, encontrará plantillas disponibles, la estructura de archivos necesaria y la configuración requerida para crear sus propios documentos en formato pdf. Además, podrá encontrar ejemplos prácticos, sugerencias y mejores prácticas para mejorar la calidad de sus documentos.

Configuración del entorno
=========================

Para comenzar el desarrollo de PDFs en Linkaform, es importante que prepare y configure su entorno de trabajo. Siga los siguientes apartados para más información.

Repositorio de PDFs
-------------------

El repositorio que contiene los PDFs actuales se encuentra en un repositorio de GitLab. Este repositorio es exclusivo para usuarios de Linkaform, utilice git para realizar cambios y contribuciones locales. 

.. seealso:: Git es una herramienta util para el control de versiones de un repositorio. Si aun no está familiarizado con Git, se recomienda que revise la documentación oficial de |git| :octicon:`report;1em;sd-text-info` para obtener más detalles.

Si su empresa desea realizar PDFs personalizados en Linkaform, podrá hacerlo sin necesidad de clonar el repositorio. Simplemente necesitará acceso al administrador de Django. El repositorio es útil para proporcionarle una base, sin embargo, en contenido posterior podrá encontrar dicho bloque de código.

.. caution:: En el repositorio de PDFs, podrá encontrar diferentes carpetas pertenecientes a diferentes clientes. Si tiene acceso, es importante que sepa que la información contenida es de suma importancia y secreta. Por lo tanto, se le solicita que tenga discreción con la información.

Si ya cuenta con una cuenta en GitLab, siga los pasos a continuación; de lo contrario, consulte el siguiente |gitlab| :octicon:`report;1em;sd-text-info` para obtener más información.

1. Solicite acceso al repositorio de PDFs a través del soporte técnico.
2. Ingrese al siguiente |gitPDF| :octicon:`report;1em;sd-text-info` y clone el repositorio.

.. tip:: Se recomienda tener una carpeta exclusiva para repositorios pertenecientes a Linkaform. En este caso, la carpeta ``lkf`` contendrá el repositorio ``PDFTemplates``.

.. _conf-django:

Administración de Django
========================

La administración de Django es la interfaz que permite realizar operaciones CRUD (crear, leer, actualizar, borrar) con los registros de las formas. Para configurar la administración de Django, siga los siguientes pasos:

1. Inicie sesión en |prodDjango| :octicon:`report;1em;sd-text-info` o desde |preprodDjango| :octicon:`report;1em;sd-text-info`.

.. note:: Solicite a soporte técnico el acceso y las credenciales necesarias de la administración de Django. 
    
    El proceso de configuración en producción y preproducción es idéntico. Sin embargo, se recomienda iniciar la configuración en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

.. image:: /imgs/PDF/pdf16.png

Una vez autenticado, se muestra la interfaz principal de la administración de Django. Observe que tiene acceso a una variedad de recursos, sin embargo, con el propósito de abordar el desarrollo de archivos PDF, la explicación se centra en la sección ``Pdfdocuments``, que consta de dos elementos clave: 

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :align: left

   * - Opción
     - Descripción
   * - Plantillas
     - Contiene todas las plantillas creadas en la plataforma.
   * - Widgets
     - Proporciona plantillas adaptadas a los diferentes tipos de datos utilizados.

En cuanto a las plantillas, encontrará dos opciones:

**Modificar** 

La opción ``Modificar`` presenta una lista de plantillas existentes actualmente utilizadas por clientes de Linkaform. Para editar una plantilla existente, simplemente seleccione el nombre de la plantilla de su preferencia.

Para agregar y configurar una nueva plantilla presione la opción ``Agregar plantilla``.

.. image:: /imgs/PDF/pdf17.png

Para eliminar una plantilla, seleccione la casilla o casillas correspondientes y seleccione la opción en el selector seguido del botón ``Ejecutar``.

.. image:: /imgs/PDF/pdf18.png

**Agregar** 

La opción ``Agregar`` permite configurar una nueva plantilla. Siga los siguientes pasos para configurar la plantilla:

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

        **Owner**: Nombre de la cuenta padre a la que se va asignar la plantilla.

        Debido a que el selector de ``Owner`` contiene muchas opciones de cuentas de usuarios actuales, puedes simplificar la búsqueda siguiendo estos pasos:

        1. Inspeccione la pagina haciendo ``clic derecho > Inspeccionar`` o presionando directamente ``F12``.
        2. Seleccione la opción de seleccionar elementos del DOM en la parte superior izquierda.
        3. Haga clic en el selector de ``Owner``.

        .. image:: /imgs/PDF/pdf19.png
        
        4. Abra el elemento que contiene a las opciones del selector.
            
        .. image:: /imgs/PDF/pdf20.png

        5. Presione ``Ctrl + F`` e ingrese el nombre o Valor del ``ID`` de la cuenta de su interés para buscar entre las opciones.
        6. Haga doble clic en la opción de su interés e ingrese la palabra ``selected`` y presione ``Enter``. Automáticamente la opción sera seleccionada.

        .. note:: Revise que el ``ID`` de la opción corresponda a la de su interés.

        .. image:: /imgs/PDF/pdf21.png













Plantillas
==========

Para el desarrollo de un PDF, se necesitan estrictamente cuatro archivos que incluyen un encabezado, cuerpo, pie de página y estilos. 

.. attention:: Se dice que es necesario contar con cuatro archivos para el desarrollo de un PDF. Sin embargo, es válido insertar directamente el encabezado y el pie de página en el cuerpo del documento. No obstante, se recomienda tener los archivos separados por la necesidad del administrador de Django, encargado de ejecutar los PDFs.

.. mermaid::

   graph TB
     
   A(PDF)
   A --> B[Header]
   A --> C[Body]
   A --> D[Footer]
   A --> E[Style]

Al tener el repositorio de PDFs clonado, podrá consultar plantillas genéricas que le servirán como base para la creación de sus propios PDFs personalizados. Podrá encontrarlos en la carpeta :bdg-secondary:`Básico`. Dentro de esta carpeta, podrá encontrar los archivos correspondientes.

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
                background-color: #E36414
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

Si ya contiene una carpeta correspondiente a su empresa, cree los archivos necesarios para el nuevo PDF. Si no la tiene, cree una nueva carpeta utilizando el nombre del cliente o empresa como identificador. Luego, cree los archivos necesarios como se muestra en el siguiente ejemplo:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: Directory Tree
        :columns: 4

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
                ├── <a class="print">Comercializadora Pánfilo</a><br>
                │   └── <a class="printf">gastos_body.xml</a><br>
                │   └── <a class="printf">gastos_footer.xml</a><br>
                │   └── <a class="printf">gastos_header.xml</a><br>
                │   └── <a class="printf">gastos_style.xml</a><br>                
            </body>
            </html>    

    .. grid-item-card:: 
        :columns: 8
        
        Para el nombre de los archivos utilice la siguiente estructura: ::

            [nombre_pdf] [_] [tipo_archivo] [.xml]
 


















































.. _estructura:

Estructura de archivos
======================

Dencódigo genérico el cual puede emplear como base para sus proyectos futuros.

 
Header
------

Encabezado del documento, que suele contener información como el logotipo y datos de identificación del cliente. El código base es el siguiente:

.. code-block:: xml
    :linenos:

    <drawRightString x="12cm" y="25cm"></drawRightString>

Para incluir elementos del ``header`` en el ``body`` utilice etiquetas y custom tags especiales de Django y Linkaform dentro de ``<pageGraphics>``. En la sección :ref:`report_markup_language` :octicon:`report;1em;sd-text-info` se habla más a cerca de las etiquetas.


.. code-block:: xml
    :linenos:

    <pageGraphics>

    <!-- Cabecera de documento -->
    {% Header company_logo parent user form Template meta %}

    </pageGraphics>

Footer
------

El pie de página puede incluir información adicional, como datos de contacto, notas importantes o número de páginas. Aunque comúnmente los documentos PDF no cuentan con un pie de página, es importante adjuntar algo en el administrador de Django. Para ello, puede utilizar la siguiente etiqueta:

.. code-block:: xml
    :linenos:

    <drawRightString x="19.5cm" y="0.85cm">Página <pageNumber/> de <getName id="LASTPAGENO"/></drawRightString>

También puede incluir elementos del ``footer`` en el ``body`` utilizando:

.. code-block:: xml
    :linenos:

    <pageGraphics>

    <!-- Pie del documento -->
    {% Footer user form Template meta %}

    </pageGraphics>

Body
----

El cuerpo del documento es la parte más importante, similar a HTML, aquí se especifica la estructura principal del PDF. La estructura base del cuerpo utiliza el siguiente código:

.. code-block:: xml
    :linenos:
    :emphasize-lines: 42, 45

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
                    <!-- Cabecera de documento -->
                    {% Header company_logo parent user form Template meta %}
                    <!-- Pie del documento -->
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
            <!-- Aquí va el código del cuerpo de la plantilla -->
            <para>Hello world</para>
        </story>
    </document>

.. important:: El código anterior ya está preparado para su uso; deberá insertar su propio código entre las etiquetas ``<story>`` (línea 42 y 45).

Style
-----

El archivo ``style`` también juega un rol importante. Este establece los parámetros estéticos necesarios para cada plantilla, definiendo aspectos como colores, dimensiones y otras características estéticas.

.. code-block:: xml
    :linenos:

    <!-- Ejemplo de estilos básicos de una tabla -->
    <blockTableStyle id="general">
    <lineStyle thickness="0.5" kind="GRID" colorName="#cfd8dc" start="0,0" stop="-1,-1" />
    <blockAlignment value="center" start="0,0" stop="-1,-1"/>
    <blockValign value="middle"/>
    </blockTableStyle>

.. important:: Tenga en cuenta utilizar un navegador diferente a la página de Linkaform para evitar posibles conflictos con las cookies.

.. important:: Consideraciones sobre navegación 

    Tenga en cuenta utilizar un navegador diferente al administrador de Django. Dado que ambos entornos comparten la misma autenticación, es aconsejable abrir el Administrador de Django en un navegador y de forma separada, acceder al entorno de formularios en otro navegador. Esto puede evitar posibles conflictos y asegurar un funcionamiento más fluido.

.. tip:: Recomendación

    Al haber establecido la configuración entre el documento PDF y el formulario, si al generar el archivo no se descarga como se espera, se sugiere seguir el siguiente procedimiento:

    1. Edite el formulario y reenvíe los datos, incluso si no se realizan modificaciones en los registros existentes.

En esta sección, ha aprendido conceptos necesarios sobre un documento PDF. También ha aprendido a configurar su entorno de trabajo. En la siguiente sección, se abordará cómo comenzar a preparar su documento utilizando el lenguaje de marcado de informes (Report Markup Language, RML) desde el código.

.. LIGAS DE INTERÉS

.. |gitlab| raw:: html

   <a href="https://docs.gitlab.com/" target="_blank">enlace</a>

.. |python| raw:: html

   <a href="https://www.python.org/" target="_blank">documentación de python</a>

.. |git| raw:: html

   <a href="https://git-scm.com/doc" target="_blank">documentación de git</a>

.. |djangoproject| raw:: html

   <a href="https://www.djangoproject.com/" target="_blank">Django</a>
   
.. |gitPDF| raw:: html

   <a href="https://gitlab.linkaform.com/develop/PDFTemplates/" target="_blank">enlace</a>

.. |prodDjango| raw:: html

   <a href="https://app.linkaform.com/admin" target="_blank">prod Administración de Django</a>

.. |preprodDjango| raw:: html

   <a href="https://preprod.linkaform.com/admin/" target="_blank">preprod Administración de Django</a>

.. - **Django**: No es necesario instalar Django, sin embargo, se recomienda revisar la documentación de |djangoproject| :octicon:`report;1em;sd-text-info` para obtener más información.
.. - **Python**: Instale Python según sea necesario. Revise la |python| :octicon:`report;1em;sd-text-info` para obtener más información. En la mayoría de los sistemas operativos Linux, Python ya viene preinstalado, sin embargo, se recomienda verificar y actualizar la versión.
