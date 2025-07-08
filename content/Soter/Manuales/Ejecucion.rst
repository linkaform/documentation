.. _doc-ejecucion-rondines:

Guía rápida: Ejecución Rondines
===============================

Este manual es una guía rápida para llevar a cabo la ejecución de **rondines**. Incluye instrucciones, ejemplos prácticos y soluciones a problemas comunes, todo enfocado en facilitar la realización de inspecciones desde la aplicación móvil.

.. note:: Antes de comenzar, es importante recordar lo siguiente:

  - Un **rondín** es una secuencia de inspecciones programadas que deben realizarse en ruta.
  - Una **inspección individual** ocurre cuando se escanea un área fuera de un rondín programado, permitiendo revisar espacios no contemplados previamente.

Este manual está dirigido al personal operativo encargado de realizar los recorridos en campo. A continuación, consulte el diagrama de casos de uso para comprender el proceso:

.. image:: /imgs/Rondines/Rondines21.png

.. warning:: Se recomienda utilizar la aplicación móvil para realizar esta configuración. Si aún no está familiarizado con la app, consulte: :ref:`doc-aplicacion-movil` :octicon:`report;1em;sd-text-info`.

Iniciar/Cerrar turno
--------------------

Para registrar el inicio y cierre de su turno de forma digital, siga los siguientes pasos:

1. Abra la aplicación móvil de LinkaForm.
2. Seleccione la forma **CheckIn Manual**.
3. Complete la forma con la información:

.. grid:: 2
    :gutter: 0

    .. grid-item-card::
      :columns: 6

      .. image:: /imgs/Rondines/Rondines22.png

    .. grid-item-card::
      :columns: 6

      - **Ubicación**: Seleccione la ubicación donde se realiza el turno.
      - **Área**: Indique el área específica (por ejemplo, caseta, acceso principal, etc.).
      - **Estatus**: Elija si desea **iniciar** o **cerrar** el turno.
      - **Fotografía**: Tome una fotografía de cuerpo completo. Este campo es obligatorio tanto al iniciar como al cerrar el turno.

      .. note:: Al cerrar el turno, no es necesario eliminar la foto anterior; simplemente añada una nueva.
      
      - **Comentarios**: Campo opcional para registrar observaciones relevantes al momento del cambio de turno.

      .. warning:: Al enviar el registro, el sistema guardará automáticamente su **nombre**, la **fecha** y la **hora** del envío (entrada o salida).
      
        Por ello, se recomienda tomar las precauciones necesarias para registrar el turno dentro del horario laboral establecido, ya que la **hora del registro será la que determine oficialmente el inicio o cierre del turno**.

4. Haga clic en el botón ``Enviar`` ubicado en la parte superior.

Ejecutar rondín
---------------

Para ejecutar un rondín, siga los pasos:

1. Abra la aplicación móvil de LinkaForm.
2. Seleccione la forma **Check Ubicaciones**.
3. Complete la forma con la información del recorrido.

.. grid:: 2
    :gutter: 0

    .. grid-item-card::
        :columns: 6

        - **Tag ID**: Escanee el código QR del área a inspeccionar.
        - **Evidencias**: Puede incluir fotos, documentos o imágenes capturadas durante la inspección.
        - **Comentarios generales**: Observaciones complementarias que no necesariamente son una incidencia.
        - **Acción al finalizar**:

          - **Continuar con el siguiente punto de inspección**: Esta opción indica que el rondín continúa con el siguiente punto programado.

            .. note:: Al seleccionar esta opción, cada punto inspeccionado se marcará automáticamente como **inspeccionado** dentro del recorrido. Cada área registrada queda almacenada en una bitácora.

                Si el área escaneada **no pertenece a un rondín programado** y se selecciona esta opción, el sistema registrará la inspección como **individual**, sin asociarla a ningún recorrido.

          - **Finalizar el rondín**: Utilice esta opción para cerrar el recorrido, incluso si no se inspeccionaron todas las áreas.
        
            .. note:: No es obligatorio cubrir todas las áreas ni seguir un orden específico. Al presionar **Finalizar el rondín**, el recorrido se da por concluido.

    .. grid-item-card::
        :columns: 6

        .. image:: /imgs/Rondines/Rondines18.png
            :height: 1200px

    .. grid-item-card::
        :columns: 6

        .. image:: /imgs/Rondines/Rondines19.png
            :height: 1000px
            
    .. grid-item-card::
        :columns: 6

        - **Incidencias**: Permite reportar eventos anómalos o situaciones relevantes observadas en el área (opcional):

          - **Tipo de incidente**
          - **Comentario** (opcional)
          - **Acción tomada**
          - **Evidencia** (foto o documento)

4. Haga clic en el botón ``Enviar`` ubicado en la parte superior.

   .. note:: Repita el proceso tantas veces como sea necesario, según la cantidad de áreas incluidas en el rondín.

Consultar bitácora de rondines
------------------------------

Cada vez que se ejecuta un rondín y se inspeccionan sus áreas, es posible consultar el historial completo en la **bitácora de rondines**. Ahí encontrará el detalle de todas las áreas inspeccionadas anteriormente, junto con la evidencia y los datos registrados.

.. warning:: Se recomienda utilizar la plataforma web para realizar esta configuración. Si aún no está familiarizado con la plataforma, consulte: :ref:`doc-usuario` :octicon:`report;1em;sd-text-info`.

Para revisar el detalle del rondin, siga los pasos:

1. Desde el menú lateral, diríjase a la sección ``Registros``.

.. warning:: De forma predeterminada, se mostrarán todos los registros almacenados en su cuenta.

2. Escriba y seleccione **Bitácora Rondines**. Aparecerán todos los registros de rondines ejecutados.

.. note:: LinkaForm le mostrará coincidencias en tiempo real según las formas disponibles en su cuenta.

3. Opcionalmente, aplique filtros según lo requiera.

.. seealso:: Consulte la sección de :ref:`crear-filtro-formas` :octicon:`report;1em;sd-text-info` para más detalles.

4. Identifique el registro de su interés. En las opciones de la fila, seleccione el ícono del **ojo** para visualizar directamente, o el ícono de **ventana** para abrirlo en una nueva pestaña.

.. image:: /imgs/Rondines/Rondines23.png

🎉 ¡Felicidades! Ahora ya sabe cómo iniciar y cerrar su turno correctamente, así como cómo llevar a cabo un rondín de forma estructurada desde la aplicación y consultar sus registros.
Con estos pasos, contribuye a mantener un control ordenado, seguro y confiable en cada recorrido.

