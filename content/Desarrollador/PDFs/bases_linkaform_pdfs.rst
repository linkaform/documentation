.. _bases-linkaform-pdfs:

==================
Bases de Linkaform
==================

Los PDF son una funcionalidad que Linkaform ofrece al momento de consultar y descargar uno o varios registros de una forma específica. Esta función le permite visualizar el registro con un diseño legible, estéticamente atractivo y simple en un reporte en PDF.

A lo largo de la documentación, podrá encontrar orientación sobre los aspectos necesarios para la creación de sus propios PDFs personalizados.

.. important:: Tenga en cuenta que el desarrollo de PDFs se basa en la información recopilada de las formas (formularios digitales), por lo que es importante que comprenda su funcionamiento. Consulte el siguiente enlace para revisar la documentación oficial de las :ref:`section-forms` :octicon:`report;1em;sd-text-info`.

Subdominios
===========

Linkaform cuenta con una serie de subdominios que serán útiles al momento de desarrollar reportes en formato PDF.

**Producción** 

Es la plataforma de Linkaform utilizada actualmente por los usuarios finales. Puede acceder a ella a través del siguiente enlace |prod| :octicon:`report;1em;sd-text-info`, utilice sus credenciales habituales.

**Preproducción**

Es una copia de producción. Es util para realizar pruebas sin riesgos en caso de cometer errores. Para acceder a |preprod| :octicon:`report;1em;sd-text-info`, inicie sesión con su correo habitual, pero solicite al soporte técnico la contraseña necesaria para acceder.

.. warning:: Tenga en cuenta que todo lo que se haga en preproducción será reemplazado por los datos de producción en cargas que se realizan cada semana.

**FAQ**

Es la página donde podrá encontrar preguntas frecuentes sobre el uso de LinkaForm. Aquí podrá realizar sus preguntas a través de publicaciones o consultas con otros usuarios relacionados. Para acceder ingrese al siguiente enlace |faq| :octicon:`report;1em;sd-text-info`.

Accesos
=======

Para el desarrollo de PDFs en Linkaform, necesitará acceso a cuentas y formas específicas. A continuación, se detallan los accesos necesarios:

**Cuenta del cliente**


Debe contar con acceso y autorización a la cuenta del cliente para el cual desea crear el PDF. Esto le permitirá configurar, visualizar y generar PDFs de las formas y registros asociados a dicho cliente.

En producción, puede acceder mediante el bypass-login. Para obtener autorización, acceso y detalles sobre el funcionamiento del bypass, comuníquese con el soporte técnico.

.. attention:: Si tiene acceso a cuentas de terceros, es importante que la información tratada sea confidencial y en ningún caso debe divulgarse.

**Forma de logotipos**

En su cuenta personal, necesitará acceso a la forma llamada ``Logotipo de Clients``. Solicite al soporte técnico que comparta esta forma con su cuenta. 

Esta forma le permitirá obtener la URL del logotipo de los clientes de Linkaform para utilizarla en los PDF.

.. image:: /imgs/PDF/pdf1.png

.. _vincular:

Configuración del pdf
=====================

La configuración implica la vinculación del pdf con la forma. Al enlazar un pdf, se especifica que es exclusivo para las necesidades del formulario. La vinculación difiere según el tipo de descarga, ya sea que necesite un solo registro o múltiples registros.

Aunque el proceso de configuración en |prod| :octicon:`report;1em;sd-text-info` y |preprod| :octicon:`report;1em;sd-text-info` es idéntico,se recomienda preparar y probar el documento en preprod. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.
 
Single record
-------------

Un pdf single record está preparado unicamente para extraer y presentar un solo registro. Para configurar el pdf en la forma siga los siguientes pasos:

1. Verifique que la plantilla esté configurada para funcionar como un registro único. Para hacerlo, ajuste el atributo **type** en la :ref:`conf-django` :octicon:`report;1em;sd-text-info`.
2. Inicie sesión en |prod| :octicon:`report;1em;sd-text-info` o |preprod| :octicon:`report;1em;sd-text-info` utilizando sus credenciales.
3. Seleccione y edite la forma a la que desea vincular el pdf. 
4. Seleccione ``opciones > opciones generales > Plantillas de PDF``. 
5. Seleccione el nombre que haya asignado a la plantilla previamente definida en la :ref:`conf-django` :octicon:`report;1em;sd-text-info`.
6. Presione ``Agregar``. Automáticamente se incluirá la ``Descripción`` definida previamente en el atributo **Description** en la :ref:`conf-django` :octicon:`report;1em;sd-text-info`, seguido del **nombre de la plantilla**, junto con dos alternativas: un ``botón azul`` y la opción de ``eliminar (x)`` en el recuadro medio.
7. Haga clic en ``OK`` y guarde la forma en su totalidad.

.. image:: /imgs/PDF/pdf2.png

8. Regrese a la configuración y seleccione la fila, el ``Nombre de la plantilla`` o el ``botón azul`` en el recuadro medio. Se habilitará la escritura del campo ``Nombre de PDF`` y otros campos posteriores.
9. Ingrese el nombre que desee al momento de descargar el pdf. Regularmente, se utiliza el nombre de la plantilla, pero **no** se incluye el nombre del cliente, seguido de un guion medio.
10. En la opción ``Campo``, seleccione un metadato o campo.

.. note:: Regularmente, al seleccionar la opción de campo, se elige el metadato o campo que formará parte del nombre de la descarga. Usualmente, se selecciona el metadato de ``Folio del registro``.

11. Presione ``Agregar``; automáticamente el campo o metadato seleccionado pasará a ser complemento del ``Nombre de PDF``.

.. image:: /imgs/PDF/pdf2.1.png

12. Presione ``Guardar``; la actualización se verá reflejada en el recuadro medio.
13. Finalmente, presione ``OK`` y guarde la forma en su totalidad. 

.. image:: /imgs/PDF/pdf3.2.png

.. _multiple:

Multiple record
---------------

Un PDF de múltiples registros está diseñado para extraer y presentar datos de varios registros, todos ellos **dependientes de una misma forma**.

El proceso de vinculación de un ``multiple record`` es más sencillo. Siga los siguientes pasos para su configuración:

1. Verifique que la configuración del **type** en la :ref:`conf-django` :octicon:`report;1em;sd-text-info` esté establecida en **multiple records**.
2. Inicie sesión en |prod| :octicon:`report;1em;sd-text-info` o |preprod| :octicon:`report;1em;sd-text-info` utilizando sus credenciales.
3. Elija y edite la forma a la que desea vincular el pdf. 
4. Seleccione ``opciones > opciones generales > Plantillas de PDF``. 
5. Seleccione el nombre que haya asignado a la plantilla previamente definida en la :ref:`conf-django` :octicon:`report;1em;sd-text-info`. Notará que se resalta una etiqueta verde con el texto ``Multiple``, indicando que está preparado para mostrar múltiples registros.
6. Presione ``Agregar``. El **nombre de la plantilla** pasara al recuadro medio, dónde encontrara dos opciones: un ``botón azul`` y la opción de ``eliminar (x)``.
7. Finalmente haga clic en ``OK`` y guarde la forma en su totalidad.

.. image:: /imgs/PDF/pdf9.png
  :align: center

Descargar PDF
=============

El proceso para descargar documentos pdf varía según el tipo de descarga. A continuación, revise las siguientes secciones según lo requiera.

.. note:: Asegúrese de que la configuración al `vincular la forma y el pdf <#vincular>`_ :octicon:`report;1em;sd-text-info` esté correctamente establecida. 

Single record
-------------

Para descargar el PDF de un registro único, siga los siguientes pasos:

1. Diríjase a ``Registros`` en el menú lateral.
2. Ingrese el nombre de la forma a la cual desea ver sus registros.
3. Filtre los registros según lo requiera.
4. Busque y seleccione el registro de su interés presionando el icono para visualizar al instante o en una nueva ventana.

.. seealso:: Si tiene dudas sobre cómo acceder y filtrar registros, consulte :ref:`registros-formas` :octicon:`report;1em;sd-text-info` para obtener más información.

.. image:: /imgs/PDF/pdf10.png

5. Haga clic en el ícono de documento en la esquina superior derecha.
6. En la sección de descargas de su navegador, podrá observar su documento PDF.

.. image:: /imgs/PDF/pdf10.1.png

Multiple record
---------------

En el caso de múltiples registros, el proceso varía ligeramente. Siga los siguientes pasos:

1. Diríjase a ``Registros``. 
2. Ingrese el nombre de la forma a la cual desea ver sus registros.
3. Filtre los registros según lo requiera.

.. attention:: Asegúrese de que los registros que necesita descargar pertenezcan a la misma forma. De lo contrario, seleccionar registros provenientes de diferentes formas podría resultar en acciones inesperadas.

4. Seleccione **los registros** de su interés marcando las casillas de selección junto a los registros.
5. Presione la opción con el icono de documento en la esquina superior derecha. 

.. image:: /imgs/PDF/pdf11.png
  :align: center

Una vez seleccionada la opción, se desplegará un modal para configurar la descarga. Siga el siguiente procedimiento:

1. Si no ha aplicado ningún filtro, seleccione la opción ``Registros seleccionados``.

.. attention:: La opción de ``Registros filtrados`` es útil para presentar información como el propietario de la forma, el usuario que creó el registro, el nombre de la forma, las fechas de captura, etc. Representar esta información solo es posible si el código del pdf está preparado para recibir y procesar los filtros.

2. Proporcione un nombre descriptivo para identificar la descarga de sus registros.
3. Seleccione el nombre de la plantilla.

.. important:: La plantilla debe estar preparada y configurada para recibir multiples registros. Revise la `configuración <#multiple>`_ :octicon:`report;1em;sd-text-info` del pdf para más detalle.

4. Haga clic en la opción ``Descargar``.

.. image:: /imgs/PDF/pdf12.png

5. Diríjase a la opción ``Registros > Descargas`` ubicada en el menú lateral.

.. image:: /imgs/PDF/pdf13.png

6. Identifique el nombre de su descarga y presione ``Descargar``. El navegador abrirá una nueva pestaña con el pdf de múltiples registros.

.. image:: /imgs/PDF/pdf14.png
  :align: center

.. LIGAS DE INTERÉS

.. |prod| raw:: html

   <a href="https://app.linkaform.com/" target="_blank">producción</a>

.. |preprod| raw:: html

   <a href="https://preprod.linkaform.com/" target="_blank">preproducción</a>

.. |faq| raw:: html

   <a href="https://faq.linkaform.com/" target="_blank">FAQs de Linkaform</a>
   