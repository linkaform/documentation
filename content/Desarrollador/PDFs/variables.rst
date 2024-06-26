.. _rml_django:

==========================
Potenciando RML con Django
==========================

Esta sección tiene el objetivo de brindarle suficiente información técnica para comprender la sintaxis del lenguaje del sistema de plantillas Django.

.. seealso:: ¿Qué es Django?

    Django es un framework gratuito y de código abierto basado en Python que sigue el patrón arquitectónico MVT (Model-View-Template). Se ejecuta del lado del servidor (back-end) y fomenta un desarrollo rápido con un diseño limpio y pragmático. 

    El sistema de plantillas de Django proporciona etiquetas que funcionan de manera similar a algunas construcciones de programación, como una etiqueta ``if`` para pruebas booleanas y una etiqueta ``for`` para bucles, entre otras. Sin embargo, estas etiquetas no se ejecutan directamente como el código Python correspondiente y el sistema de plantillas no ejecutará expresiones Python arbitrarias. De forma predeterminada, solo se admiten las etiquetas, los filtros y la sintaxis que se presentan en secciones posteriores (aunque se puede agregar extensiones propias al lenguaje de la plantilla).

    Para más información consulte la documentación oficial de |Django| :octicon:`report;1em;sd-text-info`.

.. important::

    El siguiente contenido se explicará en base al siguiente ejemplo. Asegúrese de actualizar y modificar según sus necesidades.

    También, tenga en cuenta consultar la documentación sobre formas en la aplicación web de Linkaform.

    .. dropdown:: Ver formulario

        .. image:: /imgs/PDF/ejemplocompleto.png

Variables
=========

Las variables permiten almacenar y representar información. En las plantillas de Django, puede representar variables poniéndolas entre ``{{ }}`` corchetes:

.. code-block:: xml
    :linenos:

    <story>
        {{ variable }}
    <story>

.. important:: El nombre de una variable debe seguir la convención |convención|. 

Los dobles corchetes ``{{ }}`` se utilizan para *llamar* a la variable. Cualquier contenido dentro de los dobles corchetes se interpreta como una instrucción para obtener y mostrar el valor real de la expresión en ese punto de la plantilla.

Una variable utiliza el signo de porcentajes ``{% %}`` para definir bloques de control y lógica, como declaraciones condicionales, bucles y otras operaciones que no necesariamente generan contenido directamente para mostrar, sino que afectan la estructura y el flujo de la plantilla.

Para declarar una variable utilice la palabra reservada ``set`` seguido del valor que desea asignar. Por ejemplo:

.. code-block:: xml
    :linenos:

    <story>
        {% set valor = 5 %}

        <para>{{ valor }}</para> <!-- Imprime 5 -->
    </story>

Template tags
=============

En las plantillas de Django, puede realizar lógica de programación. Sin embargo, Django tiene limitaciones; solo podrá ejecutar declaraciones ``if`` y bucles ``for``. 

.. seealso:: Las palabras reservadas ``if`` y ``for`` se denominan ``Template tags en Django``.

Para ejecutar ``template tags``, encierre entre corchetes ``{% %}``.

Condicionales
-------------

Una declaración ``if`` evalúa una variable y ejecuta un bloque de código si el valor es verdadero. 

.. code-block:: xml
    :linenos:

    <story>
        {% if condition %} 

            ... 

        {% endif %}
    </story>

.. note:: Utilice ``endif`` para cerrar la condición. Es obligatorio.

Utilice ``elif`` si la condición anterior no es verdadera.

.. code-block:: xml
    :linenos:

    <story>
        {% set variable1 = '' %}
        {% set flag = 2 %}

        {% if flag == 1 %}
            {% set variable1 = 'El valor es 1' %}
            {% elif flag == 2 %}
                {% set variable1 = 'El valor es 2' %}
            {% else %}
                {% set variable1 = 'No entro' %}
        {% endif %}
        
        <para>Variable: {{ variable1 }}</para>
    </story>

Puede utilizar los siguientes operadores lógicos. Consulte la siguiente documentación para obtener más |operadores| :octicon:`report;1em;sd-text-info`.

+-------------+----------------------------------------------------------------------------------------------+
| Operador    | Ejemplo de Uso                                                                               |
+=============+==============================================================================================+
| ==          | Usar el operador == para verificar si una variable es igual a un valor se puede eliminar     |
|             | si solo desea verificar si una variable no está vacía.                                       |
|             |                                                                                              |
|             | .. code-block:: xml                                                                          |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting %}                                                                    |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| !=          | No es igual a                                                                                |
|             |                                                                                              |
|             | .. code-block:: xml                                                                          |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting != 1 %}                                                               |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| <           | Menor que                                                                                    |
|             |                                                                                              |
|             | .. code-block::                                                                              |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting < 3 %}                                                                |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| <=          | Menor o igual que                                                                            |
|             |                                                                                              |
|             | .. code-block::                                                                              |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting <= 3 %}                                                               |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| >           | Mayor que                                                                                    |
|             |                                                                                              |
|             | .. code-block:: xml                                                                          |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting > 1 %}                                                                |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| >=          | Mayor o igual a                                                                              |
|             |                                                                                              |
|             | .. code-block:: xml                                                                          |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting >= 1 %}                                                               |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| and         | Para comprobar si más de una condición es verdadera.                                         |
|             |                                                                                              |
|             | .. code-block:: xml                                                                          |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting == 1 and day == "Friday" %}                                           |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| or          | Para comprobar si una de las condiciones es verdadera.                                       |
|             |                                                                                              |
|             | .. code-block:: xml                                                                          |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting == 1 or greeting == 5 %}                                              |
|             |             <para>Hola</para>                                                                |
|             |         {% endif %}                                                                          |
|             |     </story>                                                                                 |
|             |                                                                                              |
+-------------+----------------------------------------------------------------------------------------------+
| and/or      | Combina and y or.                                                                            |
|             |                                                                                              |
|             | .. code-block:: xml                                                                          |
|             |     :linenos:                                                                                |
|             |                                                                                              |
|             |     <story>                                                                                  |
|             |         {% if greeting == 1 and day == "Friday" or greeting == 5 %}                          |
|             |     </story>                                                                                 |
+-------------+----------------------------------------------------------------------------------------------+

.. code-block:: xml
    :linenos:

    {% if greeting == 1 and day == "Friday" or greeting == 5 %}

Bucles
------

Un bucle ``for`` se utiliza para iterar sobre una secuencia, como recorrer elementos de una matriz, una lista o un diccionario.

.. code-block:: xml
    :linenos:

    <story>
        {% for item in sequence %} 

            ... 

        {% endfor %}
    </story>

Django tiene algunas variables que están disponibles dentro de un bucle. Las más utilizadas son las siguientes. Para obtener más información, consulte el siguiente |enlace|.

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :align: left

   * - Atributo
     - Descripción
   * - forloop.counter
     - La iteración actual, comenzando en 1.

       .. code-block:: xml
        :linenos:
       
        <ul>
        {% for x in fruits %}
            <li>{{ forloop.counter }}</li>
        {% endfor %}
        </ul>

   * - forloop.counter0
     - La iteración actual, comenzando en 0.

       .. code-block:: xml
        :linenos:
       
        <ul>
        {% for x in fruits %}
            <li>{{ forloop.counter0 }}</li>
        {% endfor %}
        </ul>

   * - forloop.first
     - Le permite probar si el bucle está en su primera iteración.

       .. code-block:: xml
        :linenos:
       
        {% for x in fruits %}
        <td>
            {% if forloop.first %}
            <para> ================ </para>
            {% endif %}
        </td>
        {% endfor %}

   * - forloop.last
     - Le permite probar si el bucle está en su última iteración.

       .. code-block:: xml
        :linenos:
       
        {% for x in fruits %}
        <td>
            {% if forloop.last %}
            <para> ================ </para>
            {% endif %}
        </td>
        {% endfor %}

Acceso a atributos y métodos
============================

Puede acceder a la información de una variable utilizando un punto ``.``. Al usar ``.``  después de la variable, está indicando que necesita acceder a un atributo o método específico del objeto que representa esa variable.

Las formas en que puede utilizar el punto son las siguientes:

1. **Búsqueda de diccionario**

Si la variable es un diccionario, puede acceder a sus valores utilizando el nombre de la clave entre llaves, por ejemplo:

.. code-block:: xml
    :linenos:

    {{ usuario.nombre }}

2. **Búsqueda de atributo o método** 

Si la variable es un objeto que tiene atributos o métodos, acceda a ellos utilizando el nombre correspondiente después del punto. Por ejemplo, si tiene un objeto producto y desea obtener su método calcular_precio(), lo puede hacer de la siguiente manera: 

.. code-block:: xml
    :linenos:

    {{ producto.calcular_precio }}

3. **Indexación numérica** 

Si la variable es una lista, puede acceder a elementos específicos. Por ejemplo, si tiene una lista de nombres y desea obtener el primer nombre, lo logra así: 

.. code-block:: xml
    :linenos:

    {{ nombres.0 }}

Answers
=======

Utilice la palabra reservada ``answers`` seguida del ``ID`` del campo de la forma para extraer información de sus formularios. Por ejemplo:

.. code-block:: xml
    :linenos:

    {% set nombre = answers.646a69d6fb56c3sda00d7b036911216 %}

.. caution:: ``answers`` funciona de manera distinta para fotografías (imágenes), firmas, conjuntos repetitivos y documentos, ya que en estos casos se añade un tercer parámetro que corresponde a las URL.
        
Tags
====

Existen etiquetas que regularmente son utilizadas en los documentos. Algunas de las comúnmente utilizadas son las siguientes.

Fechas
------

Los formatos de fecha permiten personalizar la presentación de la fecha y la hora según lo requiera. 

``Y``: Año con 4 dígitos.

``m``: Mes con ceros iniciales.

``d``: Día del mes con ceros iniciales.

``H``: Hora en formato de 24 horas.

``i``: Minutos.

``s``: Segundos.

.. code-block:: xml
    :linenos:

    <story>
        <!-- FECHAS -->
        <para> FECHA :   {% set_date_format meta.created_at "%Y-%m-%d" "%Y-%m-%d %H:%M:%S" %} </para>

        <para> MES: {% get_month_txt answers.64c194dd696a295c093ef0a6 %} </para>

        <para> DÍA: {% get_day_txt  answers.64c194dd696a295c093ef0a6 %} </para>

        <para> DÍA ACTUAL: {% get_today "%d/%m/%Y %H:%M" %} </para>
    </story>

Cantidades
----------

Para realizar operaciones con cantidades, utilice la palabra reservada ``arithmetic``.

.. code-block:: xml
    :linenos:

    <story>
        <!-- CANTIDADES -->
        {% set dinero1 = 5000.950 %}
        <para>DINERO: {% money_format dinero1 decimal_precision=0 thousand_separator='.' %}</para>

        {% set valor1 = 0 %}
        {% set valor2 = 5 %}
        {% set resultado = 0 %}
        {% arithmetic 'resultado' 'valor1' '+' 'valor2' %}
        <para>SUMA: {{ resultado }}</para>

        {% set valor1 = 5 %}
        {% set valor2 = 10 %}
        {% set resultado = 0 %}
        {% arithmetic 'resultado' 'valor2' '-' 'valor1' %}
        <para>Resta: {{ resultado }}</para>

        {% set valor1 = 5 %}
        {% set valor2 = 10 %}
        {% set resultado = 0 %}
        {% arithmetic 'resultado' 'valor2' '*' 'valor1' %}
        <para>Multiplicación: {{ resultado }}</para>

        {% set valor1 = 5 %}
        {% set valor2 = 10 %}
        {% set resultado = 0 %}
        {% arithmetic 'resultado' 'valor2' '/' 'valor1' %}
        <para>División: {{ resultado }}</para>

        {% set valor = 5 %}
        <para>NOMBRE: {% number_to_txt valor %}</para>
        <para>NOMBRE: {% number_to_txt valor 'PESOS M/CTE'%}</para>
    </story>

Concatenar
----------

Se refiere a la acción de unir o combinar múltiples cadenas de texto o valores en una sola cadena. La concatenación es útil cuando se desea combinar información de diferentes variables o campos para presentarla conjuntamente. Se utiliza la palabra reservada ``concat``.

.. code-block:: xml
    :linenos:

    </story>
        <!-- CONCAT && AD -->
        {% set count = 0 %}
        {% set string = '' %}

        {% for l in answers.61a669d6fb59c3df00d7bed036d %}
            {% add_total 'count' 1 %}
            {% concat 'string' count 'True' %}

            <para> Iteración: {{ count }} </para>
        {% endfor %}
        <para> Concatenación: {{ string }} </para>
    </story>

Imágenes
--------

Para tratar imágenes utilice una condicional para evaluar que exista algo en el campo.

.. code-block:: xml
    :linenos:
    
    {% if answers.64c0644e130ce40b760135cd.0.file_url %}

.. important:: Al utilizar la condicional ``if answers.64ce10644de130ce4s0b760135cd.0.file_url`` esta dando por hecho que solo hay una imagen o que solamente quiere mostrar la primera imagen que pueda estar en el campo. Si el campo contiene mas de una imagen debe utilizar un bucle for.

Dentro de la etiqueta ``<imageAndFlowables>`` se utiliza la custom tag ``get_thumbnail`` que permite traer una copia de la imagen real pero con menor peso para evitar que el pdf no pese demasiado.

.. code-block:: xml
    :linenos:
    
    </story>
        <!--IMÁGENES -->

        <para> Imagen: </para>
        {% if answers.64c0644e130ce40b760135cd.0.file_url %}
            <imageAndFlowables
            imageName="{% get_thumbnail answers.64c0644e130ce40b760135cd.0.file_url  %}"
            imageWidth="10cm" imageHeight="6cm" imageSide="left" imageLeftPadding="4cm" />
        {% endif %}
    </story>

.. Tip:: Recuerde que la etiqueta ``<imageAndFlowables>`` no permite centrar directamente la imagen. Por ello, juegue con los atributos que ofrece. En el caso anterior, tome el siguiente ejemplo: si tiene un ancho de 18 cm y su imagen mide 10 cm por defecto, le sobran 8 cm. Sepárelas utilizando ``imageLeftPadding`` e ``imageRightPadding`` para ajustar.

Ejemplos
========

Con la información vista, contemple los siguientes casos de uso.

Catálogos
---------

Revise el siguiente ejemplo sobre catálogos.

.. tab-set::

    .. tab-item:: Ejemplo

        Considere el siguiente ejemplo sobre un catálogo de ``Tiendas``.

        .. image:: /imgs/PDF/20.png

    .. tab-item:: Código

        Los catálogos son fáciles de consultar. Simplemente declare una variable seguida de la palabra reservada ``answers``, seguido del ``Id`` del catálogo y luego el ``Id`` del campo, como se muestra a continuación:

        .. code-block:: xml
            :linenos:

            <para> Dirección: </para>
            {% set direccion = answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4af %}
            <para>{{ direccion }}</para>

        O de manera simplificada coloque:

        .. code-block:: xml
            :linenos:
            
            <para>Dirección: {{ answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4af }}</para>
        
        Si ejecuta los códigos anteriores, el resultado de ambas será:  

        .. code-block:: 
            :linenos:

            [u'Tijuana - Tecate, El Refugio, 22253, Plaza Sendero, Tijuana, B.C.']
        
        La razón por la que se obtiene así es porque los datos están estructurados e interpretados como listas. 

        Para resolver ese problema, simplemente coloque ``.0``. La notación ``.0`` indica que necesita acceder al primer elemento de una lista o un conjunto. Por ejemplo:

        .. code-block:: xml
            :linenos:

            <para> Dirección: </para>
            {% set direccion = answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4af.0 %}
            <para>{{ direccion }}</para>

        A continuación, se presenta el código necesario para imprimir los datos de un catálogo:

        .. code-block:: xml
            :linenos:  

            <para style="textTitleI"> Cadena: </para>
            {% set cadena = answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4ac %}
            <para>{{ cadena }}</para>

            <para style="textTitleI"> Tienda: </para>
            {% set tienda = answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4ae %}
            <para>{{ tienda }}</para>

            <para style="textTitleI"> Dirección: </para>
            {% set direccion = answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4af.0 %}
            <para>{{ direccion }}</para>
            
            <para style="textTitleI"> Estado: </para>
            {% set estado = answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4b0.0 %}
            <para>{{ estado }}</para>

            <para style="textTitleI"> Municipio: </para>
            <para>{{ answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4b1.0 }}</para>

    .. tab-item:: Resultado

        El resultado del ejemplo es el siguiente. Para fines prácticos, se muestra de la siguiente manera; sin embargo, considere aplicar los :ref:`estilos` :octicon:`report;1em;sd-text-info` necesarios: 

        .. image:: /imgs/PDF/21.png

        .. seealso:: En Django, al obtener datos de un formulario a veces es necesario acceder a elementos específicos de esa lista. Para saber cómo se presenta su información, puede inspeccionar la página en la que se encuentra su registro e inspeccionar sus datos y corroborar como viene la información.

Grupos repetitivos
------------------

Contemple el siguiente ejemplo sobre grupos repetitivos:

.. tab-set::

    .. tab-item:: Ejemplo

        Considere el siguiente grupo repetitivo ``Empleados``.

        .. image:: /imgs/PDF/16.png

    .. tab-item:: Código

        Para extraer datos de un grupo repetitivo de un formulario, siga los siguientes pasos:

        1. Especifique la tabla en la que desea representar el grupo repetitivo (linea 2-27).
        2. Declare un ciclo ``for`` para recorrer los elementos del grupo repetitivo colocando el ``id`` del mismo (linea 8).
        3. Si el campo es de tipo texto, simplemente llame la variable que utilizo para recorrer el grupo repetitivo seguido del ``id`` del campo (linea 12).
        4. Si dentro del grupo repetitivo hay imágenes, tenga en cuenta la siguientes consideraciones:

        - Si esta seguro de que el campo solo contendrá una imagen, podrá utilizar el siguiente código; donde está declarando la variable firma e igualándola al contenido de la imagen.

        .. code-block:: xml
            :linenos:

            {% set firma = item.64dd1d386170e28311ec20ff.file_url %}
            <imageAndFlowables imageName="{% get_thumbnail firma %}" imageWidth="5cm" imageHeight="2cm" imageSide="left"/>

        .. important:: Recuerde que una una firma es guardada y tratada como una imagen.

        - De lo contrario, si tiene mas de una imagen, deberá crear otro ciclo para mostrar todas las imágenes. 

        .. code-block:: xml
            :linenos:

            {% for image in item.64dd1c61039ce8cf6a1a91e7 %}
                {% set img = image.file_url %}
                <imageAndFlowables imageName="{% get_thumbnail img %}" imageWidth="4cm" imageHeight="2cm" imageSide="left" />
            {% endfor %}

        .. code-block:: xml
            :linenos:
            :emphasize-lines: 2, 8, 12, 27

            <story>
                <blockTable colWidths="5cm, 6cm, 6cm" style="general">
                    <tr>
                        <td><para> Nombre </para></td>
                        <td><para> Fotografía </para></td>
                        <td><para> Firma</para></td>
                    </tr>
                    {% for item in answers.64dd1bd4fd200a3308ec2140 %}
                        <tr>
                            <td>
                            <para>
                                    {{ item.64dd1c61039ce8cf6a1a91e6 }} 
                            </para>
                            </td>
                            <td>
                                {% for image in item.64dd1c61039ce8cf6a1a91e7 %}
                                    {% set img = image.file_url %}
                                    <imageAndFlowables imageName="{% get_thumbnail img %}" imageWidth="4cm" imageHeight="2cm" imageSide="left" />
                                {% endfor %}
                            </td>
                            <td>
                                {% set firma = item.64dd1d386170e28311ec20ff.file_url %}
                                <imageAndFlowables imageName="{% get_thumbnail firma %}" imageWidth="5cm" imageHeight="2cm" imageSide="left"/>
                            </td>            
                        </tr>
                {% endfor %}
                </blockTable>
            </story>

    .. tab-item:: Resultado
        
        El resultado del ejemplo es el siguiente. Para fines prácticos, se muestra de la siguiente manera, sin embargo, considere aplicar los :ref:`estilos` :octicon:`report;1em;sd-text-info` necesarios:
        
        .. image:: /imgs/PDF/19.png

Custom Tags
===========

Las custom tags son etiquetas personalizadas de Linkaform para realizar tareas específicas en las plantillas que no pueden ser manejadas con las etiquetas existentes. A continuación, se presentan algunas etiquetas personalizadas (custom tags). Revise los comentarios en el código para obtener más información.

.. code-block:: xml
    :linenos:

    <!-- Contiene los metadatos de cada registros -->
    meta
    Code: {{ meta }}
    Type: dict 

    connection
    Code: {{ meta.connection }}
    Type: string
    Default: 'N/A'

    <!-- Fecha de creación de registro en formato 'YYYY-MM-DD HH:mm:ss' -->
    created_at
    Code: {{ meta.created_at }}
    Type: string

    <!-- Nombre del usuario que creo el registro -->
    created_by_name
    Code: {{ meta.created_by_name }}
    Type: unicode string`

    <!-- Tiempo que tardo en crear el registro -->
    duration
    Code: {{ meta.duration }}
    Type: unicode string

    <!-- Fecha de finalización de registro en formato 'YYYY-MM-DD HH:mm:ss' -->
    end_date
    Code: {{ meta.end_date }}
    Type: string

    <!-- Folio del registro -->
    folio
    Code: {{ meta.folio }}
    Type: unicode string

    <!-- Contiene la url de google maps del creador/editor del registro (siempre y cuando el usuario permitió tomar la geolocalización) -->
    geolocation
    Code: {{ meta.geolocation }}
    Type: string

    points
    Code: {{ meta.points }}
    Type: int

    <!-- Fecha de inicio de creación/edición de registro en formato 'YYYY-MM-DD HH:mm:ss' -->
    start_date
    Code: {{ meta.start_date }}
    Type: string

    <!-- Fecha de última modificación de registro en formato 'YYYY-MM-DD HH:mm:ss' -->
    updated_at
    Code: {{ meta.updated_at }}
    Type: string

    <!-- Version del registro -->
    version
    Code: {{ meta.points }}
    Type: int

.. important:: Anteriormente, se mencionó que el proceso para preparar su documento depende del código del mismo. Todo el contenido visto hasta ahora funciona de manera similar tanto para un documento de registro único como para un documento de múltiples registros. Sin embargo, para documentos de múltiples registros, debe colocar su código dentro de un bucle ``for`` para indicarle a Django que ejecute ese mismo código varias veces (por cada registro seleccionado) para procesar su información.

    .. code-block:: xml
        :linenos:

        </story>
            {% for l in answers_list %}

                <!-- Código -->

            {% endfor %}
        </story>

En esta sección, aprendió el uso de Django Template Language para la creación de plantillas dinámicas, permitiéndole generar documentos adaptados a sus necesidades específicas. Aprendió el uso de variables, declaraciones condicionales y bucles, así como la forma de pasar y acceder a datos en las plantillas. Además, aprendió a cerca de custom tags (etiquetas personalizadas) para tareas específicas y la inclusión de imágenes en los documentos generados.

¡Felicidades! 🎉 Si ha seguido la documentación secuencialmente, ahora es capaz de generar sus propios documentos PDF personalizados. Si tiene alguna duda, puede regresar al contenido o consultar la documentación oficial de la sección de su preferencia.

.. LIGAS EXTERNAS

.. |Django| raw:: html

   <a href="https://www.djangoproject.com/" target="_blank">Django</a>

.. |convención| raw:: html

   <a href="https://es.wikipedia.org/wiki/Snake_case" target="_blank">snake_case</a>

.. |operadores| raw:: html

   <a href="https://www.w3schools.com/django/django_tags_if.php" target="_blank">información</a>

.. |enlace| raw:: html

   <a href="https://www.w3schools.com/django/django_tags_for.php" target="_blank">enlace</a>