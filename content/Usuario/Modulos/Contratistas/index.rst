.. _doc-contratistas:

===================
Módulo Contratistas
===================

El **Módulo Contratistas** proporciona los elementos base necesarios para gestionar y administrar la información de múltiples contratistas. Este módulo es importante para el :ref:`doc-accesos` :octicon:`report;1em;sd-text-info`.

Observe y analice el siguiente diagrama de flujo del módulo compañía. Este diagrama representa el flujo de acciones necesarias para registrar y gestionar la información de los contratistas.

.. image:: /imgs/Modulos/Contratistas/Contratistas1.png
    :align: center

.. _form-contratistas:

Forma del Módulo Contratistas
=============================

La forma **Contratistas** permite ingresar y gestionar toda la información relevante sobre los diferentes contratistas.

Para acceder a la forma, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Contratistas``.

.. image:: /imgs/Modulos/Contratistas/Contratistas2.png

Al crear un nuevo registro en esta forma, se sincroniza automáticamente con el `catálogo contratistas <#catalog-contratistas>`_ :octicon:`report;1em;sd-text-info`. Observe el flujo de acciones necesario en el siguiente diagrama.

.. image:: /imgs/Modulos/Contratistas/Contratistas1.png
    :align: center

Para la sincronización del registro con el catálogo, la forma está configurada para utilizar la acción ``Sync Catalog Records``.

.. attention:: Si realiza modificaciones en la forma de ``Contratistas``, asegúrese de actualizar también el catálogo de ``Contratistas`` y verificar que los identificadores de los campos sean los mismos.

.. seealso:: Consulte :ref:`flujos` :octicon:`report;1em;sd-text-info` para más detalles.

Al registrar un nuevo contratista, se inicia un proceso que permite al propio contratista completar su solicitud. Simplemente, asegúrese de especificar la **razón social**, el **RFC** y un **correo electrónico** válido. 

El contratista puede ir completando su solicitud en etapas y actualizar su registro cada vez que realice algún cambio. 

Una vez completada la solicitud, proceda con la autorización dentro de la empresa modificando el ``Estatus del contratista``.

.. seealso:: Consulte `alta de contratistas <#alta-contratista>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. tab-set::

    .. tab-item:: Estructura

        La forma se divide en dos secciones principales:

        1. **Datos Generales**

           - **Razón Social**: Nombre legal del contratista.
           - **RFC**: Registro Federal de Contribuyentes.
           - **Email Contratista**: Correo electrónico principal del contratista (importante para notificaciones).
           - **Teléfono Contratista**: Número telefónico de contacto.
           - **Servicios a Prestar**: Descripción de los servicios que el contratista ofrecerá.
           - **Estatus Solicitud**: Indica el estado actual del proceso de solicitud de alta del contratista.
           - **Estatus del Contratista**: Refleja el estado operativo del contratista dentro de la empresa. 
        
        .. warning:: Asegúrese de que el correo electrónico del contratista sea válido, ya que se utilizará para comunicaciones importantes relacionadas con su solicitud de alta y otros procesos importantes.

        2. **Documentos**

           - Acta de Situación Fiscal.
           - Identificación del Representante Legal.
           - Comprobante de Domicilio.

        .. image:: /imgs/Modulos/Contratistas/Contratistas3.png

    .. tab-item:: Registros
        
        Observe el siguiente ejemplo de registro.

        .. image:: /imgs/Modulos/Contratistas/Contratistas4.png
            
.. _catalog-contratistas:

Catálogo del Módulo Contratistas
================================

El catálogo **Contratistas** contiene los mismos registros que de la `forma contratistas <#form-contratistas>`_ :octicon:`report;1em;sd-text-info`.

.. attention:: Este catálogo está preparado para recibir un registro derivado de una forma, por lo tanto, no deberá preocuparse por contestar manualmente el registro en el catálogo. Simplemente preocúpese por responder la forma de `contratistas <#form-contratistas>`_ :octicon:`report;1em;sd-text-info` y Linkaform se encargará de sincronizar el mismo registro en este catálogo.

Para acceder al catálogo, seleccione la opción ``Catálogos > Catálogos`` en el menú lateral y ubique la carpeta ``Contratistas``.

.. image:: /imgs/Modulos/Contratistas/Contratistas9.png

.. tab-set::

    .. tab-item:: Estructura

       .. image:: /imgs/Modulos/Contratistas/Contratistas7.png

    .. tab-item:: Registros

        .. image:: /imgs/Modulos/Contratistas/Contratistas8.png

.. note:: Recuerde que un catálogo actúa como una base de datos donde se puede tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

.. _alta-contratista:

Alta de Contratista
===================

Si es contratista, siga siga los siguientes pasos para completar su alta:

.. important:: Si no tiene una cuenta en |linkaform| :octicon:`report;1em;sd-text-info`, podrá responder la forma sin necesidad de una cuenta o suscripción.

1. Diríjase a su |gmail| :octicon:`report;1em;sd-text-info`.
2. Identifique el correo de la empresa que solicita sus servicios. Observe la siguiente imagen como referencia, puede variar dependiendo de la empresa.

.. image:: /imgs/Modulos/Contratistas/Contratistas5.png

3. Presione el hipervínculo al final del correo. Será redirigido a una nueva pestaña con una forma prellenada.
4. Revise que los datos generales registrados sean correctos, de lo contrario, actualícelos.
5. Complete la sección de documentos y suba los archivos requeridos.
6. Cambie el ``Estatus Solicitud`` a ``Completada`` **solo si** ha completado toda la información solicitada. De lo contrario, no modifique el ``estatus`` hasta que termine su captura.

.. hint:: Considere que no es necesario completar el registro en una sola sesión. Puede enviar las respuestas parciales y acceder a la misma URL en cualquier momento para continuar con la captura.

.. image:: /imgs/Modulos/Contratistas/Contratistas6.png

.. warning:: Por ningún motivo modifique el ``Estatus del contratista``. Este campo solo puede ser modificado por la empresa que solicitó sus servicios.

.. _carga-permisos-visitas:

Carga de Permisos de Visitantes
===============================

lorem

Ha completado con éxito el proceso de configuración y utilización del módulo de contratistas. Recuerde que este módulo es adaptable a sus necesidades, lo que significa que puede ajustarlo según lo requiera.

Si tiene alguna duda o necesita asistencia técnica, no dude en ponerse en contacto con nuestro equipo de soporte.

.. LIGAS EXTERNAS

.. |gmail| raw:: html

   <a href="https://mail.google.com/" target="_blank">correo electrónico</a>

.. |linkaform| raw:: html

   <a href="https://www.linkaform.com/" target="_blank">LinkaForm</a>

