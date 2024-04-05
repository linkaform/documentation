.. _bases-linkaform-pdfs:

==================
Bases de Linkaform
==================

Los pdf son una funcionalidad que Linkaform ofrece al momento de consultar y descargar uno o varios registros de una forma específica. Esta función le permite visualizar el registro con un diseño legible, estéticamente atractivo y simple.

.. _vincular:

Configuración del pdf
=====================

La configuración implica la vinculación del pdf con la forma. Al enlazar un pdf, se especifica que es exclusivo para las necesidades del formulario. La vinculación difiere según el tipo de descarga, ya sea que necesite un solo registro o múltiples registros.

Al crear un pdf, se recomienda preparar y probar el documento en |preprod| :octicon:`report;1em;sd-text-info`. Para acceder a |preprod| :octicon:`report;1em;sd-text-info`, inicie sesión con su correo habitual, pero solicite al soporte técnico la contraseña necesaria para acceder.

.. note:: Preproducción es una copia del entorno de producción, pero es un espacio seguro para evitar interferir con las operaciones reales y causar molestias o errores para el cliente al intentar descargar el documento. El proceso de configuración en producción y |preprod| :octicon:`report;1em;sd-text-info` es idéntico. Una vez finalizado y seguro de sus cambios, puede transferirlo a |prod| :octicon:`report;1em;sd-text-info`.

Single record
-------------

Un pdf single record está preparado unicamente para extraer y presentar un solo registro. Para configurar el pdf en la forma siga los siguientes pasos:

1. Verifique que la plantilla esté configurada para funcionar como un registro único. Para hacerlo, ajuste el atributo **type** en la :ref:`conf-django` :octicon:`report;1em;sd-text-info`.
2. Inicie sesión en |prod| :octicon:`report;1em;sd-text-info` o |preprod| :octicon:`report;1em;sd-text-info` utilizando sus credenciales.
3. Seleccione y edite la forma a la que desea vincular el pdf. 
4. Seleccione ``opciones > opciones generales > Plantillas de PDF``. 
5. Seleccione el nombre que haya asignado a la plantilla previamente definida en la :ref:`conf-django` :octicon:`report;1em;sd-text-info`.
6. Presione ``Agregar``. Automáticamente se incluirá la plantilla y se rellenará el campo ``Descripción``, seguido del **nombre de la plantilla**, junto con dos alternativas: un ``botón azul`` y la opción de ``eliminar (x)``.
7. Haga clic en ``OK`` y guarde la forma en su totalidad.
8. Regrese a la configuración y seleccione el ``Nombre de la plantilla`` o el ``botón azul``. Se habilitará la escritura del campo ``Nombre de PDF``.

.. image:: /imgs/PDF/2.png
  :align: center

9. Ingrese el nombre que desee al momento de descargar el pdf. Regularmente, se utiliza el nombre de la plantilla, pero **no** se incluye el nombre del cliente, seguido de un guion medio.
10. En la opción ``Campo``, seleccione el metadato o campo de su preferencia. 

.. note:: Regularmente, al seleccionar la opción de campo, se elige el metadato o campo que se necesita al momento de descargar el PDF. Usualmente se selecciona el metadato de ``Folio del registro``.
  
11. Presione ``Agregar``; automáticamente llenará el ``Nombre de PDF`` con doble corchete ``{{}}``. 
12. Presione ``Guardar`` seguido de ``OK`` y guarde la forma en su totalidad. 

.. image:: /imgs/PDF/3.1.png


Multiple record
---------------

El proceso de vinculación de un ``multiple record`` es más sencillo. Siga los siguientes pasos para su configuración:

1. Verifique que la configuración del `type de su plantilla <#type>`_ :octicon:`report;1em;sd-text-info` esté establecida en multiple records.

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

El proceso de descarga de documentos PDF difiere según el tipo de descarga. A continuación, revise las siguientes secciones según la descarga que necesite.

.. important:: El proceso de descarga depende de la configuración que realiza al `vincular la forma y el PDF <#vincular>`_ :octicon:`report;1em;sd-text-info`.
    
Registro único
--------------

Para descargar documentos con registros únicos, siga los siguientes pasos:

1. Diríjase a ``Registros``, filtre según sus necesidades y seleccione **el registro** de su interés.

.. seealso:: Si tiene dudas sobre cómo acceder al registro, consulte :ref: `registros-formas` para obtener más información.

2. Haga clic en la opción con el ícono de documento en la esquina superior derecha.
3. En la sección de descargas de su navegador, podrá observar su documento PDF.

.. image:: /imgs/PDF/10.png
  :align: center

Multiple record
---------------

En el caso de múltiples registros, el proceso varía ligeramente. Siga los siguientes pasos:

1. Diríjase a ``Registros``. 
2. En el campo ``Nombre de la forma``, escriba el nombre de la forma de la cual desea descargar los registros y filtre los registros según sus necesidades.

.. attention:: Asegúrese de que los registros que necesita descargar pertenezcan a la misma forma. De lo contrario, seleccionar registros provenientes de diferentes formas podría resultar en errores.

3. Seleccione **los registros** de su interés marcando las casillas de selección junto a los registros.
4. Presione la opción con el icono de documento en la esquina superior derecha. 

.. image:: /imgs/PDF/11.png
  :align: center

Una vez seleccionada la opción, se desplegará un modal para configurar la descarga. Siga el siguiente procedimiento:

1. Si no ha aplicado ningún filtro, seleccione la opción ``Registros seleccionados``.

.. important:: La opción de ``Registros filtrados`` solo es posible si el código del documento está preparado para recibir y tratar el filtro.

2. Seleccione el nombre de la plantilla.

.. important:: La plantilla debe estar preparada y configurada para recibir multiples registros. `vincular la forma y el PDF <#vincular>`_ :octicon:`report;1em;sd-text-info`.
    
3. Proporcione un nombre descriptivo para identificar la descarga de sus registros.
4. Haga clic en la opción ``Descargar``.

.. image:: /imgs/PDF/12.png

5. Vaya a la opción ``Registros > Descargas`` ubicada en el menú lateral.

.. image:: /imgs/PDF/13.png

6. Identifique el nombre de su descarga y presione ``Descargar``. El navegador abrirá una nueva pestaña con el documento PDF de múltiples registros.

.. image:: /imgs/PDF/14.png
  :align: center

.. |prod| raw:: html

   <a href="https://app.linkaform.com/" target="_blank">Producción</a>

.. |preprod| raw:: html

   <a href="https://preprod.linkaform.com/" target="_blank">preproducción</a>