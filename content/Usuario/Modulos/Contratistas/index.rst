.. _doc-compania:

===================
Módulo Contratistas
===================

El **Módulo Compañía** proporciona los elementos base necesarios para gestionar y administrar la información de múltiples contratistas. Este módulo es importante para el :ref:`doc-accesos` :octicon:`report;1em;sd-text-info`. para qie lo consideres verdad

Observe y analice el siguiente diagrama de flujo del módulo compañía. Este diagrama representa el flujo de acciones necesarias para registrar y gestionar la información de los contratistas.

.. image:: /imgs/Contratistas/Contratistas1.png
    :align: center

Forma del Módulo Compañía
=========================

La forma **Compañía** permite ingresar y gestionar toda la información relevante sobre los diferentes contratistas.

Para acceder a la forma, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Contratistas``.

.. image:: /imgs/Contratistas/Contratistas2.png

Cuando se da de alta un nuevo contratista y no se cuenta con toda la documentación necesaria, se inicia un proceso que permite al propio contratista completar su solicitud de alta. Basta con registrar la razón social, RFC y un correo electrónico válido del contratista. Este último podrá ir llenando su solicitud en etapas, actualizando su registro cada vez que realice cambios. Una vez completada la solicitud, el contratista debe marcar el estatus como "Completada" para proceder con la autorización.

.. tab-set::

    .. tab-item:: Estructura

        La forma se divide en tres secciones principales:

        1. **Datos Generales**:

           - Razón Social: Nombre legal del contratista.
           - RFC: Registro Federal de Contribuyentes.
           - Email: Correo electrónico principal del contratista (importante para notificaciones).
           - Teléfono: Número telefónico de contacto.
           - Servicios a Prestar: Descripción de los servicios que el contratista ofrecerá.

        2. **Documentos**:

           - Acta de Situación Fiscal.
           - Identificación del Representante Legal.
           - Comprobante de Domicilio.

        3. **Permisos/Certificaciones**:

           - Requisitos específicos y certificaciones necesarias.

        .. warning:: Asegúrese de que el correo electrónico del contratista sea correcto, ya que se utilizará para comunicaciones importantes sobre su solicitud de alta.

        .. image:: /imgs/Contratistas/Contratistas3.png

    .. tab-item:: Registros
        
        .. image:: /imgs/Contratistas/Contratistas4.png

Consulte la siguiente pestaña para visualizar la documentación sobre los pasos que debe seguir el contratista para completar el proceso de alta.

.. dropdown:: Contratista

    Siga estos pasos en caso de ser contratista para completar el proceso de alta:

    .. important:: Si usted es un contratista y no es cliente de LinkaForm ni cuenta con una cuenta activa, no se preocupe. LinkaForm habilita sus formas para que sean públicas, por lo que no necesita una cuenta ni suscripciones.

    1. Diríjase a su |gmail| :octicon:`report;1em;sd-text-info`.
    2. Identifique el correo de la empresa que solicita sus servicios. Observe la siguiente imagen como referencia, puede variar dependiendo de la empresa.

    .. image:: /imgs/Contratistas/Contratistas5.png

    3. Presione el hipervínculo al final del correo. Será redirigido a una nueva pestaña con una forma prellenada.
    4. Revise que los datos generales registrados sean correctos, de lo contrario, actualícelos.
    5. Complete la sección de documentos y suba los archivos requeridos.
    6. Cambie el ``Estatus Solicitud`` a ``Completada`` **solo si** ha completado toda la información solicitada. De lo contrario, deje el estatus hasta que termine su captura. Observe la imagen:

    .. note:: Recuerde que no es necesario completar el registro de una sola vez. Puede acceder a él en cualquier momento para continuar con la captura.

    .. image:: /imgs/Contratistas/Contratistas6.png

    .. warning:: Por ningún motivo modifique el ``Estatus del contratista``. Este campo solo puede ser modificado por la empresa que solicitó sus servicios.

Forma del Módulo Compañía
=========================

Para acceder a las formas, seleccione la opción ``Formas > Mis Formas`` en el menú lateral. Ubique la carpeta ``Contratistas``. 

.. hint:: Presione el símbolo ``>`` para visualizar el nombre de las opciones del menú lateral.  
  
.. image:: /imgs/Formas/Formas1.1.png

Para acceder a la forma 

.. image:: /imgs/Contratistas/Contratistas2.png

El módulo de compañía utiliza una forma principal que se sincroniza automáticamente con el catálogo de compañías. A continuación, se detalla la forma y el proceso de sincronización.

- **Forma de Registro de Compañías**: Esta forma permite ingresar y gestionar toda la información relevante sobre las compañías. Los campos incluidos en esta forma están diseñados para cubrir los aspectos más importantes de cada empresa.

Campos de la Forma de Registro de Compañías
-------------------------------------------

La forma de registro de compañías incluye los siguientes campos esenciales:

- **Nombre de la Compañía**: El nombre oficial de la compañía.
- **Dirección**: La dirección física de la compañía.
- **Teléfono**: El número de contacto principal de la compañía.
- **Correo Electrónico**: El correo electrónico de contacto de la compañía.
- **Industria**: El sector o industria en la que opera la compañía.
- **Número de Identificación Fiscal**: El número de identificación fiscal de la compañía.

.. warning:: Asegúrese de que la información ingresada sea precisa y esté actualizada, ya que esta información es crucial para la correcta gestión de las compañías.

Catálogo del Módulo Compañía
============================

El catálogo **Compañía** se sincroniza automáticamente con la forma de registro, almacenando todos los registros creados a través de la forma. Este catálogo actúa como una base de datos centralizada para toda la información de las compañías.



.. note:: La sincronización automática garantiza que cualquier cambio realizado en la forma de registro se refleje inmediatamente en el catálogo, manteniendo la consistencia de los datos.

.. LIGAS EXTERNAS

.. |gmail| raw:: html

   <a href="https://mail.google.com/" target="_blank">correo electrónico</a>

