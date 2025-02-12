===========
Incidencias
===========

La interfaz de **Incidencias** permite la gestión de incidentes o fallas que se presentan en las instalaciones.

.. warning:: Este apartado está disponible únicamente cuando haya iniciado su turno. Para acceder, presione la opción **Incidentes** ubicada en el menú superior.

   .. image:: /imgs/Soter/Soter71.png

Al acceder, encontrará la información de la caseta actual. Esta sección de la interfaz proporciona la situación actual sobre la caseta, dónde:

**Ubicación**

Permite confirmar la ubicación y caseta en la que se encuentra actualmente y cambiar entre diferentes ubicaciones o casetas dentro de la misma empresa.

.. attention:: Si cambia de ubicación o caseta, la información de la bitácora se actualizará automáticamente para reflejar los datos correspondientes a la nueva selección.

**Información**

Muestra tarjetas con información relevante y útil para el monitoreo de la situación actual, lo que facilita estar al tanto de pendientes y eventos importantes. Dependiendo de la sección, las tarjetas mostrarán la cantidad de diferentes elementos, como por ejemplo:

- **Fallas x día**: Muestra el número total de fallas reportadas en el día, lo que ayuda a identificar la frecuencia de problemas que ocurren en las instalaciones.
- **Fallas por resolver**: Indica la cantidad de fallas que aún no han sido atendidas o solucionadas, lo que permite priorizar y dar seguimiento a los problemas pendientes.

Si desea colapsar la información de la caseta para visualizar solo la información de la sección:

- Presione el ícono de flecha hacia abajo. El contenido se ocultará.
- Si desea volver a ver la información, presione el mismo ícono nuevamente.

.. image:: /imgs/Soter/Soter75.png
    :width: 880px

Bitácora de Incidentes
----------------------

Un incidente es cualquier evento inesperado que interrumpe una actividad o proceso, sin que necesariamente implique un mal funcionamiento de un equipo o sistema.

En la bitácora de incidentes, los registros se organizan según su nivel de prioridad, mostrando primero los incidentes **Críticos** para una atención inmediata. La bitácora está organizada en varias columnas, donde:

- **Ubicación**: Indica la ubicación donde ocurrió el incidente.
- **Lugar del incidente**: Especifica el área exacta dentro de la ubicación donde ocurrió el evento.
- **Fecha**: Registra la fecha en la que el incidente fue reportado.
- **Incidente**: Tipo de incidente reportado.
- **Evidencia**: Muestra fotografías o archivos subidos como evidencia del incidente.
- **Comentarios**: Detalles adicionales sobre el evento, proporcionando contexto o información relevante para del incidente.
- **Reporta**: Indica el nombre del guardia o personal que reportó el incidente.

.. image:: /imgs/Soter/Soter76V.png
    :width: 880px

Para filtrar los registros de los incidentes por prioridad:

1. Identifique el selector ubicado en la parte superior de la bitácora.
2. Seleccione la prioridad donde:

- **Crítico**: Incidentes con daños severos que tienen un alto impacto en las actividades o instalaciones.
- **Alta**: Incidentes que implican daños significativos, aunque no tan severos como los críticos.
- **Mediana**: Incidentes que presentan daños moderados y cuyo impacto es limitado.
- **Baja**: Incidentes con daños menores que no afectan de forma considerable las operaciones o instalaciones.

Los registros de la bitácora se actualizarán automáticamente para mostrar solo los incidentes de la prioridad seleccionada.

.. image:: /imgs/Soter/Soter72.png

.. _nuevo-incident:

Nuevo Incidente
^^^^^^^^^^^^^^^

.. attention:: En **Soter**, el levantamiento de un reporte para un incidente funciona como un registro de los eventos que afectan una actividad o proceso. Sin embargo, no incluye un mecanismo de seguimiento o cierre del incidente, lo que significa que el reporte se limita a documentar el evento sin un proceso adicional para su resolución o cierre.

Reportar un nuevo incidente es un proceso sencillo, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Presione el botón azul ``+Nuevo Incidente``, ubicado en la parte superior derecha de la bitácora. Esto abrirá el modal correspondiente.
3. Complete los campos, según lo requiera, donde:

- **Ubicación**: Seleccione la ubicación donde ocurrió el incidente.
- **Área**: Indique la zona específica dentro de la ubicación donde se produjo el incidente.

.. image:: /imgs/Soter/Soter76.png

- **Fecha**: Especifique la fecha exacta del incidente.
- **Hora**: Ingrese la hora en que ocurrió el incidente.

.. image:: /imgs/Soter/Soter77.png

- **Reporta**: Seleccione el guardia que reporta el incidente.

.. image:: /imgs/Soter/Soter78.png

- **Prioridad**: Seleccione entre baja, media, alta o crítica, según la gravedad del incidente.

.. image:: /imgs/Soter/Soter79.png

- **Incidencia**: Seleccione el tipo de incidente de la lista predefinida.

.. image:: /imgs/Soter/Soter80.png
    :width: 650px

.. note:: Al seleccionar la opción **Depósitos** como tipo de incidencia, se desplegarán dos campos adicionales relacionados con dinero, donde:

    - **Tipo de Depósito**: Especifique el tipo de depósito.
    - **Cantidad**: Ingrese el monto del depósito. Puede agregar más de un depósito y el sistema calculará el total.

    Esta selección es la única que modifica el contenido del modal.

    .. image:: /imgs/Soter/Soter74.png
        :width: 500px

- **Comentarios**: Agregue información adicional que pueda ser útil para entender la situación.

.. image:: /imgs/Soter/Soter81.png

- **Tipo de daño**: Seleccione si el daño fue a materiales o a personas.

.. image:: /imgs/Soter/Soter82.png

- **Daños**: Describa los daños causados.

.. image:: /imgs/Soter/Soter83.png

- **Evidencia**: Adjunte imágenes o videos que respalden el reporte.
- **Documentos**: Suba documentos adicionales si es necesario.

.. image:: /imgs/Soter/Soter84.png

- **Personas involucradas**: Ingrese el nombre completo de cada persona involucrada y seleccione si es un afectado o un testigo.

.. image:: /imgs/Soter/Soter85.png

.. note:: No hay un límite en la cantidad de personas que pueden ser agregadas como involucradas. Añada tantas como sea necesario para asegurar que todos los involucrados estén debidamente registrados.

- **Acciones tomadas**: Registre las medidas que se tomaron en respuesta al incidente, junto con el responsable de cada acción.

.. image:: /imgs/Soter/Soter86.png

4. Presione ``Crear`` para finalizar el registro.

Visualizar Incidente
^^^^^^^^^^^^^^^^^^^^

Para consultar los detalles de un incidente registrado en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique el incidente deseado.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar el incidente específico que desea revisar.

5. Haga clic en el ícono de vista ubicado en la misma fila del incidente que desea revisar. Esto abrirá un modal que mostrará todos los detalles del incidente seleccionado de forma completa.

.. image:: /imgs/Soter/Soter88.png

6. Una vez revisada la información, presione el botón de ``Cerrar`` o el ícono ``X`` para salir de la ventana de detalles y regresar a la lista de la bitácora de incidentes.

.. image:: /imgs/Soter/Soter89.gif

Actualizar Incidente
^^^^^^^^^^^^^^^^^^^^

Para actualizar la información de un incidente registrado en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique el incidente que desea actualizar.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar el incidente específico que desea modificar.

5. Haga clic en el ícono de **editar** ubicado en la misma fila del incidente. Esto abrirá un modal con todos los detalles del incidente en modo de edición.

.. image:: /imgs/Soter/Soter90.png

6. Realice los cambios necesarios en los campos que desee actualizar. 

.. seealso:: Consulte los campos en la sección `nuevo incidente <#nuevo-incident>`_ :octicon:`report;1em;sd-text-info`.

7. Una vez que haya realizado las modificaciones, presione el botón ``Actualizar`` para confirmar la información del incidente. Recibirá un mensaje de confirmación indicando que la información ha sido actualizada exitosamente.

.. image:: /imgs/Soter/Soter91.png
    :width: 500px

8. Presione el botón de ``OK`` para cerrar de la ventana y regresar a la lista de la bitácora de incidentes.

.. image:: /imgs/Soter/Soter92.png

Eliminar un Registro
^^^^^^^^^^^^^^^^^^^^

Para eliminar un incidente específico de la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique el incidente que desea eliminar.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar el incidente específico que desea eliminar.

5. Seleccione el icono **Eliminar** ubicado en la misma fila del incidente que desea borrar.

.. image:: /imgs/Soter/Soter93.png

6. Presione ``Confirmar`` para proceder con la eliminación del incidente. Recibirá un mensaje de confirmación indicando que el registro ha sido eliminado exitosamente.

.. image:: /imgs/Soter/Soter94.png
    :width: 500px

Eliminar Múltiples Registros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para eliminar varios incidentes al mismo tiempo de la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Incidencias**. Aquí se mostrarán todos los incidentes registrados, ordenados por prioridad.
3. Filtre los incidentes (opcional).

.. note:: Si desea ver incidentes de una prioridad específica (**Crítico**, **Alta**, **Mediana**, **Baja**), utilice el selector de prioridad en la parte superior de la bitácora.

4. Ubique los incidentes que desea eliminar.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna para encontrar los incidentes específicos que desea eliminar.

5. Seleccione las casillas de los registros que desea eliminar.
6. Presione el botón ``Eliminar`` ubicado en la esquina superior de la bitácora.

.. image:: /imgs/Soter/Soter95.png
    :width: 880px

7. Presione ``Confirmar`` para proceder con la eliminación de los registros seleccionados.

.. image:: /imgs/Soter/Soter96.png
    :width: 500px

8. Presione ``OK`` para cerrar el modal de confirmación y finalizar el proceso.

.. image:: /imgs/Soter/Soter97.png
    :width: 500px
