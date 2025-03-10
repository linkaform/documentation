=============
Carpeta: Base
=============

La carpeta contiene formas y catálogos para registrar compañías, definir contactos y administrar otros elementos básicos de **Soter**.

.. image:: /imgs/Manual/Manual1.png

.. _soter-compania:

Catalogo: ``Compañía``
----------------------

Este catálogo es utilizada para registrar y gestionar las compañías dentro de **Soter**, utilizada para establecer la relación entre empleados y sus respectivas empresas. 

**Pasos para la configuración**:

1. Navegue a ``Catálogos > Catálogos`` en el menú lateral.
2. Identifique el catálogo **Compañia**, ubicado en la carpeta ``Base``.
3. Responda la forma según los siguientes campos:

   - **Compañía**: Nombre de la compañía.

   .. image:: /imgs/Manual/Manual24.png

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura del catálogo. 

.. _soter-contacto:

Forma: ``Contacto``
-------------------

La forma ofrece una funcionalidad similar a la de la lista de contactos en un teléfono, permitiendo almacenar y gestionar la información de contacto de personas, empresas y direcciones individuales.

**Pasos para la configuración**:

1. Navegue a ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Contacto**, ubicado en la carpeta ``Base``.
3. Responda la forma según los siguientes campos:

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

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

.. seealso:: Si necesita agregar múltiples registros, considere realizar una carga masiva a las formas. Consulte; :ref:`carga-universal-xlsx` :octicon:`report;1em;sd-text-info` para más detalles.

.. dropdown:: Revisar Sincronización

    Cuando se crea un registro en la forma, automáticamente se genera un registro sincronizado en el catálogo **Contacto**.  

    Es importante verificar que esta sincronización se haya realizado correctamente. Para ello, puede hacerlo de dos maneras:  

    **Log de Flujo**  

    1. Una vez enviado el registro, presione el botón verde **Log de flujo**, ubicado en la parte derecha de la pantalla en el detalle del registro.  
    2. En la ventana emergente del **Log de flujo**, verifique que la acción **Sync Catalogs Records** tenga el estatus **Exitoso**.  
    3. Presione la opción **Registro de catálogo** para ser redirigido al registro correspondiente. Allí podrá confirmar si la información está completa y coincide con la ingresada en la forma.  

    .. image:: /imgs/Manual/Manual26.png

    **Registros de Catálogo**  

    1. Navegue al apartado de **Catálogos > Registros de catálogo** en el menú lateral.  
    2. En el selector de catálogos, ingrese **Contacto**.  
    3. Identifique el registro mediante el nombre de la dirección u otro identificador relevante.  

    .. image:: /imgs/Manual/Manual25.png  


    .. attention:: Si la sincronización no se realizó correctamente, repórtelo a soporte técnico.
