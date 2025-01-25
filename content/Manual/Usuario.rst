=================================
MANUAL DE IMPLEMENTACIÓN DE SOTER
=================================

Este manual tiene como objetivo guiar en la configuración de las formas y catálogos necesarios para el funcionamiento de **Soter**. Aunque existen otros catálogos y formas dentro de la plataforma, este manual se centrará exclusivamente en los elementos necesarios para comenzar a utilizar el sistema. Los demás catálogos y formas se presentan solo para su referencia, pero no forman parte de la configuración inicial requerida.

**Carpeta: Base**
=================

En esta carpeta se configuran catálogos y formas, como la información sobre compañías, contactos y otros elementos generales. 

.. image:: /imgs/Manual/Manual1.png

Forma: ``Contactos``
--------------------

La forma ofrece una funcionalidad similar a la de la lista de contactos en un teléfono, permitiendo almacenar y gestionar la información de contacto de personas y empresas.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
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

        .. hint:: Ingrese la dirección o las coordenadas en la barra de búsqueda y linkaform mostrará las coincidencias disponibles para la ubicación proporcionada.

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

        .. important:: Cuando crea un registro en la forma, automáticamente se crea un registro sincronizado en el catálogo **Contacto**.

5. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

**Carpeta: Ubicaciones**
========================

La carpeta **Ubicaciones** almacena información sobre las distintas plantas o sucursales de la compañía y las áreas asociadas dentro de ellas. En este carpeta se trabajan dos formas:  

.. image:: /imgs/Manual/Manual10.png

Forma: ``Ubicación``  
--------------------

Esta forma permite registrar múltiples ubicaciones, útil para administrar diversas sucursales pertenecientes a una misma empresa.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Ubicaciones**, ubicado en la carpeta ``Ubicaciones``.
3. Responda la forma según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual11.png

    .. grid-item-card:: 
        :columns: 6

        - **Ubicación**: Nombre descriptivo de la ubicación.
        - **Contacto**: Dirección de la ubicación (catálogo **Contacto** de la carpeta ``Base``).

.. important:: Los datos ingresados en esta forma se sincronizan automáticamente con el catálogo **Ubicación**. 

    Cualquier modificación realizada en esta forma se reflejará automáticamente en el catálogo.

Forma: ``Áreas de las Ubicaciones``
----------------------------------------------- 

Esta forma permite definir las áreas que estarán asociadas a cada ubicación.  

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Areas de las Ubicaciones**, ubicado en la carpeta ``Ubicaciones``.
3. Responda la forma según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        - **Nombre del Área**: Nombre descriptivo del área dentro de la ubicación.
        - **Ubicación**: Ubicación a la que pertenece el área (catálogo **Ubicaciones**).
        - **Tipo de Área**: Tipo al que pertenece el área (catálogo **Tipo de Areas**).
        - **Dirección**: Dirección del área dentro de la ubicación (catálogo **Contacto** de la carpeta ``Base``).
        - **Estatus del Área**: Estado actual del área (``abierta``, ``cerrada``, ``clausurada``, en ``mantenimiento``, ``disponible``, ``ocupada``).
        - **Estatus**: Estado administrativo del área (``activa`` o ``inactiva``).
        - **QR Área**: Código QR asociado al área para su identificación y acceso.

        .. note:: El código QR es generado automáticamente por un script interno de **LinkaForm**, por lo que no será necesario cargar ninguna imagen relacionada con el QR.

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual12.png

.. important:: Los datos registrados en esta forma se sincronizan con los catálogos **Areas de las Ubicaciones** y **Areas de las Ubicaciones Salidas**. 
    
    Cualquier modificación realizada en esta forma se reflejará automáticamente en las mismas.

.. admonition:: Ejemplo
    :class: pied-piper

    Cuando registre una nueva área dentro de una ubicación, es posible que no cuente con una dirección específica. En tal caso, utilice la dirección de la ubicación general. 
    
    Sin embargo, para ubicaciones que no se encuentran físicamente dentro del edificio pero forman parte de la misma instalación, utilice una dirección específica. Por ejemplo:

    Para casetas de vigilancia, que se encuentran en diferentes puntos fuera de la instalación, asegúrese de asignar una dirección específica para cada una. Observe la siguiente imagen.

    .. image:: /imgs/Modulos/Ubicaciones/Ubicaciones13.png
        :width: 650px

**Carpeta: RecursosHumanos**
============================

En esta carpeta se centraliza la información de los empleados que forman parte de las compañías registradas.

.. image:: /imgs/Manual/Manual4.png

Forma: ``Empleados``
--------------------

Esta forma permite registrar y gestionar los datos personales y laborales de los empleados. Esto incluye información básica y detalles necesarios para su identificación y asignación dentro de **Soter**.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Empleados**, ubicado en la carpeta ``RecursosHumanos``.
3. Responda la forma:

.. warning:: La forma incluye varios campos que pueden ser útiles para un registro más completo de los empleados. 
    
    Sin embargo, tenga en cuenta que las siguientes secciones y campos de la forma son obligatorios.  

Datos Generales
^^^^^^^^^^^^^^^

Información básica del empleado.  

- **Nombre completo**: Registro del nombre completo del empleado, utilizado para su identificación dentro del sistema.
- **Fotografía**: Imagen reciente del empleado que facilita su identificación visual en la plataforma.
- **Estatus dentro de la empresa**: Situación laboral del empleado dentro de la compañía (``Activo`` o ``Inactivo``). 
- **Estatus de disponibilidad**: Define el estado del empleado para asignaciones específicas o actividades relacionadas (``Disponible`` o ``No disponible``)
        
.. image:: /imgs/Manual/Manual5.png

Domicilio
^^^^^^^^^

Dirección física del empleado.

.. note:: La información mostrada es la registrada en la forma **Contacto**.  

.. image:: /imgs/Manual/Manual6.png

Detalles de Contratación
^^^^^^^^^^^^^^^^^^^^^^^^

Información relacionada con la contratación del empleado.  

.. note:: Los datos se obtienen del catálogo **Compañía**.  

.. image:: /imgs/Manual/Manual7.png

Puesto de trabajo
^^^^^^^^^^^^^^^^^

Descripción del ambiente laboral en el que se desarrollará el empleado.  

.. image:: /imgs/Manual/Manual8.png

LINK
^^^^

Información sobre los accesos a **Soter**:  

- **ID de usuario**: Clave única de la cuenta del empleado en la plataforma **LinkaForm**.  
- **Username**: Nombre de usuario único del empleado en la plataforma **LinkaForm**.  
- **Email**: Correo electrónico único del empleado en la plataforma **LinkaForm**.  

.. important:: Los empleados que utilicen **Soter** deberán tener una cuenta vigente en **Linkaform**.

.. image:: /imgs/Manual/Manual9.png

Forma: ``Configuración Areas y Empleados``
------------------------------------------

Esta forma permite asociar empleados a áreas específicas dentro de una ubicación, facilitando la gestión y asignación de responsabilidades o accesos según el área designada.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Configuracion Areas y Empleados**, ubicado en la carpeta ``RecursosHumanos > Config``.
3. Responda la forma según los siguientes campos:

- **Empleado**: Seleccione el empleado que será asignado al área (catálogo **Empleados** ubicado en la carpeta ``Empleados``).  
- **Áreas**: Especifique las áreas asignadas al empleado (catálogo **Areas de las Ubicaciones** de la carpeta ``Empleados``).
- **Marcar como**: Indica si la asignación será **Default** (predeterminada) o **Normal**.  
- **Comentario**: Observaciones o notas relacionadas con la asignación.  

.. image:: /imgs/Manual/Manual13.png

.. warning:: Esta configuración es un paso importante para el correcto uso de **Soter**. La ubicación y las áreas asignadas determinarán la información que podrá consultar el empleado.
    
.. important:: Los datos registrados en esta forma se sincronizan con los catálogos **Configuracion Areas y Empleados** y **Configuracion Areas y Empleados Apoyo**. 
    
    Cualquier modificación realizada en esta forma se reflejará automáticamente en las mismas.

**Carpeta: Contratistas**
=========================

Forma: ``Contratistas``
-----------------------

Esta forma permite registrar a las empresas contratistas, incluyendo información básica, contactos clave y documentos necesarios para su identificación.

Al registrar un nuevo contratista, se inicia un proceso colaborativo en el que el contratista tiene la responsabilidad de completar su solicitud, actualizando datos y documentos conforme sea necesario. A continuación, se presenta un diagrama para facilitar su comprensión:

.. image:: /imgs/Manual/Manual14.png
    :align: center

.. important:: Envíe el manual del proceso de alta de contratistas a la empresa contratista que será registrado para que pueda completar su solicitud.

**Pasos para la configuración**:

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Contratistas**, ubicado en la carpeta ``Contratistas``.
3. Responda la forma según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        **Generales**

        - **Razón Social**: Nombre legal del contratista.
        - **RFC/RUC**: Registro Federal de Contribuyentes.
        - **Email contratista**
        
        .. warning:: Asegúrese de que el correo electrónico del contratista sea válido, ya que será utilizado para comunicaciones críticas relacionadas con su solicitud y otros procesos importantes.

        - **Teléfono contratista**
        - **Servicios a Prestar**: Servicios que el contratista ofrecerá.
        - **Estatus Solicitud**: Estado actual del proceso de solicitud del contratista (``Alta``, ``Completada``, ``En proceso`` , ``Revisión``).
        - **Estatus del Contratista**: Estado operativo del contratista dentro de la empresa (``Documentación``, ``Autorizado``, ``No autorizado``)

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual15.png

    .. grid-item-card:: 
        :columns: 12

        **Administración**

        Especificación sobre actividades de alto riesgo.

        .. image:: /imgs/Manual/Manual16.png

.. note:: 

    El contratista puede completar su solicitud en varias etapas, actualizando su registro conforme realice cambios. 

    La responsabilidad será de la forma revisar cada actualización y cambiar el estatus según lo requiera. 

    Una vez que la solicitud esté completamente llena, deberá proceder con la autorización dentro de la empresa, actualizando el estatus del contratista a ``Autorizado``.

.. warning:: Solo los trabajadores de contratistas con estado ``Autorizado`` podrán ser considerados como candidatos para convertirse en visitas autorizadas y generar pases de entrada que les permitan acceder a las instalaciones de la compañía.

.. important:: Los datos ingresados en esta forma se sincronizan automáticamente con el catálogo **Contratistas**. 

    Cualquier modificación realizada en esta forma se reflejará automáticamente en el catálogo.

**Carpeta: Seguridad**
======================

A través de las formas incluidas en esta carpeta, se configuran aspectos críticos como visitas, permisos, accesos y la asignación de roles específicos para el personal de seguridad. Este manual se enfocará en la configuración de las siguientes formas:  

- **Configuración Accesos**  
- **Configuración Módulo Seguridad**  
- **Puestos de Guardias**
- **Visita Autorizada** 
- **Pase de Entrada**

Forma: ``Configuración Accesos``
--------------------------------

Esta forma permite configurar y asignar el acceso del usuario o grupo a las distintas funcionalidades de la aplicación **Soter**.

**Pasos para la configuración**:  

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Configuracion Accesos**, ubicado en la carpeta ``Seguridad > Config``.
3. Responda la forma según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual20.png

    .. grid-item-card:: 
        :columns: 6

        - **Usuario**: Empleado que tendrá acceso a las funcionalidades.
        - **Grupos**: Grupo de empleados.
        - **Menus**: Funcionalidades específicas de la aplicación a las que el empleado tendrá acceso.

.. warning::
    
    - Puede asignar funcionalidades a un **usuario individual** o a **grupos**.
    - Si asigna funcionalidades a un grupo, **todos los miembros de dicho grupo** tendrán acceso a las mismas funcionalidades seleccionadas.
    - Asegúrese de que las funcionalidades asignadas correspondan al rol del empleado y no generen conflictos con otros accesos previamente otorgados.
    - Los cambios realizados en esta forma tendrán un impacto inmediato en las funcionalidades disponibles para el usuario dentro de la aplicación.
    - Es recomendable revisar y actualizar los permisos regularmente para mantener la seguridad y funcionalidad del sistema.

Forma: ``Configuración Módulo Seguridad``
-----------------------------------------

Esta forma permite establecer los requisitos necesarios para regular el acceso a las instalaciones. Es utilizada principalmente para asegurar que los requisitos de seguridad definidos sean obligatorios durante el proceso de emisión de pases.

**Pasos para la configuración**:  

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Configuracion Modulo Seguridad**, ubicado en la carpeta ``Seguridad > Config``.
3. Responda la forma según los siguientes campos:

- **Ubicación**: Ubicación donde se aplicarán los requisitos de seguridad.
- **Datos requeridos**: Datos que serán obligatorios para emitir los pases de entrada.

.. image:: /imgs/Manual/Manual21.png

.. hint:: Si cuenta con múltiples sucursales o instalaciones, asegúrese de agregar las configuraciones correspondientes para cada una.

Forma: ``Visita Autorizada``
----------------------------

Esta forma permite registrar al personal de empresas contratistas que realizarán servicios a beneficio de la empresa. 

La principal función de la forma es gestionar el estado de los empleados (visitas) en relación con la empresa, facilitando la identificación de aquellos que podrían convertirse en visitantes recurrentes.

.. important::

    - Antes de registrar a un empleado del contratista, asegúrese de recopilar toda la información relevante de la persona, similar a los datos que se solicitan a un trabajador antes de su contratación. Esto permite verificar su identidad antes de permitir el acceso a la ubicación.

    - Solo los visitantes registrados como **Autorizados** pueden recibir un pase de entrada (invitación para acceder a la empresa).

    - Una vez que la visita esté registrada y autorizada, podrá generar un pase de entrada y especificar las áreas a las que el visitante tendrá permitido acceder.

**Pasos para la configuración**:  

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Visita Autorizada**, ubicado en la carpeta ``Seguridad``.
3. Responda la forma según los siguientes campos:

.. grid:: 2
    :gutter: 0

    .. grid-item-card:: 
        :columns: 6

        - **Nombre de la Visita**: Nombre completo del visitante (Campo obligatorio).
        - **CURP**: Clave Única de Registro de Población.
        - **Email**: Dirección de correo electrónico de la visita.   
        - **Teléfono**: Número de teléfono de la visita.
        - **Foto**: Imagen de la persona que realiza la visita.
        - **Identificación**: Documento de identificación oficial.
        - **Contratista**: Empresa a la que pertenece el visitante (catálogo **Contratistas**).

        .. note:: Si la visita no corresponde a un trabajador de un contratista, deje este campo en blanco.

        - **Estatus**: Estado actual de la visita (**Autorizado**, **Boletinado**, **Baja**, etc.).

    .. grid-item-card:: 
        :columns: 6

        .. image:: /imgs/Manual/Manual22.png
            :width: 390px

Una vez que el estatus de la visita esté **autorizado**, el contratista asociado será notificado por correo electrónico, informándole que su empleado es candidato para recibir pases de entrada. Observe el siguiente correo de ejemplo:

.. image:: /imgs/Modulos/Accesos/Accesos45.png
    :width: 500px

.. warning:: 

    - Registrar una visita **no** significa que el visitante tenga acceso inmediato a la ubicación o a todas las áreas. 

    - Esta forma actúa como un filtro de seguridad, diferenciando a los visitantes autorizados de aquellos que tienen acceso restringido o que han sido boletinados. También permite actualizar el estado de visitantes que previamente eran regulares pero han sido dados de baja.

.. note:: Cada empleado registrado se asigna a un perfil, el cual define los requerimientos y restricciones obligatorios que deben cumplirse para que pueda desempeñar su función dentro de la ubicación.

    La asignación de perfiles será abordada en secciones posteriores. Por el momento, enfoque el proceso en registrar y autorizar las visitas necesarias.

.. important:: 

    Los datos ingresados en esta forma se sincronizan automáticamente con el catálogo **Visita Autorizada**.

    Cualquier modificación realizada en esta forma se reflejará automáticamente en el catálogo.