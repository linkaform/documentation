===============================
Plantillas estructura en Django
===============================

Para iniciar la estructura de su PDF, debe realizar algunas configuraciones dentro del entorno de Django. Siga los siguientes pasos:

1. Inicie sesión en Django.
  
  - producción https://preprod.linkaform.com/admin :octicon:`report;1em;sd-text-info`.
  
  - preproducción https://app.linkaform.com/admin :octicon:`report;1em;sd-text-info`.

2. Una vez autenticado, se muestra la siguiente interfaz.

.. image:: /imgs/PDF/4/4.1.1.png
  :align: center

La administración de Django permite el acceso a una gran variedad de recursos. No obstante, con el propósito de abordar el desarrollo de archivos PDFs, se continuará por detallar la sección ``Pdfdocuments``, la cual se compone de dos elementos importantes:

+-----------+---------------------------------------------------------+
| Opción    | Descripción                                             |
+===========+=========================================================+
| Plantillas| Contiene todas las plantillas generadas en Linkaform.   |
+-----------+---------------------------------------------------------+
| Widgets   | Proporciona plantillas adaptadas a los diferentes tipos |
|           | de datos utilizados.                                    |
+-----------+---------------------------------------------------------+

En cuanto a las ``plantillas``, al ingresar a esta sección se visualiza
un listado en el que se muestra la opción de ``agregar`` o ``modificar``
una plantilla.

.. image:: /imgs/PDF/4/4.1.2.png
  :align: center


En la opción ``modificar plantilla``, se muestra una lista
de plantillas ya existentes y que actualmente son utilizadas por
clientes de ``LinkaForm``. De igual manera, existe la opción de agregar
una plantilla nueva.

.. image:: /imgs/PDF/4/4.1.4.png
  :align: center


En ``agregar plantilla`` se muestra un formulario con las siguientes
opciones.

:bdg-secondary:`Name`: Nombre de la plantilla.

.. note::
   El estándar utilizado para el nombre de una plantilla es: :bdg-success:`[ nombre cliente ] [ _ ] [ nombre PDF ]`


**Type:**

:bdg-secondary:`Single record`: Plantilla preparada para un solo registro. 

:bdg-secondary:`Multiple records`: Plantilla preparada para recibir múltiples registros.

:bdg-secondary:`Paginate`: Permite colocar el número de página del documento (Opcional).

:bdg-secondary:`Description`: Está estandarizada y se inicia con <``Template``><``de``><``nombre del PDF``><``para``><``nombre del cliente``>.

.. important::
   Ciertamente, se puede ofrecer una descripción más detallada. No
   obstante, es recomendable mantenerla concisa debido a la posibilidad
   de generar confusión al vincular el PDF con la forma.

:bdg-secondary:`Defalut`: Define la plantilla por defecto de la forma cuando no se ha seleccionado ninguna.

:bdg-secondary:`Preview`: —

:bdg-secondary:`Header`: Encabezado del documento con lenguaje RML (opcional).

:bdg-secondary:`Body`: Cuerpo del documento con lenguaje RML (requerido).

:bdg-secondary:`Footer`: Píe de página del documento con lenguaje RML (requerido).

:bdg-secondary:`Style`: Estilo del documento con lenguaje RML (requerido).

:bdg-secondary:`Owner`: Cuenta padre a la que se va asignar la plantilla.

.. image:: /imgs/PDF/4/4.1.3.1.png
  :align: center

.. image:: /imgs/PDF/4/4.1.3.2.png
  :align: center

.. image:: /imgs/PDF/4/4.1.3.3.png
  :align: center

Plantillas estructura en archivos
=================================

El objetivo de las plantillas consiste en establecer una estructura
estandarizada para el proyecto, de manera que cada cliente cuente con un
único archivo de encabezado, cuerpo, pie de página y estilos.

.. mermaid::

   graph TB
     
   A(Cliente)
   A --> B[Header]
   A --> C[Body]
   A --> D[Footer]
   A --> E[Style]

La estructura estándar de los archivos utilizan la siguiente notación:
:bdg-success:`[ nombre cliente ] [ _ ] [ tipo de archivo ] [.xml]`


.. image:: /imgs/PDF/4/4.1.5.png
  :align: center

Estructura header y footer
==========================

Tal como se explicó previamente es opcional tener un archivo ``header``
y ``footer``, ya que es válido insertar el ``header`` y el ``footer``
directamente en el archivo ``body``. No obstante, el propósito es lograr
una organización más eficiente mediante la separación de código para una
mejor estructura.

Los archivos de ``header`` y ``footer`` se llaman gracias a las
etiquetas de django del archivo base ``body_base.xml``, por ahora se
muestran las etiquetas donde se llaman ambos archivos:

.. code:: xml

    <pageGraphics>

    <!-- Cabecera de documento -->
    {% Header company_logo parent user form Template meta %}

    <!-- Pie del documento -->
    {% Footer user form Template meta %}

    </pageGraphics>

Estructura body
===============

La estructura base de ``body`` utiliza en su mayoría el siguiente
código.

.. code-block:: xml

   <?xml version="1.0"?>
   <!-- Variables de Django - No se mueve-->
   {% load PrintFields %}
   {% load set_var %}
   {% load custom_tags %}
   <!-- Condiguración del documento -->
   <document filename="Example" xmlns:doc="http://namespaces.zope.org/rml/doc">
       <!-- Propiedades informativas -->
       <pageInfo pageSize="(21cm,27.5cm)" doc:example="" />
           <!-- Tipografia del documento -->
           <docinit> 
           <registerTTFont faceName="Montserrat-Regular" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Regular.ttf" />
           <registerTTFont faceName="Montserrat-Bold" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-Bold.ttf" />
           <registerTTFont faceName="Montserrat-BoldItalic" fileName="/srv/backend.linkaform.com/infosync-api/backend/staticfiles/fonts/Montserrat-BoldItalic.ttf" />
       </docinit>
       <!-- En Template se define el tamaño(pageSize) y limites de la hoja(frame y sus atributos) -->
       <template pageSize="(22cm,28cm)" title="Examples" author="LinkaForm">
           <pageTemplate id="first">
               <frame id="first"    x1="1.5cm"   y1="1.5cm" width="19cm" height="25cm"/>
               <pageGraphics>
                   <setFont name="Montserrat-Regular" size="7.5"/>
                   <setFont name="Montserrat-Regular" size="8"/>
                   <!-- drawCenteredString - No se mueve -->
                   <drawCenteredString x="10.5cm" y="27.8cm">
                   {{direccion}}
                   </drawCenteredString>
                   <!-- Cabecera de documento - No se mueve-->
                   {% Header company_logo parent user form Template meta %}
                   <!-- Pie del documento - No se mueve -->
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
       </story>
   </document>

Estructura style
================

El archivo ``style`` adquiere un rol significativo en el proceso. En
este documento, se establecen los parámetros estéticos necesarios para
cada plantilla, definiendo aspectos como colores, dimensiones y otras
características esenciales.

.. code-block:: xml

    <!-- Ejemplo de estilos básicos de una tabla -->
    <blockTableStyle id="general">
      <lineStyle thickness="0.5" kind="GRID" colorName="#cfd8dc" start="0,0" stop="-1,-1" />
      <blockAlignment value="center" start="0,0" stop="-1,-1"/>
      <blockValign value="middle"/>
    </blockTableStyle>

En esta sección, se ha abordado de manera detallada la estructura y los
componentes fundamentales relacionados con la creación y administración
de plantillas en el entorno de Administración de Django. Se subrayó la
relevancia de la interfaz ``Pdfdocuments``, resaltando sus dos elementos
principales: ``plantillas`` y ``widgets``. Asimismo, se destacó la
intención de estandarizar la organización de los archivos ``Header``,
``Body``, ``Footer`` y ``Style`` para lograr una mejor estructuración.

En secciones posteriores, se profundizará en explicar las estructuras de
código antes presentadas, se abordaran aspectos tales como programación,
etiquetas básicas y la gestión de estilos en el ``lenguaje RML``. Este
contenido proporcionará una comprensión más completa y técnica para
aprovechar al máximo las capacidades de generación de PDFS, llevando la
gestión de plantillas a un nivel más avanzado y efectivo.
