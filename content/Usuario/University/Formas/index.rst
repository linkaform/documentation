======
Formas
======

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

Al realizar un formulario, Linkaform proporciona campos básicos para personalizar sus formularios según sus necesidades. 

.. _configuracion:

Campo texto 
^^^^^^^^^^^

Los campos de tipo texto son utilizados para capturar datos que consisten en caracteres alfabéticos, numéricos o alfanuméricos, tales como nombres, descripciones, comentarios u otra información textual. En las siguientes pestañas, podrá encontrar información útil acerca de su uso.

.. tab-set::

    .. tab-item:: Texto una línea

        Están diseñados para capturar respuestas abiertas de hasta 500 caracteres. También es posible activar la lectura de códigos de barras y códigos QR en las propiedades de este campo.

        .. image:: /imgs/Formas/Formas6.png

    .. tab-item:: Párrafo

        Permiten capturar respuestas abiertas de hasta 500 caracteres. A diferencia del campo de ``Una Línea``, en este campo es posible saltar de línea y copiar vínculos, respetando el enlace.

        .. image:: /imgs/Formas/Formas6.1.png

    .. tab-item:: Secreto

        Se utiliza para capturar información sin que la respuesta sea visible durante la captura. 

        .. image:: /imgs/Formas/Formas6.2.png
      
        .. important:: La información capturada solo se revelará una vez que se haya enviado el registro.

    .. tab-item:: Descripción

        Este campo se utiliza para incluir texto en la forma y que sirva como referencia al momento de capturar información. Puede contener recomendaciones o instrucciones a seguir.

        .. image:: /imgs/Formas/Formas6.3.png
        
        .. caution:: La información capturada en este campo será visible al responder, pero no estará presente en el PDF final.

    .. tab-item:: Email

        En el campo Email, puede capturar direcciones de correo electrónico. 

        Cuando este campo se establece como requerido, Linkaform realiza una validación para asegurarse de que la dirección tenga la estructura correspondiente a un correo electrónico. Sin embargo, Linkaform no verifica la existencia real del correo electrónico.

        .. image:: /imgs/Formas/Formas6.4.png
          
        Además, puede activar la opción ``Enviar Email`` y Linkaform enviará una copia del registro capturado al correo que seleccione.

        Al activar la opción ``Enviar Email``, en las opciones a la derecha de su pantalla, se habilitará la función ``Configuración de Email``. A continuación, siga las siguientes configuraciones:
        
        .. tab-set::

            .. tab-item:: De

                En esta opción, se configura el remitente. Haga clic en el campo y seleccione el remitente deseado.

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

                De manera similar al caso anterior en el asunto, simplemente seleccione el campo deseado y haga clic en ``Agregar``. 

                .. image:: /imgs/Formas/Formas7.3.png

            .. tab-item:: Vista previa

                En la vista previa, podrá revisar el resultado final de las configuraciones que realizó anteriormente.
                
                .. image:: /imgs/Formas/Formas7.4.png

        Al estar seguro de sus cambios, seleccione ``Guardar``.

Campo respuesta múltiple
^^^^^^^^^^^^^^^^^^^^^^^^

Un campo de respuesta múltiple resulta útil cuando se busca recopilar datos sobre preferencias, habilidades o situaciones en las que las respuestas no son excluyentes entre sí. 

Dos configuraciones comunes que comparten la mayoría de los campos de respuesta múltiple son la ponderación y el envío de notificaciones.

.. _pond:

La ponderación es el proceso de asignar un peso o valor relativo a cada opción seleccionada por el usuario.

Para habilitar la opción de ``Configuración de la ponderación``, es necesario realizar una configuración en `Opciones Generales <#ponde>`_ :octicon:`report;1em;sd-text-info`, seguido de los siguientes pasos:

1. Seleccione el botón ``Configuración de la ponderación``.
2. Seleccione la respuesta en el selector.
3. En el recuadro inferior, especifique el puntaje o porcentaje.
4. Haga clic en ``Agregar opción``. La respuesta aparecerá en el recuadro inferior.
5. Presione ``Guardar``.

.. image:: /imgs/Formas/Formas9.jpg
    :height: 400px
    :width: 600px

.. important:: Este proceso se repite según sea necesario, en función de las respuestas disponibles en el campo.

Para configurar las notificaciones y habilitar el envío de notificaciones, consulte la `configuración de Email <#configuracion>`_ :octicon:`report;1em;sd-text-info` en el campo email.
        
En el siguiente recuadro, podrá encontrar los tipo de respuesta múltiple. Considere los puntos anteriores:

.. tab-set::

    .. tab-item:: Respuesta única

        Este campo se utiliza para seleccionar una sola opción de una lista de opciones proporcionadas. Considere activar la ``opción abierta`` para que el usuario pueda ingresar otra respuesta.
        
        .. image:: /imgs/Formas/Formas9.0.png
          
    .. tab-item:: Respuesta múltiple

        Permite seleccionar más de una opción de la lista proporcionada. De la misma forma, tenga en consideración activar la ``opción abierta`` para que el usuario pueda ingresar otra respuesta.

        .. image:: /imgs/Formas/Formas9.1.png

    .. tab-item:: Sí/No

        Este campo simplifica las opciones de respuesta a solo dos: ``Sí`` o ``No``. En este campo sólo se puede elegir una de las respuestas.
        
        .. image:: /imgs/Formas/Formas9.2.png

    .. tab-item:: Selecciona un campo

        Se utiliza para crear menús desplegables o listas de opciones donde los usuarios deben seleccionar una respuesta.

        .. image:: /imgs/Formas/Formas9.3.png

Campo número
^^^^^^^^^^^^

Los campos numéricos se utilizan para recopilar información numérica de las formas. Considere las siguientes configuraciones que comparten:

- Revise y si es necesario, configure la `ponderacion <#pond>`_ :octicon:`report;1em;sd-text-info` del campo.
        
- Si requiere, habilite la `configuración de Email <#configuracion>`_ :octicon:`report;1em;sd-text-info` en el campo email.

- Establezca parámetros de rango de mínimos y máximos en las propiedades del campo.
    
.. tab-set::

    .. tab-item:: Entero

        Este tipo de campo permite introducir únicamente números enteros.

        .. image:: /imgs/Formas/Formas10.png

    .. tab-item:: Decimal
      
        Permite introducir números con decimales. 

        .. image:: /imgs/Formas/Formas10.1.png

Campo fecha
^^^^^^^^^^^

Este campo es útil para recopilar información relacionada con el tiempo. Se utiliza comúnmente para agregar información de fecha y hora en una misma captura.

.. image:: /imgs/Formas/Formas11.png
  
.. important:: Si lo requiere, puede agregar estos campos por separado.

Campo grupo repetitivo
^^^^^^^^^^^^^^^^^^^^^^

Un grupo repetitivo es un campo utilizado para agregar varios campos dentro de él. Considérelo como un campo que permite incluir pequeños formularios dentro del formulario principal, con la ventaja de poder responder las veces que sea necesario.

.. image:: /imgs/Formas/Formas12.jpg

Para utilizarlo, siga estos pasos:

1. Agregue el campo.
2. Asigne un nombre con el título del campo.
3. Guarde la forma en su totalidad.

.. important:: Guardar el formulario permitirá habilitar la opción ``Editar``.

4. Seleccione ``Editar`` (se mostrará una plantilla en blanco).
5. Coloque los campos que formarán parte de este grupo repetitivo (son los mismos vistos en esta sección).

.. image:: /imgs/Formas/Formas13.jpg

Campo geolocalización
^^^^^^^^^^^^^^^^^^^^^

El campo de Geolocalización se utiliza para incluir la ubicación geográfica en el registro capturado. Este campo es editable, por lo que modificarla según sea necesario.

.. image:: /imgs/Formas/Formas14.jpg
    :height: 150px
    :width: 700px

Campo fotografías
^^^^^^^^^^^^^^^^^

Este campo es utilizado para agregar evidencias fotográficas al registro en el momento de la captura y/o edición. 

.. image:: /imgs/Formas/Formas15.jpg
    :height: 150px
    :width: 700px
    
.. _config:

En la opción ``Config`` de este campo, se definen parámetros que son posibles de configurar, los cuales son:

.. grid:: 2
    :gutter: 0
    :padding: 0
    :margin: 0

    .. grid-item-card:: 
        :columns: 5
        :padding: 0
        :margin: 0

        .. image:: /imgs/Formas/Formas15.1.png
            :height: 550px

    .. grid-item-card:: 
        :columns: 7

        **Cantidad de imágenes:** Mínimo 0, Máximo 15.

        **Seleccionar imágenes de:** Cámara, Galería, Dibujar. Las opciones activadas serán las permitidas para este campo.

        **Configuración de campos** contiene las siguientes opciones:

        - **Agregar a la imagen:** Permite incluir los parámetros de Geolocalización (ubicación) en la que se tomó o agregó la foto, así como la fecha de captura.
        - **Campos:** Permite incluir campos correspondientes de la forma para agregarlos impresos en esa imagen. Simplemente teclee el título del campo y Linkaform lo sugerirá; presione ``Enter`` y se agregará.
        - **Nombre de archivo:** Permite incluir metadatos correspondientes a ese registro en el nombre de archivo o puede introducir un texto para que se imprima en la imagen.
        - **Configurar marca de agua:** Habilitar esta opción permite definir el color, tamaño y la posición de la marca de agua en la foto donde desea que aparezca impresa la información.

Campo documentos
^^^^^^^^^^^^^^^^
Este campo permite agregar diferentes tipos de archivos al registro de la forma en el momento de la captura y/o edición. 

.. image:: /imgs/Formas/Formas16.jpg
    :height: 150px
    :width: 700px

Del mismo modo que el campo fotografías, puede configurar los parámetros en `conf <#config>`_ :octicon:`report;1em;sd-text-info`. Sin embargo, aquí tiene la posibilidad de seleccionar qué tipo de archivos son permitidos.

Campo firma
^^^^^^^^^^^

Este tipo de campo permite a los usuarios firmar digitalmente el formulario.

Si se utiliza desde un formulario en la aplicación web, simplemente podrán utilizar el teclado. Por otro lado, al utilizar dispositivos móviles, podrán dibujar su firma.

Este campo es útil en situaciones donde se requiere una confirmación o autorización.

.. image:: /imgs/Formas/Formas16.1.png
    :height: 150px
    :width: 700px

.. important:: Al momento de responder el formulario, la firma se guardará y tratará como un archivo de tipo imagen.

Campo catálogo
^^^^^^^^^^^^^^

El campo Catálogo es una función diferente, aunque está directamente relacionado con la sección de catálogos que ofrece Linkaform. Consulte catálogos aquí (hipervínculo). En este apartado, se tratará como un campo.

El campo Catálogo se utiliza para mostrar en la forma información correspondiente a un catálogo. Para utilizarla, tenga en cuenta los siguientes aspectos y siga los siguientes pasos:

1. Primero, considere tener o, en su defecto, crear un catálogo (hipervínculo). En este caso, contemple el catálogo ``Tiendas``.
2. Agregue el campo catálogo a la forma.
3. Asigne un nombre al catálogo.
4. En ``Catalog Name``, coloque el nombre del catálogo previamente preparado. Automáticamente, Linkaform sugerirá el nombre del catálogo.

.. important:: No puede tener dos campos catálogo utilizando el mismo catálogo.

5. Guarde la forma en su totalidad.
6. Presione el botón ``Editar``.

.. image:: /imgs/Formas/Formas17.png

.. dropdown:: Editar
  
      En la interfaz de edición, podrá configurar los siguientes apartados. 

      **Filtro de catálogo:** Puede crear un filtro de la información del catálogo y al aplicar el filtro, la forma solo mostrará el resultado de ese filtro. (hipervínculo de filtros en catálogos)

      .. image:: /imgs/Formas/Formas17.1.png

      **Editar campos del catálogo:** En la opción ``Editar``, seleccione los campos del catálogo que desea incluir en la forma.
      
      .. admonition:: Ejemplo
          :class: pied-piper

          Por ejemplo, aunque el catálogo tenga 10 campos, en la forma solo puede utilizar 3 campos.

      .. image:: /imgs/Formas/Formas17.2.1.png

      Al seleccionar los campos, podrá observarlos en la interfaz de edición y tendrá las siguientes opciones:
      
      .. image:: /imgs/Formas/Formas17.2.2.png

      - **Solo lectura:** Al activar esta opción, el campo solo será visible. El usuario al capturar información no podrá seleccionarlo. 

      .. admonition:: Ejemplo
          :class: pied-piper
          
          Por ejemplo, en el catálogo ``Tiendas``, se incluyen los campos de tipo texto ``Tienda`` y ``Cadena`` con la opción de lectura deshabilitada. Al ejecutarlo en el formulario, permitirá al usuario seleccionar estos campos. En cambio, los campos ``Determinante`` y ``Dirección``, al estar habilitados, no podrán ser seleccionados, pero con los dos campos anteriores permitirán el autorellenado.

      - **Requerido:** Activar esta opción asegura que no se enviará la información sin todos los datos del catálogo.

      - **Ayuda:** Habilita una opción de texto adicional en el campo como referencia a la respuesta que se solicita.

      En **Propiedades** ubicada debajo del campo, puede habilitar la lectura de código de barras. Esto aplica para campos en los que su información corresponda a alguna etiqueta. También, puede establecer el **Tipo** para que haga la lectura directa o búsqueda de la información en la base de datos.

      .. image:: /imgs/Formas/Formas18.jpg
      
      .. important:: Para organizar los campos seleccionados; simplemente haga clic en el campo y arrástralo a la posición deseada.

      - **Geocerca:** Una funcionalidad de catálogos es poder dar de alta ubicaciones mediante coordenadas GPS. Al habilitarse Geocerca, se define la distancia de referencia permitida de las coordenadas, y así solo se mostrará la información si se encuentra en el rango de metros configurado.

      .. image:: /imgs/Formas/Formas17.3.png

      Al tener tus configuraciones listas, presione ``Guardar`` y regrese al formulario presionando ``Cerrar``.

Opciones
--------

Las opciones son configuraciones que se pueden aplicar a la forma. Puede encontrar opciones generales, configuraciones sobre flujos, reglas para aplicar a la forma, embeber la forma, imprimir la forma en formato PDF y utilizar botones. En los siguientes apartados podrá encontrar información más detallada acerca de cada una de ellas.

.. image:: /imgs/Formas/Formas20.jpg

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

- **Pública**: Con la activación de esta función, permite que el formulario pueda ser contestado libremente por cualquier persona que no tenga una cuenta en Linkaform. Simplemente copie el enlace que aparecerá a la derecha y compártala, esto permitirá que personas que no utilicen Linkaform puedan generar información.

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

.. _ponde:

Ponderación 
^^^^^^^^^^^

En esta sección podrá especificar si desea utilizar la ponderación en la forma. 

1. Active la opción ``Ponderación``.
2. Defina si se calificará por puntos o porcentaje. 

.. important:: Tenga en cuenta que solo es posible utilizar una de ambas ponderaciones. 

.. note:: Si elige calificar por porcentaje, debe establecer la puntuación máxima.

.. image:: /imgs/Formas/Formas23.2.png

Temporizador 
^^^^^^^^^^^^

**Opciones Generales - Temporizador**

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

Configuración de flujos
-----------------------

La configuración de flujos se utiliza para automatizar procesos en las formas.

Si desea configurar un flujo para una acción específica, siga estos pasos:

1. Diríjase a ``Opciones > Configuración de Flujos``.

En esta sección, Linkaform presenta una página en blanco donde se agregarán los flujos deseados para esta forma.

2. Haga clic en el botón verde para ``Agregar Regla``.

.. image:: /imgs/Formas/Formas26.png

Ahora continúe con la configuración siguiendo las recomendaciones y teniendo en cuenta las secciones que la componen.

3. Asigne un nombre al flujo. Para hacerlo, simplemente haga clic en ``Nombre de regla`` y establezca el nombre.

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

Acciones
^^^^^^^^

En ``Acciones``, se especifica lo que se desea que se realice. Aquí puede encontrar varias opciones, como asignar a un usuario, a una conexión, ejecutar un script, enviar un correo, entre otras. Siga los primeros pasos que son necesarios para todas las acciones.

1. Realice la configuración del `trigger <#triggers>`_ :octicon:`report;1em;sd-text-info`.
2. Haga clic en el botón verde con el símbolo más para ``Agregar acción``. Al hacer esto se agrega una barra verde con el titulo ``Acción vacía``. Haga clic sobre ella.
3. Presione en el selector de ``Acción`` y elija una opción según su necesidad.

.. image:: /imgs/Formas/Formas33.png

.. important:: En base a un ``Trigger``, que establece las condiciones para que se dispare un flujo de trabajo, se pueden configurar varias acciones. Estas acciones se ejecutarán automáticamente cuando se cumplan las condiciones especificadas en el Trigger. 

En el selector de ``Acción``, contemple las siguientes pestañas que contiene las opciones e información más detallada sobre cada una de estas acciones. 

Asignar a conexión
~~~~~~~~~~~~~~~~~~

Para asignar un registro a una ``Conexión`` por medio de un flujo de trabajo, siga estos pasos:

.. important:: Recuerde que una conexión es un usuario que no pertenece a su cuenta de Linkaform.

1. En el campo ``Acción`` seleccione ``Asignar a conexión``.

.. image:: /imgs/Formas/Formas34.jpg

2. Agregue un título para identificar la acción.

.. image:: /imgs/Formas/Formas35.jpg

3. En el selector ``Asignar a`` seleccione ``Conexión`` del menú.

.. image:: /imgs/Formas/Formas36.jpg

4. Capture el ``Nombre del usuario`` al que se le asignará el registro.

.. important:: Recuerde que la forma ya debe haberse compartido con ese usuario; de lo contrario, el registro no se asignará. Si la forma está compartida, al ingresar el correo del usuario, Linkaform sugerirá el nombre, que se puede seleccionar para acelerar el proceso.

.. image:: /imgs/Formas/Formas38.jpg

5. Habilite el bullet ``Enviar correo``.

.. note:: Si habilita esta opción, se enviará un correo electrónico de notificación a la persona a la que se le asignó el registro.

6. Habilite el bullet ``¿Enviar push notificación?``.

.. note:: Al habilitar esta opción, enviará una notificación a la aplicación móvil de Linkaform para el usuario al que se le asignó el registro.

Asignar a usuario
~~~~~~~~~~~~~~~~~

Para asignar un registro a un ``Usuario``, el proceso es similar a asignar a una ``Conexión`` mediante flujos. Siga los siguientes pasos:

.. important:: Recuerde que un usuario es una persona que pertenece a su empresa. 

1. En el campo ``Acción`` seleccione ``Asignar a usuario``.

.. image:: /imgs/Formas/Formas39.jpg

2. Agregue un título para identificar la acción.

3. En el selector ``Asignar a`` seleccione ``Usuario`` del menú.

4. Capture el ``Nombre del usuario`` al que se le asignará el registro.

.. important:: Recuerde que la forma ya debe haberse compartido con ese usuario; de lo contrario, el registro no se asignará. Si la forma está compartida, al ingresar el correo del usuario, Linkaform sugerirá el nombre, que se puede seleccionar para acelerar el proceso.

5. Habilite el bullet ``Enviar correo``.

.. note:: Si habilita esta opción, se enviará un correo electrónico de notificación a la persona a la que se le asignó el registro.

6. Habilite el bullet ``¿Enviar push notificación?``.

.. note:: Al habilitar esta opción, enviará una notificación a la aplicación móvil de Linkaform para el usuario al que se le asignó el registro.

Ejecutar script
~~~~~~~~~~~~~~~

Ejecutar un script permite realizar tareas específicas de manera automatizada.

.. important:: Para tener un script personalizado contacte a soporte técnico y explique su necesidad para su desarrollo. 

1. En el campo ``Acción`` seleccione ``Ejecutar script``.

.. image:: /imgs/Formas/Formas42.jpg

2. Agregue un título para identificar la acción.

3. Escriba el nombre del script en el selector ``Script``.

4. Seleccione ``Configuración del script``. Aparecerá una interfaz nueva, donde podrá configurar los siguientes parámetros.

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

Enviar correo
~~~~~~~~~~~~~

Puede configurar esta acción para enviar correos electrónicos con información específica del registro.

1. En el campo ``Acción`` seleccione ``Enviar correo``.
2. Agregue un título para identificar la acción.
3. Seleccione ``Configuración de Email``. 

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

      En este campo, se define el asunto que mostrará el correo. 
                
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

Forma a catálogo
~~~~~~~~~~~~~~~~

Esta acción permite insertar el registro de una forma a un catálogo, sin necesidad de hacerlo directamente creando un registro en el catálogo

.. important:: Es muy importante tener en cuenta los siguientes puntos antes de utilizar la acción de ``Forma a catálogo``:

    1. Debe tener preparado el catálogo al que desea asignar los registros de la forma.
    2. En su forma, los campos deben coincidir exactamente con los del catálogo, incluido el tipo de campo, nombre y las mismas configuraciones como ponderación, incluso si se encuentran como requeridos.

Ahora continue siguiendo los siguientes pasos para configurar la acción:

1. En el campo ``Acción`` seleccione ``Forma a catálogo``.
2. Agregue un título para identificar la acción.
3. Escriba el nombre del catálogo en el campo. Al teclear las primeras letras, Linkaform mostrará las coincidencias.

.. image:: /imgs/Formas/Formas51.jpg

Observe que hay dos columnas: una corresponde al nombre de su forma, en este caso, la forma que se está utilizando se llama ``Prueba básica APP`` y la del lado derecho corresponde al nombre del catálogo, en este caso, ``FAQ``.

4. Seleccione una opción en la columna correspondiente a la forma.

.. dropdown:: Opciones

  **Usar campo**: Mostrará la lista de todos los campos de la forma.

  .. image:: /imgs/Formas/Formas54.jpg

  **Usar valor**: Establece un valor fijo que siempre se utilizará.

  .. image:: /imgs/Formas/Formas55.jpg

  **Usar metadato**: Permite elegir los datos que se generan desde el servidor.

  .. image:: /imgs/Formas/Formas56.jpg

5. Seleccione el campo de la forma a la que desea relacionar con el catalogo. 
6. Seleccione el campo del catalogo. En la columna del catalogo seleccione el mismo campo que de la forma. 

.. admonition:: Ejemplo
  :class: pied-piper

  Para este ejemplo, se utiliza la opción ``Usar campo``. Se irá eligiendo campo por campo para conectar con el catálogo. Recuerde que del lado izquierdo se encuentran los campos de la forma y del lado derecho los campos del catálogo al que se conectará.

  .. image:: /imgs/Formas/Formas57.jpg

  .. important:: Agregue todos los campos necesarios. En el ejercicio anterior, solo se necesitaron 2 campos, pero puede añadir los que necesite haciendo clic en el botón verde con el símbolo más.

7. Después de realizar su configuración, haga clic en el botón ``Guardar`` y la automatización para enviar información de una forma a un catálogo estará lista.

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

Grupo a catálogo
~~~~~~~~~~~~~~~~

Esta acción es similar a la acción ``Forma a catálogo``. Sin embargo, es específicamente para grupos repetitivos de una forma.   
permite insertar el registro de una forma a un catálogo, sin necesidad de hacerlo directamente creando un registro en el catálogo


Grupo a registros
~~~~~~~~~~~~~~~~~

Sincronización de registros
~~~~~~~~~~~~~~~~~~~~~~~~~~~











4. **Enviar Notificación:** Envía notificaciones a usuarios de Linkaform relacionadas con el registro.

5. **Cambiar Estado:** Permite cambiar el estado del registro, lo que puede ser útil para el seguimiento de procesos.

6. **Asignar a Grupo:** Similar a la asignación a usuario o conexión, pero para grupos.

7. **Insertar Registro:** Permite insertar un nuevo registro en otra forma.

8. **Actualizar Registro:** Actualiza la información de otro registro en otra forma.

9. **Eliminar Registro:** Elimina un registro específico.

10. **Generar PDF:** Crea un archivo PDF basado en la información del registro.