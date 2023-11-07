======================
Documentando LinkaForm
======================

¡Bienvenido y gracias por considerar contribuir a la documentación de **Linkaform** y por aportar su tiempo y experiencia!

Esta guía introductoria le permitirá adquirir las herramientas y el conocimiento que necesita para escribir documentación y desarrollar nuevos módulos para ampliar la funcionalidad de Linkaform. Al crear módulos personalizados y ponerlos a disposición de otros, puede ayudar a hacer crecer el ecosistema de Linkaform y brindar valor adicional a los usuarios de la plataforma.

Linkaform utiliza el entorno Sphinx y el lenguaje reStructuredText como sus herramientas principales para desarrollar documentación en línea. En esta sección, le ofrecemos una breve introducción a Sphinx y su uso. Al final, tendrá un proyecto listo para su lanzamiento público.

Para obtener detalles adicionales, consulte la guía completa de `Sphinx <https://www.sphinx-doc.org/en/master/>`_ :octicon:`report;1em;sd-text-info`.

Pautas de contenido
===================

Con el fin de ofrecer a la comunidad la mejor documentación posible, se presentan algunas pautas, consejos y trucos que debe tener en cuenta para que su contenido destaque.

Estructura del documento 
------------------------

Antes de iniciar una sección, es importante definir y elaborar un esquema de contenidos. Esto le permitirá organizar y dar prioridad a los elementos. Siempre es más conveniente comenzar elaborando un borrador y posteriormente, preocuparse por la conversión de su texto a rst (reStructuredText).

Utilice distintos niveles de encabezado para estructurar su texto en secciones y subsecciones. Estos encabezados no sólo se mostrarán en el documento, sino también en el menú de navegación, lo que facilitará que el usuario encuentre rápidamente el contenido de su interés.

.. tip:: Al comienzo de una sección, inicie con un párrafo introductorio que oriente al lector y le ayude a confirmar que ha llegado a la página correcta.

Imágenes
--------

Incorporar algunas imágenes para ilustrar su texto beneficia a los lectores al facilitar la comprensión de su contenido. Sin embargo, es importante evitar la inclusión excesiva de imágenes.

.. caution:: No es necesario ilustrar cada paso y función, ya que esto puede sobrecargar su página.

Capturas de pantalla
^^^^^^^^^^^^^^^^^^^^

Cuando deba incluir capturas de pantalla en su documentación, asegúrese de cumplir con las siguientes pautas:

- Las imágenes deben ser coherentes con el contenido circundante.

- Ajuste el tamaño de las capturas para mostrar los detalles esenciales.

- Evite capturar la pantalla completa y si es necesario, edite las imágenes para resaltar lo que se quiere demostrar.

- Utilice texto alternativo con nombres cortos (máximo una línea) y evite que sea una repetición de una oración o título previamente mencionado.

.. important:: Para editar sus imágenes, utilice Paint o puede acceder a `jspaint <https://jspaint.app/>`_ :octicon:`report;1em;sd-text-info`. Utilice la herramienta de dibujo con el color rojo para resaltar áreas específicas, y si necesita señalar un elemento, puede utilizar una imagen genérica llamada ``flecha_roja.png`` ubicada en ``documentation/content/imgs``.

Escritura
---------

En la documentación, es más probable que los lectores busquen información específica al explorar el contenido. Por lo tanto, es importante recordar que la documentación de usuario tiene como propósito informar y describir, en lugar de convencer o promocionar.

Tiempos gramaticales
^^^^^^^^^^^^^^^^^^^^

Cuando se dirija al usuario y proporcione descripciones, pasos e instrucciones, utilice el presente simple. Para ejemplos o eventos futuros, utilice el futuro simple. A continuación, se presentan algunos ejemplos:

.. tab-set::

    .. tab-item:: Presente simple

        Correcto: La computadora realiza copias de seguridad automáticas cada noche.

        Incorrecto: La computadora realizará copias de seguridad automáticas cada noche.

    .. tab-item:: Futuro simple

        Correcto: La nueva versión del software se lanzará la próxima semana.

        Incorrecto: La nueva versión del software se lanza la próxima semana.

También asegúrese de cumplir los siguientes puntos:

- **Claridad y Simplicidad**: Utilice un lenguaje claro y sencillo para explicar conceptos técnicos. Por ejemplo: En lugar de *la interfaz de programación de aplicaciones* utilice *herramienta de programación*.

- **Consistencia**: Organice el contenido de forma lógica, utilizando secciones, subtítulos y una introducción clara. Si modifica un texto existente, procure igualar el tono y la presentación ya establecidos o escriba de manera que concuerde con su propio estilo.

- **Definición de Términos Técnicos**: Proporcione definiciones claras para términos técnicos o acrónimos. Por ejemplo, *API significa Interfaz de Programación de Aplicaciones*.

- **Uso de Ejemplos y Casos de Uso**: Utilice  ejemplos prácticos que ilustren cómo utilizar la tecnología o solución.

.. tip:: Recuerde tener un equilibrio entre texto e imágenes.

Es momento de iniciar con la configuración de su entorno, o en su defecto, comience por escribir sus primeros archivos rst.
