======
Formas
======

En Linkaform, el término ``forma`` hace referencia a un formulario digital que posibilita la automatización de procesos. En este apartado, encontrará documentación sobre las funcionalidades que ofrece una forma, entre las que se incluyen:

#. Crear y editar formas.
#. Crear carpetas para organizar y almacenar formas.
#. Compartir formas con otros usuarios.
#. Responder formas para generar nuevos registros.
#. Acceder directamente a los registros de la forma seleccionada.
#. Realizar búsquedas de formas dentro de la cuenta.
#. Realizar configuraciones para uso personalizado. 

Este apartado abarcará todos los aspectos necesarios para diseñar una solución integral y aprovechar al máximo el potencial que Linkaform ofrece a su empresa.

La estructura de la documentación está organizada en secciones, visibles en el menú lateral ubicado al lado derecho de su pantalla. Aunque se recomienda seguir un orden cronológico, las secciones están disponibles para que pueda revisar un tema específico en cualquier momento.

Para acceder a las formas, siga los siguientes pasos:

1. Ingrese a la aplicación web oficial de Linkaform en |app| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales. 

.. note:: En caso de no contar con credenciales, solicítelas al soporte técnico.

3. Seleccione la opción ``Mis Formas``, ubicada en el menú vertical a la izquierda de su pantalla.

Una vez dentro de ``Mis Formas``, podrá comenzar a crear y configurar sus formas según sus necesidades.

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
     - Al activar esta opción, permite visualizar la información de este campo al realizar consultas en registros completados desde la app o al consultar los registros desde la web en el apartado de registros.
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

.. _grupo_repetitivo:

Campo grupo repetitivo
^^^^^^^^^^^^^^^^^^^^^^

Un grupo repetitivo es un campo utilizado para agregar varios sets dentro de él. Considérelo como un campo que permite incluir pequeños formularios dentro del formulario principal, con la ventaja de poder responder las veces que sea necesario.

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

.. image:: /imgs/Formas/Formas16.1.1.png


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

El campo catálogo es una función diferente, aunque está directamente relacionado con la sección de catálogos que ofrece Linkaform. Consulte catálogos aquí (hipervínculo). En este apartado, se tratará como un campo.

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

.. _flujos:

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

Reglas de Forma
---------------

Las reglas de forma son configuraciones que posibilitan:

- Mostrar campos
- Deshabilitar campos
- Requerir campos
- Ocultar campos

.. important:: La configuración de las reglas de forma es independiente para cada forma. En otras palabras, si duplica la misma forma, es necesario crear las reglas de forma de manera independiente, ya que no se duplicarán automáticamente.

Siga los siguientes pasos, que son requeridos para cada regla de campo:

1. Ubíquese en la forma a la que desea aplicar la regla de campo.
2. Seleccione ``Opciones > Reglas de Forma``.

.. image:: /imgs/Formas/Formas62.jpg

3. Haga clic en el botón verde con el icono de más para ``Agregar Regla``.

.. image:: /imgs/Formas/Formas63.jpg

4. Asigne un nombre descriptivo que diferencie su regla, haciendo doble clic en el nombre predeterminado ``Regla N``.

5. En el campo ``Deseo``, seleccione una opción.

.. seealso:: Opciones

  - **Mostrar**: Se utiliza para que, al cumplir una validación configurada, se muestren uno o más campos.
  - **Deshabilitar**: Funciona para que, al cumplir una validación configurada, se deshabiliten uno o más campos.
  - **Requerir**: Es útil para que, al cumplir una validación configurada, se requieran de manera obligatoria uno o más campos.
  - **Ocultar**: Se utiliza para que, al cumplir una validación configurada, se oculten uno o más campos.

6. Seleccione el o los campos que serán afectados por la regla, presionando el botón ``Campos``. Observe que aparecerán los campos de su forma.

.. image:: /imgs/Formas/Formas66.jpg

7. Escriba el nombre del campo que hará la condición que se debe cumplir para la ejecución de la regla de forma.  Observe que aparecerá un recuadro verde con el tipo de campo que representa dicho campo.

.. tip:: Si no recuerda el nombre del campo, teclee dos puntos ``(:)`` y Linkaform mostrará todos los campos de la forma.

  .. image:: /imgs/Formas/Formas67.jpg

8. Seleccione una condición para que se cumpla la regla. 

.. seealso:: Opciones

  - **No está vacío**: Esta opción valida si el campo no está vacío, es decir, si contiene algún valor.
  - **Está vacío**: Verifica si el campo está vacío, sin contener ningún valor.
  - **No contiene opción**: Comprueba si el campo no contiene una opción específica.
  - **Contiene opción**: Evalúa si el campo contiene una opción específica.
  - **NO es igual a**: Esta opción verifica si el campo no es igual al valor especificado.
  - **Igual a**: Verifica si el campo es igual al valor especificado.

La elección de las últimas cuatro opciones permitirá seleccionar o escribir contenido para realizar la validación. Puede incluir más de una validación para un campo; sin embargo, debe aplicar una relación lógica ``AND`` o ``OR``.

.. image:: /imgs/Formas/Formas68.1.png

9. Opcionalmente, seleccione el botón ``Duplicar`` para replicar la regla exactamente como está configurada en ese momento (esta opción es útil cuando se desean crear reglas muy similares).
10. Opcionalmente, seleccione ``Condiciones de usuario`` con el ícono de un solo usuario para incluir o excluir usuarios de esta regla de forma.
11. Opcionalmente, seleccione ``Condiciones de grupo`` con el ícono de grupo para incluir o excluir un grupo de usuarios de esta regla de forma.
12. Guarde sus cambios.

Consulte el video a continuación para obtener ejemplos visuales.

.. youtube:: N-eQmvPNo40
  :aspect: 16:9
  :width: 100%
  :height: 480
  :align: center
  :privacy_mode: enable_privacy_mode
  :url_parameters: ?start=23

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

Carpetas
========

Las carpetas permiten organizar y facilitar el acceso y la gestión de las formas. En las siguientes secciones, encontrará más información acerca de cómo trabajar con carpetas.

Crear carpeta
-------------

La creación de una carpeta en Linkaform sirve para almacenar una o más formas dentro de ella. Siga los siguientes pasos para crear una carpeta:

1. Seleccione la opción ``Mis Formas``, ubicada en el menú vertical a la izquierda de su pantalla.
2. Haga clic en el ícono de la burbuja con el icono de carpeta, ubicado en la parte superior derecha. Al pasar el ratón sobre ella, podrá ver la funcionalidad que ofrece.
3. Escriba el nombre de la carpeta. Observe que del lado izquierdo podrá encontrar la carpeta que creó.

.. image:: /imgs/Formas/Formas97.png

Compartir Carpeta
-----------------

Compartir una carpeta es sencillo, siga los pasos:

1. Identifique la carpeta de su interés.
2. Haga clic en el segundo ícono de compartir que aparece a la derecha.
3. En la ventana que aparece, escriba el nombre del usuario con el que desea compartir la carpeta, presione ``Enter`` y el nombre del usuario aparecerá en la parte inferior.

.. image:: /imgs/Formas/Formas98.png

.. _compartir:

4. Defina los permisos que el usuario tendrá en la carpeta:

- **Lectura**: El usuario podrá ver las formas dentro de la carpeta y crear registros.
- **Compartir**: El usuario podrá ver y responder a las formas, además de poder compartir la carpeta con otros usuarios.
- **Admin**: El usuario tendrá los mismos privilegios que los perfiles anteriores, además de poder modificar y eliminar las formas.
- **Borrar registros**: Al activar esta opción, el usuario podrá eliminar registros de las formas. Si no se activa, el usuario no podrá eliminar registros incluso si tiene el perfil de ``Admin``.

.. important:: Cuando se comparte una carpeta, las formas que contiene heredan automáticamente los permisos.

.. tip:: Si necesita mover una forma a una carpeta, simplemente arrástrela al lugar que necesite. Si necesita mover una forma fuera de alguna carpeta, a la raíz, simplemente arrástrela a la columna principal.

Opciones de forma
=================

Las formas proporcionan opciones que permiten una rápida gestión de las mismas, las cuales incluyen;

- **Borrar**
- **Compartir**: Permite otorgar permisos. Siga los `pasos <#compartir>`_ :octicon:`report;1em;sd-text-info`
- **Editar**: Permite realizar cambios en la estructura de la forma. Se pueden agregar campos, modificar respuestas, etc.
- **Duplicar**: Duplica la forma, incluidos los IDs y reglas de campo, excepto flujos de trabajo.
- **Responder**: Permite crear registros de la forma deseada. Simplemente haga clic sobre la opción y se mostrará la estructura de la forma en modo ``Responder``. Al terminar de capturar la información, haga clic en ``Mandar respuestas``.

- **Ver Registros**: Mostrará los registros de la forma. Esta opción tiene dos tipos de resultados:

  * Si la forma se tiene compartida en modo ``Solo Lectura``, el usuario solo podrá ver sus propios registros.
  * Si la forma se tiene compartida en modo ``Admin``, el usuario podrá ver todos los registros, independientemente del usuario que los haya creado.

.. image:: /imgs/Formas/Formas99.png

¡Felicitaciones! 🎉 Si ha seguido la documentación secuencialmente, ahora es capaz de diseñar y crear sus propios formularios personalizados. Si tiene alguna duda, puede regresar al contenido o preguntar directamente al soporte técnico de Linkaform.

.. LIGAS DE INTERÉS EXTERNO 

.. |app| raw:: html

    <a href="https://app.linkaform.com/" target="_blank">https://app.linkaform.com/</a>