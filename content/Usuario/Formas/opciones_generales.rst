.. _menu-opciones-generales:

==================
Opciones Generales
==================

Las opciones son configuraciones que se pueden aplicar a la forma. Puede encontrar opciones generales, configuraciones sobre flujos, reglas para aplicar a la forma, embeber la forma, imprimir la forma en formato PDF y utilizar botones.

1. Diríjase a ``Opciones > Opciones generales``.

.. image:: /imgs/Formas/Formas20.jpg

En los siguientes apartados podrá encontrar información más detallada acerca de cada funcionalidad.

.. _geolozalizacion:

Opciones generales
^^^^^^^^^^^^^^^^^^

Las opciones generales permiten definir configuraciones aplicables principalmente al responder la forma.

.. image:: /imgs/Formas/Formas21.jpg

Podrá encontrar las siguientes configuraciones:

- **Registros Editables**: Permite que las respuestas puedan ser editadas, ya sea por usuarios o por administradores.

.. important:: Solo son editables los registros que son creados mientras esta opción está activa.

- **Geolocalización**: Al activar esta opción, Linkaform almacenará la ubicación desde donde se contestó el formulario y lo mostrará en los metadatos.

- **Notificaciones**: Si está activa, permite configurar el envío de correos electrónicos para el envío de notificaciones. 

.. important:: Esta opción, solo esta disponible para campos de opción múltiple y número. 

- **Logo de usuario en PDF de registro**: Si se tiene un logotipo definido, esta opción reflejará el logotipo en el PDF del registro.

- **Pública**: Con la activación de esta función, permite que el formulario pueda ser pública para que sea contestado libremente por cualquier persona que no tenga una cuenta en Linkaform. Simplemente copie el enlace que aparecerá a la derecha y compártala, esto permitirá que personas que no utilicen Linkaform puedan generar información.

.. important:: Responder un formulario de este tipo solo podrá hacerse a través de la aplicación web.

- **Editar registros públicos**: Cuando se tiene una forma pública, debe considerar activar esta opción si desea modificar los registros.

Plantillas de PDF
^^^^^^^^^^^^^^^^^

Esta opción permite configuraciones y establecer un vínculo entre el PDF y la forma.

.. image:: /imgs/Formas/Formas22.jpg

A continuación, se explicarán de manera general los pasos y campos que la componen. Sin embargo, puede revisar el siguiente enlace (:ref:`vincular` :octicon:`report;1em;sd-text-info`) que corresponde a PDFs y su principal diferencia entre las configuraciones de una plantilla de un solo registro y de múltiples registros.

1. Seleccione el nombre de la plantilla que desea establecer en la forma. En este campo se muestran las plantillas disponibles para la forma.
2. Haga clic en el botón ``Agregar``.
3. Revise y observe que en el campo descripción encontrará información de la plantilla seleccionada.
4. Pulse ``OK``.
5. Guarde el formulario en su totalidad.
6. Seleccione el botón azul que aparece en el recuadro del medio.
7. En el nombre del PDF, defina la nomenclatura que tendrá el PDF al momento de descargar el archivo. Regularmente es el nombre de la plantilla seguido de un guion ``-``.
8. Seleccione el campo que, regularmente, es el metadato ``folio del registro``.

.. note:: Si es necesario, puede agregar campos de la forma, pero debe asegurarse de marcarlos como requeridos. 

9. Presione en ``Agregar`` y verá reflejado el nombre del metadato o campo entre llaves dobles ``{{}}``.
10. Al finalizar su configuración, haga clic en el primer botón ``Guardar``.
11. Nuevamente, guarde el formulario en su totalidad.

.. image:: /imgs/Formas/Formas23.png

Confirmación 
^^^^^^^^^^^^

Esta configuración permite personalizar los mensajes al momento de capturar un registro de la forma por la aplicación web. A continuación, se detallan los campos relevantes:

- **Mensaje final**: Lo que se establezca en este campo se mostrará después de enviar el registro.

- **Texto en botón final**: Por defecto, está configurado como ``Mandar respuesta``, pero puede personalizar el texto.

- **URL destino**: Configure para que, después del envío del registro, Linkaform redireccione al usuario a un sitio web específico.

.. image:: /imgs/Formas/Formas23.1.png

.. _ponderacion-conf:

Ponderación 
^^^^^^^^^^^

Esta configuración le permitirá especificar si desea utilizar alguna puntuación de los campos de la forma. Para acceder a la ponderación, ubíquese en la ``forma de su interés > Opciones > Opciones generales > Ponderación``.

.. attention:: Esta configuración es exclusiva para las opciones de un campo de respuesta múltiple. 

Para definir el tipo de valor, siga los pasos:

1. Active el bullet ``Ponderación`` para habilitar la configuración.
2. Defina si calificará por puntos o porcentaje. Tenga en cuenta que solo puede elegir una opción.

.. note:: Si elige calificar por puntos, los puntos deben ser especificados individualmente en el campo de opción múltiple. Si elige calificar por porcentaje, debe establecer la puntuación máxima.

.. image:: /imgs/Formas/Formas23.2.png

Temporizador 
^^^^^^^^^^^^

La funcionalidad del temporizador es utilizada para definir parámetros de tiempo relacionados con la captura de información en la forma. La configuración es la siguiente:

- **Minutos para contestar**: Define los minutos que tiene permitido el usuario para enviar la información.
- **Cantidad de clics permitidos a la URL**: Establece la cantidad de veces que el usuario puede hacer clic al momento de responder la forma.
- **Expira en**: Define el tiempo en horas y minutos en el que expira el registro. 

.. admonition:: Ejemplo
  :class: pied-piper

  Si la persona A crea un registro, la persona B deberá completar la captura dentro del tiempo establecido en este campo.

- **Mensaje al contestar**: Muestra al usuario un mensaje al momento de responder la forma.
- **Mensaje al terminar el tiempo**: Mensaje que se mostrará al estar cerca de finalizar el tiempo para responder.

.. image:: /imgs/Formas/Formas24.jpg

.. _opciones-avanzadas:

Opciones avanzadas
^^^^^^^^^^^^^^^^^^

En las opciones avanzadas, se establecen los valores para el folio, los versionamientos de los registros de la forma, y la posibilidad de visualizar los ID de los campos. A continuación, se detallan los campos relevantes:

- **Opciones avanzadas**: Activar esta opción permite visualizar los ``ID`` únicos de cada campo en esta forma.
- **Habilitar versionamientos**: Si activa esta opción, Linkaform guardará la información capturada en cada registro cuando se edite y la mostrará. De lo contrario, solo se verá la información de la edición más reciente.

Dentro de **Folio** podrá personalizar ajustando las siguientes opciones:

- **Folio automático**: Linkaform asignará automáticamente el folio al registro.
- **Folio manual**: Permite que el usuario capture el folio. 

.. important:: Si el usuario no proporciona un folio, Linkaform le asignará uno.

- **Folio manual requerido**: Linkaform permitirá que el usuario capture el folio, pero no permitirá el envío hasta que sea definido por el usuario.

Dentro de **Folio Configurable**, podrá establecer la nomenclatura para los registros de la forma, configurando las siguientes opciones:

- **Prefijo**: Define los valores de inicio del folio.
- **Sufijo:** Complemento al folio.
- **Comenzar en:** Establece el primer folio.
- **Incrementar por:** Permite configurar el consecutivo de los folios.
- **Longitud de Folio:** Limita los caracteres permitidos en la definición del folio.

.. image:: /imgs/Formas/Formas25.jpg

.. important:: Recuerde que después de realizar cada configuración, presione ``OK`` y guarde la forma en su totalidad.


Embeber forma
-------------

La funcionalidad de embeber una forma implica exportar código HTML de la forma para integrar el formulario directamente en una página web o aplicación.

Embeber una forma es sencillo, simplemente siga estos pasos:

1. Ingrese a la forma de la que desea obtener el código.
2. Configure su forma como pública. Diríjase a ``Opciones > Opciones Generales`` y habilite la opción ``Pública``.
3. Guarde la forma en su totalidad.
4. Seleccione ``Opciones > Embeber Forma``.
5. Ingrese la ``URL de destino`` (el sitio web donde desea embeber la forma) o puede dejarla en el valor predeterminado.

.. image:: /imgs/Formas/Formas90.jpg

6. Haga clic en el botón ``Siguiente``.
7. Copie y pegue el código HTML que Linkaform le proporciona.

.. image:: /imgs/Formas/Formas91.jpg

Consulte el siguiente video para ver un ejemplo:

.. youtube:: 3P-9icCr3vY
  :aspect: 16:9
  :width: 100%
  :height: 480
  :align: center
  :privacy_mode: enable_privacy_mode
  :url_parameters: ?start=65

Imprimir PDF
------------

Esta funcionalidad permite generar una plantilla únicamente con los campos que conforman la forma, sin necesidad de crear un registro.

Para generar un documento PDF, siga estos sencillos pasos:

1. Ubíquese en la forma de la cual desea obtener el PDF.
2. Vaya a ``Opciones > Imprimir PDF``.
3. En el historial de descargas de su navegador, encontrará el archivo PDF con la estructura de su forma.

Botones
-------

Los botones tienen la función de ejecutar una acción que afecte a un campo. La configuración es la siguiente:

1. Ingrese a la forma en la que desea agregar el botón.
2. Diríjase a ``Opciones > Botones``.
3. Haga clic en el botón verde para ``Agregar botón``.
4. Asigne un nombre descriptivo al botón haciendo doble clic sobre el campo ``Título de la pregunta``.

.. image:: /imgs/Formas/Formas94.jpg

Las características de los botones son las siguientes:

+------------------------+----------------------------------------------------------------------------------+
| Función                | Descripción                                                                      |
+========================+==================================================================================+
| **Ícono**              | Seleccione la figura que se mostrará como botón en la forma. Para ello, haga     |
|                        | doble clic en el icono de nave.                                                  |
+------------------------+----------------------------------------------------------------------------------+
| **Color**              | Establezca el color del botón elegido. Puede utilizar un número hexadecimal o    |
|                        | incluso usar la barra de colores.                                                |
+------------------------+----------------------------------------------------------------------------------+
| **Visible en**         | Determine el momento en que se visualizará el botón.                             |
+------------------------+----------------------------------------------------------------------------------+
| **Esperar respuesta**  | Habilite si está relacionado con un proceso y debe esperar confirmación (por     |
|                        | ejemplo, en el caso de afectación por Script).                                   |
+------------------------+----------------------------------------------------------------------------------+
| **Script**             | Habilite para configurarlo con la ejecución de un Script.                        |
+------------------------+----------------------------------------------------------------------------------+
| **Ayuda**              | Habilite la opción si requiere que brinde ayuda e introduzca el texto de ayuda.  |
+------------------------+----------------------------------------------------------------------------------+
| **Actualizar valores** | Escriba el nombre del campo que será afectado por el botón cuando se haga clic   |
|                        | en él. Por ejemplo, al hacer clic en el botón, puede cambiar la respuesta del    |
|                        | campo ``Estatus`` al valor ``Resuelto``.                                         |
+------------------------+----------------------------------------------------------------------------------+
|                                                                                                           |
+------------------------+----------------------------------------------------------------------------------+  
| .. image:: /imgs/Formas/Formas95.jpg                                                                      |
+------------------------+----------------------------------------------------------------------------------+  
| **Web services**       | Ingrese los parámetros correspondientes a la interacción con un servicio web     |
|                        | cuando se hace clic en el botón. Esto podría incluir datos que se envían al      |
|                        | servicio web para realizar alguna acción o solicitar información específica.     |
+------------------------+----------------------------------------------------------------------------------+
|                                                                                                           |
+------------------------+----------------------------------------------------------------------------------+  
| .. image:: /imgs/Formas/Formas96.jpg                                                                      |
+------------------------+----------------------------------------------------------------------------------+
