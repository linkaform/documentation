===================
Errores comunes 
===================

En esta sección, podrá identificar errores comunes al trabajar con Sphinx y aprender cuáles son las mejores formas de corregirlos.

Afortunadamente, Sphinx es demasiado flexible y facilita el proceso de identificación de errores. Proporciona la ubicación exacta del archivo en el que se produce el error y un mensaje breve pero conciso que señala la causa del mismo. Esto simplifica la corrección de errores y la depuración de la documentación.

Secciones
---------

El error más común que puede surgir al trabajar con Sphinx está relacionado con las secciones, especialmente al trabajar con títulos y subtítulos. 

En la siguiente imagen observe el título y subtítulo:

.. image:: /imgs/Contribución/20.png

Del ejemplo anterior la terminal nos muestra los siguientes errores:

.. image:: /imgs/Contribución/19.png

El mensaje de error :bdg-danger:`CRITICAL: Title overline & underline mismatch` indica que la línea superior y la línea inferior del título no coinciden en longitud. Es importante garantizar que el título principal no presente este error, ya que en el peor de los casos, el contenido no se mostrará en el índice principal.

El mensaje de advertencia :bdg-danger:`WARNING: Title underline too short` indica que la línea que sigue al subtítulo tiene una línea de subrayado demasiado corta para considerarse válido. 

.. tip:: Para solucionar este problema, asegúrese de que las líneas de formato coincidan con la longitud del título o subtítulo.

.. image:: /imgs/Contribución/21.png
