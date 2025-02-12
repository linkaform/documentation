======
Fallas
======

La bitácora de **fallas** permite registrar y realizar un seguimiento de problemas técnicos o malfuncionamientos que ocurren en las instalaciones. 

.. attention:: A diferencia de los incidentes, las fallas requieren un proceso de resolución para poder ser cerradas, asegurando que los problemas sean atendidos y solucionados de manera adecuada.

En la bitácora de fallas, los registros se organizan según el estado, mostrando primero las fallas abiertas para una atención inmediata. La bitácora está organizada en varias columnas, donde:

- **Fecha y Hora**: Indica el momento en que se reportó la falla.
- **Estado**: Muestra el estado actual de la falla.

.. note:: 
    
    - **Abierto**: Pendiente de resolver.
    - **Cerrado**: Falla resuelta.

- **Ubicación**: Indica la ubicación donde ocurrió la falla.
- **Lugar de la falla**: Especifica la zona exacta dentro de la ubicación donde se presentó el problema.
- **Falla**: Tipo de problema o malfuncionamiento reportado.
- **Evidencia**: Fotografías o documentos que respalden la existencia de la falla y faciliten su comprensión para los responsables.
- **Comentarios**: Observaciones adicionales relacionadas con la falla, como detalles de su origen o posibles soluciones.
- **Reporta**: Guardia o persona que realizó el reporte de la falla.
- **Responsable**: Responsable para dar seguimiento a la falla y asegurar su solución.

.. image:: /imgs/Soter/Soter98.png
    :width: 850px

Nueva Falla
^^^^^^^^^^^

Para registrar una nueva falla en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Presione el botón azul ``+Nueva Falla`` ubicado en la esquina derecha de la bitácora. Se abrirá un modal para el registro de la nueva falla.
4. Complete los campos requeridos según corresponda:

- **Ubicación**: Seleccione la ubicación donde se ha presentado la falla.
- **Área**: Seleccione el área específica dentro de la ubicación donde ocurrió la falla.
- **Fecha**: Indique la fecha en la que se detectó la falla.
- **Hora**: Registre la hora exacta de la detección de la falla.
- **Falla**: Seleccione el tipo de falla de la lista predefinida. 
- **Objeto afectado**: Especifique el objeto que ha sido afectado por la falla (si aplica).

.. note:: Algunas fallas están relacionadas con objetos que afectan. Por ejemplo, la falla **Mal funcionamiento de equipos informáticos** puede afectar a un objeto específico como una laptop, servidor, etc.

- **Evidencia**: Adjunte fotografías u otros archivos visuales que muestren la falla detectada.
- **Documentación**: Adjunte documentos relevantes a la falla (manuales, informes técnicos, etc.).
- **Comentarios**: Agregue detalles adicionales que consideren importantes para el seguimiento de la falla.
- **Reporta**: Guardia o personal que está reportando la falla.
- **Responsable a solucionar**: Seleccione la persona encargada de resolver la falla.

5. Presione ``Registrar`` para finalizar el registro de la falla.

.. image:: /imgs/Soter/Soter99.png
    :width: 500px

Visualizar Falla
^^^^^^^^^^^^^^^^

Para consultar los detalles de una falla registrada en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Ubique la falla deseada.

.. note:: En caso de múltiples registros, utilice la barra de búsqueda de alguna columna.

4. Haga clic en el ícono de vista ubicado en la misma fila de la falla que desea revisar. Esto abrirá un modal que mostrará todos los detalles de la falla seleccionada.

.. image:: /imgs/Soter/Soter100.png

5. Una vez revisada la información, presione el botón ``Cerrar`` o el ícono ``X`` para salir de la ventana de detalles y regresar a la lista de la bitácora de fallas.

.. image:: /imgs/Soter/Soter101.png
    :width: 650px

Actualizar una falla
^^^^^^^^^^^^^^^^^^^^

Para modificar los detalles de una falla registrada en la bitácora, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Ubique la falla deseada.

.. note:: Si hay múltiples registros, la búsqueda por columna le permitirá encontrar la falla específica de manera más eficiente.

4. Haga clic en el ícono de edición ubicado en la misma fila de la falla que desea actualizar. Esto abrirá un modal con los detalles de la falla.

.. image:: /imgs/Soter/Soter102.png

5. Modifique los campos necesarios.

.. seealso:: Consulte los campos en la sección `nueva falla <#nueva-falla>`_ :octicon:`report;1em;sd-text-info`.

7. Una vez que haya realizado las modificaciones necesarias, presione el botón ``Actualizar`` para confirmar los cambios.

.. note:: Las actualizaciones se reflejarán de inmediato en la bitácora de fallas y estarán disponibles para todos los usuarios autorizados.

.. image:: /imgs/Soter/Soter103.png
    :width: 650px

Cerrar Falla
^^^^^^^^^^^^

A diferencia de los incidentes, las fallas requieren un proceso de seguimiento que implica la revisión del problema y la eventual resolución para poder marcar el registro como **Cerrado**. Esto asegura que todos los problemas técnicos sean debidamente atendidos y resueltos, manteniendo la operatividad de las instalaciones.

.. attention:: El cierre de una falla es un proceso que corresponde únicamente al responsable asignado al momento de crear la falla.

Para cerrar una falla registrada en la bitácora una vez que ha sido solucionada, siga los siguientes pasos:

1. Ubíquese en la interfaz de ``Incidentes`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**. 
3. Ubique la falla que desea cerrar.

.. note:: Si hay múltiples registros, la búsqueda por columna le permitirá encontrar la falla específica de manera más eficiente.

4. Haga clic en el ícono de **check** (palomita) ubicado en la misma fila de la falla que desea cerrar. Esto abrirá un modal.

.. image:: /imgs/Soter/Soter104.png

6. Complete los siguientes campos en el modal de cierre:

- **Folio del reporte de acción correctiva**: Ingrese el número de folio correspondiente a la acción correctiva que se llevó a cabo para solucionar la falla.
- **Comentario**: Agregue un comentario detallando la solución aplicada o cualquier observación relevante sobre el proceso de cierre.
- **Evidencia de solución**: Cargue fotografías que muestren la solución implementada y el estado actual de la situación.
- **Documento de solución**: Adjunte cualquier documento relevante que respalde la solución aplicada, como reportes de mantenimiento, certificados de reparación, etc.

7. Una vez que haya completado todos los campos, presione el botón ``Cerrar`` para finalizar el proceso.

.. image:: /imgs/Soter/Soter105.png
    :width: 650px

.. warning:: 
    
    - Una falla solo puede ser cerrada una vez. 
    - Al cerrar la falla, el registro se actualizará y pasará a la sección de **Resueltos**.
    - Una vez que una falla está marcada como resuelta, no podrá ser editada ni cerrada nuevamente.

    .. image:: /imgs/Soter/Soter106.png
        :width: 780px

Eliminar un Registro
^^^^^^^^^^^^^^^^^^^^

1. Ubíquese en la interfaz de ``Fallas`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas**.
3. Filtre las fallas según su estado (opcional).

.. note:: Si tiene muchos registros, utilice la barra de búsqueda para encontrar la falla específica que desea eliminar.

4. Ubique la falla deseada en la bitácora.
5. Seleccione el ícono de **Eliminar** (ícono de papelera) en la misma fila de la falla que desea eliminar.

.. image:: /imgs/Soter/Soter107.png

6. Presione el botón ``Confirmar`` en el modal de confirmación para proceder con la eliminación de la falla.

.. image:: /imgs/Soter/Soter108.png

Eliminar Múltiples Registros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Ubíquese en la interfaz de ``Fallas`` en el menú principal de Soter.
2. Asegúrese de estar en la pestaña **Fallas** para visualizar los registros.
3. Filtre las fallas según su estado (opcional).

.. note:: Utilice la barra de búsqueda si desea buscar y seleccionar registros específicos para eliminar.

4. Marque las casillas de verificación de las fallas que desea eliminar.
5. Presione el botón ``Eliminar`` ubicado en la esquina superior de la bitácora.

.. image:: /imgs/Soter/Soter109.png
    :width: 880px

6. En el modal de confirmación, presione ``Confirmar`` para eliminar las fallas seleccionadas.

.. image:: /imgs/Soter/Soter96.png
    :width: 500px

7. Presione ``OK`` para cerrar el modal de confirmación y regresar a la lista actualizada de fallas.

.. image:: /imgs/Soter/Soter110.png
    :width: 500px