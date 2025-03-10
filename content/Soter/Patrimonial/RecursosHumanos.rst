=========================
Carpeta: Recursos Humanos
=========================

La carpeta agrupa las formas necesarias para gestionar la información del personal. Aquí podrá registrar empleados, definir departamentos y asignar puestos.

.. image:: /imgs/Manual/Manual4.png
    :width: 880px

Catálogo: ``Departamentos``
---------------------------

El catálogo contiene posibles departamentos dentro de una empresa.

.. important:: Este catálogo incluye registros predefinidos. No es necesario agregar nuevos registros a menos que requiera un departamento que no se encuentre disponible.  

**Verificación de registros**  

Verifique que el catálogo tenga registros siguiendo estos pasos:

1. Navegue al apartado **Catálogos > Registros de catálogo** en el menú lateral.  
2. En el selector de catálogos, ingrese **Departamentos** e identifique los registros existentes.

.. image:: /imgs/Modulos/Empleados/Empleados3.png

.. attention:: Si no encuentra registros o necesita agregar más, repórtelo con **soporte técnico** o realice una **importación masiva** desde el catálogo. Para ello, descargue la plantilla de registros |departamentos| :octicon:`report;1em;sd-text-info`.

    Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para más detalles.

Catálogo: ``Puestos``
---------------------

El catálogo contiene posibles puestos dentro de una empresa.

.. important:: Este catálogo incluye registros predefinidos. No es necesario agregar nuevos registros a menos que requiera un puesto que no se encuentre disponible.  
 
**Verificación de registros**  

Confirme la existencia de registros en el catálogo con los siguientes pasos:

1. Navegue al apartado **Catálogos > Registros de catálogo** en el menú lateral.  
2. En el selector de catálogos, ingrese **Puestos** e identifique los registros existentes.

.. image:: /imgs/Modulos/Empleados/Empleados5.png

.. attention:: Si no encuentra registros o necesita agregar más, repórtelo con **soporte técnico** o realice una **importación masiva** desde el catálogo. Para ello, descargue la plantilla de registros |puestos| :octicon:`report;1em;sd-text-info`.

    Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para más detalles.


.. _soter-departamentos-puestos:

Forma: ``Configuración de Departamentos y Puestos``
---------------------------------------------------

Esta forma le permite relacionar departamentos con puestos, según el contexto. 

.. important:: Esta forma incluye registros predefinidos. Por lo que no es necesario agregar nuevos registros a menos que requiera una nueva configuración entre departamentos y puestos.

**Verificación de registros**  

Asegúrese de que la forma contenga registros. Para verificarlo, siga estos pasos:  

1. Navegue al apartado **Registros > Registros** en el menú lateral.  
2. En el buscador, ingrese **Configuracion de Departamentos y Puestos** e identifique los registros existentes.

.. image:: /imgs/Manual/Manual29.png

.. attention:: Si no encuentra registros o necesita agregar más, repórtelo con **soporte técnico** o realice una importación a través de la :ref:`carga-universal-xlsx` :octicon:`report;1em;sd-text-info`. Para ello, descargue la plantilla de registros |config-departamentos-puestos| :octicon:`report;1em;sd-text-info`.

.. dropdown:: Revisar Sincronización

    Al crear un registro en esta forma, se ejecuta automáticamente el script **sync conf departamentos puestos**, que sincroniza la información con el catálogo correspondiente.  

    Es importante que revise que la sincronización se haya realizado correctamente. Para hacerlo, puede hacerlo de las siguientes maneras:  

    **Log de Flujo**  

    1. Después de enviar el registro, presione **Log de flujo**, ubicado en el detalle del registro.  
    2. En la ventana emergente del **Log de flujo**, verifique que la acción
       **script sync conf departamentos puestos** tenga el estatus **Exitoso**.  

    **Registros de Catálogo**  

    1. Navegue al apartado de **Catálogos > Registros de catálogo** en el menú lateral.  
    2. En el selector de catálogos, ingrese **Configuración de Departamentos y Puestos**.  
    3. Identifique los registro mediante el nombre del departamento o puesto.

    .. attention:: Si la sincronización no se realizó correctamente, repórtelo a soporte técnico.

.. _soter-usuarios:

Forma: ``Usuarios``
-------------------

La forma **Usuarios** es una de las más importantes dentro de **Soter**, ya que permite registrar y gestionar las credenciales de acceso de los usuarios que utilizarán la plataforma.  

.. warning:: Los usuarios que utilicen **Soter** deberán tener una cuenta vigente en **Linkaform**.
    
    Para más detalles sobre como crear usuarios activos en Linkaform consulte; :ref:`usuarios-admin` :octicon:`report;1em;sd-text-info` para más detalles. 

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Usuarios**, ubicado en la carpeta ``RecursosHumanos``.
3. Responda la forma según los siguientes campos:

   - **Nombre**: Ingrese el nombre completo del usuario.  
   - **ID de usuario**: Clave única de la cuenta del empleado en la plataforma **LinkaForm**.  
   - **Username**: Nombre de usuario único del empleado en la plataforma **LinkaForm**.  
   - **Email**: Correo electrónico único del empleado en la plataforma **LinkaForm**.  
   - **Estatus**: Define si el usuario está **activo** (puede acceder a la plataforma) o **inactivo** (sin acceso hasta nueva autorización).  

   .. image:: /imgs/Manual/Manual36.png

   .. seealso:: Consulte; :ref:`informacion-usuario-administrador` :octicon:`report;1em;sd-text-info` para obtener los datos de los usuarios.

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

.. seealso:: Si necesita agregar múltiples registros, considere realizar una carga masiva a las formas. Consulte; :ref:`carga-universal-xlsx` :octicon:`report;1em;sd-text-info` para más detalles.

.. dropdown:: Revisar Sincronización

    Una vez creado o actualizado un usuario, la información se sincroniza automáticamente con el catálogo **Usuarios**.  

    Para verificar que la sincronización se haya realizado correctamente:  

    **Log de Flujo**  

    1. Acceda al **Log de Flujo** desde el detalle del registro.  
    2. Verifique que la acción **Sync records** tenga el estatus **Exitoso**.  
    3. Consulte el catálogo **Usuarios** y confirme que el registro ha sido creado o actualizado correctamente.

    **Registros de Catálogo**  

    1. Navegue al apartado de **Catálogos > Registros de catálogo** en el menú lateral.  
    2. En el selector de catálogos, ingrese **Usuarios**.  
    3. Identifique los registro mediante el nombre del departamento o puesto.

    .. attention:: Si la sincronización no se realizó correctamente, repórtelo a soporte técnico.

.. _soter-empleados:

Forma: ``Empleados``
--------------------

Esta forma permite registrar y gestionar los datos personales y laborales de los empleados. Esto incluye información básica y detalles necesarios para su identificación y asignación dentro de **Soter**.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Empleados**, ubicado en la carpeta ``RecursosHumanos``.
3. Responda la forma:

.. warning:: La forma incluye varios campos que pueden ser útiles para un registro más completo de los empleados.
    
    Sin embargo, tenga en cuenta que las siguientes secciones y campos de la forma son obligatorios. 

.. grid:: 1
    :gutter: 0
    :padding: 0
    :margin: 0

    .. grid-item-card:: 
        :columns: 12
        
        **Datos Generales**

        Información básica del empleado.  

        - **Nombre completo**: Registro del nombre completo del empleado, utilizado para su identificación dentro del sistema (mismo nombre que el registrado en :ref:`soter-usuarios` :octicon:`report;1em;sd-text-info`).
        - **Fotografía**: Imagen reciente del empleado que facilita su identificación visual en la plataforma.
        - **Estatus dentro de la empresa**: Situación laboral del empleado dentro de la compañía (``Activo`` o ``Inactivo``). 
        - **Estatus de disponibilidad**: Define el estado del empleado para asignaciones específicas o actividades relacionadas (``Disponible`` o ``No disponible``)
                
        .. image:: /imgs/Manual/Manual5.png

        **Domicilio**

        Dirección física del empleado.

        .. seealso:: Consulte la :ref:`soter-contacto` :octicon:`report;1em;sd-text-info` para más detalles. 

        .. image:: /imgs/Manual/Manual6.png

        **Detalles de Contratación**

        Información relacionada con la contratación del empleado.  

        .. seealso:: Consulte el :ref:`soter-compania` :octicon:`report;1em;sd-text-info` para más detalles. 

        .. image:: /imgs/Manual/Manual7.png

        **Puesto de trabajo**

        Descripción del ambiente laboral en el que se desarrollará el empleado.

        .. seealso:: Consulte la :ref:`soter-departamentos-puestos` :octicon:`report;1em;sd-text-info` para más detalles. 

        .. image:: /imgs/Manual/Manual8.png

        **LINK**

        Información sobre los accesos a **Soter**.

        .. seealso:: Consulte la :ref:`soter-usuarios` :octicon:`report;1em;sd-text-info` para más detalles. 

        .. image:: /imgs/Manual/Manual33.png

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

.. seealso:: Si necesita agregar varios registros a la vez, realice una :ref:`carga-universal-xlsx` :octicon:`report;1em;sd-text-info` en las formas. Descargue la plantilla de registros |empleados| :octicon:`report;1em;sd-text-info`.

.. dropdown:: Revisar Sincronización 

    Los datos ingresados en la forma se sincronizan automáticamente con los catálogos **Empleados** y **Empleados Jefes Directos**.  

    Para verificar la sincronización:  

    **Log de Flujo**

    1. Tras enviar el registro, presione **Log de Flujo** en el detalle del registro.  
    2. Confirme que las acciones **Sync Catalogs Records** y **Form to catalog** tengan el estatus **Exitoso**.  
    3. Use la opción **Registro de catálogo** para revisar la información.  

    **Registros de Catálogo**

    1. Vaya a **Catálogos > Registros de catálogo**.  
    2. Seleccione **Empleados** o **Empleados Jefes Directos**.  
    3. Busque el registro por su nombre o algún otro identificador.  

    .. attention:: Si la sincronización no se realizó correctamente, repórtelo a soporte técnico.

Forma: ``Configuración Areas y Empleados``
------------------------------------------

Esta forma permite asociar empleados a áreas específicas dentro de una ubicación.

.. warning:: Esta configuración es un paso importante para el correcto uso de **Soter** y aplica únicamente a los empleados encargados del control de casetas de vigilancia y seguridad.

    La ubicación y las áreas asignadas definirán la información que el personal de seguridad podrá consultar.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Configuracion Areas y Empleados**, ubicado en la carpeta ``RecursosHumanos > Config``.
3. Responda la forma según los siguientes campos:

   - **Empleado**: Seleccione el empleado que será asignado al área.

   .. seealso:: Consulte la :ref:`soter-empleados` :octicon:`report;1em;sd-text-info` para más detalles. 

   - **Áreas**: Especifique las áreas asignadas al empleado.
   
   .. seealso:: Consulte la :ref:`soter-areas-de-las-ubicaciones` :octicon:`report;1em;sd-text-info` para más detalles. 
   
   - **Marcar como**: Indica si la asignación será **Default** (predeterminada) o **Normal**.  
   
   - **Comentario**: Observaciones o notas relacionadas con la asignación.  

   .. image:: /imgs/Manual/Manual30.png
        :width: 600px

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

.. seealso:: Si necesita agregar varios registros a la vez, realice una :ref:`carga-universal-xlsx` :octicon:`report;1em;sd-text-info` en las formas. Descargue la plantilla de registros |config-areas-empleados| :octicon:`report;1em;sd-text-info`.

.. dropdown:: Revisar Sincronización

    Al crear un registro en esta forma, se ejecuta automáticamente el script **Sync Catalogo Areas y Empleados**, que sincroniza la información con los catálogos correspondientes.  

    Es importante que revise que la sincronización se haya realizado correctamente. Para hacerlo, puede hacerlo de las siguientes maneras:  

    **Log de Flujo**  

    1. Después de enviar el registro, presione **Log de flujo**, ubicado en el detalle del registro.  
    2. En la ventana emergente del **Log de flujo**, verifique que la acción **Sync Catalogo Areas y Empleados** tenga el estatus **Exitoso**.  

    **Registros de Catálogo**  

    1. Navegue al apartado de **Catálogos > Registros de catálogo** en el menú lateral.  
    2. En el selector de catálogos, ingrese **Configuracion Areas y Empleados** o **Configuracion Areas y Empleados Apoyo**. 
    3. Identifique los registro mediante el nombre o algún otro identificador.

    .. attention:: Si la sincronización no se realizó correctamente, repórtelo a soporte técnico.

.. |departamentos| raw:: html

    <a href="https://f001.backblazeb2.com/file/app-linkaform/public-client-126/71202/6650c41a967ad190e6a76dd3/67a1a5eb7a6874a8e6f17c9d.xlsx" target="_blank">aquí</a>

.. |puestos| raw:: html

    <a href="https://f001.backblazeb2.com/file/app-linkaform/public-client-126/71202/6650c41a967ad190e6a76dd3/67a1a5ec7a6874a8e6f17c9e.xlsx" target="_blank">aquí</a>

.. |config-departamentos-puestos| raw:: html

    <a href="https://f001.backblazeb2.com/file/app-linkaform/public-client-126/71202/6650c41a967ad190e6a76dd3/67a2563b714d580a4ff17c7b.xlsx" target="_blank">aquí</a>

.. |empleados| raw:: html

    <a href="https://f001.backblazeb2.com/file/app-linkaform/public-client-126/71202/6650c41a967ad190e6a76dd3/67a2936a790af66dc4d4dc24.xls" target="_blank">aquí</a>

.. |config-areas-empleados| raw:: html

    <a href="https://f001.backblazeb2.com/file/app-linkaform/public-client-126/71202/6650c41a967ad190e6a76dd3/67a29626ea531157bc19588b.xlsx" target="_blank">aquí</a>

