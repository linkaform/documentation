============================
Report Markup Language (RML)
============================

Linkaform utiliza RML (Report Markup Language) para simplificar el proceso y permitir la creación automatizada y personalizada de documentos PDF.

.. seealso:: ¿Qué es RML?

    RML (Report Markup Language), es un miembro de la familia de los lenguajes XML, su dialecto XML es utilizado por rml2pdf para producir documentos en formato de Adobe’s Portable Document (PDF). RML permite crear documentos en PDF de forma tan simple como HTML o cualquier otro lenguaje de marcado como XML. 

    Para más información consulte la guía oficial de RML |reportlab| :octicon:`report;1em;sd-text-info`.

Anteriormente, en la sección sobre :ref:`estructura` :octicon:`report;1em;sd-text-info`, se presentó brevemente el contenido de los archivos base para un documento PDF. En el siguiente código, se explica con más detalle algunas etiquetas que debe tener en cuenta para sus futuros proyectos.

.. code-block:: xml
    :linenos: 
    :emphasize-lines: 1,4,6,9-10,13-14
    :caption: Archivo Body


    <?xml version="1.0"?>

    <!-- Configuración del documento -->
    <document filename="Name" xmlns:doc="http://namespaces.zope.org/rml/doc">
        <!-- Propiedades informativas -->
        <pageInfo pageSize="(21cm,27.5cm)" doc:example="" />

        <docinit>
            <!-- Fuentes -->
        </docinit>

        <!-- Definiciones de la plantilla -->
        <template title="Name" pageSize="(22cm,28cm)" author="Linkaform"></template>

        <!-- Estilos -->
        <stylesheet>
        </stylesheet>

        <story>
            <!-- Aquí va el código del cuerpo de la plantilla -->
        </story>
    </document>

**version**: Versión de xml.

**document**: Configuración del documento.

- **filename**: Nombre del documento.

**pageInfo**: Propiedades informativas del documento.

- **pageSize**: Tamaño de la página.

.. seealso:: Si necesita ajustar el tamaño de su página con medidas reales, utilice la herramienta diferenciadora de tamaños de papel. Ingrese al siguiente |diferenciador| para obtener más información.

**docinit**: Fuentes del documento.

**template**: Definiciones para todas las hojas que se generen.

- **title**: Título del documento.
- **pageSize**: Tamaño que se establece a la página.
- **author**: Autor del documento.

**stylesheet**: Define la totalidad de estilos que se van a implementar.

**story**: Dentro se desarrolla todo el cuerpo del PDF.

Conceptos básicos
=================

En esta sección, se presentan los elementos que comúnmente se utilizan para la elaboración de código en las plantillas de los PDF de Linkaform. Para obtener más detalles, consulte la documentación oficial |reportlab| :octicon:`report;1em;sd-text-info`.

Fonts
-----

Las fuentes permiten dar una apariencia más agradable al contenido escrito del documento. Las fuentes comúnmente usadas son ``montserrat`` y ``PT Sans``; sin embargo, en la siguiente lista se incluyen otras fuentes compatibles.

.. dropdown:: Fonts

    .. code-block:: xml
        :caption: Fonts

        Symbola_hint.ttf
        DejaVuSans.ttf
        Montserrat-BoldItalic.ttf
        Montserrat-ExtraLight.ttf
        Montserrat-Medium.ttf
        Montserrat-Thin.ttf
        times-new-roman.ttf
        FreeMonoBold.ttf
        Montserrat-Bold.ttf
        Montserrat-Italic.ttf
        Montserrat-Regular.ttf
        Symbola_hint.ttf
        Wingdings.ttf
        janeaust-webfont.ttf
        Montserrat-ExtraBoldItalic.ttf
        Montserrat-LightItalic.ttf
        Montserrat-SemiBoldItalic.ttf
        times-new-roman-bold-italic.ttf
        Montserrat-BlackItalic.ttf
        Montserrat-ExtraBold.ttf
        Montserrat-Light.ttf
        Montserrat-SemiBold.ttf
        times-new-roman-bold.ttf
        Montserrat-Black.ttf
        Montserrat-ExtraLightItalic.ttf
        Montserrat-MediumItalic.ttf
        Montserrat-ThinItalic.ttf
        times-new-roman-italic.ttf

Para incluir una fuente, puede hacerlo dentro de la etiqueta ``docinit``, haciendo referencia a la API donde se encuentra almacenada. Simplemente cambie el nombre de la fuente, como se muestra en el siguiente ejemplo:

.. code-block:: xml
    :linenos:
    :emphasize-lines: 1, 5

    <docinit>
        <registerTTFont faceName="Montserrat-Regular" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Regular.ttf" />
        <registerTTFont faceName="Montserrat-Bold" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Bold.ttf" />
        <registerTTFont faceName="Montserrat-BoldItalic" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-BoldItalic.ttf" />
    </docinit>

Coordenadas cartesianas
-----------------------

Las coordenadas cartesianas son un sistema de localización en un plano usando dos números, uno para la posición horizontal ``(x)`` y otro para la posición vertical ``(y)``. En los documentos PDF las coordenadas cartesianas se utilizan como referencia para ubicar elementos.

.. image:: /imgs/PDF/5/5.1.png

Graphics vs Flowables
---------------------

En RML, las etiquetas que posicionan elementos se llaman ``Graphics``. El otro grupo principal de etiquetas son los ``Flowables``, a continuación se explican algunos ejemplos.

Los ``Graphics`` son etiquetas que requieren coordenadas específicas (x, y), como es el caso de ``<blockTableStyle>``.

.. code-block:: xml
    :linenos:

    <blockTableStyle id="general">
        <blockAlignment value="center" start="0,0" stop="-1,-1"/>
    </blockTableStyle>

Por otro lado, los ``Flowables`` son etiquetas que no requieren un posicionamiento preciso e incluyen párrafos, separadores y tablas, entre otros. Estos elementos se colocan en secuencia descendente en un marco y se desplazan al siguiente cuando el marco no tiene más espacio y así sucesivamente. No se colocan explícitamente por coordenadas. Por ejemplo:

.. code-block:: xml
    :linenos:

    <blockTable colWidths="18cm">
        <tr>
            <td>
                <para>Hello world</para>
            </td>
        </tr>
    </blockTable>

Espacios
--------

La etiqueta ``<spacer>`` se utiliza para agregar espacios en blanco verticalmente entre elementos del documento. ``<spacer>`` utiliza el atributo ``length`` para definir el tamaño del espacio en blanco, utilizando unidades como píxeles, puntos, milímetros, etc.

.. code-block:: xml
    :linenos:

    <spacer length="0.5cm" />

Párrafos
--------

Para incluir párrafos, utilice la etiqueta ``<para>``. Puede incluir texto directamente dentro de la etiqueta o utilizar variables y expresiones de Django para mostrar contenido dinámico.

La etiqueta ``<para>`` utiliza el atributo ``style`` para especificar el nombre de un estilo (`paraStyle <#estilo>`_ :octicon:`report;1em;sd-text-info`) y usarla posteriormente para aplicar estilos, similar al atributo ``class`` en HTML.

.. code-block:: xml
    :linenos:

    <para style="nombre_estilo">
        Texto
    </para>

Tablas
------

Definir una tabla en su documento PDF es posible utilizando la etiqueta ``<blockTable>``. Su uso es principalmente para organizar y mostrar datos en forma de filas y columnas. 

Los atributos de ``<blockTable>`` son:

+--------------+------------------------------------------------------------------------------------------------+
| Atributo     | Descripción                                                                                    |
+==============+================================================================================================+
| style        | Define el nombre del estilo de la tabla definido con ``<blockTableStyle>``.                    |
+--------------+------------------------------------------------------------------------------------------------+
| colWidths    | Define el ancho de las columnas en la tabla, lo que afectará la distribución y el diseño de los|
|              | datos en esas columnas.                                                                        |
+--------------+------------------------------------------------------------------------------------------------+
| rowHeights   | Define la altura de las filas en la tabla.                                                     |
+--------------+------------------------------------------------------------------------------------------------+
| repeatRows   | Se utiliza para controlar la repetición de filas cuando una tabla se divide en varias páginas  |
|              | debido al contenido.                                                                           |
+--------------+------------------------------------------------------------------------------------------------+

.. note:: El nombre del estilo (Style) permite aplicar estilos personalizados utilizando `<blockTableStyle> <#table>`_ :octicon:`report;1em;sd-text-info`

Una tabla se compone de dos etiquetas principales: ``<tr>`` y ``<td>``. Estas se utilizan para estructurar y dar forma a las tablas, de manera similar a HTML. Sin embargo, en RML, se utilizan las etiquetas ``<tr>`` y ``<td>`` dentro de la etiqueta ``<blockTable>`` para definir las filas y celdas de la tabla, respectivamente.

-  ``<tr>`` (Tabla Row): Se utiliza para definir una fila en una tabla. Dentro de esta etiqueta, se pueden colocar una o más etiquetas ``<td>`` que representarán las celdas en esa fila.

-  ``<td>`` (Tabla Data): Se utiliza para definir una columna en una tabla. Puede aplicar estilos y atributos específicos a las celdas utilizando las propiedades de estilo de RML.

.. tip:: El ancho del atributo ``colWidths`` depende del tamaño de su página. Por ejemplo, suponga que el ``pageSize`` de su página es de 21 cm x 27.5 cm con un margen de 1.5 cm por lado. Por lo tanto, su página ya no contará con 3 cm, y ahora tendrá un tamaño de 19 cm x 25 cm, por lo que su tabla no podrá medir más de 19 cm. De esos 19 cm, puede distribuir el ancho según su necesidad.

    .. code-block:: xml
        :linenos:

        <blockTable colWidths="6cm, 8cm, 5cm">
            <tr>
                <td>Contenido de la celda 1</td>
                <td>Contenido de la celda 2</td>
                <td>Contenido de la celda 3</td>
            </tr>
            <tr>
                <td>Contenido de la celda 4</td>
                <td>Contenido de la celda 5</td>
                <td>Contenido de la celda 6</td>
            </tr>
        </blockTable>

    En el ejemplo anterior, se está definiendo una tabla con dos filas (``<tr>``) y tres columnas (``<td>``).

Imágenes
--------

Utilizar imágenes es posible utilizando la etiqueta ``<imageAndFlowables>``. Esta contiene los siguientes atributos

+-----------------------+-----------------------------------------------------------------------------------+
| Atributo              | Descripción                                                                       |
+=======================+===================================================================================+
| imageName             | Nombre del archivo de imagen o la ruta.                                           |
+-----------------------+-----------------------------------------------------------------------------------+
| imageWidth            | Ancho de la imagen; 0 utiliza el tamaño de píxel en puntos.                       | 
+-----------------------+-----------------------------------------------------------------------------------+
| imageHeight           | Altura de la imagen; 0 utiliza el tamaño de píxel en puntos.                      |
+-----------------------+-----------------------------------------------------------------------------------+
| imageMask             | Color de transparencia o ``auto`` (funciona solo para imágenes con transparencia).|
+-----------------------+-----------------------------------------------------------------------------------+
| imageLeftPadding      | Espacio a la izquierda de la imagen.                                              |
+-----------------------+-----------------------------------------------------------------------------------+
| imageRightPadding     | Espacio a la derecha de la imagen.                                                |
+-----------------------+-----------------------------------------------------------------------------------+
| imageTopPadding       | Espacio en la parte superior de la imagen.                                        |
+-----------------------+-----------------------------------------------------------------------------------+
| imageBottomPadding    | Espacio en la parte inferior de la imagen.                                        |
+-----------------------+-----------------------------------------------------------------------------------+
| imageSide             | Lado en el que se ubicará la imagen ("izquierda" o "derecha").                    |
+-----------------------+-----------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    <imageAndFlowables
        imageName="path"
        imageWidth="float"
        imageHeight="float"
        imageMask="color"
        imageLeftPadding="float"
        imageRightPadding="float"
        imageTopPadding="float"
        imageBottomPadding="float"
        imageSide="left"
    >

.. note:: Si necesita incluir imágenes externas en su documento, obtenga la URL pública almacenada por Linkaform e integre en ``imageName``.

.. _estilos:

Estilos
=======

Los estilos son un elemento clave que proporciona una presentación visual más agradable, permitiendo definir características como el color, el tamaño de fuente, el espaciado y otros atributos visuales que afectan la apariencia final del documento. 

A continuación, se presentan los elementos que comúnmente se utilizan para proporcionar estilos. En algunos casos, ya se encuentra estandarizada. Sin embargo, para más información, consulte la documentación oficial |reportlab| :octicon:`report;1em;sd-text-info`.

.. _estilo:

paraStyle
---------

La etiqueta ``<paraStyle>`` se utiliza para definir el estilo de uno o varios párrafos en el documento. Los estilos definidos con ``<paraStyle>`` incluyen características como fuente, tamaño de fuente, color de fuente, sangrías, interlineado, etc. En la siguiente tabla se presentan los atributos que la componen:

+---------------------+---------------------------------------------------------------------------------------------+
| Atributo            | Descripción                                                                                 |
+=====================+=============================================================================================+
| name                | Es el nombre del estilo que ha asignado a los párrafos. Se usa para aplicar ese estilo a    |
|                     | partes específicas del documento usando ``<para>``.                                         |
+---------------------+---------------------------------------------------------------------------------------------+
| alias               | Permite asignar un alias (nombre alternativo) al estilo. Puede usar este alias en lugar del |
|                     | nombre completo del estilo cuando aplique estilos a etiquetas ``<para>``.                   |
+---------------------+---------------------------------------------------------------------------------------------+
| parent              | Indica el nombre del estilo del cual heredará este estilo. Los atributos del estilo heredado|
|                     | se aplicarán a menos que se sobrescriban explícitamente en el estilo actual.                |
+---------------------+---------------------------------------------------------------------------------------------+
| fontname            | Define el nombre de la fuente para el estilo de párrafo.                                    |
+---------------------+---------------------------------------------------------------------------------------------+
| fontsize            | Establece el tamaño de la fuente para el estilo.                                            |
+---------------------+---------------------------------------------------------------------------------------------+
| leading             | Define el espacio interlineal para el estilo, es decir, el espacio vertical entre líneas.   |
+---------------------+---------------------------------------------------------------------------------------------+
| leftIndent,         | Establecen la sangría izquierda y derecha para el estilo.                                   |
| rightIndent         |                                                                                             |
+---------------------+---------------------------------------------------------------------------------------------+
| firstLineIndent     | Define la sangría de la primera línea del párrafo.                                          |
+---------------------+---------------------------------------------------------------------------------------------+
| spaceBefore,        | Establecen el espacio antes y después del párrafo.                                          |
| spaceAfter          |                                                                                             |
+---------------------+---------------------------------------------------------------------------------------------+
| alignment           | Define la alineación del párrafo (``left``, ``right``, ``center``, ``justify``).            |
+---------------------+---------------------------------------------------------------------------------------------+
| bulletFontName,     | Define la fuente y el tamaño de fuente para viñetas en listas (párrafos con viñetas).       |
| bulletFontsize      |                                                                                             |
+---------------------+---------------------------------------------------------------------------------------------+
| bulletIndent        | Define la sangría para las viñetas en listas.                                               |
+---------------------+---------------------------------------------------------------------------------------------+
| textColor           | Define el color del texto en el párrafo.                                                    |
+---------------------+---------------------------------------------------------------------------------------------+
| backColor           | Define el color de fondo del párrafo.                                                       |
+---------------------+---------------------------------------------------------------------------------------------+

Estos atributos permiten personalizar y controlar la apariencia de los párrafos en el documento. Puede aplicar estos estilos a diferentes partes del documento según sea su necesidad.

.. code-block:: xml
    :linenos:

    <paraStyle name="mystyle" alias="pretty" parent="oldstyle" fontname="Courier-Oblique" fontsize="13" leading="20" leftIndent="1.25in" rightIndent="2.5in" firstLineIndent="0.5in" spaceBefore="0.2in" spaceAfter="3cm" alignment="justify" bulletFontName="Courier" bulletFontsize="13" bulletIndent="0.2in" textColor="red" backColor="cyan" />

Ya se tienen estilos previamente preparados, simplemente llame el nombre de ``<paraStyle>`` en la etiqueta ``<para>`` del archivo ``<body>``.

.. code-block:: xml
    :linenos:

    <paraStyle name="textTitleI" fontName="Montserrat-Bold" fontSize="16" alignment="center" />
    <paraStyle name="textTitleII" fontName="Montserrat-Regular" fontSize="10" alignment="right" />
    <paraStyle name="textSubTitleI" fontName="Montserrat-Bold" fontSize="12" alignment="left" />
    <paraStyle name="textParaI" fontName="Montserrat-Regular" fontSize="10" alignment="left" />
    <paraStyle name="textParaII" fontName="Montserrat-Bold" fontSize="10" alignment="center" />
    <paraStyle name="textParaIII" fontName="Montserrat-Bold" fontSize="10" alignment="left" />

.. _table:

blockTableStyle
---------------

La etiqueta ``<blockTableStyle>`` se utiliza para definir estilos que pueden aplicarse a una o más tablas en el documento. El atributo principal de ``<blockTableStyle>`` es su ``id``, ayuda a definir el nombre del estilo de la tabla para que pueda llamarse en ``<blockTable>`` del archivo body.

.. code-block:: xml
    :linenos:

    <blockTableStyle id="nombreTabla">
        ...
    </blockTableStyle>

La etiqueta ``<blockTableStyle>`` también contiene descriptores de estilo; básicamente, son etiquetas con respectivos atributos dentro de la misma. A continuación, se presentan las más utilizadas.

lineStyle
^^^^^^^^^

Permite utilizar líneas para bordear la tabla. Sus propiedades incluyen:

+-------------+------------------------------------------------------------------------------------------------------------------------+
| Atributo    | Descripción                                                                                                            |
+=============+========================================================================================================================+
| kind        | Especifica el tipo de línea que se va a dibujar alrededor de la tabla. Puede contener:                                 |
|             |                                                                                                                        |
|             | - GRID: Dibuja un borde exterior (BOX) y líneas internas (INNERGRID) en los bordes de la tabla.                        |
|             |                                                                                                                        |
|             | - BOX y OUTLINE: Dibujan un borde completo alrededor de la tabla en los bordes superior, inferior, izquierdo y derecho.|
|             |                                                                                                                        |
|             | - INNERGRID: Dibuja líneas internas en los bordes de las celdas individuales de la tabla.                              |
|             |                                                                                                                        |
|             | - LINEBELOW: Dibuja una línea debajo de la celda.                                                                      |
|             |                                                                                                                        |
|             | - LINEABOVE: Dibuja una línea encima de la celda.                                                                      |
|             |                                                                                                                        |
|             | - LINEBEFORE: Dibuja una línea a la izquierda de la celda.                                                             |
|             |                                                                                                                        | 
|             | - LINEAFTER: Dibuja una línea a la derecha de la celda.                                                                |    
+-------------+------------------------------------------------------------------------------------------------------------------------+
| thickness   | Define el grosor de la línea en la tabla.                                                                              |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| colorName   | Define el color de la línea. Puede ser un nombre de color predefinido o un valor en formato hexadecimal.               |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| start       | Indica dónde comienza la secuencia de líneas punteadas o discontinuas.                                                 |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| stop        | Indica dónde termina la secuencia de líneas punteadas o discontinuas.                                                  |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| count       | Especifica la cantidad de segmentos en la línea punteada.                                                              |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| space       | Determina el espacio entre los segmentos en la línea punteada.                                                         |
+-------------+------------------------------------------------------------------------------------------------------------------------+
| dash        | Define una secuencia de segmentos de línea. El primer valor es la longitud del segmento visible y el segundo valor es  |
|             | la longitud del espacio en blanco. Por ejemplo, dash="2,2" crea un patrón de línea con segmentos visibles de 2 unidades|
|             | y espacios en blanco de 2 unidades.                                                                                    |
+-------------+------------------------------------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    <lineStyle
        kind="BOX"
        thickness="4"
        colorName="magenta"
        start="4"
        stop="11" 
        count="2" 
        space="2" 
        dash="2,2"
    />

blockFont
^^^^^^^^^

Establece la fuente que se utilizará en un bloque de la tabla. Lo que lo define son los siguientes atributos:

+-----------+-----------------------------------------------------------------------------------------------+
| Atributo  | Descripción                                                                                   |
+===========+===============================================================================================+
| nombre    | Establece el nombre de la fuente que se utilizará en un bloque de la tabla.                   |
+-----------+-----------------------------------------------------------------------------------------------+
| size      | Atributo opcional. Define el tamaño de la fuente.                                             |
+-----------+-----------------------------------------------------------------------------------------------+
| leading   | Atributo opcional. Define el espacio interlineal (leading), es decir, el espacio vertical     |
|           | entre líneas.                                                                                 |
+-----------+-----------------------------------------------------------------------------------------------+
| start     | Atributo opcional. Indica dónde comienza la secuencia de líneas punteadas o discontinuas.     |
+-----------+-----------------------------------------------------------------------------------------------+
| stop      | Atributo opcional. Indica dónde termina la secuencia de líneas punteadas o discontinuas.      |
+-----------+-----------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    <blockFont
        name="TimesRoman" 
        size="8" 
        leading="10" 
        start="4" 
        stop="11" 
    />

blockAlignment
^^^^^^^^^^^^^^

Establece la alineación del texto en un bloque de la tabla. Sus atributos son los siguientes:

+------------+---------------------------------------------------------------------------------------------+
| Atributo   | Descripción                                                                                 |
+============+=============================================================================================+
| value      | Atributo obligatorio. Establece la alineación del texto en un bloque de la tabla. Puede ser |
|            | LEFT, RIGHT, CENTER.                                                                        |
+------------+---------------------------------------------------------------------------------------------+
| start      | Atributo opcional. Indica dónde comienza la secuencia de líneas punteadas o discontinuas.   |
+------------+---------------------------------------------------------------------------------------------+
| stop       | Atributo opcional. Indica dónde termina la secuencia de líneas punteadas o discontinuas.    |
+------------+---------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    <blockAlignment
        value="left"
        start="4" 
        stop="11" 
    />

blockBackground
^^^^^^^^^^^^^^^

Establece el color que se utilizará para el fondo de un bloque de celdas en la tabla. Su descripción incluye:

+-------------+---------------------------------------------------------------------------------------------+
| Atributo    | Descripción                                                                                 |
+=============+=============================================================================================+
| colorName   | Atributo obligatorio. Establece el color que se utilizará para el fondo de un bloque de     |
|             | celdas en su tabla.                                                                         |
+-------------+---------------------------------------------------------------------------------------------+
| start       | Atributo opcional. Indica dónde comienza la secuencia de líneas punteadas o discontinuas.   |
+-------------+---------------------------------------------------------------------------------------------+
| stop        | Atributo opcional. Indica dónde termina la secuencia de líneas punteadas o discontinuas.    |
+-------------+---------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    <blockBackground
        colorName="indigo"  
        start="4" 
        stop="11" 
    />

blockLeading
^^^^^^^^^^^^

Establece el interlineado que se utilizará para el texto en un bloque de la tabla. Entre las características que presenta se encuentran los siguientes:

+----------------+---------------------------------------------------------------------------------------------+
| Atributo       | Descripción                                                                                 |
+================+=============================================================================================+
| length         | Atributo obligatorio. Establece el interlineado que se utilizará para el texto en un bloque |
|                | de la tabla.                                                                                |
+----------------+---------------------------------------------------------------------------------------------+
| start          | Atributo opcional. Indica dónde comienza la secuencia de líneas punteadas o discontinuas.   |
+----------------+---------------------------------------------------------------------------------------------+
| start          | Atributo opcional. Indica dónde termina la secuencia de líneas punteadas o discontinuas.    |
+----------------+---------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    <blockLeading
        length="10" 
        start="4" 
        stop="11" 
    />

blockTextColor
^^^^^^^^^^^^^^

Establece el color que se utilizará para el texto en un bloque de la tabla. Se describen mediante los siguientes atributos:

+-------------+---------------------------------------------------------------------------------------------+
| Atributo    | Descripción                                                                                 |
+=============+=============================================================================================+
| colorName   | Atributo obligatorio. Define el color que se utilizará para el texto en un bloque de la     |
|             | tabla.                                                                                      |
+-------------+---------------------------------------------------------------------------------------------+
| start       | Atributo opcional. Indica dónde comienza la secuencia de líneas punteadas o discontinuas.   |
+-------------+---------------------------------------------------------------------------------------------+
| stop        | Atributo opcional. Indica dónde termina la secuencia de líneas punteadas o discontinuas.    |
+-------------+---------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:
        
    <blockTextColor
        colorName="pink"
        start="4" 
        stop="11" 
    />

blockValign
^^^^^^^^^^^

Establece cómo se alinea el contenido de un bloque de celdas en dirección vertical. Se puede identificar por sus atributos, que son los siguientes:

+-------------+---------------------------------------------------------------------------------------------+
| Atributo    | Descripción                                                                                 |
+=============+=============================================================================================+
| colorName   | Atributo obligatorio. Establece cómo se alinea el contenido de un bloque de celdas en su    |
|             | tabla en dirección vertical. Puede ser TOP, MIDDLE, o BOTTOM (predeterminado).              |
+-------------+---------------------------------------------------------------------------------------------+
| start       | Atributo opcional. Indica dónde comienza la secuencia de líneas punteadas o discontinuas.   |
+-------------+---------------------------------------------------------------------------------------------+
| stop        | Atributo opcional. Indica dónde termina la secuencia de líneas punteadas o discontinuas.    |
+-------------+---------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    <blockValign
        value="left"
        start="4" 
        stop="11" 
    />

En esta sección, aprendió acerca de los componentes que conforman un archivo rml. Similar a HTML y CSS estas etiquetas permiten integrar una estructura y dar un formato agradable. En la siguiente sección, aprenderá acerca de las variables que ofrece Django para hacer el documento dinámico.
 
.. LIGAS EXTERNAS

.. |reportlab| raw:: html

   <a href="https://www.reportlab.com/docs/rml2pdf-userguide.pdf" target="_blank">aquí</a>

.. |diferenciador| raw:: html

   <a href="https://www.diferenciador.com/tamanos-de-papel-carta-oficio-letter-legal-tabloide" target="_blank">enlace</a>