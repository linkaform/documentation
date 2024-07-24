.. _doc-accesos:

===================
Módulo de Seguridad
===================

El **módulo de Seguridad** está diseñado para gestionar y controlar el acceso de personas a una ubicación. Su objetivo es garantizar la seguridad, proteger activos y recursos, y mantener un registro detallado de las actividades de entrada y salida, así como otras funciones relacionadas con la seguridad.

Este módulo opera mediante una interfaz de usuario utilizada exclusivamente por el personal de seguridad en las casetas de acceso. Las casetas son puntos de control que permiten la entrada a la ubicación.

El módulo de seguridad es utilizado por dos roles diferentes:

- **Personal dentro de la instalación**: Son responsables de generar pases de entrada (invitaciones) y gestionar perfiles de visitantes y empleados. Este personal interactúa directamente con algunas formas y catálogos del módulo.
- **Personal de Seguridad**: Utiliza la interfaz de usuario para ejecutar funciones de control de acceso, reportar incidencias, gestionar equipos y más.

.. seealso:: El personal de seguridad no interactúa directamente con las formas y catálogos; consulte :ref:`doc-base` :octicon:`report;1em;sd-text-info` para más detalles.

Esta documentación se centra en explicar el funcionamiento, los flujos y las configuraciones de las formas y catálogos que involucra el módulo de seguridad. A medida que avance en la lectura, encontrará más detalles sobre cada forma y catálogo, junto con ejemplos y guías paso a paso para su correcta implementación y utilización.

Para acceder a las formas del módulo, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Seguridad``.

.. image:: /imgs/Modulos/Accesos/Accesos2.png

Para acceder a los catálogos, seleccione la opción ``Catálogos > Catálogos`` en el menú lateral y ubique la carpeta ``Seguridad``.

.. image:: /imgs/Modulos/Accesos/Accesos3.png

.. warning:: Antes de utilizar el módulo, asegúrese de contar con la instalación y registros necesarios del :ref:`doc-employee` :octicon:`report;1em;sd-text-info`, :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` y :ref:`doc-contratistas` :octicon:`report;1em;sd-text-info`.

Generar Pase de Entrada
=======================

Observe y analice el siguiente diagrama de flujo del módulo de seguridad. Este diagrama representa de manera general el flujo de acciones necesarias para generar un pase de entrada. Cada recuadro representa un proceso que involucra varios pasos. Siga el proceso y continúe leyendo las secciones en el orden indicado en el diagrama para comprender completamente el funcionamiento del módulo.

.. image:: /imgs/Modulos/Accesos/Accesos2.png

Definición de Permisos
----------------------

La **Definición de Permisos** es un proceso importante dentro del módulo de seguridad que permite establecer y gestionar los requisitos necesarios para los perfiles de visitantes.

Este proceso garantiza que cada visitante cumpla con los requisitos específicos necesarios antes de ser autorizado para acceder a las instalaciones. Al definir y gestionar estos permisos, se asegura que solo aquellos que cumplen con los criterios establecidos puedan ingresar, mejorando así la seguridad y el control dentro de las instalaciones.

Observe y analice el siguiente diagrama y consulte las siguientes secciones para más detalles de los elementos:

.. image:: /imgs/Modulos/Accesos/Accesos5.png
   :align: center

.. _catalog-examenes:

Catálogo: ``Definición de Exámenes``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo permite definir los exámenes necesarios para ciertos permisos requeridos. Estos exámenes pueden ser necesarios para otorgar acceso a áreas específicas, cumplir con requisitos de seguridad u otros criterios establecidos.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.
      
.. tab-set::

    .. tab-item:: Estructura

      Este catálogo incluye los siguientes campos principales:

      - **ID Forma**: Identificador único de la forma que contiene el examen.
      - **Nombre del Examen**: El nombre descriptivo del examen.

      .. image:: /imgs/Modulos/Accesos/Accesos6.png

    .. tab-item:: Registros

      Para aprovechar todas las funcionalidades que ofrece |linkaform| :octicon:`report;1em;sd-text-info`, cree formularios con ponderaciones específicas para cada examen que desea que el visitante apruebe para que el examen sea considerado válido.
      
      .. seealso:: Consulte :ref:`ponderacion-conf` :octicon:`report;1em;sd-text-info` para más detalles sobre cómo configurar su forma.

      Cada registro en este catálogo representa un tipo de examen o certificado necesario para los visitantes, observe el ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos7.png

.. _catalog-permisos:

Catálogo: ``Definición de Permisos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo contiene la lista de permisos o certificaciones necesarias según algún tipo de perfil. Incluye los mismos registros que la `forma Definición de Permisos <#form-permisos>`_ :octicon:`report;1em;sd-text-info`. Revise la documentación correspondiente para obtener más detalles sobre la estructura del mismo.

.. warning:: Este catálogo está preparado para recibir registros derivados de una forma. Por lo tanto, no es necesario ingresar manualmente los registros. Simplemente complete la forma `Definición de Permisos <#form-permisos>`_ :octicon:`report;1em;sd-text-info` y |linkaform| :octicon:`report;1em;sd-text-info` se encargará de sincronizar automáticamente los registros en este catálogo.

.. image:: /imgs/Modulos/Accesos/Accesos8.png

.. _form-permisos:

Forma: ``Definición de Permisos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta forma permite crear y gestionar los permisos o certificaciones necesarias según el tipo de perfil. Al definir y configurar adecuadamente los exámenes, permisos y perfiles, se asegura que solo personas debidamente autorizadas y preparadas puedan acceder a áreas críticas dentro de la ubicación.

A través de esta forma, se pueden registrar nuevos permisos y asignar requisitos específicos a cada uno.

La forma incluye los siguientes campos:

- **Nombre del Permiso o Certificación**: Nombre descriptivo del permiso o certificación.
- **Requerimientos**: Requisitos necesarios para el permiso, que pueden incluir aprobaciones de exámenes u otros criterios específicos.
- **Vigencia**: Período de validez del permiso o certificación, expresado en número entero.
- **Vigencia Expresada en**: Periodo de validez del permiso o certificación en días, meses, semanas o años.
- **Ejemplo de Documento del Permiso/Certificación**: Documento que demuestra el permiso o certificación.
- **Ejemplo en Imagen**: Imagen del documento que acredita el permiso o certificación.
- **Examen**: Examen que debe ser aprobado para obtener el permiso, sincronizado con el **Catálogo de Definición de Exámenes**.
- **Estado del Permiso/Certificación**: Estado actual del permiso o certificación.

Cada vez que se registre un nuevo permiso a través de esta forma, el **Catálogo de Definición de Permisos** se actualizará automáticamente con la nueva entrada.

.. note:: La sincronización entre los registros de la forma y el catálogo garantiza que todos los permisos y requisitos estén actualizados y disponibles para la asignación a los perfiles de visitantes.

La forma de **Definición de Permisos** valida que los requisitos de examen sean cumplidos antes de que se puedan asignar permisos a los visitantes. Los registros en el catálogo deben completarse y estar actualizados para asegurar una correcta gestión de los permisos.

La sincronización entre el **Catálogo de Definición de Permisos** y el **Catálogo de Definición de Exámenes** garantiza que los permisos otorgados se basen en la aprobación de exámenes específicos. Esto asegura que solo las personas que cumplan con todos los requisitos necesarios puedan acceder a áreas restringidas o desempeñar ciertas funciones.

**Ejemplo:**

En este ejemplo, el **Catálogo de Definición de Permisos** utiliza la información del **Catálogo de Definición de Exámenes** para validar que el permiso de **Acceso a Zonas Elevadas** solo sea otorgado a personas que hayan aprobado el **Examen de Seguridad en Alturas**.

1. **Catálogo de Definición de Exámenes**:
   - ID Forma: 001
   - Nombre del Examen: Examen de Seguridad en Alturas

2. **Catálogo de Definición de Permisos**:
   - Nombre del Permiso o Certificación: Acceso a Zonas Elevadas
   - Requerimientos: Aprobación del Examen de Seguridad en Alturas
   - Vigencia: 1 año
   - Vigencia Expresada en: 12 meses
   - Ejemplo de Documento del Permiso/Certificación: Documento adjunto
   - Ejemplo en Imagen: Imagen del documento adjunto
   - Examen: Examen de Seguridad en Alturas (ID Forma: 001)
   - Estado del Permiso/Certificación: Activo

.. LIGAS EXTERNAS

.. |linkaform| raw:: html

   <a href="https://www.linkaform.com/" target="_blank">LinkaForm</a>