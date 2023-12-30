==================
Bases de Linkaform
==================

En el módulo ``Reportes`` de Linkaform, tiene la capacidad de explorar visualmente los resultados extraídos de las formas a través de filtros, gráficos y tablas.

Para acceder a los ``Reportes``, siga los pasos:

1. Ingrese a la aplicación web oficial de |Linkaform| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales.

.. note:: En caso de no contar con credenciales, solicite asistencia a soporte técnico.

3. Seleccione la opción ``Reportes`` en el menú lateral. 

.. image:: /imgs/Reportes/Reportes1.png

Ver reporte
===========

Para examinar un reporte en detalle, siga los siguientes pasos:

1. Seleccione la opción ``Reportes`` en el menú lateral. 
2. Presione el icono de engrane, seguido de ``Ver reportes`` o elija el tercer icono.

.. image:: /imgs/Reportes/Reportes2.png

En términos generales, observe la siguiente imagen que describe los elementos básicos presentes en un reporte.

.. image:: /imgs/Reportes/Reportes3.png

Crear carpeta
=============

Crear una carpeta le permitirá almacenar uno o más reportes dentro de ella. Siga los pasos para crear una carpeta:

1. Diríjase y seleccione la opción ``Reportes``.
2. Haga clic en el icono sobre ``Carpeta`` ubicada en el menú superior derecho.

.. image:: /imgs/Reportes/Reportes6.png

3. Escriba el nombre de la ``Carpeta``.
4. Presione ``Crear``.

Compartir Carpeta/Reporte
=========================

Compartir una carpeta o un reporte es un proceso sencillo. Siga los pasos:

1. Diríjase y presione la opción ``Reportes`` en el menú lateral.
2. Identifique la carpeta o la forma de su interés.
3. Presione el icono de engrane, seguido de ``Compartir`` o haga clic en el segundo ícono de compartir.

.. image:: /imgs/Reportes/Reportes4.png

4. Escriba el nombre del usuario con el que desea compartir la carpeta o el reporte y presione ``Enter``. Observe que el nombre del usuario aparecerá en la parte inferior de la ventana.

.. image:: /imgs/Reportes/Reportes5.png

.. seealso:: 

    La diferencia en las opciones de permisos se debe a que el usuario Omar Vázquez es una conexión. Es decir, pertenece a otra cuenta principal diferente a la suya.

    En cambio, el usuario Erika pertenece a la misma cuenta padre.

5. Establezca al usuario el permiso que requiera. Tenga en cuenta las descripciones:

- **Lectura**: El usuario puede ver todos los reportes dentro de la carpeta. 
- **Compartir**: El usuario puede ver y compartir la carpeta con otros usuarios. 
- **Admin**: El usuario tiene los mismos privilegios que los perfiles anteriores y puede modificar y eliminar los reportes.
- **Borrar registros**: Al activar esta opción, el usuario puede eliminar los reportes. Si no se activa, el usuario no puede eliminar los reportes, incluso si tiene el perfil de ``Admin``.

.. caution:: Cuando se comparte una carpeta, los reportes que contiene heredan automáticamente los permisos. Sin embargo, compartir un reporte e intentar moverlo a una carpeta puede causar problemas.

.. tip:: 
    
    Si necesita mover un reporte a una carpeta, simplemente arrástrelo al lugar necesario. 
    
    Si necesita mover un reporte fuera de alguna carpeta, a la raíz, simplemente arrástrelo a la columna principal.

Si necesita editar el nombre de su carpeta siga los siguientes pasos:

.. grid:: 2
    :gutter: 0
    :padding: 0
    :margin: 0

    .. grid-item-card:: 
        :columns: 3
        :padding: 0
        :margin: 0

        .. image:: /imgs/Reportes/Reportes9.png
            :width: 400
            :height: 200

    .. grid-item-card:: 
        :columns: 9
        :padding: 0
        :margin: 0

        1. Presione el icono de engrane, seguido de ``Editar``.
        2. Renombre a la carpeta.
        3. Haga clic en ``Renombrar``.

.. _config-reporte:

Crear reporte
=============

Crear un reporte en Linkaform es un proceso sencillo. Siga el siguiente procedimiento teniendo en cuenta las notas y recomendaciones:

.. caution:: Tenga en cuenta que estos son los pasos que debe seguir para configurar el reporte (previamente preparado) en su cuenta de Linkaform; sin embargo, NO constituyen la totalidad del proceso.

1. Ingrese a la aplicación web oficial de Linkaform en |Producción| :octicon:`report;1em;sd-text-info` o en otro caso, en |Preproducción| :octicon:`report;1em;sd-text-info`.

.. important:: El proceso de configuración en producción y preproducción es idéntico. Sin embargo, se recomienda iniciar el proceso de creación de reportes en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

2. Seleccione la opción ``Reportes`` en el menú lateral. 
3. Presione el icono de archivo, ubicado en la parte superior.

.. image:: /imgs/Reportes/Reportes7.png

.. note:: Pase el cursor sobre las opciones para conocer las funcionalidades que ofrecen.

4. Configure el reporte teniendo en cuenta lo siguiente:

- **Nombre del Reporte**: Identificador del reporte, no necesariamente es el mismo que se visualiza en el nombre del reporte.
- **URL**: Dirección del reporte. 

.. note:: En la siguiente figura, observe que se está asignando la ``URL`` de servido, indicando que es un reporte de demostración. 

Consulte la sección :ref:`url-acceso` :octicon:`report;1em;sd-text-info`, específicamente :ref:`link-servido` :octicon:`report;1em;sd-text-info`.
 
- **Script**: Nombre del script previamente escrito en lenguaje Python. 

.. note:: Automáticamente e internamente, ya se sabe que el ``ID`` del ``script`` es el que debe enviarse como parámetro en la ``URL``. Por esta razón, el script no se coloca directamente en la ``URL``, ya que es dinámico.

.. image:: /imgs/Reportes/Reportes8.png

5. Presione el botón ``Cargar``.

Si necesita editar las configuraciones de su reporte, simplemente presione el icono de engranaje, seguido de ``Editar`` y modifique su reporte según las instrucciones anteriores.

.. image:: /imgs/Reportes/Reportes9.png

.. seealso:: Si desea crear su propio reporte personalizado, le sugerimos revisar las siguientes secciones de la documentación que explican cómo crear reportes. En caso contrario, le recomendamos contactar a soporte técnico para que el equipo de Linkaform pueda elaborar una propuesta a la medida.

.. LIGAS EXTERNAS

.. |Linkaform| raw:: html

   <a href="https://app.linkaform.com/" target="_blank">Linkaform</a>

.. |Producción| raw:: html

   <a href="https://app.linkaform.com/" target="_blank">Producción</a>

.. |Preproducción| raw:: html

   <a href="https://preprod.linkaform.com/" target="_blank">Preproducción</a>