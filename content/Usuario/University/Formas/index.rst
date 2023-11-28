=============
Módulo formas
=============

En este apartado, encontrará información importante sobre el módulo de formas. En Linkaform el módulo de formas sirve como repositorio central para los formularios creados o compartidos en la cuenta. Desde este módulo, se pueden realizar diversas acciones, tales como:

#. Crear y editar formas.
#. Responder formas para generar nuevos registros.
#. Compartir formas con otros usuarios.
#. Crear carpetas para organizar y almacenar formas.
#. Acceder directamente a los registros de la forma seleccionada.
#. Realizar búsquedas de formas dentro de la cuenta.

Para acceder al módulo de formas, ubique el segundo ícono en el menú vertical situado a la izquierda de su pantalla. Dentro de este menú, encontrará la opción ``Mis Formas``.

Crear forma
===========

Para crear una forma, identifique el ícono de ``Crear Forma`` ubicado en la parte superior derecha. Al posicionar el cursor sobre el ícono, la ayuda visual proporcionará información sobre su función. Al hacer clic en el ícono, Linkaform presentará una plantilla en blanco, a partir de la cual se inicia el proceso de creación de la forma.

.. image:: /imgs/Formas/Formas2.jpg

Nombre de forma
---------------

Si desea establecer o cambiar el nombre de la forma, haga clic en el título en la parte superior izquierda. En esta opción, Linkaform mostrará el ícono de un lápiz para edición, lo que le permitirá modificar el nombre de la forma según sea necesario.

.. image:: /imgs/Formas/Formas3.png

.. important:: Recuerde que después de realizar cualquier cambio en la forma, debe hacer clic en el botón ``Guardar`` para asegurar que las modificaciones se guarden correctamente. 

Nombre de Página en forma
-------------------------

Definir o cambiar el nombre de una página es sencillo. Seleccione la página a la que desea aplicar esta acción y verá el título actual en la parte superior. Para cambiarlo, haga clic en el ícono de edición, escriba el nuevo nombre y presione Enter.

.. image:: /imgs/Formas/Formas4.jpg

Características de campos
-------------------------

.. :octicon:`star-fill;1em;sd-text-warning` 

Las características que comparten la mayoría de los campos de Linkaform son las siguientes:

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :align: left

   * - Característica
     - Descripción
   * - ⭐ Favorito
     - Al activar esta opción, permite visualizar la información de este campo al realizar consultas en Registros completados desde la app o al consultar los registros desde la web en el módulo de registros.
   * - Ascendente/Descendente
     - Permite ordenar las respuestas incluidas en este campo en el orden elegido.
   * - Duplicar
     - Crea una copia exacta del campo.
   * - Config
     - Establece cantidades límites, orígenes de archivos permitidos, impresión de fechas y localizaciones.
   * - Requerido
     - Hace obligatoria la respuesta al campo al crear un registro.
   * - Default
     - Define una respuesta predeterminada en la forma, la cual se puede modificar al responder la forma.
   * - Enviar email
     - Al activar esta opción, se puede enviar una copia del registro que se está capturando al correo capturado en este campo.
   * - Opción abierta
     - Permite agregar una opción adicional en la respuesta cuando se definen respuestas únicas.
   * - Propiedades
     - En el campo de texto, sirve para habilitar la lectura de códigos de barras o QR. En campos numéricos, esta opción establece parámetros mínimos y máximos aceptados.
   * - Configuración de la notificación
     - Permite configurar el envío de un correo electrónico al seleccionar una de las opciones de respuesta disponibles.
   * - Configuración de la ponderación
     - Establece el puntaje deseado para las respuestas.
   * - Ayuda
     - Habilita una opción de texto adicional en el campo como referencia a la respuesta solicitada.

Campos
------

Al realizar un formulario, Linkaform proporciona campos básicos para personalizar sus formularios según sus necesidades. A continuación, se presentan los campos en la siguiente tabla:

Campo texto 
^^^^^^^^^^^

.. image:: /imgs/Formas/Formas6.jpg

**Campo de Texto Una Línea**

Están diseñados para capturar respuestas abiertas de hasta 500 caracteres. También es posible activar la lectura de códigos de barras y códigos QR en las propiedades de este campo.

**Campo de Texto Párrafo**

Permiten capturar respuestas abiertas de hasta 500 caracteres. A diferencia del campo de ``Una Línea``, en este campo es posible saltar de línea y copiar vínculos, respetando el enlace.

**Campo de Texto Secreto**

Se utiliza para capturar información sin que la respuesta sea visible durante la captura. La información capturada solo se revelará una vez que se haya enviado el registro.

**Campo de Texto Descripción**

Este campo se utiliza para incluir texto en la forma y que sirva como referencia al momento de capturar información. Puede contener recomendaciones o instrucciones a seguir. La información capturada en este campo será visible al responder, pero no estará presente en el PDF final.

**Campo texto Email**

En el campo Email, puede capturar direcciones de correo electrónico. 

.. note:: Cuando este campo se establece como requerido, Linkaform realiza una validación para asegurarse de que la dirección tenga la estructura correspondiente a un correo electrónico. Sin embargo, Linkaform no verifica la existencia real del correo electrónico.

Además, puede activar la opción ``Enviar Email`` y Linkaform enviará una copia del registro capturado al correo que se capture en el mismo.

Al activar la opción ``Enviar email``, en las opciones a la derecha de su pantalla, se habilitará la función ``Configuración de Email``. A continuación, se detallan las configuraciones requeridas:

.. tab-set::

    .. tab-item:: De

        En esta opción, se configura el remitente. Haga clic en el campo, Linkaform presenta opciones para seleccionar y configurar el remitente deseado para el envío.

        .. image:: /imgs/Formas/Formas7.png

        .. important:: Todos los correos generados llegan de la dirección de correo que se elija en esta configuración.

    .. tab-item:: Para

        Esta opción permite configurar al destinatario y realizar las siguientes acciones:

        - Enviar una copia al correo cada vez que se edite el registro.

        - Activar el envío del PDF.

        .. caution:: Si esta opción no se activa, el correo se enviará sin incluir el PDF.

        - Adjuntar el logo de la compañía.

        - Adjuntar los documentos que pueda contener este registro en el envío del correo.
        
        - Seleccionar el formato de plantilla deseado para este registro (en el caso de que la forma tenga más de un formato de PDF diseñado).

        .. image:: /imgs/Formas/Formas7.1.png

    .. tab-item:: Asunto

        En este campo, se define el asunto que mostrará el correo. En la parte inferior, Linkaform permite utilizar metadatos o los campos de la forma para personalizar el asunto. Simplemente seleccione el campo deseado y haga clic en ``Agregar``. Al hacerlo, aparecerá un código correspondiente al campo seleccionado.

        .. image:: /imgs/Formas/Formas7.2.png

    .. tab-item:: Cuerpo

        De manera similar al caso anterior en el asunto, simplemente seleccione el campo deseado y haga clic en ``Agregar``. Al hacerlo, aparecerá un código correspondiente al campo seleccionado.
        
        .. image:: /imgs/Formas/Formas7.3.png

    .. tab-item:: Vista previa

        Aquí se revisa la configuración final, muestra un previo de lo que se seleccionó.

        .. image:: /imgs/Formas/Formas7.4.png

Al estar seguro de sus cambios seleccione de clic en ``Guardar``.