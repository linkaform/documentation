.. _flujos:

=======================
Configuración de flujos
=======================

La configuración de flujos se utiliza para automatizar procesos en las formas.

Si desea configurar un flujo para una acción específica, siga estos pasos:

1. Edite la forma a la que desea aplicar una configuración de flujo.
2. Seleccione ``Opciones > Configuración de Flujos``. Será redirigido a otra página.
3. Haga clic en el botón verde para ``Agregar Regla``.

.. image:: /imgs/Formas/Formas26.png

4. Asigne un nombre al flujo. Para hacerlo, simplemente haga clic en ``Nombre de regla`` y establezca el nombre.

.. important:: Es importante establecer un nombre para el flujo, ya que facilita la identificación y modificación rápida cuando sea necesario editar este flujo, especialmente si hay muchos flujos configurados.

A partir de aquí, tenga en cuenta que la configuración del flujo se divide en dos partes importantes: Triggers y Acciones.

.. _triggers:

Triggers
^^^^^^^^

En ``Triggers`` se configuran las validaciones que debe cumplir el registro para que se puedan ejecutar las acciones.

.. image:: /imgs/Formas/Formas27.jpg

1. Elija cuándo se ejecutará el flujo. Puede seleccionar que el flujo se ejecute ``Antes`` o ``Después`` de recibir el registro.
2. En los campos de tipo checkbox, seleccione los eventos que necesita para la validación, pueden ser:

- Creación de registro.
- Edición de registro.
- Borrado de registro.
- Correr múltiples veces se refiere a ejecutar siempre que edite n veces el registro.

3. En la sección sobre ``Triggers de campos`` elija una opción, ``Todos`` o ``Cualquiera``

- **Todos**: Si selecciona ``Todos``, está especificando que todas las condiciones de los campos seleccionados deben cumplirse para que se active el flujo.
- **Cualquiera**: Si selecciona ``Cualquiera``, está diciendo que cualquiera de las condiciones de los campos seleccionados puede cumplirse para activar el flujo. En este caso, se activará el flujo si al menos una de las condiciones establecidas en los campos seleccionados se cumple.

.. important:: Elegir entre ``Todos`` y ``Cualquiera`` depende de la lógica que desee aplicar a sus flujos.

4. Haga clic en ``Selecciona un campo``. Esto abrirá una lista desplegable que contiene todos los campos disponibles en su formulario.
5. Seleccione el campo que desea para la validación. Al hacer clic en el campo, se agregará a la configuración del flujo.
6. Elija ``contiene opción`` y seleccione una condición para ese campo. Dependiendo de sus necesidades, elija la condición que debe cumplir ese campo. 
7. Seleccione el icono verde con el símbolo más y continúe a partir del paso 4 si necesita agregar más campos a la validación. Puede agregar múltiples campos con diferentes condiciones según sus requisitos.

.. dropdown:: Ejemplo

  Este es un ejemplo básico sobre como configurar ``triggers``. 

  Considere un ``trigger`` ejecutándose ``Después`` de la ``Creación del registro``

  .. image:: /imgs/Formas/Formas28.jpg

  En ``Selecciona un campo``, seleccionamos el campo ``Cliente``.

  .. image:: /imgs/Formas/Formas29.jpg

  Seleccionamos una condición, seguido de una opción, en este caso ``Cliente Contiene opción Infosync``

  .. image:: /imgs/Formas/Formas30.jpg

  .. important:: En la sección de ``Triggers de campos``, puede agregar más campos que, en conjunto, realicen una validación específica. Solo es necesario revisar cuidadosamente para evitar seleccionar opciones que se contradigan entre sí. Considere el siguiente caso:

    .. image:: /imgs/Formas/Formas31.jpg

    Aquí se añadió el campo ``Cliente`` dos veces. Este flujo nunca se ejecutaría. Porque en la parte superior se seleccionó la opción ``Todos``, es decir, que el flujo se ejecuta si y solo si cumple con todas las validaciones de los campos. Dado que hay solo un campo ``Cliente``, nunca cumpliría con la opción ``Cliente Infosync`` y ``Cliente Linkaform`` al mismo tiempo en el mismo registro. En este caso, se debe elegir ``Cualquiera`` para que el flujo se ejecute al cumplirse una de esas dos condiciones.

8. En ``Triggers de metadatos``, seleccione a un usuario.

.. important:: Aquí se ingresa el nombre del usuario que, en conjunto con las otras opciones de Triggers, puede activar la ejecución del flujo de manera más específica. Para esta opción, es necesario haber compartido la forma con el usuario seleccionado; de lo contrario, no se podrá configurar esta parte.

9. Seleccione una conexión.
10. Seleccione una calificación.

.. important:: Solo se utiliza si la forma tiene ponderación. En este caso, puede elegir una calificación para que, al cumplirse, se ejecute la acción.

.. image:: /imgs/Formas/Formas32.jpg

Si después de revisar la información tiene dudas sobre la configuración de ``triggers``, puede consultar el siguiente vídeo para obtener una guía visual y más detallada.

.. youtube:: o15HvwiHVR8
  :aspect: 16:9
  :width: 100%
  :height: 480
  :align: center
  :privacy_mode: enable_privacy_mode
  :url_parameters: ?start=109

De esta manera se realiza la configuración de la sección Triggers. Ahora continúe con la configuración de las acciones.

.. _acciones:

Acciones
^^^^^^^^

En ``Acciones``, se especifica lo que se desea que se realice. Aquí puede encontrar varias opciones, como asignar a un usuario, a una conexión, ejecutar un script, enviar un correo, entre otras. Siga los primeros pasos que son necesarios para todas las acciones.

1. Inicie con la `configuración del flujo <#flujos>`_ :octicon:`report;1em;sd-text-info`.
2. Realice la `configuración del trigger <#triggers>`_ :octicon:`report;1em;sd-text-info`.
3. Haga clic en el botón verde con el símbolo más para ``Agregar acción``. Al hacer esto se agrega una barra verde con el titulo ``Acción vacía``. Haga clic sobre ella.
4. Presione en el selector de ``Acción`` y elija una opción según su necesidad.

.. image:: /imgs/Formas/Formas33.png

.. important:: En base a un ``Trigger``, que establece las condiciones para que se dispare un flujo de trabajo, se pueden configurar varias acciones. Estas acciones se ejecutarán automáticamente cuando se cumplan las condiciones especificadas en el Trigger. 

En el selector de ``Acción``, contemple las siguientes pestañas que contiene las opciones e información más detallada sobre cada una de estas acciones. 

Asignar a conexión
~~~~~~~~~~~~~~~~~~

Para asignar un registro a una ``Conexión`` por medio de un flujo de trabajo, siga estos pasos:

.. important:: Recuerde que una conexión es un usuario que no pertenece a su cuenta de Linkaform.

1. Prepare su `flujo de trabajo <#acciones>`_ :octicon:`report;1em;sd-text-info`.

2. En el campo ``Acción`` seleccione ``Asignar a conexión``.

.. image:: /imgs/Formas/Formas34.jpg

3. Agregue un título para identificar la acción.

.. image:: /imgs/Formas/Formas35.jpg

4. En el selector ``Asignar a`` seleccione ``Conexión`` del menú.

.. image:: /imgs/Formas/Formas36.jpg

5. Capture el ``Nombre del usuario`` al que se le asignará el registro.

.. important:: Recuerde que la forma ya debe haberse compartido con ese usuario; de lo contrario, el registro no se asignará. Si la forma está compartida, al ingresar el correo del usuario, Linkaform sugerirá el nombre, que se puede seleccionar para acelerar el proceso.

.. image:: /imgs/Formas/Formas38.jpg

6. Habilite el bullet ``Enviar correo``.

.. note:: Si habilita esta opción, se enviará un correo electrónico de notificación a la persona a la que se le asignó el registro.

7. Habilite el bullet ``¿Enviar push notificación?``.

.. note:: Al habilitar esta opción, enviará una notificación a la aplicación móvil de Linkaform para el usuario al que se le asignó el registro.

Asignar a usuario
~~~~~~~~~~~~~~~~~

Para asignar un registro a un ``Usuario``, el proceso es similar a asignar a una ``Conexión`` mediante flujos. Siga los siguientes pasos:

.. important:: Recuerde que un usuario es una persona que pertenece a su empresa. 

1. Prepare su `flujo de trabajo <#acciones>`_ :octicon:`report;1em;sd-text-info`.

2. En el campo ``Acción`` seleccione ``Asignar a usuario``.

.. image:: /imgs/Formas/Formas39.jpg

3. Agregue un título para identificar la acción.

4. En el selector ``Asignar a`` seleccione ``Usuario`` del menú.

5. Capture el ``Nombre del usuario`` al que se le asignará el registro.

.. important:: Recuerde que la forma ya debe haberse compartido con ese usuario; de lo contrario, el registro no se asignará. Si la forma está compartida, al ingresar el correo del usuario, Linkaform sugerirá el nombre, que se puede seleccionar para acelerar el proceso.

6. Habilite el bullet ``Enviar correo``.

.. note:: Si habilita esta opción, se enviará un correo electrónico de notificación a la persona a la que se le asignó el registro.

7. Habilite el bullet ``¿Enviar push notificación?``.

.. note:: Al habilitar esta opción, enviará una notificación a la aplicación móvil de Linkaform para el usuario al que se le asignó el registro.

Ejecutar script
~~~~~~~~~~~~~~~

Ejecutar un script permite realizar tareas específicas de manera automatizada.

.. important:: Para tener un script personalizado contacte a soporte técnico y explique su necesidad para su desarrollo. 

1. Prepare su `flujo de trabajo <#acciones>`_ :octicon:`report;1em;sd-text-info`.

2. En el campo ``Acción`` seleccione ``Ejecutar script``.

.. image:: /imgs/Formas/Formas42.jpg

3. Agregue un título para identificar la acción.

4. Escriba el nombre del script en el selector ``Script``.

5. Seleccione ``Configuración del script``. Aparecerá una interfaz nueva, donde podrá configurar los siguientes parámetros.

En la pestaña ``Usuario`` podrá encontrar:

- **Ejecutor**: En este campo se establece el usuario que tendrá como historial la ejecución.
- **Notificar a**: En este campo establece el correo electrónico para que le llegue la notificación, el cuál se enviará cuando este flujo-script sean ejecutados

.. image:: /imgs/Formas/Formas44.jpg

En la pestaña ``Argumentos`` se establecen valores específicos para el Script.

.. important:: El script recibirá como primer argumento el registro como string y como segundo argumento un diccionario como string con los argumentos definidos.

.. admonition:: Ejemplo
  :class: pied-piper

  En ``Campo``, considere ``precio`` y en ``Valor``, ``5``. 

  Así, al script le llegará como ``{"precio": 5}``. Puede utilizar este valor en el script para realizar operaciones. 

  Este enfoque es útil, por ejemplo, si luego pone el script en otra forma y ahí el ``precio`` lo puede cambiar a ``10``. Si desea hacer una validación sobre ese ``precio`` en la Forma 1, la validación se realizará sobre el ``valor 5``, y en la Forma 2, sobre el ``valor 10``. 
  De esta manera, puede configurar los argumentos para la validación de datos.

.. _personalizar-envio-correo:

Enviar correo
~~~~~~~~~~~~~

Puede configurar esta acción para enviar correos electrónicos con información específica del registro.

1. Prepare su `flujo de trabajo <#acciones>`_ :octicon:`report;1em;sd-text-info`.
2. En el campo ``Acción`` seleccione ``Enviar correo``.
3. Agregue un título para identificar la acción.
4. Seleccione ``Configuración de Email``. 

.. image:: /imgs/Formas/Formas46.jpg

A continuación, siga las siguientes configuraciones:

.. tab-set::

  .. tab-item:: De

      En esta opción, se configura el remitente. Haga clic en el campo y seleccione el remitente deseado.

      .. image:: /imgs/Formas/Formas7.png

  .. tab-item:: Para

      Esta opción permite configurar al destinatario. Siga estos pasos para hacerlo:

      1. Seleccione el campo que activará la notificación. O en su defecto
      2. Presione el botón verde con el signo más para agregar una opción.

      .. image:: /imgs/Formas/Formas47.jpg

      .. note:: En la imagen anterior, se eligió la opción Móvil Android (campo Respuesta Múltiple)

      3. Seleccione al usuario destinatario al que se le notificará o en su defecto:
      4. Seleccione una opción en el campo ``Enviar A``.
      5. Active la opción ``Adjuntar PDF`` si es necesario.
      6. Active la opción ``Adjuntar imagen de compañía`` si es necesario.
      7. Active la opción ``Enviar adjuntos`` si necesita incluir algunos campos de su interés.
       
      .. image:: /imgs/Formas/Formas48.jpg
      
      .. note:: En la imagen anterior, se agregó el correo ``soporte@linkaform.com`` como ejemplo. Continuamos con la configuración de ``Reenvío`` (si es necesario), Adjuntar, elegir la plantilla PDF, así como si se adjuntan en el correo el logotipo de la empresa y datos adjuntos. Los datos adjuntos corresponden a si el registro capturado tiene imágenes, se agregarán en el correo de manera adjunta.

  .. tab-item:: Asunto

      En este apartado, se define el asunto que mostrará el correo. 
                
      1. Si lo requiere, personalice el texto del asunto.
              
      En la parte inferior, Linkaform permite utilizar metadatos y campos de la forma para personalizar el asunto. 
                
      1. Seleccione el metadato deseado y haga clic en ``Agregar``. Al hacerlo, aparecerá un código correspondiente al campo seleccionado.

      Del lado derecho, podrá insertar una respuesta del campo.

      1. Seleccione el campo deseado y haga clic en ``Agregar``. Al hacerlo, aparecerá un código correspondiente al campo seleccionado.

      .. admonition:: Ejemplo
          :class: pied-piper

          Considere el siguiente ejemplo, es un texto personalizado donde:

          .. image:: /imgs/Formas/Formas48.1.png

          - ``{{record.folio}}`` es el metadato que muestra el numero de folio del registro.
          - ``{{record.answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4ae}}`` es el campo, tienda de tipo texto, como identificador utiliza su ``ID``.
          - ``{{record.answers.6564fc4b7abbbbec1ea2b4ab.6564fc4b7abbbbec1ea2b4af}}`` es otro campo correspondiente al campo dirección. 


  .. tab-item:: Cuerpo

      De manera similar al caso anterior, simplemente seleccione el campo o metadato deseado y haga clic en ``Agregar``. 

      .. image:: /imgs/Formas/Formas48.2.png

  .. tab-item:: Vista previa

      En vista previa, podrá revisar el resultado final de las configuraciones que realizó anteriormente.
                
      .. image:: /imgs/Formas/Formas7.4.png

Al estar seguro de sus cambios, seleccione ``Guardar``.

.. _forma_catalogo:

Forma a catálogo
~~~~~~~~~~~~~~~~

Esta acción permite insertar el registro de una forma a un catálogo, sin necesidad de hacerlo directamente creando un registro en el catálogo

.. important:: Es muy importante tener en cuenta los siguientes puntos antes de utilizar la acción de ``Forma a catálogo``:

    1. Debe tener preparado el catálogo al que desea asignar los registros de la forma.
    2. En su forma, los campos deben coincidir exactamente con los del catálogo, incluido el tipo de campo, nombre y las mismas configuraciones como ponderación, incluso si se encuentran como requeridos.

Ahora continue siguiendo los siguientes pasos para configurar la acción:

1. Prepare su `flujo de trabajo <#acciones>`_ :octicon:`report;1em;sd-text-info`.
2. En el campo ``Acción`` seleccione ``Forma a catálogo``.
3. Agregue un título para identificar la acción.
4. Escriba el nombre del catálogo en el campo. Al teclear las primeras letras, Linkaform mostrará las coincidencias.

.. image:: /imgs/Formas/Formas51.jpg

Observe que hay dos columnas: una corresponde al nombre de su forma, en este caso, la forma que se está utilizando se llama ``Prueba básica APP`` y la del lado derecho corresponde al nombre del catálogo, en este caso, ``FAQ``.

5. Seleccione una opción en la columna correspondiente a la forma.

.. dropdown:: Opciones

  **Usar campo**: Mostrará la lista de todos los campos de la forma.

  .. image:: /imgs/Formas/Formas54.jpg

  **Usar valor**: Establece un valor fijo que siempre se utilizará.

  .. image:: /imgs/Formas/Formas55.jpg

  **Usar metadato**: Permite elegir los datos que se generan desde el servidor.

  .. image:: /imgs/Formas/Formas56.jpg

6. Seleccione el campo de la forma a la que desea relacionar con el catalogo. 
7. Seleccione el campo del catalogo. En la columna del catalogo seleccione el mismo campo que de la forma. 

.. admonition:: Ejemplo
  :class: pied-piper

  Para este ejemplo, se utiliza la opción ``Usar campo``. Se irá eligiendo campo por campo para conectar con el catálogo. Recuerde que del lado izquierdo se encuentran los campos de la forma y del lado derecho los campos del catálogo al que se conectará.

  .. image:: /imgs/Formas/Formas57.jpg

  .. important:: Agregue todos los campos necesarios. En el ejercicio anterior, solo se necesitaron 2 campos, pero puede añadir los que necesite haciendo clic en el botón verde con el símbolo más.

8. Después de realizar su configuración, haga clic en el botón ``Guardar`` y la automatización para enviar información de una forma a un catálogo estará lista.

Consulte el siguiente vídeo para obtener un ejemplo visual.

.. youtube:: o15HvwiHVR8
  :aspect: 16:9
  :width: 100%
  :height: 480
  :align: center
  :privacy_mode: enable_privacy_mode
  :url_parameters: ?start=1213

Forma a forma
~~~~~~~~~~~~~

Esta acción permite enviar información desde una forma hacia otra u otras formas.

.. important:: La estructura y configuración de los campos dentro de la forma deben coincidir con los de la forma a la que se desea conectar.

1. Prepare su `flujo de trabajo <#acciones>`_ :octicon:`report;1em;sd-text-info`.
2. Ubíquese en la forma principal que generará la conexión.
3. En el campo ``Acción``, seleccione ``Forma a Forma``.
4. Agregue un título para identificar la acción.
5. En el campo ``Forma``, escriba el nombre de la forma con la que desea establecer la conexión.

Tenga en cuenta que hay dos columnas: la izquierda corresponde a la forma actual y la derecha a la forma a la que se desea conectar.

6. ``Seleccione una opción`` en la columna correspondiente a la forma actual.

.. seealso:: Opciones

  - **Usar campo**: Muestra la lista de todos los campos de la forma actual.
  - **Usar valor**: Establece un valor fijo que siempre se utilizará.
  - **Usar metadato**: Permite elegir los datos generados desde el servidor.

7. Seleccione el campo, metadato o escriba el valor que desea relacionar con la forma.
8. En la columna derecha, correspondiente a la forma a la que se desea conectar, seleccione el campo correspondiente.

En el siguiente video podrá encontrar un ejemplo visual sobre el proceso de una acción ``Forma a Forma``.

.. youtube:: o15HvwiHVR8
  :aspect: 16:9
  :width: 100%
  :height: 480
  :align: center
  :privacy_mode: enable_privacy_mode
  :url_parameters: ?start=1771

Grupo a catálogo
~~~~~~~~~~~~~~~~

Esta acción es similar a la acción `forma a catálogo <#forma_catalogo>`_  :octicon:`report;1em;sd-text-info`. Sin embargo, está específicamente diseñada para trabajar con `grupos repetitivos <#grupo_repetitivo>`_  :octicon:`report;1em;sd-text-info` de una forma. Es más sencillo si se necesitan almacenar múltiples registros, ya que un grupo repetitivo permite agregar los sets que se requieran.

.. important:: Consideraciones Importantes:

    1. Tenga preparado el catálogo al que desea asignar los registros del grupo repetitivo.
    2. La estructura y configuración de los campos dentro del grupo repetitivo deben coincidir con los del catálogo al que desea asignar los registros.

Siga los siguientes pasos para hacer la configuración necesaria:

1. Prepare su `flujo de trabajo <#acciones>`_ :octicon:`report;1em;sd-text-info`.
2. En el campo ``Acción``, seleccione ``Grupo a catálogo``.
3. Agregue un título para identificar la acción.

Observe que hay dos columnas: en el lado izquierdo podrá encontrar opciones correspondientes al grupo repetitivo, mientras que en el lado derecho podrá encontrar opciones del catálogo al que se hará la conexión.

.. image:: /imgs/Formas/Formas59.jpg

4. En el campo ``Grupo``, seleccione el nombre del grupo repetitivo de su forma.
5. En el campo ``Catálogo``, escriba el nombre del catálogo al que desea asignar. Al teclear, Linkaform le sugerirá el nombre del catálogo.
6. ``Seleccione una opción`` en la columna correspondiente al grupo repetitivo. 

.. seealso:: Opciones

  - **Usar campo**: Mostrará la lista de todos los campos de la forma.
  - **Usar valor**: Establece un valor fijo que siempre se utilizará.
  - **Usar metadato**: Permite elegir los datos que se generan desde el servidor.

.. note:: Observe que al elegir el grupo repetitivo de la forma, solo aparecerán campos dentro de este, excluyendo a los restantes de la forma. De la misma manera, al seleccionar el catálogo de su preferencia.

7. Seleccione el campo, metadato o escriba el valor que desea relacionar con el catálogo.
8. Del lado del catálogo, seleccione el campo del catálogo.

En el siguiente video podrá encontrar un ejemplo visual del proceso. 

.. youtube:: o15HvwiHVR8
  :aspect: 16:9
  :width: 100%
  :height: 480
  :align: center
  :privacy_mode: enable_privacy_mode
  :url_parameters: ?start=1600
