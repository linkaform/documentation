================================
Vinculación de PDF con una forma
================================

La vinculación del PDF con la forma es una acción importante. Cuando se
liga un PDF especificamos que es exclusivo a las necesidades de la
forma. Independientemente de si trabaja con un ``single record`` o
``multiple record`` la vinculación es diferente. 

Vinculación single record
=========================

El primer paso consiste en garantizar que la plantilla esté configurada
para funcionar como un ``single record`` (registro único). Para lograr
esto, es esencial verificar y ajustar el atributo ``type`` en la
interfaz de administración de Django.

.. image:: /imgs/PDF/4/4.3.0.png
  :align: center

Posteriormente la configuración del lado de la forma es la siguiente.

Seleccione la forma a la que desea vincular el PDF. Para realizar esto
seleccione ``opciónes`` y dentro de ella ``opciones generales``.

.. image:: /imgs/PDF/4/4.3.1.png
  :align: center

Dentro de la sección ``Opciones Generales``, proceda a elegir la opción
``Plantillas de PDF``. En el apartado de plantilla, seleccione el nombre
que haya asignado a la plantilla previamente definida en el entorno de
Django.

.. image:: /imgs/PDF/4/4.3.2.png
  :align: center

Al seleccionar la opción, agregue la plantilla y automáticamente se
mostrará el nombre, seguido de dos alternativas: un botón azul y la
opción de eliminar. A continuación, haga clic en “OK”.

.. important::
   No se debe seleccionar el punto azul en este momento, ya que esta acción será realizada en etapas posteriores del proceso.


.. note::
   Es fundamental resaltar también que, después de hacer clic en “OK”, es necesario guardar la forma de manera completa.

.. image:: /imgs/PDF/4/4.3.3.png
  :align: center

Una vez guardada la forma, regrese a la sección de “Plantillas de PDF”.
Después, elija el nombre de la plantilla en el recuadro azul. A
continuación, en el campo “Nombre de PDF”, escriba el ``nombre`` que le
asignó previamente en la plantilla de Django, seguido de un guion medio
``-``.

Luego, en el “Campo”, seleccione el metadato relacionado con el
``folio del registro``, que es el número único del registro
correspondiente, automáticamente llenará el nombre del PDF con doble
corchete ``{{}}``. Finalmente, haga clic en “Guardar”.


.. note::
   El estándar utilizado para el nombre del PDF es: :bdg-success:`[ nombre PDF ] [ _ ] [ campo ]`

.. image:: /imgs/PDF/4/4.3.4.png
  :align: center

Después de guardar, el nombre del PDF se insertará automáticamente en el
recuadro del nombre de la plantilla. Solo necesita hacer clic en “OK”.

.. image:: /imgs/PDF/4/4.3.5.png
  :align: center

Asimismo, es aconsejable guardar la forma en su totalidad. Al seguir
este proceso, se asegura la adecuada vinculación y creación de los PDFs
bajo el enfoque de ``single record``.

.. image:: /imgs/PDF/4/4.3.6.png
  :align: center


Vinculación Multiple record
===========================

De la misma manera verifique que la configuración del ``type`` en el
administrador de plantillas de Django esté establecida en
``multiple records`` (registros múltiples).

.. image:: /imgs/PDF/4/4.3.7.png
  :align: center

Siga los pasos anteriores para llegar a la opción de “Plantillas de PDF” en ``opciones generales``.

Cuando se trabaja con el tipo ``multiple records`` (registros
múltiples), la configuración es más simple. Simplemente seleccione el
nombre de la plantilla que previamente estableció en el administrador de
plantillas de Django. Al hacer esta elección, notará que se resalta una
etiqueta verde con el texto ``multiple``. Luego, agregue la plantilla y
observe cómo se añade al recuadro. Finalmente, haga clic en “OK” y
guarde la forma en su totalidad.

Siguiendo estos pasos, asegura que la plantilla esté adecuadamente
preparada para recibir múltiples registros bajo el enfoque de
``multiple records``.

.. image:: /imgs/PDF/4/4.3.9.png
  :align: center

