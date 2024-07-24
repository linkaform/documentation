.. _report_markup_language:

============================
Report Markup Language (RML)
============================

En esta sección, encontrará una guía sobre **Report Markup Language (RML)**, el lenguaje de marcado de informes utilizado para estructurar los elementos que componen un PDF. 

Este apartado **no** pretende ser un tutorial completo y detallado, pero sí cubre todos los aspectos relevantes para el desarrollo de plantillas de Linkaform. Encontrará ejemplos prácticos, sugerencias y buenas prácticas para el desarrollo de reportes en formato PDF. 

.. seealso:: **Acerca de RML**

    Report Markup Language (RML) es un lenguaje de estilo XML utilizado para describir el diseño de documentos. Permite definir y manipular cualquier aspecto de un documento, incluido el contenido y el estilo, mediante el uso de etiquetas. Muchas de estas etiquetas son similares a las utilizadas en HTML.

    La generación de un documento PDF a partir de RML se realiza mediante el módulo de Python llamado ``rml2pdf``. Sin embargo, es importante tener en cuenta que ``rml2pdf`` forma parte de la versión de paga de ``ReportLab``. Para evitar esta dependencia, Linkaform utiliza la alternativa de código abierto llamada ``z3c``.

    También es importante señalar que la alternativa |z3c| :octicon:`report;1em;sd-text-info` no es totalmente compatible con RML de |reportlab| :octicon:`report;1em;sd-text-info`, por lo que pueden existir partes del código que no sean compatibles. Revise las diferencias de implementación de ``rml2pdf`` y ``z3c.rml`` |diferencias| :octicon:`report;1em;sd-text-info`.

    Para más información sobre las etiquetas consulte la guía oficial de |RML| :octicon:`report;1em;sd-text-info`.

Conceptos básicos
=================

En esta sección, encontrará los elementos y aspectos comúnmente utilizados en la elaboración de plantillas. Para más información, consulte la guía de usuario de |RML| :octicon:`report;1em;sd-text-info`.

Etiquetas y atributos
---------------------

Las **etiquetas** son elementos que se utilizan para estructurar y organizar el contenido. Por otro lado, los **atributos** son características o propiedades que se pueden asignar a las etiquetas para proporcionar más información sobre ellos o modificar su comportamiento.

Al igual que con cualquier dialecto XML, RML requiere una sintaxis XML correcta. Si está familiarizado con HTML, preste atención a las diferencias entre la sintaxis XML y algunas de las construcciones más permisivas permitidas en HTML.

Los **valores** de atributos deben estar encerrados entre comillas.

.. code-block:: xml
    :caption: Correcto
    :linenos:

    <document filename="outfile.pdf">

.. code-block:: xml
    :caption: Incorrecto

    <document filename=outfile.pdf>

Un **elemento no vacío** debe tener tanto una etiqueta de apertura como una de cierre.

.. code-block:: xml
    :caption: Ejemplo
    :linenos:

    <document> </document>
 
Los **elementos vacíos** son aquellos que no tienen ningún contenido y se cierran con ``/>`` al final de la misma etiqueta en lugar de tener una etiqueta de cierre separada.

.. code-block:: xml
    :caption: Ejemplo
    :linenos:

    <getName id="Header.Title"/>

Las etiquetas deben estar anidadas correctamente.

.. code-block:: xml
    :caption: Correcto
    :linenos:

    <b>
        <i>texto</i>
    </b>

.. code-block:: xml
    :caption: Incorrecto
    :linenos:

    <b>
        <i>texto
    </b>
    </i>

En general, los **espacios** en blanco se ignoran en RML. Excepto dentro de cadenas de texto, puede formatear e indentar documentos RML de la manera que considere más legible. 

Dentro de cadenas de texto, el espacio en blanco se considera equivalente a un solo espacio y los saltos de línea se agregan automáticamente según sea necesario durante el formateo.

Por ejemplo, considere el siguiente fragmento de código RML:

.. code-block:: xml
    :caption: Ejemplo
    :linenos:

    <para>
        Esto es      un    ejemplo de
        texto   con   varios espacios
        y saltos
        de línea.
    </para>

.. code-block:: xml
    :caption: Resultado

    Esto es un ejemplo de texto con varios espacios y saltos de línea.

RML es **case sensitive**, lo que significa que distingue entre mayúsculas y minúsculas.  La capitalización en los nombres de las etiquetas y variables es importante y significativa.

.. code-block:: xml
    :caption: Ejemplo
    :linenos:

    {% set nombre %}
    {% set NOMBRE %}
    {% set Nombre %}

Convenciones
------------

Las prácticas comúnmente más usadas y admitidas por RML son las siguientes:

1. Los colores se pueden especificar de tres maneras: 

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :align: left

   * - Elemento
     - Ejemplo
   * - nombre
     - Red
   * - hexadecimal
     - #FF0000
   * - rgb
     - (255,255,255)
   * - CMYK
     - #ff99001f

.. note:: Regularmente se utiliza el formato hexadecimal.

2. Las coordenadas cartesianas son un sistema de localización en un plano usando dos números, uno para la posición horizontal ``(x)`` y otro para la posición vertical ``(y)``. En los documentos PDF las coordenadas cartesianas se utilizan como referencia para ubicar elementos.

.. image:: /imgs/PDF/5/5.1.png

3. Las medidas predeterminadas son puntos, pero pueden ser:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :align: left

   * - Medida
     - Ejemplo
   * - milímetros (mm)
     - y='10mm'
   * - centímetros (cm)
     - height='2cm'
   * - pulgadas (pulg)
     - width='2in'
   * - puntos (pto)
     - size='7.5'

.. note:: Regularmente se utilizan las medidas en centímetros(cm).

Fonts
-----

Las fuentes son útiles para determinar el tipo de letra utilizado en el contenido. Algunas de las fuentes comúnmente utilizadas en las plantillas son ``Montserrat`` y ``PT Sans``. En la siguiente lista encontrará otras fuentes compatibles:

.. dropdown:: Fonts

    .. code-block:: xml
        :caption: Fonts
        :linenos:

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

Para incluir una de las fuentes anteriores, siga los pasos:

1. Copie una de las líneas de ``registerTTFont``.
2. Edite el nombre de la fuente en ``faceName``.
3. Ajuste el final de ``fileName``.
4. Coloque la linea dentro de la etiqueta ``<docinit>``.

.. code-block:: xml
    :linenos:
    :emphasize-lines: 1, 5

    <docinit>
        <registerTTFont faceName="Montserrat-Regular" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Regular.ttf" />
        <registerTTFont faceName="Montserrat-Bold" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Bold.ttf" />
        <registerTTFont faceName="Montserrat-BoldItalic" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-BoldItalic.ttf" />
    </docinit>

Graphics vs Flowables
---------------------

Al diseñar un documento en RML, es importante comprender que existen dos tipos de elementos: ``Graphics`` y ``Flowables``.

Los elementos ``Graphics`` están fijos en la página y se posicionan utilizando coordenadas (``x``, ``y``), como es el caso de los elementos que componen al ``header`` y el ``footer``. 

.. code-block:: xml
    :linenos:

    <drawString x="1.5cm" y="27.4cm">{{ form.name }} </drawString>

Por otro lado, los elementos ``Flowables`` fluyen dentro de un **Frame**. Esto significa que no requieren posicionamiento explícito en coordenadas cartesianas. En lugar de eso, los elementos se colocan en secuencia descendente en el **Frame** y se desplazan automáticamente al siguiente cuando el **Frame** no tiene más espacio, y así sucesivamente. Ejemplos de estos elementos son párrafos, espacios, tablas, entre otros.

.. code-block:: xml
    :linenos:

    <blockTable colWidths="18cm">
        <tr>
            <td>
                <para>Hello world</para>
            </td>
        </tr>
    </blockTable>

Comentarios
-----------

RML permite el uso de comentarios en el código para documentar fragmentos importantes. Los comentarios no se mostrarán en el archivo PDF de salida. Para comentar dentro de las plantillas, utilice la siguiente sintaxis:

.. code-block:: xml
    :linenos:

    <!-- Su comentario aquí -->

.. warning:: Tenga en cuenta que los comentarios no pueden estar anidados. Además, no se pueden utilizar los caracteres ``--`` dentro de la sección de comentarios.

Espacios
--------

Para agregar espacios en blanco verticalmente entre elementos del documento, utilice la etiqueta ``<spacer>``. Esta etiqueta utiliza el atributo ``length`` para definir el tamaño del espacio, utilizando unidades como píxeles, puntos, milímetros, etc.

.. note:: Regularmente, se utilizan centímetros (cm).

.. code-block:: xml
    :linenos:

    <spacer length="0.5cm" />

Párrafos
--------

Para incluir textos en linea o párrafos, utilice la etiqueta ``<para>``. Puede incluir texto directamente dentro de la etiqueta o utilizar variables y expresiones propios de Django para mostrar contenido dinámico.

.. seealso:: Consulte :ref:`rml_django` :octicon:`report;1em;sd-text-info` para mas información. 

.. code-block:: xml
    :linenos:

    <para>Texto</para>

    <para>{{ nombre_variable }}</para>

Cuando trabaje con tablas u otros elementos que incluyan texto, asegúrese de incluirlo dentro de la etiqueta ``<para>``. Esta etiqueta se encarga de mantener el texto dentro del **frame**  sin desbordarse. 

Por ejemplo, al especificar el nombre de las columnas en una tabla, es común saber la longitud del texto estático. Sin embargo, para el contenido dinámico, como los párrafos de texto, la longitud puede variar y no siempre se conoce de antemano. Si simplemente incluye el texto entre las etiquetas de la tabla, es probable que el contenido se desborde.

En cambio, al utilizar la etiqueta ``<para>`` dentro de las etiquetas de la tabla, el contenido se ajustará automáticamente dentro de las dimensiones de la tabla. Observe los siguientes ejemplos visuales:

.. tab-set::

    .. tab-item:: Incorrecto

        .. code-block:: xml
            :linenos:

            <blockTable>
                    <tr>
                        <td>
                            Detalle
                        </td>
                        <td>
                            {{ set.6492412ec0d7d35fe4a66dd7 }}
                        </td>
                        <td>
                        </td>
                    </tr>
            </blockTable>

        .. image:: /imgs/PDF/pdf23.png

    .. tab-item:: Correcto

        .. code-block:: xml
            :linenos:

            <blockTable>
                    <tr>
                        <td>
                            <para>Detalle<para>
                        </td>
                        <td>
                            <para>{{ set.6492412ec0d7d35fe4a66dd7 }}<para>
                        </td>
                        <td>
                        </td>
                    </tr>
            </blockTable>

        .. image:: /imgs/PDF/pdf24.png

La etiqueta ``<para>`` utiliza el atributo ``style`` para especificar el nombre de un estilo y usarla posteriormente para aplicar estilos, similar al atributo ``class`` en HTML. Consulte `paraStyle <#estilo>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. code-block:: xml
    :linenos:

    <para style="nombre_estilo">
        Texto
    </para>

Tablas
------

Definir una tabla en la plantilla es posible utilizando la etiqueta ``<blockTable>``. Su uso es principalmente para organizar y mostrar datos en forma de filas y columnas. 

Los atributos de ``<blockTable>`` son:

+--------------+------------------------------------------------------------------------------------------------+
| Atributo     | Descripción                                                                                    |
+==============+================================================================================================+
| style        | Define el nombre del estilo de la tabla definido con ``<blockTableStyle>``.                    |
+--------------+------------------------------------------------------------------------------------------------+
| colWidths    | Define el ancho de las columnas en la tabla, lo que afectará la distribución y el diseño de los|
|              | datos en esas columnas. Regularmente se expresa en centímetros (cm).                           |
+--------------+------------------------------------------------------------------------------------------------+
| rowHeights   | Define la altura de las filas en la tabla. Regularmente se expresa en centímetros (cm).        |
+--------------+------------------------------------------------------------------------------------------------+
| repeatRows   | Se utiliza para controlar la repetición de filas cuando una tabla se divide en varias páginas  |
|              | debido al contenido.                                                                           |
+--------------+------------------------------------------------------------------------------------------------+

La etiqueta ``<blockTable>`` utiliza el atributo ``style`` para especificar el nombre de un estilo y usarla posteriormente para aplicar estilos, similar al atributo ``class`` en HTML. Consulte `<blockTableStyle> <#table>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. code-block:: xml
    :linenos:

    <blockTable colWidths="4.8cm, 9.4cm, 4.8cm" style="nombre_estilo">

En RML, se utilizan las etiquetas ``<tr>`` y ``<td>`` dentro de la etiqueta ``<blockTable>`` para definir las filas y celdas de la tabla, respectivamente.

.. grid:: 2
    :gutter: 0

    .. grid-item-card::
        :columns: 7

        ``<td>`` (Tabla Data): Define una columna en una tabla.
        
        .. note:: Puede aplicar estilos y atributos específicos a las celdas utilizando las propiedades de estilo de `<blockTableStyle> <#table>`_ :octicon:`report;1em;sd-text-info`.

        ``<tr>`` (Tabla Row): Define una fila en una tabla. 
        
        .. note:: Coloque las etiquetas ``<td>`` necesarias para representar las celdas en esa fila.

    .. grid-item-card::
        :columns: 5

        .. image:: /imgs/PDF/pdf25.png

.. attention:: El ancho del atributo ``colWidths`` depende del tamaño de la página.

    Por ejemplo, supongamos que el ``pageSize`` de la página es de **21 cm x 27.5 cm** con un margen de **1.5 cm** por lado. Restando el espacio del margen, la página ya no contará con **3 cm**, por lo que tendrá un espacio utilizable de **19 cm x 25 cm**. En consecuencia, la tabla no podrá medir más de **19 cm**. Dentro de esos **19 cm**, deberá distribuir el ancho según sus necesidades.

    .. code-block:: xml
        :linenos:

        <pageTemplate id="first" pagesize="21cm, 27.5cm">
            <frame id="first" x1="1cm" y1="1.5cm" width="19cm" height="23cm"/>
        </pageTemplate>

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

    En el ejemplo anterior, se definió una tabla con dos filas (``<tr>``) y tres columnas (``<td>``).

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

Los atributos anteriores permiten personalizar y controlar la apariencia del texto utilizado en el documento. 

.. code-block:: xml
    :linenos:

    <paraStyle name="mystyle" alias="pretty" parent="oldstyle" fontname="Courier-Oblique" fontsize="13" leading="20" leftIndent="1.25in" rightIndent="2.5in" firstLineIndent="0.5in" spaceBefore="0.2in" spaceAfter="3cm" alignment="justify" bulletFontName="Courier" bulletFontsize="13" bulletIndent="0.2in" textColor="red" backColor="cyan" />

Actualmente, existen estilos previamente preparados para párrafos y textos. En el siguiente bloque de código, copie, modifique y pegue según sea necesario. Asegurase de que los nombres del ``<paraStyle>`` y ``<para>`` sean las mismas. observe los siguientes ejemplos:

.. note:: Si no asigna ningún color, por defecto se tomará el color negro.

.. tab-set::

    .. tab-item:: Estructura

        .. code-block:: xml
            :linenos:

            <story>

                <para style="textTitleI">textTitleI</para>
                <para style="textSubtitleI">textSubtitleI</para>

                <para style="textParaI">textParaI</para>
                <para style="textParaII">textParaII</para>

                <para style="textParaIII">textParaIII</para>
                <para style="textParaIV">textParaIV</para>

                <para style="textParaV">textParaV</para>
                <para style="textParaVI">textParaVI</para>
                
                <para style="textParaVII">textParaVII</para>
                <para style="textParaVIII">textParaVIII</para>

            </story>

    .. tab-item:: Estilos

        .. code-block:: xml
            :linenos:

            <paraStyle name="textTitleI" fontName="Montserrat-Bold" fontSize="12" alignment="left" textColor="red"/>
            <paraStyle name="textSubtitleI" fontName="Montserrat-Bold" fontSize="10" alignment="left" textColor="blue"/>

            <paraStyle name="textParaI" fontName="Montserrat-Regular" fontSize="8" alignment="left" textColor="#803D3B"/>
            <paraStyle name="textParaII" fontName="Montserrat-Bold" fontSize="8" alignment="left" textColor="#0E46A3"/>

            <paraStyle name="textParaIII" fontName="Montserrat-Regular" fontSize="8" alignment="center" textColor="#DD5746"/>
            <paraStyle name="textParaIV" fontName="Montserrat-Bold" fontSize="8" alignment="center" textColor="#DD5746"/>

            <paraStyle name="textParaV" fontName="Montserrat-Regular" fontSize="8" alignment="right" textColor="#B3C8CF"/>
            <paraStyle name="textParaVI" fontName="Montserrat-Bold" fontSize="8" alignment="right" textColor="#8B322C"/>

            <paraStyle name="textParaVII" fontName="Montserrat-Regular" fontSize="8" alignment="justify" textColor="#1C1678"/>
            <paraStyle name="textParaVIII" fontName="Montserrat-Bold" fontSize="8" alignment="justify" textColor="#007F73"/>

    .. tab-item:: Resultado
        
        .. image:: /imgs/PDF/pdf26.png

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
| name      | Establece el nombre de la fuente que se utilizará en un bloque de la tabla.                   |
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
| stop           | Atributo opcional. Indica dónde termina la secuencia de líneas punteadas o discontinuas.    |
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
| Value       | Atributo obligatorio. Establece cómo se alinea el contenido de un bloque de celdas en su    |
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

Template
========

Anteriormente, en la sección :ref:`estructura` :octicon:`report;1em;sd-text-info`, se presentaron brevemente las plantillas para un documento PDF. 

En el siguiente bloque de código, encontrará detalles sobre el archivo **body**, el encargado de establecer la estructura del PDF. Revise la siguiente tabla y compárela con el bloque de código. Estas etiquetas son importantes para la base del archivo y deben tenerse en cuenta para las plantillas futuras.

.. list-table::
   :widths: 15 85
   :header-rows: 1
   :align: left

   * - Elemento
     - Descripción
   * - version
     - Versión de xml.
   * - document
     - Configuración del documento.

       - filename: Nombre del documento (cambiar).

   * - pageInfo
     - Propiedades informativas del documento.

       - pageSize: Tamaño de la página.

   * - docinit
     - Fuentes del documento.
   * - template
     - Definiciones para todas las hojas que se generen.

       - title: Título del documento.

       - pageSize: Tamaño que se establece a la página.

       - author: Autor del documento.
   * - stylesheet
     - Define la totalidad de estilos que se van a implementar.
   * - story
     - Dentro se desarrolla todo el cuerpo del PDF.

.. seealso:: Para definir el atributo ``pageSize``, utilicé la herramienta diferenciadora de tamaños de papel para obtener medidas reales sobre los tamaños. Para más información, ingrese al siguiente |diferenciador| :octicon:`report;1em;sd-text-info`.

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

En esta sección, aprendió acerca de los componentes que conforman un archivo rml. Similar a HTML y CSS estas etiquetas permiten integrar una estructura y dar un formato agradable. En la siguiente sección, aprenderá acerca de las variables que ofrece Django para hacer el documento dinámico.
 
.. LIGAS EXTERNAS

.. |rml| raw:: html

   <a href="https://www.reportlab.com/docs/rml2pdf-userguide.pdf" target="_blank">RML</a>

.. |reportlab| raw:: html

   <a href="https://docs.reportlab.com/rmlfornewbies/" target="_blank">ReportLab</a>

.. |diferencias| raw:: html

   <a href="https://github.com/zopefoundation/z3c.rml/blob/master/RML-DIFFERENCES.rst" target="_blank">aquí</a>

.. |diferenciador| raw:: html

   <a href="https://www.diferenciador.com/tamanos-de-papel-carta-oficio-letter-legal-tabloide" target="_blank">enlace</a>

.. |z3c| raw:: html

   <a href="https://github.com/zopefoundation/z3c.rml/" target="_blank">z3c</a>

   