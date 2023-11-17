=========================
Configuración del entorno
=========================

En esta sección, se detallan las plantillas disponibles, la estructura de archivos necesaria y la configuración específica en el entorno Django que se requiere para crear sus propios documentos en formato PDF.

Repositorio de PDFs
===================

Linkaform hace uso de un repositorio especial para el desarrollo de PDFs, proporcionando un control sobre los documentos generados para los clientes. Linkaform utiliza GitLab, si ya cuenta con una cuenta en la misma, siga los pasos a continuación; de lo contrario, consulte el `enlace <https://about.gitlab.com/>`_ :octicon:`report;1em;sd-text-info` para obtener más información.

1. Solicite acceso al repositorio de PDFs a través de soporte técnico.
2. Ingrese a la siguiente dirección `gitlab.linkaform.com/develop/PDFTemplates <https://gitlab.linkaform.com/develop/PDFTemplates/>`_ :octicon:`report;1em;sd-text-info` y clone el repositorio.

Estos pasos le permitirán acceder al repositorio de PDFs en GitLab, brindándole la capacidad de realizar cambios y contribuciones locales.

Plantillas
==========

Al tener su repositorio clonado, podrá visualizar plantillas genéricas que le servirán como base para la creación de sus propios archivos en formato PDF. El propósito de estas plantillas es establecer una estructura estandarizada para el proyecto, asegurando que cada cliente disponga de un archivo único que incluya encabezado, cuerpo, pie de página y estilos.

.. mermaid::

   graph TB
     
   A(Cliente)
   A --> B[Header]
   A --> C[Body]
   A --> D[Footer]
   A --> E[Style]

La estructura estándar de los archivos utilizan la siguiente notación: :: 
    
    [nombre_cliente] [_] [tipo_archivo] [.xml]

.. image:: /imgs/PDF/4/4.1.5.png

Observe que dentro de su repositorio también existen varias carpetas y en cada una de ellas se encuentran los archivos correspondientes a los PDFs. 

.. note:: Debe crear una carpeta específica para su proyecto, utilizando el nombre del cliente o empresa como identificador.

.. estructura:

Estructura de archivos
======================

Dentro de sus archivos, tendrá código genérico el cual puede emplear como base para sus proyectos futuros.

.. note:: Es opcional contar con archivos separados para el encabezado (header) y el pie de página (footer), ya que es válido insertar directamente el encabezado y el pie de página en el archivo del cuerpo (body). No obstante, el propósito de proporcionar archivos distintos es lograr una organización más eficiente mediante la separación de código para obtener una estructura más clara y mantenible.
    
Header
------

Encabezado del documento, que suele contener información como el logotipo y datos de identificación del cliente. El código base es el siguiente:

.. code-block:: xml
    :linenos:

    <drawRightString x="12cm" y="25cm"></drawRightString>

Para incluir elementos del ``header`` en el ``body`` utilice etiquetas y custom tags especiales de Django y Linkaform dentro de ``<pageGraphics>``. En la sección de Report Markup Language (RML) se habla más a cerca de las etiquetas.(HACER REFERENCIA A RML)

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

También puede incluir elementos del ``header`` en el ``body`` utilizando:

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
    :emphasize-lines: 40, 42

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

.. important:: El código anterior ya está preparado para su uso; deberá insertar su propio código entre las etiquetas ``<story>`` (línea 40 y 42).

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

Configuración en Django
=======================

Antes de empezar con los detalles de la configuración en Django para el desarrollo de PDFs, es importante conocer a cerca de Django. 

.. seealso::

    Django es un marco de desarrollo web de alto nivel y de código abierto en Python que fomenta la creación rápida y eficiente de aplicaciones web robustas y escalables. Para más información consulte la documentación oficial `aqui <https://www.djangoproject.com/>`_ :octicon:`report;1em;sd-text-info`. 

Ahora, continúe con las configuraciones necesarias dentro del entorno de Django, siguiendo los siguientes pasos:

1. Solicite a soporte técnico el acceso a la administración de Django.

.. note:: Soporte le proporcionará las credenciales necesarias para ingresar, uselas con precaucion. 

2. Inicie sesión en producción o preproducción.

- `app.linkaform.com/admin <https://app.linkaform.com/admin/>`_ :octicon:`report;1em;sd-text-info`

- `preprod.linkaform.com/admin <https://preprod.linkaform.com/admin/>`_ :octicon:`report;1em;sd-text-info`

.. important:: El proceso de configuración en producción y preproducción es idéntico. Sin embargo, se recomienda iniciar la creación de un documento PDF en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

Una vez autenticado, se muestra la interfaz de administración de Django.

.. image:: /imgs/PDF/4/4.1.2.png
  :align: center

La administración de Django ofrece acceso a una variedad de recursos. Sin embargo, con el propósito de abordar el desarrollo de archivos PDF, se explica la sección ``Pdfdocuments``, que consta de dos elementos clave: 

+-----------+---------------------------------------------------------+
| Opción    | Descripción                                             |
+===========+=========================================================+
| Plantillas| Contiene todas las plantillas generadas en Linkaform.   |
+-----------+---------------------------------------------------------+
| Widgets   | Proporciona plantillas adaptadas a los diferentes tipos |
|           | de datos utilizados.                                    |
+-----------+---------------------------------------------------------+

En cuanto a las plantillas, se muestra la opción de ``agregar`` o ``modificar``. En la opción ``Modificar``, se presenta una lista de plantillas existentes actualmente utilizadas por clientes de Linkaform. De igual manera, se brinda la opción de agregar una nueva plantilla.

.. image:: /imgs/PDF/4/4.1.4.png
  :align: center

La opción ``Agregar plantilla`` también se muestra un el formulario anterior. Las siguientes opciones de una nueva plantilla deberá completarla según sus necesidades:

.. grid:: 2
    :gutter: 0
    :padding: 0
    :margin: 0

    .. grid-item-card::  Descripciones
        :columns: 6
        :padding: 0
        :margin: 0
        
        **Name**: Nombre de la plantilla.

        .. note:: El estándar utilizado para el nombre de una plantilla es: ::
            
            [nombre_cliente] [-] [nombre_PDF]

        .. _type:

        **Type**:

        - Single Record (registro único): Plantilla que se centra en un solo conjunto de datos. Diseñadas para recibir y presentar información personalizada de manera clara y detallada. Al llenar la plantilla con los datos de un solo registro, se crea un PDF que captura los datos únicos de ese elemento.

        - Multiple Records (múltiples registros): Plantilla para presentar información de múltiples registros. Está preparada para recibir y organizar datos de varios registros en una estructura coherente.

        .. important:: Es obligatorio seleccionar  el tipo de PDF. Después de seleccionar el tipo de documento, el proceso de configuración es el mismo.

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

        **Paginate**: Permite colocar el número de página del documento (Opcional).

        **Description**: Descripción breve que ayuda a diferenciar entre documentos.

        .. note:: Descripción está estandarizada con la siguiente estructura: ::
            
            [Template] [de] [nombre_PDF] [para] [nombre_cliente]

        **Default**: Define la plantilla por defecto para la forma cuando no se ha seleccionado ninguna.

        **Preview**: —

        **Header**: Código del encabezado del documento (requerido).

        **Body**: Código del cuerpo del documento (requerido).

        **Footer**: Código del pie de página del documento (requerido).

        **Style**: Código de los estilos usados (requerido).

        **Owner**: Cuenta padre a la que se va asignar la plantilla.

        **Properties**: —


.. _vincular:

Configuración de forma
======================

La configuración implica la vinculación del PDF con el formulario. Al enlazar un PDF, se especifica que es exclusivo para las necesidades del formulario. Ya sea que esté trabajando con un solo registro o múltiples registros, la vinculación difiere.

.. important:: De manera similar a la configuración de Django, se recomienda utilizar preproducción para probar sus cambios. Una vez que esté listo, puede llevar a cabo la transición a producción.

Single record
-------------

Siga las siguientes instrucciones para configurar la forma y vincular su documento.  

1. Verifique que la plantilla esté configurada para funcionar como un single record (registro único). Para lograr esto, ajuste el atributo `type <#type>`_ :octicon:`report;1em;sd-text-info` en la interfaz de administración de Django. 

2. Inicie sesión en producción o preproducción con sus credenciales.

- `preprod.linkaform.com <https://preprod.linkaform.com/>`_ :octicon:`report;1em;sd-text-info`

- `app.linkaform.com <https://app.linkaform.com/>`_ :octicon:`report;1em;sd-text-info`

3. Seleccione y edite la forma a la que desea vincular el PDF. 

4. Seleccione ``opciones > opciones generales > Plantillas de PDF``. 

5. Seleccione el nombre que haya asignado a la plantilla previamente definida en la administración de Django.

.. image:: /imgs/PDF/1.png
  :align: center

6. Presione ``Agregar`` para incluir la plantilla y automáticamente se rellenará el campo ``Descripción``, seguido del ``nombre de la plantilla``, junto con dos alternativas: un ``botón azul`` y la opción de ``eliminar`` (símbolo X). A continuación, haga clic en ``OK``, regrese al formulario y guarde los cambios.

.. image:: /imgs/PDF/2.png
  :align: center

7. Seleccione el ``Nombre de la plantilla`` o el ``botón azul``. Se habilitará la escritura del campo ``Nombre de PDF``.

8. Escriba el nombre del PDF (no incluya el nombre del cliente), seguido de un guion medio ``-``.

.. image:: /imgs/PDF/3.png

9. En la opción ``Campo`` seleccione el metadato ``Folio del registro`` y presione ``Agregar``; automáticamente llenará el nombre del PDF con doble corchete ``{{}}``. 

.. note:: Puede seleccionar cualquier metadato disponible. Sin embargo, por defecto, suele usarse ``folio del registro``.

.. image:: /imgs/PDF/8.png
  :align: center

10. Seleccione la opción ``Guardar`` y haga clic en ``OK``.

11. Finalmente, guarde la forma.

Multiple record
---------------

El proceso de vinculación de un ``multiple record`` es más sencillo. Siga los siguientes pasos para su configuración:

1. Verifique que la configuración del `type <#type>`_ :octicon:`report;1em;sd-text-info` esté establecida en multiple records.

2. Inicie sesión en producción o preproducción con sus credenciales.

3. Elija y edite la forma a la que desea vincular el PDF. 

4. Seleccione ``opciones > opciones generales > Plantillas de PDF``. 

5. En el selector, elija el nombre que haya asignado a la plantilla previamente definida. Notará que se resalta una etiqueta verde con el texto ``multiple``.

6. Presione ``Agregar``.

7. Finalmente haga clic en ``OK`` y guarde la forma en su totalidad.

.. image:: /imgs/PDF/9.png
  :align: center

Descargar PDF
=============

El proceso de descarga de sus documentos PDF difiere según el tipo de documento. El proceso de descarga de sus documentos PDF difiere según el tipo de documento. A continuación, siga los pasos según su necesidad.

.. important:: Recuerde que el proceso de descarga depende de la configuración que realizó al `vincular su forma y el PDF <#vincular>`_ :octicon:`report;1em;sd-text-info`.
    
Single record
-------------

Para descargar documentos con registros únicos, siga los siguientes pasos:

#. Seleccione el registro que desea descargar.

#. Seleccione la opción con el icono de documento en la esquina superior derecha.

#. En la sección de descargas de su navegador, podrá observar su documento PDF.

.. image:: /imgs/PDF/10.png
  :align: center

Multiple record
---------------

En el caso de múltiples registros, el proceso varía ligeramente. Siga los siguientes pasos:

1. Ingrese a la interfaz de registros. 

2. En el campo ``Nombre de la forma``, escriba el nombre de la forma de la cual desea descargar los registros. 

.. important:: Es importante verificar la forma de los registros que necesita descargar. De lo contrario, seleccionar registros provenientes de diferentes formas podría resultar en errores.

3. Seleccione la opción con el icono de documento en la esquina superior derecha. 

.. image:: /imgs/PDF/11.png
  :align: center

Una vez seleccionado la opción, se desplegará la siguiente interfaz. Siga el siguiente procedimiento:

1. Si no ha aplicado ningún filtro, seleccione la opción ``Registros seleccionados``.

.. important:: La opción de ``Registros filtrados`` solo es posible si el código de su documento está preparado para recibir y tratar el filtro.

2. Seleccione el nombre de la plantilla.

3. Proporcione un nombre descriptivo para identificar la descarga de sus registros.

4. Haga clic en la opción ``Descargar``.

.. image:: /imgs/PDF/12.png

5. Ahora diríjase a la opción ``Descargas`` ubicada en el menú en el lado izquierdo.

.. image:: /imgs/PDF/13.png

6. Identifique el nombre de su descarga y presione ``Descargar``. El navegador abrirá una pestaña nueva con su documento.

.. image:: /imgs/PDF/14.png
  :align: center

En esta sección, ha aprendido conceptos necesarios sobre un documento PDF. También ha aprendido a configurar su entorno de trabajo. En la siguiente sección, se abordará cómo comenzar a preparar su documento utilizando el lenguaje de marcado de informes (Report Markup Language, RML) desde el código.