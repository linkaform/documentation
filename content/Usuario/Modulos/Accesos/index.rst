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

Observe y analice el siguiente diagrama de flujo del módulo de seguridad. Este diagrama representa de manera general el flujo de acciones necesarias para generar un pase de entrada. Cada recuadro representa un proceso que involucra varios pasos. Siga el proceso y continúe leyendo las secciones en el orden indicado en el diagrama para comprender parte del funcionamiento del módulo.

.. image:: /imgs/Modulos/Accesos/Accesos2.png

.. _definir-permisos:

Definición de Permisos
----------------------

La **Definición de Permisos** es un proceso importante dentro del módulo de seguridad que permite establecer y gestionar los requisitos necesarios para los perfiles de visitantes.
 
Al definir y gestionar estos permisos, se asegura que solo aquellos que cumplen con los criterios establecidos puedan ingresar, mejorando así la seguridad y el control dentro de las instalaciones.

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

      Este catálogo incluye los siguientes campos:

      - **ID Forma**: Identificador único de la forma que contiene el examen.
      - **Nombre del Examen**: El nombre descriptivo del examen.

      .. image:: /imgs/Modulos/Accesos/Accesos6.png

    .. tab-item:: Registros

      Para aprovechar todas las funcionalidades que ofrece |linkaform| :octicon:`report;1em;sd-text-info`, cree formularios con ponderaciones específicas para cada examen que desea que el visitante apruebe para que el examen sea considerado válido.
      
      .. seealso:: Consulte :ref:`ponderacion-conf` :octicon:`report;1em;sd-text-info` para más detalles sobre cómo configurar su forma.

      Cada registro en este catálogo representa un tipo de examen o certificado necesario para los visitantes, observe el ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos7.png

      .. note:: Recuerde que un catálogo actúa como una base de datos donde se puede tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

.. _catalog-permisos:

Catálogo: ``Definición de Permisos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo contiene la lista de permisos o certificaciones necesarias según algún tipo de perfil. Incluye los mismos registros que la `forma Definición de Permisos <#form-permisos>`_ :octicon:`report;1em;sd-text-info`. Revise la documentación correspondiente para obtener más detalles sobre la estructura del mismo.
 
.. warning:: Este catálogo está preparado para recibir registros derivados de una forma. Por lo tanto, no es necesario ingresar manualmente los registros. Simplemente complete la `forma Definición de Permisos <#form-permisos>`_ :octicon:`report;1em;sd-text-info` y linkaform se encargará de sincronizar automáticamente los registros en este catálogo.

.. image:: /imgs/Modulos/Accesos/Accesos8.png

.. note:: Recuerde que un catálogo actúa como una base de datos donde se puede tener acceso rápido a los datos necesarios para distintas funciones dentro de otras formas o catálogos.

.. _form-permisos:

Forma: ``Definición de Permisos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta forma permite crear y gestionar los permisos o certificaciones necesarias según el tipo de perfil. En esta forma registre nuevos permisos y asigne requisitos específicos a cada uno.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura
      
      La forma incluye los siguientes campos:

      **Nombre del Permiso o Certificación**: Nombre descriptivo del permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos9.png

      **Requerimientos**: Requisitos necesarios para obtener el permiso, como la aprobación de exámenes u otros criterios específicos.

      .. image:: /imgs/Modulos/Accesos/Accesos10.png

      **Vigencia**: Periodo de validez del permiso o certificación, expresado en un número entero.

      .. image:: /imgs/Modulos/Accesos/Accesos11.png

      **Vigencia Expresada en**: Unidad de tiempo de la validez del permiso o certificación (días, meses, semanas o años).

      .. image:: /imgs/Modulos/Accesos/Accesos12.png

      **Ejemplo de Documento del Permiso/Certificación**: Documento que acredita el permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos13.png

      **Ejemplo en Imagen**: Imagen del documento que demuestra el permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos14.png

      **Examen**: Examen requerido para obtener el permiso, enlazado al catálogo de `exámenes <#catalog-examenes>`_ :octicon:`report;1em;sd-text-info`.

      .. image:: /imgs/Modulos/Accesos/Accesos15.png

      **Estado del Permiso/Certificación**: Estado actual del permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos16.png

   .. tab-item:: Registros

      Al responder la forma y seleccionar los requerimientos, Linkaform mostrará los campos correspondientes para ingresar la información necesaria. Observe el ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos17.gif

      Cada vez que registre un nuevo permiso o certificación a través de esta forma, el `catálogo Definición de Permisos <#catalog-permisos>`_ :octicon:`report;1em;sd-text-info` se actualizará automáticamente con la nueva entrada.

      Para sincronizar el registro con el catálogo, la forma utiliza la acción ``Sync Catalog Records`` en la configuración de flujo.

      .. warning:: Si modifica la forma, asegúrese de también actualizar el catálogo correspondiente. Verifique que los **IDs** de los campos en la forma coincidan con los **IDs** de los campos en el catálogo. Para más detalles sobre configuraciones de flujos de trabajo, consulte :ref:`flujos` :octicon:`report;1em;sd-text-info`.

      .. admonition:: Ejemplo
         :class: pied-piper

         En este ejemplo, el permiso **Trabajo en Zonas Elevadas** requiere que el visitante apruebe el **Examen Primeros Auxilios**, también especifica que el permiso tiene una vigencia de 6 meses.

         .. image:: /imgs/Modulos/Accesos/Accesos18.png

Configuración de Perfiles
-------------------------

La **Configuración de Perfiles** es el proceso que permite definir y gestionar los perfiles de los visitantes y asociarles los permisos necesarios para acceder a diferentes áreas o realizar funciones específicas. Este proceso asegura que cada tipo de visitante o empleado tenga el nivel adecuado de acceso según sus responsabilidades y necesidades.

Para comprende cómo se integra este proceso, observe el siguiente diagrama que ilustra la relación entre la **Configuración de Perfiles** y la `Definición de Permisos <#definir-permisos>`_ :octicon:`report;1em;sd-text-info`. Revise las siguientes secciones para obtener más detalles sobre los elementos involucrados y cómo se configuran:
 
.. image:: /imgs/Modulos/Accesos/Accesos19.png
   :align: center

.. _catalog-perfiles:

Catálogo: ``Perfiles``
^^^^^^^^^^^^^^^^^^^^^^

Este catálogo permite definir los diferentes perfiles de usuarios que pueden acceder a las ubicaciones. Cada perfil representa un tipo específico de visitante o trabajador que puede tener diferentes niveles de acceso y requisitos asociados.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura

      El catálogo incluye el siguiente campo:

      - **Nombre del Perfil**: Nombre descriptivo del perfil, que identifica el tipo de acceso y permisos asociados. 

      .. image:: /imgs/Modulos/Accesos/Accesos20.png

   .. tab-item:: Registros

      De manera predeterminada, se incluye el perfil de **Visita General**. Defina otros perfiles necesarios para su contexto, por ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos21.png

.. _form-config-perfiles:

Forma: ``Configuración de Perfiles``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta forma permite relacionar los perfiles con los permisos que requieren. Este proceso garantiza que cada visitante cumpla con los requisitos específicos necesarios antes de ser autorizado para acceder a las instalaciones.

.. admonition:: Ejemplo
   :class: pied-piper

   Por ejemplo, un perfil puede ser un **Chofer** que necesita acceso solo a áreas de carga, mientras que otro perfil puede ser un **Instalador** con acceso a zonas técnicas especializadas.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura

      La forma incluye los siguientes campos:

      - **Catálogo Perfiles**: Selección del perfil definido en el catálogo de `Perfiles <#catalog-perfiles>`_ :octicon:`report;1em;sd-text-info`.

      - **Permisos Requeridos**: Grupo repetitivo donde se seleccionan los permisos necesarios para el perfil desde el catálogo de `Definicion de Permisos <#catalog-permisos>`_ :octicon:`report;1em;sd-text-info`.

      .. image:: /imgs/Modulos/Accesos/Accesos22.png

   .. tab-item:: Registros

      Cada registro en esta forma relaciona un perfil con uno o más permisos necesarios. Observe el siguiente ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos23.png

      .. attention:: El único perfil que no necesita permisos es la **Visita General**. Este perfil se utiliza para registrar a las visitas que no tienen una cita previa ni un trabajo especial que realizar dentro de las instalaciones. Es una visita espontánea.

         .. image:: /imgs/Modulos/Accesos/Accesos24.png

      .. warning:: Al crear un nuevo registro en esta forma, es necesario sincronizarlo con el catálogo `Configuración de Perfiles <#catalog-config-perfiles>`_ :octicon:`report;1em;sd-text-info`. Sin embargo, debido a la limitación de que los catálogos no admiten campos de grupo repetitivo, no es posible aplicar la sincronización automática completa en estos casos.

         Por lo tanto, cuando registre un nuevo perfil en la forma, asegúrese de también registrarlo manualmente en el catálogo. Si tiene múltiples registros, considere utilizar la funcionalidad de importación masiva para agilizar el proceso; consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para más detalles.

         Actualmente, estamos trabajando en una solución para mejorar este flujo y automatizar completamente la sincronización en futuras versiones.

.. _catalog-config-perfiles: 

Catálogo: ``Configuración de Perfiles``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo es una réplica de la forma `Configuración de Perfiles <#form-config-perfiles>`_ :octicon:`report;1em;sd-text-info` y contiene la lista de registros que relacionan perfiles con sus permisos necesarios.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura

      El catálogo incluye los siguientes campos:

      - **Perfil**: Selección del perfil definido en el catálogo de `Perfiles <#catalog-perfiles>`_ :octicon:`report;1em;sd-text-info`.
      
      - **Permisos/Certificaciones**: Lista de permisos necesarios para el perfil, derivados del catálogo de `Definición de Permisos <#catalog-permisos>`_ :octicon:`report;1em;sd-text-info`.

      .. image:: /imgs/Modulos/Accesos/Accesos25.png

   .. tab-item:: Registros

      A diferencia de la forma **Configuración de Perfiles**, este catálogo no admite campos de grupo repetitivo, por lo que es necesario registrar manualmente los permisos asociados a cada perfil. Observe el siguiente ejemplo:

      .. seealso:: Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para una importación masiva de registros.

      .. image:: /imgs/Modulos/Accesos/Accesos26.png

.. LIGAS EXTERNAS

.. |linkaform| raw:: html

   <a href="https://www.linkaform.com/" target="_blank">LinkaForm</a>