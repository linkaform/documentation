.. _crear-form:

===========
Crear forma
===========

Para crear una forma siga el procedimiento:

1. |iniciar-sesion| :octicon:`report;1em;sd-text-info` utilizando sus credenciales.
2. Diríjase a ``Formas > Mis formas`` en el menú lateral.
3. Identifique y presione el ícono de ``Archivo`` ubicado en la parte superior derecha. 

.. hint:: Posicione el cursor sobre el ícono y la ayuda visual proporcionará información sobre su función.

Linkaform presentará una plantilla en blanco, a partir de la cual podrá estructurar su formulario.

.. image:: /imgs/Formas/Formas2.png

Nombre de la forma
------------------

Para establecer o cambiar el nombre de una forma, siga los pasos:

1. Presione el icono de lápiz o haga clic en el título actual en la parte superior izquierda. 
2. Ingrese el nuevo nombre de la forma.
3. Presione ``Enter``.
4. Guarde la forma.

.. image:: /imgs/Formas/Formas3.png

.. important:: Después de realizar cualquier cambio en la forma, debe guardar los cambios. Para ello, haga clic en el botón ``Guardar`` ubicado en la parte superior derecha.

Páginas en la forma
-------------------

Las páginas son útiles para organizar la información de formularios extensas de manera clara y fácil de navegar.

Para agregar una nueva página, simplemente presione el botón verde ``Nueva página``. 

.. note:: Puede crear las páginas necesarias, que por defecto van tomando el número de página por orden de creación, es decir, página 1, página 2, etc.

.. image:: /imgs/Formas/Formas103.png

Para duplicar la página, presione el botón ``Duplicar Página`` ubicado en la parte superior derecha. 

.. note:: Al duplicar, se creará una copia exacta de la página actual, incluido el nombre seguido de la leyenda **copy**, lo que identificará a la página como una copia.

.. image:: /imgs/Formas/Formas106.png

Para definir o cambiar el nombre de una página es sencillo. Siga los siguientes pasos:

1. Identifique la página en la que se encuentra, que por defecto al abrir la forma es la **Pagina 1**.
2. Haga clic en el título o ícono de edición de la página.
3. Ingrese el nuevo nombre.
4. Presione Enter.

.. image:: /imgs/Formas/Formas4.jpg

Para eliminar una página haga clic en el icono ``x`` ubicado a un costado del nombre de la página.

.. image:: /imgs/Formas/Formas105.png

Si tiene un formulario extenso, utilice el buscador que permite filtrar las páginas.

.. image:: /imgs/Formas/Formas104.png

.. _opciones-campos:

Campos
------

Los campos son elementos del formulario que permiten recopilar y almacenar la información. Para preparar su propio formulario, Linkaform proporciona campos básicos para personalizar sus formas o :ref:`catalogo` :octicon:`report;1em;sd-text-info`.

En la siguiente tabla, encontrará características que están disponibles para algunos campos y que realizan acciones específicas dependiendo del campo.

.. list-table::
   :widths: 25 75
   :header-rows: 1
   :align: left

   * - Característica
     - Descripción
   * - ⭐ Favorito
     - Al activar esta opción, permite visualizar la información de este campo al realizar consultas en registros completados desde el :ref:`inbox-app` :octicon:`report;1em;sd-text-info`  o al consultar los registros desde la web en el apartado de registros.
   * - Ascendente/Descendente
     - Permite ordenar las respuestas del campo en el orden elegido.
   * - Duplicar
     - Crea una copia exacta del campo.
   * - Config
     - Configuraciones para establecer cantidades límite de imágenes o documentos, orígenes de archivos permitidos, impresión de fechas y localizaciones.
   * - Requerido
     - Hace obligatoria la respuesta al campo al crear un registro.
   * - Default
     - Define una respuesta predeterminada en la forma o catálogo, la cual se puede modificar al responder.
   * - Enviar email
     - Al activar esta opción, se puede enviar una copia del registro que se está capturando al correo capturado en este campo.
   * - Opción abierta
     - Permite agregar una opción adicional en la respuesta cuando se definen respuestas únicas.
   * - Propiedades
     - En el campo de texto, sirve para habilitar la lectura de códigos de barras o QR. En campos numéricos, esta opción establece parámetros mínimos y máximos aceptados.
   * - Configuración notificación
     - Permite configurar el envío de un correo electrónico al seleccionar una de las opciones de respuesta disponibles.
   * - Configuración ponderación
     - Establece el puntaje deseado para las respuestas.
   * - Ayuda
     - Habilita una opción de texto adicional en el campo como referencia a la respuesta solicitada.

.. _configuracion:

Nombre de los campos
^^^^^^^^^^^^^^^^^^^^

La opción de actualizar el nombre está disponible para **todos** los campos. Cuando crea un nuevo campo, el nombre predeterminado es ``Título de la pregunta``. Para actualizar, siga estos pasos:

1. Presione el icono de lápiz o haga clic en el título actual del campo.
2. Ingrese el nuevo nombre del campo.
3. Presione el botón verde ``✓`` o directamente ``Enter`` para completar los cambios.

.. image:: /imgs/Formas/Formas108.png

.. attention:: Recuerde que es muy importante guardar cambios después de realizar cualquier modificación dentro de la forma. Para hacerlo, simplemente presione el botón ``Guardar`` ubicado en la parte superior derecha.

  .. image:: /imgs/Formas/Formas107.png

Campo texto 
^^^^^^^^^^^

Los campos de tipo texto son utilizados para capturar datos que consisten en caracteres alfabéticos, numéricos o alfanuméricos, tales como nombres, descripciones, comentarios u otra información textual. En las siguientes pestañas, podrá encontrar información detallada acerca de su uso.

.. tab-set::

    .. tab-item:: Texto una línea

        Está diseñado para recopilar respuestas breves, con una limitación de hasta 255 caracteres. 
        
        Estos campos presentan una interfaz de entrada de una sola línea, ideal para capturar información concisa como nombres, direcciones o números de teléfono.
        
        Este campo ofrece la posibilidad de activar la lectura de códigos de barras y códigos QR para una entrada eficiente de datos. Para utilizarlo, simplemente active la opción correspondiente como se muestra en la imagen.        

        .. image:: /imgs/Formas/Formas6.png

    .. tab-item:: Párrafo

        Permiten recopilar respuestas más extensas, con una restricción de hasta 500 caracteres. A diferencia del campo ``texto una línea``, estos campos ofrecen un área más amplia que facilita la entrada de textos más largos, como comentarios detallados o descripciones. 
        
        Este campo permite a los usuarios saltar de línea y copiar vínculos, manteniendo la integridad de los enlaces proporcionados en la respuesta.

        .. image:: /imgs/Formas/Formas6.1.png

    .. tab-item:: Secreto

        Se utiliza para capturar información sin que la respuesta sea visible durante la captura. La información capturada solo se revelará una vez que se haya enviado el registro.

        .. image:: /imgs/Formas/Formas6.2.png
      
    .. tab-item:: Descripción

        Este campo se utiliza para incluir texto en la forma y que sirva como referencia al momento de capturar información. Puede contener recomendaciones o instrucciones a seguir.

        .. image:: /imgs/Formas/Formas6.3.png
        
        .. note:: Si requiere un PDF del registro, este campo no estará presente en el documento; solo será visible al responder la forma.

    .. tab-item:: Email

        Este campo es útil para capturar únicamente direcciones de correo electrónico. 

        .. important:: Linkaform realiza una validación para asegurarse de que la dirección tenga la estructura correspondiente a un correo electrónico. Sin embargo, Linkaform **no** verifica la existencia real del correo electrónico.
        
        El campo **Email** permite configurar la forma para enviar una copia del registro capturado por correo. Para activar esta función, seleccione la opción ``Enviar Email``.

        .. attention:: Esta opción está disponible unicamente para formas. 

        .. image:: /imgs/Formas/Formas6.4.png

        Se habilitará el botón ``Configuración de Email``. A continuación, siga las siguientes configuraciones:

        .. tab-set::

          .. tab-item:: De

              En este apartado, configure al remitente. Haga clic en el campo y seleccione el remitente deseado.

              .. list-table::
                :widths: 30 70
                :header-rows: 1
                :align: left

                * - Campo
                  - Descripción
                * - Dueño de la forma
                  - Usuario que creó la forma.
                * - Dueño de la cuenta
                  - Propietario de la cuenta.
                * - Usuarios que contestan
                  - Usuarios que responden el formulario.
                * - Usuario que creó el registro
                  - Usuarios que creó el registro.
                * - Conexión del registro
                  - Usuario que no pertenece a la misma cuenta padre pero tiene acceso a visualizar el registro.
                * - Email personalizado
                  - Si elige esta opción, ingrese el correo electrónico.
                * - Respuesta a campo de correo
                  - La dirección de correo electrónico proporcionada en un campo email del formulario.

              .. image:: /imgs/Formas/Formas7.png

          .. tab-item:: Para

              Esta opción permite configurar las acciones que se llevarán a cabo cuando se envíe el registro. 
              
              .. attention:: Por defecto, el correo capturado o especificado en el campo al enviar el registro se toma como destinatario . Para configurar al destinatario, debe hacerlo en la :ref:`configurar-correo-email` :octicon:`report;1em;sd-text-info` de toda la forma. 
              
              Siga los siguientes pasos:
              
              1. Seleccione una acción al editar un registro.
              2. Active la opción ``Adjuntar PDF`` si necesita enviar el registro en un documento PDF y seleccione una plantilla.
              
              .. seealso::  Por defecto, la lista de opciones contienen plantillas genéricas que se adaptan a cualquier formulario. Si necesita un documento personalizado, consulte la documentación sobre :ref:`doc-pdfs` :octicon:`report;1em;sd-text-info`
        
              3. Active la opción ``Adjuntar imagen de compañía`` para que el PDF contenga el logo de su empresa.
              4. Active la opción ``Enviar adjuntos`` si necesita incluir algunos campos de su interés.

              .. image:: /imgs/Formas/Formas7.1.png

          .. tab-item:: Asunto

              En este apartado, defina el asunto que mostrará el correo. En la parte inferior, Linkaform permite utilizar metadatos y campos de la forma para personalizar el asunto. 
              
              Para seleccionar un metadato o campo, elija y haga clic en ``Agregar``. Al hacerlo, aparecerá el **metadato** o el ``id`` correspondiente al **campo** seleccionado.

              .. admonition:: Ejemplo
                  :class: pied-piper

                  En este ejemplo, ``{{record.form.name}}`` es el metadato que muestra el nombre de la forma.

                  .. image:: /imgs/Formas/Formas111.png

          .. tab-item:: Cuerpo

              Este apartado es para definir el cuerpo del correo. El cuerpo de un correo es útil para agregar una descripción más detallada y extensa. 
              
              De manera similar al caso anterior, puede utilizar **metadatos** y **campos** de la forma para personalizar el cuerpo. 
              
              Simplemente seleccione el **metadato** o el **campo** deseado y haga clic en ``Agregar``.

              .. admonition:: Ejemplo
                  :class: pied-piper

                  En este ejemplo, ``{{record.answers.65a72ad10e0c..}}`` representa los identificadores únicos de los campos asociados al formulario. Observe la diferencia entre un metadato y un campo.

                  .. image:: /imgs/Formas/Formas112.png

          .. tab-item:: Vista previa

              En vista previa, podrá revisar el resultado final de las configuraciones que realizó anteriormente.

              Al estar seguro de sus cambios, seleccione ``Guardar``.
                        
              .. image:: /imgs/Formas/Formas115.png


.. _campo-respuesta-multiple:

Campo respuesta múltiple
^^^^^^^^^^^^^^^^^^^^^^^^

Un campo de respuesta múltiple resulta útil cuando se busca recopilar datos sobre preferencias, habilidades o situaciones en las que las respuestas no son excluyentes entre sí. 

Consulte las siguientes pestañas donde podrá encontrar los tipos de respuesta múltiple disponibles:

.. tab-set::

    .. tab-item:: Respuesta única

        Este campo se utiliza para seleccionar **una opción** de una lista de opciones proporcionadas. 
        
        - Para añadir una nueva respuesta, presione ``Agregar otra opción``.
        - Para permitir al usuario ingresar una respuesta personalizada, active el bullet ``Opción abierta``.
        - Para ordenar alfabéticamente (A-Z o de la Z-A) las respuestas, presione ``Ascendente`` o ``Descendente``.
        - Si lo necesita, ordene manualmente las respuestas arrastrando la opción al lugar deseado.
        - Para eliminar una respuesta, presione el botón ``x`` ubicado al lado de la opción.
        
        .. image:: /imgs/Formas/Formas9.0.png
          
    .. tab-item:: Respuesta múltiple

        Este campo permite seleccionar **más de una opción** de la lista proporcionada. 

        - Para agregar otra respuesta, use ``Agregar otra opción``.
        - Active ``Opción abierta`` para respuestas personalizadas.
        - Ordene alfabéticamente con ``Ascendente`` o ``Descendente``.
        - Reordene arrastrando las respuestas.
        - Elimine opciones con el botón ``x``.

        .. image:: /imgs/Formas/Formas9.1.png

    .. tab-item:: Sí/No

        Este campo simplifica las opciones de respuesta a solo **Sí** o **No**,  donde solo se puede elegir una respuesta.

        - Ordene alfabéticamente con ``Ascendente`` o ``Descendente``.
        - Ordene manualmente arrastrando las respuestas.
        - Elimine una respuesta con el botón ``x``.

        .. image:: /imgs/Formas/Formas9.2.png

    .. tab-item:: Selecciona un campo

        Este campo se utiliza para mostrar las opciones en un selector desplegable, donde los usuarios deben seleccionar una respuesta.

        - Para agregar otra respuesta, use ``Agregar otra opción``.
        - Ordene alfabéticamente con ``Ascendente`` o ``Descendente``.
        - Reordene arrastrando las respuestas.
        - Elimine opciones con el botón ``x``.

        .. image:: /imgs/Formas/Formas9.3.png

Revise las siguientes configuraciones:

.. _pond:

.. dropdown:: Configuración de la ponderación
  
  La ponderación es el proceso de asignar un peso o valor relativo a cada opción del campo. Esta configuración es útil para obtener una calificación al responder la forma, lo que puede ser útil para auditorías u otros fines de evaluación. Para configurar la ponderación, siga los siguientes pasos:

  1. Habilite la opción de la configuración de la ponderación en `Opciones Generales <#ponderacion-conf>`_ :octicon:`report;1em;sd-text-info` y seleccione el método de ponderación.
  2. Seleccione ``Configuración de la ponderación`` del campo.
  3. Elija la respuesta en el selector correspondiente.
  4. Especifique el puntaje (si seleccionó por puntos) en el recuadro.
  5. Haga clic en ``Agregar opción``. La respuesta aparecerá en el recuadro inferior. 
  6. Presione ``Guardar``.

  .. note:: Repita el proceso según el número de respuestas del campo.

  .. image:: /imgs/Formas/Formas9.png

.. dropdown:: Configuración de la notificación

  La configuración de correo electrónico permite establecer y personalizar cómo se gestionan y entregan los correos electrónicos para notificar al destinatario según se responda la forma.

  .. seealso:: Para personalizar el envío de un correo electrónico de acuerdo a una acción más específica, puede crear un flujo de trabajo personalizado. Consulte la sección `enviar correo <#personalizar-envio-correo>`_ :octicon:`report;1em;sd-text-info` para mas detalles.

  Para acceder y realizar la configuración necesaria, consulte las siguientes pestañas:

  1. Seleccione ``Configuración de Email``.

  .. image:: /imgs/Formas/Formas109.png

  .. tab-set::

    .. tab-item:: De

        En este apartado, configure al remitente. 
        
        Haga clic en el selector y elija la opción según lo requiera, teniendo en cuenta la siguiente información:

        .. list-table::
          :widths: 30 70
          :header-rows: 1
          :align: left

          * - Campo
            - Descripción
          * - Dueño de la forma
            - Usuario que creó la forma.
          * - Dueño de la cuenta
            - Propietario de la cuenta.
          * - Usuarios que contestan
            - Usuarios que responden el formulario.
          * - Usuario que creó el registro
            - Usuarios que creó el registro.
          * - Conexión del registro
            - Usuario que no pertenece a la misma cuenta padre pero tiene acceso a visualizar el registro.
          * - Email personalizado
            - Si elige esta opción, ingrese el correo electrónico.

        .. image:: /imgs/Formas/Formas7.png

    .. tab-item:: Para

        En este apartado, configure a los destinatarios que recibirán la notificación cuando se seleccione una opción del campo de respuesta múltiple. Siga los siguientes pasos:

        1. Seleccione la opción del campo para la cual se enviará la notificación y presione ``Agregar opción``. Para eliminar una opción, presione el botón ``x``.
        2. Si necesita notificar a un usuario específico de su empresa, ingrese el nombre o correo del destinatario y presione ``Enter``.

        .. note:: Al ingresar el nombre, Linkaform proporcionará coincidencias automáticamente. Si el usuario de su interés tiene un a cuenta vigente, aparecerá en la lista desplegable. De lo contrario, no se mostrará ninguna sugerencia.

        3. Si lo requiere, puede seleccionar una opción determinada. Si elige una opción de este campo, oprima el botón ``Agregar`` cada vez que seleccione una opción. Para eliminar alguna opción, oprima el icono ``x``.

        .. list-table::
          :widths: 30 70
          :header-rows: 1
          :align: left

          * - Campo
            - Descripción
          * - Dueño de la forma
            - Usuario que creó la forma.
          * - Dueño de la cuenta
            - Propietario de la cuenta.
          * - Usuarios que contestan
            - Usuarios que responden el formulario.

        4. Seleccione una acción al editar un registro.
        5. Active la opción ``Adjuntar PDF`` si necesita enviar el registro en un documento PDF y seleccione una plantilla.
          
        .. seealso::  Por defecto, la lista de opciones contienen plantillas genéricas que se adaptan a cualquier formulario. Si necesita un documento personalizado, consulte la documentación sobre :ref:`doc-pdfs` :octicon:`report;1em;sd-text-info`

        6. Active la opción ``Adjuntar imagen de compañía`` para que el PDF contenga el logo de su empresa.
        7. Active la opción ``Enviar adjuntos`` si necesita incluir algunos campos de su interés.

        .. image:: /imgs/Formas/Formas117.png

    .. tab-item:: Asunto

        En este apartado, defina el asunto que mostrará el correo. 
        
        En la parte inferior, Linkaform permite utilizar metadatos y campos de la forma para personalizar el asunto. 
        
        Para seleccionar un metadato o campo, elija y haga clic en ``Agregar``. Al hacerlo, aparecerá el **metadato** o el ``id`` correspondiente al **campo** seleccionado.

        .. admonition:: Ejemplo
            :class: pied-piper

            En este ejemplo, ``{{record.form.name}}`` es el metadato que muestra el nombre de la forma.

            .. image:: /imgs/Formas/Formas111.png

    .. tab-item:: Cuerpo

        En este apartado, defina el cuerpo del correo, que es útil para agregar una descripción más detallada y extensa. 

        De manera similar al caso anterior, utilice **metadatos** y/o **campos** de la forma para personalizar el cuerpo, seleccionando y haciendo clic en ``Agregar``.

        .. admonition:: Ejemplo
            :class: pied-piper

            En este ejemplo, ``{{record.answers.65a72ad10e0c..}}`` representa los identificadores únicos de los campos asociados al formulario. Observe la diferencia entre un metadato y un campo.

            .. image:: /imgs/Formas/Formas112.png


    .. tab-item:: Vista previa

        En vista previa, podrá revisar el resultado final de las configuraciones que realizó anteriormente.

        Al estar seguro de sus cambios, seleccione ``Guardar``.
                  
        .. image:: /imgs/Formas/Formas113.png

.. _campo-numerico:

Campo número
^^^^^^^^^^^^

Los campos numéricos se utilizan para recopilar información numérica. Considere las siguientes configuraciones que comparten:

- Revise y si es necesario, configure la `ponderacion <#pond>`_ :octicon:`report;1em;sd-text-info` del campo.
        
- Si requiere, habilite la `configuración de Email <#configuracion>`_ :octicon:`report;1em;sd-text-info` en el campo email.

- Establezca parámetros de rango de mínimos y máximos en las ``Propiedades`` del campo.
    
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

.. attention:: Esta opción está disponible unicamente para formas. 

Para utilizarlo, siga estos pasos:

1. Agregue el campo.
2. Asigne un nombre con el título del campo.
3. Guarde la forma en su totalidad.

.. important:: Guardar el formulario permitirá habilitar la opción ``Editar``.

4. Seleccione ``Editar`` (se mostrará una plantilla en blanco).
5. Coloque los campos que formarán parte de este grupo repetitivo (son los mismos vistos en esta sección, excepto los grupos repetitivos).

.. image:: /imgs/Formas/Formas13.jpg

Campo geolocalización
^^^^^^^^^^^^^^^^^^^^^

El campo de geolocalización se utiliza para incluir la ubicación geográfica en el registro capturado. Este campo es editable, por lo que podrá modificarla según sea necesario.

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

        **Cantidad de imágenes:** Mínimo 0, Máximo 10.

        **Seleccionar imágenes de:** Cámara, Galería, Dibujar. Las opciones activadas serán las permitidas para este campo.

        **Configuración de campos** contiene las siguientes opciones:

        - **Agregar a la imagen:** Permite incluir los parámetros de geolocalización (ubicación) en la que se tomó o agregó la foto, así como la fecha de captura.
        - **Campos:** Permite incluir campos correspondientes de la forma o catálogo para agregarlos impresos en esa imagen. Simplemente teclee el título del campo y Linkaform lo sugerirá; presione ``Enter`` y se agregará.
        - **Nombre de archivo:** Permite incluir metadatos correspondientes a ese registro en el nombre de archivo o puede introducir un texto para que se imprima en la imagen.
        - **Configurar marca de agua:** Habilitar esta opción permite definir el color, tamaño y la posición de la marca de agua en la foto donde desea que aparezca impresa la información.

Campo documentos
^^^^^^^^^^^^^^^^

Este campo permite agregar diferentes tipos de archivos en el momento de la captura y/o edición del registro.

.. image:: /imgs/Formas/Formas16.jpg
    :height: 150px
    :width: 700px

Del mismo modo que el campo fotografías, puede configurar los parámetros en `conf <#config>`_ :octicon:`report;1em;sd-text-info`. Sin embargo, aquí tiene la posibilidad de seleccionar qué tipo de archivos son permitidos.

.. image:: /imgs/Formas/Formas16.1.1.png

Campo firma
^^^^^^^^^^^

Este tipo de campo permite a los usuarios firmar digitalmente, es útil en situaciones donde se requiere una confirmación o autorización.

Si se contesta o edita el formulario o catálogo desde la aplicación web, simplemente podrán utilizar el teclado. Por otro lado, al utilizar dispositivos móviles, podrán dibujar su firma.

.. image:: /imgs/Formas/Formas16.1.png
    :height: 150px
    :width: 700px

.. important:: Al momento de responder o editar, la firma se guardará y tratará como un archivo de tipo imagen.

.. _campo-catalogo:

Campo catálogo
^^^^^^^^^^^^^^

Un campo de tipo catálogo permite consultar los registros almacenados en la misma.

.. seealso:: consulte :ref:`catalogo` :octicon:`report;1em;sd-text-info` para más detalles. 

Para utilizar un catálogo, siga los siguientes pasos:

1. Cree un catálogo.

.. seealso:: consulte :ref:`crear-catalogo` :octicon:`report;1em;sd-text-info`.

2. Agregue el campo catálogo.
3. Asigne un nombre al campo catálogo.
4. Ingrese el nombre del catálogo previamente preparado en el recuadro vacío. Linkaform sugerirá automáticamente el catálogo correspondiente.

.. warning:: Dentro de una forma, no es posible utilizar el mismo catálogo más de una vez.

5. Guarde la forma o el catálogo en su totalidad.
6. Presione el botón ``Editar`` para personalizar los campos del catálogo. Consulte el siguiente desplegable para más detalles.

.. image:: /imgs/Formas/Formas17.png

.. dropdown:: Editar
  
    En la interfaz de edición, podrá configurar los siguientes apartados: 

    .. tab-set::

      .. tab-item:: Filtros

          Los filtros permiten que la forma muestre únicamente los registros que cumplan con los criterios seleccionados.

          .. image:: /imgs/Formas/Formas17.1.png
          
          .. seealso:: Consulte :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` para crear y guardar filtros.

      .. tab-item:: Editar

          La opción ``Editar`` permite seleccionar los campos del catálogo que desea mostrar en la forma. Es decir, aunque el catálogo tenga 10 campos, en la forma solo visualizará las que haya seleccionado.

          .. image:: /imgs/Formas/Formas17.2.1.png

          Al seleccionar los campos, podrá observarlos en la interfaz de edición. Considere las siguientes opciones:

          - **Solo lectura:** Al activar esta opción, el campo solo será visible. El usuario al capturar información no podrá seleccionarlo. 

          .. admonition:: Ejemplo
              :class: pied-piper
                
              Por ejemplo, en el catálogo ``Tiendas``, se incluyen los campos de tipo texto ``Tienda`` y ``Cadena`` con la opción de lectura deshabilitada. Al ejecutarlo en el formulario, permitirá al usuario seleccionar estos campos. En cambio, los campos ``Determinante`` y ``Dirección``, al estar habilitados, no podrán ser seleccionados, pero con los dos campos anteriores permitirán el autorellenado.

          - **Requerido:** Al activar esta opción, se obliga a seleccionar un dato, garantizando que la información no se envíe hasta que se complete el campo. 

          - **Ayuda:** Habilita una opción de texto adicional en el campo como referencia a la respuesta que se solicita.

          .. image:: /imgs/Formas/Formas17.2.2.png

          En **Propiedades** ubicada debajo del campo, puede habilitar la lectura de código de barras. Esto aplica para campos en los que su información corresponda a alguna etiqueta. 
          
          También, puede establecer el **Tipo** para que haga la lectura directa o búsqueda de la información en la base de datos.

          .. image:: /imgs/Formas/Formas18.jpg
            
          .. important:: Para organizar los campos seleccionados; simplemente haga clic en el campo y arrástralo a la posición deseada.

      .. tab-item:: Geocerca

          Esta funcionalidad permite dar de alta ubicaciones mediante coordenadas GPS. 
          
          Al habilitarse, deberá definir la distancia de referencia permitida de las coordenadas y solo así se mostrará la información si se encuentra en el rango de metros configurado.

          .. image:: /imgs/Formas/Formas17.3.png

          Al tener tus configuraciones listas, presione ``Guardar`` y regrese presionando ``Cerrar``.

.. dropdown:: Relacionar

  Relacionar un catálogo con otro catálogo se refiere al proceso de establecer una conexión o vínculo entre dos catálogos diferentes, permitiendo que los registros de uno puedan ser utilizados o referenciados en el otro. 

  Para que esta relación funcione, ambos catálogos deben compartir un identificador común que los conecte.

.. _configurar-correo-email:

Configuración de Email
----------------------

La configuración de correo electrónico permite establecer y personalizar cómo se gestionan y entregan los correos electrónicos para notificar al destinatario según se responda la forma.

.. seealso:: Para personalizar el envío de un correo electrónico de acuerdo a una acción más específica, puede crear un flujo de trabajo personalizado. Consulte la sección `enviar correo <#personalizar-envio-correo>`_ :octicon:`report;1em;sd-text-info` para mas detalles.

Para acceder y realizar la configuración necesaria, consulte las siguientes pestañas:

1. Seleccione ``Configuración de Email``.

.. image:: /imgs/Formas/Formas109.png

.. tab-set::

  .. tab-item:: De

      En este apartado, configure al remitente. Haga clic en el campo y seleccione el remitente deseado.

      .. list-table::
        :widths: 30 70
        :header-rows: 1
        :align: left

        * - Campo
          - Descripción
        * - Dueño de la forma
          - Usuario que creó la forma.
        * - Dueño de la cuenta
          - Propietario de la cuenta.
        * - Usuarios que contestan
          - Usuarios que responden el formulario.
        * - Usuario que creó el registro
          - Usuarios que creó el registro.
        * - Conexión del registro
          - Usuario que no pertenece a la misma cuenta padre pero tiene acceso a visualizar el registro.
        * - Email personalizado
          - Si elige esta opción, ingrese el correo electrónico.
        * - Respuesta a campo de correo
          - La dirección de correo electrónico proporcionada en un campo email del formulario.

      .. image:: /imgs/Formas/Formas7.png

  .. tab-item:: Para

      En este apartado, configure al destinatario y las opciones de envío de los registros. Siga los siguientes pasos:

      1. Si necesita notificar a un usuario específico de su empresa, ingrese el nombre o correo del destinatario y presione ``Enter``.

      .. note:: Al ingresar el nombre, Linkaform proporcionará coincidencias automáticamente. Si el usuario de su interés tiene una cuenta vigente, aparecerá en la lista desplegable. De lo contrario, no se mostrará ninguna sugerencia.

      2. Si lo requiere, puede seleccionar una opción determinada en el campo ``Enviar A``. Si elige una opción de este campo, oprima el botón ``Agregar`` cada vez que seleccione una opción. Para eliminar alguna opción, oprima el icono ``x``.
      
      .. list-table::
        :widths: 30 70
        :header-rows: 1
        :align: left

        * - Campo
          - Descripción
        * - Dueño de la forma
          - Usuario que creó la forma.
        * - Dueño de la cuenta
          - Propietario de la cuenta.
        * - Usuarios que contestan
          - Usuarios que responden el formulario.
        * - Usuario que creó el registro
          - Usuarios que creó el registro.
        * - Conexión del registro
          - Usuario que no pertenece a la misma cuenta padre pero tiene acceso a visualizar el registro.
        * - Respuesta a campo de correo
          - La dirección de correo electrónico proporcionada en un campo email del formulario.

      3. Seleccione una acción al editar un registro.
      4. Active la opción ``Adjuntar PDF`` si necesita enviar el registro en un documento PDF y seleccione una plantilla.
      
      .. seealso::  Por defecto, la lista de opciones contienen plantillas genéricas que se adaptan a cualquier formulario. Si necesita un documento personalizado, consulte la documentación sobre :ref:`doc-pdfs` :octicon:`report;1em;sd-text-info`
 
      5. Active la opción ``Adjuntar imagen de compañía`` para que el PDF contenga el logo de su empresa.
      6. Active la opción ``Enviar adjuntos`` si necesita incluir algunos campos de su interés.

      .. image:: /imgs/Formas/Formas110.png

  .. tab-item:: Asunto

      En este apartado, defina el asunto que mostrará el correo. En la parte inferior, Linkaform permite utilizar metadatos y campos de la forma para personalizar el asunto. 
      
      Para seleccionar un metadato o campo, elija y haga clic en ``Agregar``. Al hacerlo, aparecerá el **metadato** o el ``id`` correspondiente al **campo** seleccionado.

      .. admonition:: Ejemplo
          :class: pied-piper

          En este ejemplo, ``{{record.form.name}}`` es el metadato que muestra el nombre de la forma.

          .. image:: /imgs/Formas/Formas111.png

  .. tab-item:: Cuerpo

      Este apartado es para definir el cuerpo del correo. El cuerpo de un correo es útil para agregar una descripción más detallada y extensa. 
      
      De manera similar al caso anterior, puede utilizar **metadatos** y **campos** de la forma para personalizar el cuerpo. 
      
      Simplemente seleccione el **metadato** o el **campo** deseado y haga clic en ``Agregar``.

      .. admonition:: Ejemplo
          :class: pied-piper

          En este ejemplo, ``{{record.answers.65a72ad10e0c..}}`` representa los identificadores únicos de los campos asociados al formulario. Observe la diferencia entre un metadato y un campo.

          .. image:: /imgs/Formas/Formas112.png
            
  .. tab-item:: Vista previa

      En vista previa, podrá revisar el resultado final de las configuraciones que realizó anteriormente.

      Al estar seguro de sus cambios, seleccione ``Guardar``.
                
      .. image:: /imgs/Formas/Formas113.png

.. LIGAS DE INTERÉS EXTERNO 

.. |app| raw:: html

    <a href="https://app.linkaform.com/" target="_blank">app.linkaform.com</a>

.. |iniciar-sesion| raw:: html

    <a href="https://app.linkaform.com/" target="_blank">Inicie sesión</a>