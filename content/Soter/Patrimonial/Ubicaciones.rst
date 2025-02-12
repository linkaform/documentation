====================
Carpeta: Ubicaciones
====================

La carpeta contiene las formas necesarias para registrar y gestionar los lugares físicos donde opera la compañía. Aquí podrá agregar nuevas ubicaciones y definir sus áreas.

.. image:: /imgs/Manual/Manual10.png
    :width: 880px

.. _soter-ubicaciones:

Forma: ``Ubicaciones``  
----------------------

Esta forma permite registrar múltiples sucursales, plantas o edificios físicos pertenecientes a una misma compañía.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Ubicaciones**, ubicado en la carpeta ``Ubicaciones``.
3. Responda la forma según los siguientes campos:

   - **Ubicación**: Nombre descriptivo de la ubicación.
   - **Contacto**: Dirección de la ubicación 

   .. seealso:: Consulte la :ref:`soter-contacto` :octicon:`report;1em;sd-text-info` para más detalles. 

   .. image:: /imgs/Manual/Manual11.png
        :width: 400px

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

.. seealso:: Si necesita agregar múltiples registros, considere realizar una carga universal desde las formas. Para más detalles, consulte la sección **Carga Universal**.

.. dropdown:: Revisar Sincronización

    El registro ingresado en la forma se sincronizan automáticamente con el catálogo **Ubicaciones**.  

    Es importante verificar que la sincronización se haya realizado correctamente. Para hacerlo, puede seguir los mismos pasos descritos anteriormente:  

    **Log de Flujo**  

    1. Después de enviar el registro, presione **Log de flujo**, ubicado en el detalle del registro.  
    2. En la ventana emergente del **Log de flujo**, verifique que la acción **Sync Catalogs Records** tenga el estatus **Exitoso**.  
    3. Presione la opción **Registro de catálogo** para ser redirigido al catálogo correspondiente y confirme que la información se haya registrado correctamente.  

    **Registros de Catálogo**  

    Siga estos pasos:  

    1. Navegue al apartado de **Catálogos > Registros de catálogo** en el menú lateral.  
    2. En el selector de catálogos, ingrese **Ubicaciones**.  
    3. Identifique el registro mediante el nombre de la ubicación u otro identificador relevante.

    .. attention:: Si la sincronización no se realizó correctamente, repórtelo a soporte técnico.

.. _soter-tipo-areas:

Catálogo: ``Tipo de Areas``
---------------------------

Este catálogo clasifica los distintos tipos de áreas dentro de una ubicación.  

.. important:: Este catálogo incluye registros predefinidos. No es necesario agregar nuevos registros a menos que requiera un tipo de área que no se encuentre disponible.  

**Verificación de registros**  

Confirme que el catálogo no esté vacía mediante los siguientes pasos:

1. Navegue al apartado **Catálogos > Registros de catálogo** en el menú lateral.  
2. En el selector de catálogos, ingrese **Tipo de Áreas** e identifique los registros existentes.

.. image:: /imgs/Manual/Manual28.png

.. attention:: Si no encuentra registros o necesita agregar más, repórtelo con **soporte técnico** o realice una **importación masiva** desde el catálogo. Para ello, descargue la plantilla de registros |Tipo_area| :octicon:`report;1em;sd-text-info`.

    Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para más detalles.

.. _soter-areas-de-las-ubicaciones:

Forma: ``Áreas de las Ubicaciones``
-----------------------------------

Esta forma permite definir las áreas que estarán asociadas a cada ubicación.  

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Areas de las Ubicaciones**, ubicado en la carpeta ``Ubicaciones``.
3. Responda la forma según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual12.png

    .. grid-item-card:: 
        :columns: 6

        - **Nombre del Área**: Nombre descriptivo del área dentro de la ubicación.
        - **Ubicación**: Ubicación a la que pertenece el área.

        .. seealso:: Consulte la :ref:`soter-ubicaciones` :octicon:`report;1em;sd-text-info` para más detalles. 

        - **Tipo de Área**: Tipo al que pertenece el área.

        .. seealso:: Consulte el :ref:`soter-tipo-areas` :octicon:`report;1em;sd-text-info` para más detalles. 

        - **Dirección**: Dirección del área dentro de la ubicación.

        .. seealso:: Consulte la :ref:`soter-contacto` :octicon:`report;1em;sd-text-info` para más detalles. 

        - **Estatus del Área**: Estado actual del área (``abierta``, ``cerrada``, ``clausurada``, en ``mantenimiento``, ``disponible``, ``ocupada``).

    .. grid-item-card:: 
        :columns: 12

        - **Estatus**: Estado administrativo del área (``activa`` o ``inactiva``).
        - **QR Área**: Código QR asociado al área para su identificación y acceso.

        .. attention:: El código QR se genera automáticamente mediante un script interno de **LinkaForm**, por lo que no es necesario cargar ninguna imagen. Si el QR no aparece tras enviar la respuesta, repórtelo a soporte técnico.

        .. admonition:: Ejemplo
            :class: pied-piper

            Cuando registre una nueva área dentro de una ubicación, es posible que no cuente con una dirección específica. En tal caso, utilice la dirección de la ubicación general. 
            
            Sin embargo, para ubicaciones que no se encuentran físicamente dentro del edificio pero forman parte de la misma instalación, utilice una dirección específica. Por ejemplo:

            Supongamos que un edificio cuenta con cuatro casetas de vigilancia ubicadas en distintos puntos: la principal en la calle X, otra en la calle Y, una más en la calle V y otra en la calle Z. Para casetas de vigilancia situadas en diferentes accesos fuera de la instalación, considere asignar una dirección específica a cada una. Consulte la siguiente imagen.

            .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones13.png
                :width: 650px

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

.. seealso:: Si requiere agregar varios registros a la vez, utilice la opción de Carga Universal en las formas. Consulte la sección correspondiente para más información.

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


.. |Tipo_area| raw:: html

    <a href="https://f001.backblazeb2.com/file/app-linkaform/public-client-126/71202/6650c41a967ad190e6a76dd3/679d63b5a697fa99533eaf85.xlsx" target="_blank">aquí</a>