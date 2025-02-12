==================
Carpeta: Seguridad
==================

A través de las formas incluidas podrá gestionar permisos, definir roles y administrar los usuarios que interactúan con el sistema de seguridad.

Este manual se enfocará en la configuración de las siguientes formas:  

.. image:: /imgs/Manual/Manual34.png
    :align: Center

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

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

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

4. Presione el botón ``Mandar respuestas`` o el botón flotante de envío para finalizar la captura de la forma. 

.. hint:: Si cuenta con múltiples sucursales o instalaciones, asegúrese de agregar las configuraciones correspondientes para cada una.

Forma: ``Puestos de Guardias``
------------------------------

La forma permite configurar los puestos de seguridad, asignar responsabilidades y definir el alcance de sus funciones dentro de una o varias casetas de vigilancia en una ubicación. Es decir, permite determinar si un guardia, jefe, supervisor o inspector de seguridad puede desempeñar funciones de apoyo en otras casetas de seguridad, en caso de que la ubicación cuente con varias casetas.
 
.. important:: Esta configuración aplica para todo aquel personal de seguridad que trabajará dentro de casetas de seguridad e iniciaran turnos en las casetas correspondientes.

**Pasos para la configuración**:  

1. Navegue al apartado de formas seleccionando la opción ``Formas > Mis Formas`` en el menú lateral.
2. Identifique la forma **Puestos de Guardias**, ubicado en la carpeta ``Seguridad > Config``.
3. Responda la forma según los siguientes campos:

   - **Nombre del puesto**: Seleccione el nombre del puesto de seguridad

   - **Tipo de Guardia**

     Seleccione el rol del puesto según sus responsabilidades:

     - **Guardia Líder**: Actúa como el único responsable y líder de la caseta.
     - **Guardia de Apoyo**: Brinda asistencia a otras casetas de seguridad según sea necesario.

.. image:: /imgs/Manual/Manual23.png

4. Guarde el registro de la configuración presionando el botón **Guardar**.

   