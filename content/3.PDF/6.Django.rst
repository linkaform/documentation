=========
Variables
=========

Una variable es la representación de un valor. Puede almacenar
información que se puede usar y modificar. La estructura de una variable
es la siguiente ``{{variable}}``.

.. note::
   Los nombres de variables consisten en cualquier combinación de
   caracteres alfanuméricos y el guión bajo ``__``, pero no pueden
   comenzar con un guión bajo y no puede ser un número. También es
   importante destacar que no puede tener espacios o caracteres de
   puntuación.

Para definir una variable se utiliza la palabra reservada ``set``
seguido del valor que se desea asignar. Por ejemplo:
``{{ set variable = "contenido" }}``

Los dobles corchetes ``{{ }}`` se utilizan para “imprimir”. Cualquier
contenido dentro de los dobles corchetes se interpreta como una
instrucción para obtener y mostrar el valor real de la expresión en ese
punto de la plantilla. Dentro de los dobles corchetes, se pueden
insertar variables, aplicar filtros y realizar operaciones.

Los porcentajes ``{% %}`` se utilizan para definir bloques de control y
lógica, como declaraciones condicionales, bucles y otras operaciones que
no necesariamente generan contenido directamente para mostrar, sino que
afectan la estructura y el flujo de la plantilla.

Acceso a Atributos y Métodos con el Punto (.)
---------------------------------------------

Se utiliza un punto (``.``) para acceder a los atributos de una
variable. Cuando se usa un punto ``(.)`` después de una variable, se
está indicando que se desea acceder a un atributo o método del objeto
que representa esa variable.

Las formas en que se intentan las búsquedas cuando se utiliza un punto
después de una variables son las siguientes:

1. **Búsqueda de diccionario**: Si la variable es un diccionario, se
   puede acceder a sus valores utilizando el nombre de la clave entre
   llaves ``{{ usuario.nombre }}``.

2. **Búsqueda de atributo o método**: Si la variable es un objeto que
   tiene atributos o métodos, se puede acceder a ellos usando el nombre
   del atributo o método después del punto. Por ejemplo, si tiene un
   objeto ``producto`` y quiere obtener su método ``calcular_precio()``,
   se realiza de la siguiente manera:
   ``{{ producto.calcular_precio }}``.

3. **Indexación numérica**: Si la variable es una lista se puede acceder
   a elementos específicos. Por ejemplo, si tiene una lista ``nombres``
   y se desea obtener el primer nombre, se obtiene así:
   ``{{ nombres.0 }}``.

Answers
-------

Se utiliza la palabra reservada ``answers`` para traer los datos reales
del formulario. Es decir,
``{% set num_serie = answers.64669d6fb56c300d7bed036a %}``. El número
seguido del punto es la key generada en el formulario. (LINK Generar ID's)

.. important::

   El answers funciona diferente para las fotografías (imágenes),
   firmas, sets repetitivos y documentos. Ya que tienen un tercer
   parámetro que son las URL.



Estructuras de control
----------------------

Declaraciones condicionales con {% if %}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Las declaraciones condicionales permiten realizar acciones basadas en
condiciones específicas. Se utiliza
``{% if condition %} ... {% endif %}`` para construir bloques
condicionales. Si la condición se cumple, el contenido dentro del bloque
se ejecuta.

Declaraciones lógicas con {% if %}, {% elif %} y {% else %}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Además de ``{% if %}``, se puede usar ``{% elif %}`` y ``{% else %}``
para construir declaraciones lógicas más complejas. Esto permite manejar
múltiples condiciones y posibilidades.

.. code:: xml

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
        <para>VARIABLE: {{ variable1 }}</para>
   </story>

Bucles con {% for %}
^^^^^^^^^^^^^^^^^^^^

Los bucles permiten iterar sobre una secuencia de elementos, como una
lista o un conjunto. Aquí se utiliza
``{% for set item  in sequence %} ... {% endfor %}`` para crear bucles.
Cada iteración se realiza con un valor diferente de ``item`` en la
secuencia.

.. code:: xml

   <document>
       <template>
           <pageTemplate>
               <!-- Definir la estructura de la página -->
           </pageTemplate>
       </template>
       
       <story>
           <para>Informe de Productos con Precios Especiales</para>
           
           {% for producto in productos %}
               <para>Producto: {{ producto.name }}</para>
               <para>Precio: ${{ producto.precio|floatformat:2 }}</para>
               
               {% if producto.especial %}
                   <para>¡Precio Especial!</para>
               {% endif %}
               <br/>
           {% endfor %}
       </story>
   </document>

En este ejemplo:

-  ``{% for producto in productos %} ... {% endfor %}`` itera sobre una
   lista de productos. ``producto`` se refiere a cada elemento en la
   lista.
-  ``{% if product.especial %} ... {% endif %}`` verifica si el producto
   tiene un precio especial. Si es así, muestra un mensaje de “Precio
   Especial”.

Custom Tags de LinkaForm
------------------------

Las custom tags de LinkaForm son etiquetas personalizadas para realizar
tareas específicas en las plantillas que no pueden ser manejadas con las
etiquetas y filtros existentes.

.. code:: xml

   meta
   Code: {{ meta }}
   Type: dict contiene una o mas llaves listadas a contuniación.
   Contiene los metadatos de cada registros.

   connection
   Code: {{ meta.connection }}
   Type: string
   Default: 'N/A'

   created_at
   Code: {{ meta.created_at }}
   Type: string
   Fecha de creación de registro en formato 'YYYY-MM-DD HH:mm:ss'

   created_by_name
   Code: {{ meta.created_by_name }}
   Type: unicode string`

   duration
   Code: {{ meta.duration }}
   Type: unicode string

   end_date
   Code: {{ meta.end_date }}
   Type: string
   Fecha de finalización de registro en formato 'YYYY-MM-DD HH:mm:ss'

   folio
   Code: {{ meta.folio }}
   Type: unicode string

   geolocation
   Code: {{ meta.geolocation }}
   Type: string
   Contiene la url de google maps del creador/editor del registro (siempre y cuando el usuario permitió tomar la geolocalización)

   points
   Code: {{ meta.points }}
   Type: int

   start_date
   Code: {{ meta.start_date }}
   Type: string
   Fecha de inicio de creación/edición de registro en formato 'YYYY-MM-DD HH:mm:ss'

   updated_at 
   Code: {{ meta.updated_at }}
   Type: string
   Fecha de última modificación de registro en formato 'YYYY-MM-DD HH:mm:ss'
   string of date in format 'YYYY-MM-DD HH:mm:ss'

   version
   Code: {{ meta.points }}
   Type: int
   Versión del registro.

Fechas
^^^^^^

Los formatos de fecha se basan en códigos que representan partes
específicas de la fecha y la hora.

-  ``Y``: Año con 4 dígitos.
-  ``m``: Mes con ceros iniciales.
-  ``d``: Día del mes con ceros iniciales.
-  ``H``: Hora en formato de 24 horas.
-  ``i``: Minutos.
-  ``s``: Segundos.

.. code:: xml

   <!-- FECHAS -->
       <para>FECHA : {% set_date_format meta.created_at "%Y-%m-%d" "%Y-%m-%d %H:%M:%S" %} </para>
       
       <para >MES: {% get_month_txt answers.64c194dd696a295c093ef0a6 %} </para>
       
       <para>DÍA: {% get_day_txt answers.64c194dd696a295c093ef0a6 %} </para>
       
   <para>DÍA ACTUAL: {% get_today "%d/%m/%Y %H:%M" %} </para>

Cantidades
^^^^^^^^^^

Realizar operaciones con cantidades se utiliza la palabra reservada
``arithmetic`` .

.. code:: xml

     
      <!-- CANTIDADES -->
      {% set  dinero1 = 5000.950 %}
      <para >DINERO: {% money_format dinero1 decimal_precision=0 thousand_separator='.' %}</para>

      {% set  valor1 = 0 %}
      {% set  valor2 = 5 %}
      {% set  resultado = 0 %}
      {% arithmetic 'resultado' 'valor1' '+' 'valor2' %}
      <para >SUMA: {{ resultado }}</para>


      {% set  valor1 = 5 %}
      {% set  valor2 = 10 %}
      {% set  resultado = 0 %}   
      {% arithmetic 'resultado' 'valor2' '-' 'valor1' %}
      <para >Resta: {{ resultado }}</para>
      
      
      {% set  valor1 = 5 %}
      {% set  valor2 = 10 %}
      {% set  resultado = 0 %}
      {% arithmetic 'resultado' 'valor2' '*' 'valor1' %}
      <para >Multiplicación: {{ resultado }}</para>
      
      
      {% set  valor1 = 5 %}
      {% set  valor2 = 10 %}
      {% set  resultado = 0 %}
      {% arithmetic 'resultado' 'valor2' '/' 'valor1' %}
      <para >División: {{ resultado }}</para>
      
      
      {% set  valor = 5 %}
      <para >NOMBRE: {% number_to_txt valor %}</para>
      <para >NOMBRE:  {% number_to_txt valor 'PESOS M/CTE'%}</para>

Concatenar
----------

Se refiere a la acción de unir o combinar múltiples cadenas de texto o
valores en una sola cadena. La concatenación es útil cuando se desea
combinar información de diferentes variables o campos para presentarla
de manera conjunta en tus plantillas. Se utiliza la palabra reservada
``concat``.

.. code:: xml

   <!-- CONCAT && AD -->
   {% set count = 0 %}
   {% set string = '' %}

      {% for l in answers.64669d6fb56c300d7bed036d %}
         {% add_total 'count' 1 %}
         {% concat 'string' count 'True' %}
         
         <para> Iteración: {{ count }} </para>
      {% endfor %}
      <para> Concatenación: {{ string }} </para>

Imágenes
--------

**Rutas de Imágenes:** Antes de imprimir las imágenes es importante
obtener la ruta o URL de la imagen. Esta ruta es una URL pública
generada por LinkaForm.

.. code:: xml

   <!-- IMÁGENES -->
   <para> Imágen: </para>

   {% if answers.64c0644e130ce40b760135cd.0.file_url %}
      <imageAndFlowables
         imageName="{% get_thumbnail answers.64c0644e130ce40b760135cd.0.file_url %}"
         imageWidth="10cm"
         imageHeight="6cm"
         imageSide="left"
         imageLeftPadding="4cm"
      />
   {% endif %}


En esta sección, se exploró cómo utilizar Django Template Language en el
contexto de RML (Report Markup Language). Se presentó la forma de
trabajar con variables, controlar el flujo de contenido con
declaraciones condicionales y bucles, y cómo pasar y acceder a datos en
las plantillas. También se mostraron custom tags (etiquetas
personalizadas) para tareas específicas y cómo trabajar con imágenes en
los documentos generados. Estas tags permiten crear plantillas dinámicas
y generar plantillas a la medida.

