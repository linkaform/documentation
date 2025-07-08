.. _doc-configuracion-rondines:

Guía rápida: Configuración de Rondines
======================================

.. toctree::
    :maxdepth: 1
    :titlesonly:

Este manual es una guía rápida para configurar la funcionalidad de **Rondines**. Incluye ejemplos, tutoriales y soluciones a problemas comunes, todo pensado para facilitar su implementación y uso.

La configuración de rondines consiste en registrar digitalmente las ubicaciones y las áreas físicas dentro de ellas, asignar a cada área un identificador único en forma de código QR para facilitar su reconocimiento, y dejar listos los rondines programados para que puedan ser ejecutados desde la aplicación móvil. 

A continuación, consulte el siguiente diagrama de casos de uso para entender el flujo completo:

.. image:: /imgs/Rondines/Rondines1.png
   :width: 400px

Registro de ubicaciones
-----------------------

El registro de ubicaciones consiste en dar de alta las sucursales, plantas o edificios físicos que forman parte de una misma compañía.

.. warning:: Se recomienda utilizar la plataforma web para realizar esta configuración. Si aún no está familiarizado con la plataforma, consulte: :ref:`doc-usuario` :octicon:`report;1em;sd-text-info`.

Para registrar las ubicaciones, siga los siguientes pasos:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. (Opcional) Si desea agregar una dirección a la ubicación o a las áreas, busque la forma **Contacto**, ubicada en la carpeta ``Base``, y llénela según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        - **Nombre de Dirección**: Alias con el que desea guardar al contacto.
        - **Imagen**: Imagen descriptiva del contacto (opcionalmente).
        - **Dirección**: Ubicación específica del lugar (número, calle, etc.).

        - **Geolocalización**: Ubicación del contacto.

        .. hint:: Ingrese la dirección en la barra de búsqueda y observe las coincidencias disponibles para la ubicación ingresada.

        .. image:: /imgs/Manual/Manual3.png

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual2.png

    .. grid-item-card:: 
        :columns: 12

        **Tipo de Contacto**
                        
        - **Empresa**: Dirección de la ubicación de una empresa.
        - **Persona**: Dirección personal de la residencia del usuario.
        - **Dirección**: Dirección única sobre una ubicación en concreto.

        .. image:: /imgs/Modulos/Base/Base25.png

        **Status**
                            
        - **Activo**: El contacto es vigente y utilizado.
        - **Inactivo**: El contacto no es utilizado.

        .. image:: /imgs/Modulos/Base/Base26.png


3. Identifique la forma **Ubicaciones**, ubicado en la carpeta ``Ubicaciones``, y Responda según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual11.png

    .. grid-item-card:: 
        :columns: 6

        - **Ubicación**: Nombre descriptivo de la ubicación.
        - **Contacto**: Dirección de la ubicación 

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la información. 

.. seealso:: Si necesita agregar varios registros a la vez, realice una :ref:`carga-universal-xlsx` :octicon:`report;1em;sd-text-info` en las formas.
    
Registro de áreas
-----------------

El registro de areas involucra definir los espacios físicos que se van a inspeccionar durante los rondines (ej. pasillos, almacenes, accesos, etc.).

.. warning:: Se recomienda utilizar la plataforma web para realizar esta configuración. Si aún no está familiarizado con la plataforma, consulte: :ref:`doc-usuario` :octicon:`report;1em;sd-text-info`.

Para registrar las areas, siga los siguientes pasos:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Areas de las Ubicaciones**, ubicado en la carpeta ``Ubicaciones``.
3. Responda la forma según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Rondines/Rondines2.png

    .. grid-item-card:: 
        :columns: 6

        - **Nombre del Área**: Nombre descriptivo del área dentro de la ubicación.
        - **Ubicación**: Ubicación a la que pertenece el área.
        - **Tipo de Área**: Tipo al que pertenece el área.
        - **Dirección**: Dirección del área dentro de la ubicación.

        .. note:: Si no tiene dirección, utilice la de la ubicación.

        - **Estatus del Área**: Estado actual del área.
        - **Estatus**: Estado administrativo del área.

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la información. 

.. seealso:: Si necesita agregar varios registros a la vez, realice una :ref:`carga-universal-xlsx` :octicon:`report;1em;sd-text-info` en las formas.
    
.. dropdown:: Revisar Sincronización

    Los datos ingresados en la forma se sincronizan automáticamente con los catálogos **Áreas de las Ubicaciones** y **Áreas de las Ubicaciones Salidas**.  

    Para verificar la sincronización:  

    **Log de Flujo**

    1. Tras enviar el registro, presione **Log de Flujo** en el detalle del registro.  
    2. Confirme que las acciones **Sync Catalogs Records** y **Form to catalog** tengan el estatus **Exitoso**.  
    3. Use la opción **Registro de catálogo** para revisar la información.  

    **Registros de Catálogo**

    1. Vaya a **Catálogos > Registros de catálogo**.  
    2. Seleccione **Áreas de las Ubicaciones** o **Áreas de las Ubicaciones Salidas**.  
    3. Busque el registro por su nombre o identificador.  

    .. attention:: Si la sincronización no se realizó correctamente, repórtelo a soporte técnico.

Impresión de códigos QR
------------------------

Los código QR son etiquetas con un código único que identifica cada área física. Esto facilita su inspección durante los rondines.

Para imprimir los identificadores QR, siga los siguientes pasos:

1. Diríjase al apartado ``Formas > Mis Formas`` desde el menú lateral.
2. Identifique la forma **Impresion de QR**, ubicada en la carpeta ``Seguridad > Config``.
3. Complete el siguiente campo para generar los identificadores:

   - **Páginas a Imprimir**: Indique el número de páginas que necesita.

   .. image:: /imgs/Rondines/Rondines3.png

   .. note:: Cada pagina incluye 20 códigos QR,

4. Haga clic en el botón ``Mandar respuestas`` o use el botón flotante para enviar la información. 
5. En el detalle del registro, descargue el PDF con los QR generados desde la esquina superior derecha. 

   .. image:: /imgs/Rondines/Rondines4.png

6. Imprima los QR.

   .. hint::
         
      - Utilice impresoras láser o de buena resolución para evitar errores de escaneo.
      - Considere el uso de papel adhesivo, etiquetas térmicas o impresión en vinil si se colocarán en exteriores.
      - Proteja los códigos QR con mica o laminado si estarán expuestos a humedad, polvo o manipulación constante.
         
   .. warning:: Los QR recién impresos aún no están vinculados a ninguna área.

7. Coloque un código QR directamente en cada área física.

Asignación de identificador a área
----------------------------------

Asignar un identificador a un área consiste en vincular físicamente un código QR con dicho espacio. Esto permite que el área sea reconocida digitalmente durante los rondines.

.. warning:: Se recomienda utilizar la aplicación móvil para realizar esta configuración. Si aún no está familiarizado con la app, consulte: :ref:`doc-aplicacion-movil` :octicon:`report;1em;sd-text-info`.

Para asignar un qr a una area física, siga los siguientes pasos:

1. Abra la app e inicie sesión.
2. Seleccione la forma **Configuracion de Area**
3. Llene el formulario. Al hacerlo, observe que existen tres formas de operar, seleccionables en el campo **Tipo de movimiento**. Dependiendo de la opción elegida, se solicitarán distintos datos.

.. warning:: Antes de realizar esta asignación, asegúrese de haber colocado físicamente el código QR en el área correspondiente.

.. tab-set::

    .. tab-item:: 📸 Actualizar foto con escaneo de QR

      Este movimiento permite hacer un **registro desde cero**.

      .. grid:: 2
          :gutter: 0
      
          .. grid-item-card:: 
              :columns: 6

              1. Seleccione el tipo de movimiento ``Actualizar foto con escaneo de QR`` o presione el botón ``Scann``.
              2. Escanee el QR físico colocado en el área. 
              
              .. hint:: - Para escanear, utilice el botón con ícono de código de barras que aparece junto al campo. Esto abrirá la cámara de su dispositivo para leer el QR.
                - Si el QR es escaneado correctamente, podrá observar un código alfanumérico en el campo correspondiente. 

              .. important:: Para que las áreas estén disponibles durante los rondines, deben tener asignado el código alfanumérico. Este identificador es obligatorio y debe registrarse antes de realizar una inspección en cualquier área.

              3. Capture una **fotografía del área** (opcional pero recomendable).
              4. Agregue un **comentario descriptivo** (opcional).
              5. Envíe el registro para completar la asignación.

              .. note:: Este proceso debe repetirse para cada área involucrada en los rondines. Una vez que todas las áreas estén correctamente identificadas, estarán listas para integrarse en los recorridos de inspección.

          .. grid-item-card:: 
              :columns: 6

              .. image:: /imgs/Rondines/Rondines6.png
                  :alt: Escaneo y asignación inicial

    .. tab-item:: 🖼️ Actualizar foto con selección de nombre

      Este tipo de movimiento permite **reemplazar únicamente la fotografía** de un área que ya está registrada, sin cambiar el QR que tiene asignado.

      .. grid:: 2
          :gutter: 0
      
          .. grid-item-card:: 
              :columns: 6

              1. Seleccione el tipo de movimiento ``Actualizar foto con Seleccion de Nombre`` o presione el botón ``Seleccion``.
              2. Elija la ubicación donde se encuentra el área.
              3. Seleccione el area a la que se remplazará la imagen.

              .. warning:: Asegúrese de seleccionar correctamente el área, ya que no se realiza escaneo de QR en esta modalidad.

              4. Elimine la foto actual y tome una nueva fotografía.
              5. Agregue un **comentario descriptivo** (opcional).
              6. Envíe el registro para completar la asignación.

          .. grid-item-card:: 
              :columns: 6

              .. image:: /imgs/Rondines/Rondines7.png
                  :alt: Actualización de foto por selección

    .. tab-item:: ✅ Actualización de QR

      Este movimiento permite **reemplazar únicamente el código QR asignado** a un área específica, sin afectar la foto o comentarios anteriores.

      .. hint::  Utilice esta opción cuando sea necesario sustituir un QR dañado o perdido sin alterar la información visual del área.

      .. grid:: 2
          :gutter: 0
      
          .. grid-item-card:: 
              :columns: 6


              1. Seleccione el tipo de movimiento ``Actualizacion de QR`` o presione el botón ``Actualizar QR``.
              2. Elija la ubicación donde se encuentra el área.
              3. Seleccione el area al que se remplazará el código.
              4. Escanee el nuevo QR físico colocado en el área.
              
              .. hint:: 

                - Presiona el ícono de código de barras junto al campo para abrir la cámara.
                - Si el QR es escaneado correctamente, podrá observar un código alfanumérico en el campo correspondiente. 

              5. Agregue un **comentario descriptivo** (opcional).
              6. Envíe el registro para completar la asignación.

          .. grid-item-card:: 
              :columns: 6

              .. image:: /imgs/Rondines/Rondines8.png


4. Haga clic en el botón ``Mandar respuestas`` o use el botón flotante para enviar la información. 

Configuración del rondín
------------------------

Esta configuración permite programar recorridos, definir qué áreas deben inspeccionarse, establecer su frecuencia y asignarlos a grupos de usuarios responsables.

A continuación, consulte el diagrama de casos de uso para comprender el proceso:

.. image:: /imgs/Rondines/Rondines20.png

.. Supervisores o encargados de seguridad son quienes programan los rondines, seleccionan las áreas que deben inspeccionarse y determinan la recurrencia con la que deben ejecutarse.

.. warning:: Se recomienda utilizar la plataforma web para realizar esta configuración. Si aún no está familiarizado con la plataforma, consulte: :ref:`doc-usuario` :octicon:`report;1em;sd-text-info`.

.. important:: Asegúrese de que **todas las áreas cuenten con su código QR asignado** antes de programar rondines.

Para programar un rondín, siga los siguientes pasos:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Configuracion de Recorridos**, ubicado en la carpeta ``Seguridad > Config``.
3. Responda la forma según los siguientes campos:

.. tab-set::

    .. tab-item:: Datos del recorrido

        Esta sección permite definir la información básica del recorrido que se va a programar.

        .. grid:: 2
            :gutter: 0

            .. grid-item-card:: 
                :columns: 6

                - **Nombre del recorrido**: Título representativo del recorrido programado.
                - **Ubicación**: Lugar físico donde se ejecutará el rondín.
                - **Duración estimada**: Tiempo aproximado que tomará realizar el recorrido.
                - **Áreas**: Lista de todas las áreas que deben inspeccionarse durante el rondín.
                - **Grupo**: Grupo de usuarios al que se le asignará el recorrido.  

                .. important:: Por la rotación de turnos, los rondines se asignan a grupos dinámicos de usuarios en lugar de personas específicas. Así, cualquier miembro del grupo puede realizar el recorrido según el turno que le corresponda.
                .. .. note:: Todos los miembros recibirán la tarea en su bandeja de entrada (inbox).

            .. grid-item-card:: 
                :columns: 6

                .. image:: /imgs/Rondines/Rondines9.png

    .. tab-item:: Programación de recurrencia

        Esta sección permite definir la fecha, anticipación y frecuencia con la que debe ejecutarse el recorrido.
        
        **DATOS BASE**

        - **Fecha Primer Evento**: Fecha y hora en la que se ejecutará por primera vez el recorrido.  

          .. note:: A partir de esta fecha se programarán las siguientes tareas recurrentes.
                
          .. image:: /imgs/Rondines/Rondines10.png

        - **Programar con anticipación**: Seleccione ``Sí`` si se requiere que la notificación se envíe antes del evento, en el horario definido. En caso contrario, la tarea se asignará automáticamente 5 horas antes del evento.

          .. note:: La notificación se enviará al inbox del usuario. Si no está familiarizado con esta funcionalidad, consulte la sección :ref:`section-inbox` :octicon:`report;1em;sd-text-info`.
           
          - **Tiempo de anticipación**: Cantidad de tiempo con la que se enviará la tarea al inbox del usuario.
          - **Tiempo expresado en**: Seleccione entre minutos, horas, días, semanas o meses.
           
          .. image:: /imgs/Rondines/Rondines11.png

        - **Tiempo para ejecutar la tarea**: Límite que tendrá el usuario para completar la tarea desde que le sea asignada.

          .. note:: Funciona en bloques de 1 hora.
           
          - **Unidad de tiempo**: Indique si se mide en minutos, horas, días, semanas o meses.
           
          .. image:: /imgs/Rondines/Rondines12.png

        **TIPO DE EJECUCIÓN**

        - **La tarea es de**: 

          - **Única ocasión**: La tarea se ejecutará solo una vez.
          - **Cuenta con recurrencia**: La tarea se repetirá con una frecuencia definida.

          .. note:: Si selecciona **cuenta con recurrencia** Se habilitarán campos adicionales para personalizar el patrón de repetición.
           
          .. image:: /imgs/Rondines/Rondines13.png

        **REPETICIÓN ESTÁNDAR**

        - **Se repite cada**: Intervalo de repetición regular (hora, diario, semana, mes, año, configurable).

          .. note:: Si selecciona **configurable** Se habilitarán campos adicionales para personalizar el patrón de repetición.
           
          .. image:: /imgs/Rondines/Rondines14.png

        **REPETICIÓN CONFIGURABLE**

        Si desea definir un patrón más personalizado de recurrencia, complete los siguientes campos:

        - **Sucede**:

          - **Igual que la primera fecha**: La repetición se basará en la misma hora y día.
          - **Al principio del período**: La repetición se ejecutará al inicio del período seleccionado.

          .. image:: /imgs/Rondines/Rondines15.png

        - **La recurrencia sucede cada**: Unidad base sobre la que se construye el patrón.

          .. note:: Dependiendo de la opción seleccionada, podrá establecer el valor de repetición.

          .. image:: /imgs/Rondines/Rondines16.png

        **FECHA DE FINALIZACIÓN**

        - **¿La recurrencia tiene fecha final?**: Seleccione ``Sí`` si desea definir una fecha límite.
        - **Fecha final de recurrencia**: Último día en el que se ejecutará el recorrido.

          .. image:: /imgs/Rondines/Rondines17.png

4. Haga clic en el botón ``Mandar respuestas`` o utilice el botón flotante para enviar la información. ¡Listo! El rondín ha sido programado 🎉

🎉 ¡Felicidades! Ha concluido la configuración necesaria para programar un rondín.
Ahora puede comenzar a ejecutar inspecciones de forma ordenada y eficiente 🎊.