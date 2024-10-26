.. _doc-accesos:

===================
Módulo de Seguridad
===================

El **módulo de Seguridad** está diseñado para brindar seguridad industrial, se enfoca en proteger a los trabajadores, el entorno de trabajo y la infraestructura de la empresa, especialmente en industrias donde hay riesgos físicos significativos, como fábricas, plantas de producción, minería, y construcción.

Su objetivo es prevenir accidentes laborales y enfermedades ocupacionales, garantizando que se cumplan las normativas de seguridad y salud en el trabajo.

Este módulo está diseñado para integrarse con un sistema de control de seguridad patrimonial, operado por el personal de seguridad en las casetas de acceso. Las casetas funcionan como puntos de control responsables de gestionar y supervisar la entrada y salida de visitantes en una ubicación, asegurando un control eficiente y seguro de los accesos.

.. seealso:: Para más detalles, revise la documentación de :ref:`doc-soter` :octicon:`report;1em;sd-text-info`.

El módulo de seguridad es utilizado por el personal que tienen la responsabilidad de generar pases de entrada (invitaciones) y gestionar todo lo relacionado con la seguridad de visitantes y empleados.

Esta documentación se centra en explicar flujos y configuraciones de las formas y catálogos que involucra el módulo de seguridad. A medida que avance, encontrará más detalles, ejemplos y guías paso a paso para la correcta implementación y utilización del módulo.

Para acceder a las formas del módulo, seleccione la opción ``Formas > Mis Formas`` en el menú lateral y ubique la carpeta ``Seguridad``.

.. image:: /imgs/Modulos/Accesos/Accesos2.png

Para acceder a los catálogos, seleccione la opción ``Catálogos > Catálogos`` en el menú lateral y ubique la carpeta ``Seguridad``.

.. image:: /imgs/Modulos/Accesos/Accesos3.png

.. warning:: Antes de utilizar el módulo, asegúrese de contar con la instalación y registros necesarios del :ref:`doc-employee` :octicon:`report;1em;sd-text-info`, :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` y :ref:`doc-contratistas` :octicon:`report;1em;sd-text-info`.

Generar Pase de Entrada
=======================

Observe y analice el siguiente diagrama de flujo del módulo. Este diagrama representa el flujo de acciones necesarias para generar un pase de entrada. Cada recuadro representa un proceso. Siga el proceso y continúe leyendo las secciones en el orden indicado en el diagrama para comprender el módulo.

.. image:: /imgs/Modulos/Accesos/Accesos1.png
   :width: 880px

.. _proceso-definir-permisos:

Definición de Permisos
----------------------

La **Definición de Permisos** es el proceso que permite establecer y gestionar los requisitos y certificaciones necesarios para los perfiles de visitantes, garantizando que cumplan con los estándares y regulaciones de seguridad antes de ingresar a las ubicaciones.

Observe y analice el siguiente diagrama, y consulte las secciones siguientes para obtener más detalles sobre los elementos involucrados:

.. image:: /imgs/Modulos/Accesos/Accesos5.png
   :align: center

.. _catalog-categorias-objetos:

Catálogo: ``Categorías de Objetos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo es utilizado en diferentes procesos dentro del módulo de seguridad, específicamente para:

- **Lista de Objetos**: Permite registrar y gestionar diferentes tipos de categorías para clasificar objetos. 
- **Activos Fijos**: Permite clasificar nuevos objetos dentro de la ubicación para el proceso de concesión de objetos. 

Revise las siguientes pestañas para obtener más detalles sobre la estructura del catálogo y ejemplos de registros.

.. tab-set::

    .. tab-item:: Estructura

      Este catálogo incluye los siguientes campos:

      - **Categoría del Objeto**: Nombre de la categoría a la cual pertenece el objeto.
      - **Descripción de la Categoría**: Descripción detallada de la categoría para proporcionar más contexto y facilitar la identificación de los objetos.

      .. image:: /imgs/Modulos/Accesos/Accesos39.png

    .. tab-item:: Registros

      Cada registro en este catálogo representa una categoría de objetos. Observe los ejemplos:

      .. image:: /imgs/Modulos/Accesos/Accesos40.png

      .. note:: Al instalar el módulo, este catálogo incluye registros precargados. Sin embargo, considere agregar más registros según lo requiera.

      Al instalar el módulo, asegúrese de que el catálogo incluya el filtro ``Activos_fijos``. Si no encuentra el filtro, consulte la documentación para aprender a :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` y aplique los siguientes valores:

      .. code-block::
         :caption: Guarde el filtro con el nombre ``Activos_fijos``.

         Campo = Categoría del Objeto
         Condición = Igual a
         Valor = Artículos de Higiene Personal
                 Llaves y Tarjetas de Acceso
                 Equipos informáticos
                 Equipos/Productos/Utencilios de limpieza
                 Equipos Electrónicos y de Telecomunicaciones
                 Equipos de climatización y aire acondicionado
                 Mobiliario
                 Equipos de iluminación y lámparas
                 Equipos médicos/Medicamentos
                 Equipos/Utensilios de cocina
                 Vehículos/Accesorios/Productos automotrices 
                 Efectivo/Tarjetas de Crédito/Valores Monetarios
                 Herramientas eléctricas/Equipos de trabajo/Protección personal
                 Sistemas de Seguridad Contra Intrusos y Robos
                 Equipos de Energía y Monitoreo

         //Este filtro mostrará únicamente las categorías relevantes para dar de alta un activo fijo.

.. _catalog-lista-objetos:

Catálogo: ``Lista de Objetos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo es utilizado en diferentes procesos dentro del módulo de seguridad, tales como:

- **Definición de Permisos**: Permite especificar los objetos, herramientas o equipos que son necesarios u obligatorios para ciertos permisos requeridos.
- **Bitácora Objetos Perdidos**: Registra y gestiona los objetos reportados como perdidos.

.. tab-set::

    .. tab-item:: Estructura

      Este catálogo incluye los siguientes campos:

      - **Categoría del Objeto**: Categorías definidos en el catálogo `categorías <#catalog-categorias-objetos>`_ :octicon:`report;1em;sd-text-info`.
      - **Descripción de la Categoría**: Descripción correspondiente a la categoría seleccionada.
      - **Objeto**: Nombre del objeto perteneciente a la categoría seleccionada.

      .. image:: /imgs/Modulos/Accesos/Accesos41.png
      

    .. tab-item:: Registros

      Cada registro en este catálogo representa un objeto clasificado en una categoría de objetos. Observe los registros de ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos42.png
         :align: center

      .. note:: Al instalar el módulo, este catálogo ya cuenta con registros precargados. Sin embargo, si lo requiere, considere agregar más registros.

      Al instalar el módulo, asegúrese de que el catálogo incluya el filtro ``Equipos_para_permisos``. Si no encuentra el filtro, consulte la documentación para aprender a :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` y aplique los siguientes valores:

      .. code-block::
         :caption: Guarde el filtro con el nombre **Equipos_para_permisos**

         Campo = Categoría del Objeto
         Condición = Igual a
         Valor = Equipos informáticos 
               Equipos Electrónicos y de Telecomunicaciones
               Herramientas eléctricas/Equipos de trabajo/Protección personal
               Equipos/Productos/Utencilios de limpieza
               Sistemas de Seguridad Contra Intrusos y Robos
               Equipos de Energía y Monitoreo

         //Este filtro mostrará únicamente los objetos relevantes para relacionar con los permisos.

.. _catalog-examenes:

Catálogo: ``Definición de Exámenes``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo permite establecer y gestionar los exámenes necesarios para evaluar si una visita cumple con los requisitos de seguridad o habilidades requeridas para obtener ciertos permisos o acceder a áreas específicas. 

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.
      
.. tab-set::

    .. tab-item:: Estructura

      Este catálogo incluye los siguientes campos:

      - **ID Forma**: Identificador único de la forma que contiene el examen.
      - **Nombre del Examen**: El nombre descriptivo del examen.

      .. image:: /imgs/Modulos/Accesos/Accesos6.png

    .. tab-item:: Registros

      Cada registro en este catálogo representa un formulario de examen, observe el ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos7.png

      Para aprovechar todas las funcionalidades que ofrece |linkaform| :octicon:`report;1em;sd-text-info`, cree formularios con ponderaciones personalizadas para cada examen.
      
      .. seealso:: Consulte :ref:`ponderacion-conf` :octicon:`report;1em;sd-text-info` para más detalles sobre cómo configurar su forma.

      Al crear sus propios formularios de exámenes, asegúrese de guardarlos en la carpeta: ``Seguridad > Exámenes``, tal como se muestra en la siguiente imagen.

      .. image:: /imgs/Modulos/Accesos/Accesos44.png

.. _form-definicion-permisos:

Forma: ``Definición de Permisos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta forma se utiliza para definir permisos o certificaciones, especificando los requerimientos necesarios para cada uno, como vigencia, documentación, materiales o equipos requeridos. Es la relación del permiso con los elementos necesarios para su cumplimiento.

Consulte las siguientes pestañas para obtener más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura
      
      La forma incluye los siguientes campos:

      **Nombre del Permiso o Certificación**: Nombre descriptivo del permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos9.png

      **Requerimientos**: Requisitos necesarios para comprobar el permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos10.png

      **Vigencia**: Periodo de validez del permiso o certificación, expresado en un número entero.

      .. image:: /imgs/Modulos/Accesos/Accesos11.png

      **Vigencia Expresada en**: Unidad de tiempo de la validez del permiso o certificación (días, meses, semanas o años).

      .. image:: /imgs/Modulos/Accesos/Accesos12.png

      **Ejemplo de Documento del Permiso/Certificación**: Documento que acredita el permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos13.png

      **Ejemplo en Imagen**: Imagen del documento que demuestra el permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos14.png

      **Examen**: Examen requerido por el permiso, enlazado al catálogo de `exámenes <#catalog-examenes>`_ :octicon:`report;1em;sd-text-info`.

      .. image:: /imgs/Modulos/Accesos/Accesos15.png
      
      **Materiales/Equipo**: Grupo repetitivo que especifica el material, objeto o equipo requerido para el permiso, enlazado al catálogo de `lista de objetos <#catalog-lista-objetos>`_ :octicon:`report;1em;sd-text-info`.
      
      .. warning:: En el `Catálogo Definición de Permisos <#catalog-definicion-permisos>`_ :octicon:`report;1em;sd-text-info`, no es posible utilizar un grupo repetitivo. Por lo tanto, se utiliza directamente al catálogo de lista de objetos.

      .. image:: /imgs/Modulos/Accesos/Accesos43.png

      **Estado del Permiso/Certificación**: Estado actual del permiso o certificación.

      .. image:: /imgs/Modulos/Accesos/Accesos16.png

   .. tab-item:: Registros

      Al responder la forma y seleccionar los requerimientos del permiso, Linkaform mostrará los campos correspondientes para ingresar la información necesaria. Observe el ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos17.gif

      .. warning:: Los registros de esta forma son indispensables y son utilizados por otras formas, lo que implica la necesidad de que estén disponibles en un catálogo. Sin embargo, debido a que los catálogos no admiten campos con grupos repetitivos, no es posible una sincronización automática completa en estos casos.

         Por lo tanto, cuando registre un permiso en la forma, asegúrese de ingresarlo manualmente en el `catálogo definición de permisos <#catalog-definicion-permisos>`_ :octicon:`report;1em;sd-text-info`. Si tiene múltiples registros, considere utilizar la funcionalidad de importación masiva para agilizar el proceso; consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para más detalles.

         Actualmente, estamos trabajando en una solución para mejorar este flujo y automatizar completamente la sincronización en futuras versiones.

      .. admonition:: Ejemplo
         :class: pied-piper

         En este ejemplo, el permiso **Equipo de Seguridad Constructivo** requiere que el visitante apruebe el **Examen de Seguridad para Trabajos en Alturas**. Además, se requiere una inspección visual de las herramientas, que incluye el casco protector, el arnés de seguridad y los guantes de seguridad.

         .. image:: /imgs/Modulos/Accesos/Accesos18.png

.. _catalog-definicion-permisos:

Catálogo: ``Definición de Permisos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo contiene los permisos o certificaciones, detallando los requisitos específicos necesarios para cada uno. Para obtener más información sobre su estructura y funcionamiento, consulte la documentación correspondiente a la `forma definición de permisos <#form-definicion-permisos>`_ :octicon:`report;1em;sd-text-info`.

.. image:: /imgs/Modulos/Accesos/Accesos8.png
   :width: 880px

A diferencia de la forma **Definición de Permisos**, este catálogo no permite el uso de campos de grupo repetitivo, lo que implica que los permisos asociados a cada requisito deben ser registrados manualmente.

.. seealso:: Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para una importación masiva de registros.

Configuración de Perfiles
-------------------------

El proceso de configuración de perfiles implica definir distintos tipos de visitantes y personalizar sus características mediante la asignación de permisos específicos. Esto asegura que cada usuario tenga el acceso adecuado a las funciones y recursos necesarios, según su rol y responsabilidades dentro de la ubicación.

Observe el siguiente diagrama, que ilustra la relación entre la **Configuración de Perfiles** y la `Definición de Permisos <#proceso-definir-permisos>`_ :octicon:`report;1em;sd-text-info`. Consulte las secciones a continuación para obtener más detalles sobre los elementos involucrados.

.. image:: /imgs/Modulos/Accesos/Accesos19.png
   :align: center

.. _catalog-perfiles:

Catálogo: ``Perfiles``
^^^^^^^^^^^^^^^^^^^^^^

Este catálogo es útil para definir diferentes tipos de visitas. 

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura

      .. grid:: 2
         :gutter: 0

         .. grid-item-card::
            :columns: 6

            El catálogo incluye los siguientes campos:

            - **Nombre del Perfil**: Nombre descriptivo del perfil.
            - **Motivo de Visita**: Propósito del perfil.
            - **Walkin**: Indica si la visita puede ser espontánea.

            .. note::

               **Sí** indica que no es necesario programar la visita con anticipación.

               **No** significa que la visita debe ser planificada.

         .. grid-item-card::   
            :columns: 6

            .. image:: /imgs/Modulos/Accesos/Accesos20.png

   .. tab-item:: Registros

      Cada registro en este catálogo representa un tipo de perfil. Observe los ejemplos:

      .. image:: /imgs/Modulos/Accesos/Accesos21.png

      .. note:: Al instalar el módulo, este catálogo incluye registros precargados. Sin embargo, considere definir otros perfiles necesarios para su contexto.

.. _form-config-perfiles:

Forma: ``Configuración de Perfiles``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta forma permite asociar perfiles con los permisos requeridos, garantizando que cada perfil cumpla con los requisitos establecidos antes de autorizar su acceso a la ubicación.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura

      La forma incluye los siguientes campos:

      - **Perfil**: Tipo de perfile, definido en el catálogo `Perfiles <#catalog-perfiles>`_ :octicon:`report;1em;sd-text-info`.

      - **Permisos/Certificaciones**: Grupo repetitivo que detalla los permisos necesarios para cada perfil, especificados en el `catálogo Definición de Permisos <#catalog-definicion-permisos>`_ :octicon:`report;1em;sd-text-info`.

      .. note:: Un perfil puede contener uno o varios permisos

      - **Ubicación**: Ubicación a la cual se aplicará esta configuración.

      .. warning:: Si no se selecciona una ubicación, la configuración del perfil y los permisos estará disponible en todas las ubicaciones.

      .. seealso:: Revise la documentación del :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` para obtener más detalles.

      .. image:: /imgs/Modulos/Accesos/Accesos22.png

   .. tab-item:: Registros

      Cada registro representa un perfil relacionado con uno o varios permisos. Observe el siguiente ejemplo:

      .. image:: /imgs/Modulos/Accesos/Accesos23.png
         :width: 880px
            
      .. attention:: El único perfil que no necesita permisos es la **Visita General**. Este perfil se utiliza para registrar a las visitas que no tienen una cita previa ni un trabajo especial que realizar dentro de las instalaciones. Es una visita espontánea.

         .. image:: /imgs/Modulos/Accesos/Accesos24.png

      .. warning:: Los registros de esta forma son indispensables y son utilizados por otras formas, lo que requiere que estén disponibles también en un catálogo. Sin embargo, debido a la limitación de que los catálogos no admiten campos de grupo repetitivo, no es posible realizar una sincronización automática completa en estos casos.

         Por lo tanto, cuando registre la configuración de un nuevo perfil en la forma, asegúrese de también ingresarlo manualmente en el catálogo `configuración de perfiles <#catalog-config-perfiles>`_ :octicon:`report;1em;sd-text-info`. Si tiene múltiples registros, considere utilizar la funcionalidad de importación masiva para agilizar el proceso; consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para más detalles.

         Actualmente, estamos trabajando en una solución para mejorar este flujo y automatizar completamente la sincronización en futuras versiones.

.. _catalog-config-perfiles: 

Catálogo: ``Configuración de Perfiles``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo es una réplica de la `forma configuración de perfiles <#form-config-perfiles>`_ :octicon:`report;1em;sd-text-info` y contiene la lista de registros que relacionan perfiles con los permisos necesarios.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura

      El catálogo incluye los siguientes campos:

      - **Perfil**: Tipo de perfile, definido en el catálogo `Perfiles <#catalog-perfiles>`_ :octicon:`report;1em;sd-text-info`.
      
      - **Permisos/Certificaciones**: Lista de permisos para el perfil, especificados en el `catálogo definición de permisos <#catalog-definicion-permisos>`_ :octicon:`report;1em;sd-text-info` .

      - **Ubicación**: Ubicación a la cual se aplicará esta configuración.

      .. warning:: Si no se selecciona una ubicación, la configuración del perfil y los permisos estará disponible en todas las ubicaciones.

      .. image:: /imgs/Modulos/Accesos/Accesos25.png

   .. tab-item:: Registros

      A diferencia de la `forma <#form-config-perfiles>`_ :octicon:`report;1em;sd-text-info`, un catálogo no admite campos de grupo repetitivo, por lo que es necesario registrar manualmente los permisos asociados a cada perfil. Observe el siguiente ejemplo:

      .. seealso:: Consulte :ref:`importar-registros` :octicon:`report;1em;sd-text-info` para una importación masiva.

      .. image:: /imgs/Modulos/Accesos/Accesos26.png
         :width: 880 px

Generar Visita
--------------

El proceso de **Generar una Visita** está diseñado para registrar y gestionar los datos de los visitantes. Este proceso, mantiene un control adecuado de las personas que ingresan a las instalaciones.

.. warning:: Antes de continuar con el proceso, asegúrese de contar con la instalación y registros necesarios del :ref:`doc-contratistas` :octicon:`report;1em;sd-text-info`.
 
Aunque este proceso no requiere los procesos anteriormente vistos, sí involucra catálogos pertenecientes a otro módulo. Observe el siguiente diagrama y revise las siguientes secciones para obtener más detalles sobre los elementos involucrados y cómo se configuran:

.. image:: /imgs/Modulos/Accesos/Accesos27.png
   :align: center
   
.. _form-visita-autorizada:

Forma: ``Visita Autorizada``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta forma permite registrar los datos de un visitante y gestionar su estado en relación con la empresa. Se utiliza principalmente para registrar a personas que realizarán una tarea o función beneficiosa para la empresa, facilitando la identificación de aquellos que podrían convertirse en visitantes recurrentes.

Revise las siguientes pestañas para más detalles sobre la estructura y algunos ejemplos.

.. tab-set::

   .. tab-item:: Estructura

      .. hint:: Considere ajustar la estructura de la forma según el nivel de detalle de los datos que necesite recopilar.

      La forma incluye los siguientes campos:

      **Nombre de la Visita**: Nombre completo del visitante.

      .. image:: /imgs/Modulos/Accesos/Accesos28.png

      **CURP**: Clave Única de Registro de Población.
            
      .. image:: /imgs/Modulos/Accesos/Accesos29.png
            
      **Email**: Dirección de correo electrónico de la visita.
            
      .. image:: /imgs/Modulos/Accesos/Accesos30.png
            
      **Teléfono**: Número de teléfono de la visita.
            
      .. image:: /imgs/Modulos/Accesos/Accesos31.png
            
      **Foto**: Imagen de la persona que realiza la visita.
            
      .. image:: /imgs/Modulos/Accesos/Accesos32.png
            
      **Identificación**: Documento de identificación oficial.
            
      .. image:: /imgs/Modulos/Accesos/Accesos33.png
            
      **Contratista**: Empresa a la que pertenece el visitante. Utiliza el :ref:`catalog-contratistas` :octicon:`report;1em;sd-text-info`.

      .. note:: Si la visita no corresponde a un trabajador de un contratista, deje este campo en blanco.

      .. image:: /imgs/Modulos/Accesos/Accesos34.png
            
      **Estatus**: Estado actual de la visita (**autorizado**, **boletinado**, **baja**, etc.).
          
      .. image:: /imgs/Modulos/Accesos/Accesos35.png

   .. tab-item:: Responder

      Al responder la forma, tenga en cuenta los siguientes puntos:

      - Antes de registrar un visita, asegúrese de recopilar toda la información relevante de la persona, similar a cómo se solicitarían los datos a un trabajador antes de su contratación. Esto permite verificar su identidad antes de permitir el acceso a la ubicación.

      - Solo los visitantes registrados como **autorizados** pueden recibir un pase de entrada (invitación para acceder a la ubicación).

      - Una vez que la visita esté registrada y autorizada, podrá generar un pase de entrada y especificar las áreas a las que el visitante tendrá permitido acceder.

      .. warning:: Registrar una visita **no** significa que el visitante tenga acceso inmediato a la ubicación o a todas las áreas. 

      - La forma actúa como un filtro de seguridad, separando a los visitantes autorizados de aquellos que tienen prohibido el acceso (boletinados). Además, permite actualizar el estado de visitantes que anteriormente eran regulares pero ahora están dados de baja.

      - Cada visita es asignado a un perfil específico. Esta asignación se tratará en secciones posteriores, por el momento, centre el proceso para registrar y autorizar las visitas que necesite.
      
      Observe el siguiente registro de ejemplo:
      
      .. image:: /imgs/Modulos/Accesos/Accesos36.png

      .. note:: Una vez que el estatus de la visita esté **autorizado**, el contratista asociado será notificado por correo electrónico, informándole que su empleado es candidato para recibir pases de entrada. Observe el siguiente correo de ejemplo:

         .. image:: /imgs/Modulos/Accesos/Accesos45.png

      Al crear un nuevo registro en esta forma, la información se sincroniza automáticamente con el `catálogo visita autorizada <#catalog-visita-autorizada>`_ :octicon:`report;1em;sd-text-info`.
      
      .. attention:: Si realiza cambios en la forma, asegúrese de actualizar también el catálogo, verificando que los identificadores de los campos coincidan; Consulte :ref:`flujos` :octicon:`report;1em;sd-text-info` para más detalles.

.. _catalog-visita-autorizada:

Catálogo: ``Visita Autorizada``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo es una réplica de la `forma visita autorizada <#form-visita-autorizada>`_ :octicon:`report;1em;sd-text-info`. Su propósito es mantener la información organizada para su consulta en otras formas y catálogos.
  
.. attention:: Este catálogo está diseñado para recibir registros automáticamente derivados de una forma. Por lo tanto, no es necesario ingresar los datos manualmente. En su lugar, complete la forma correspondiente y LinkaForm sincronizará automáticamente esos registros en el catálogo.

Consulte la forma para obtener más detalles sobre la estructura del catálogo. Observe los siguientes registros de ejemplo:

.. image:: /imgs/Modulos/Accesos/Accesos37.png

Al instalar el módulo, asegúrese de que el catálogo incluya el filtro ``Autorizada``. En caso de que el filtro no exista, consulte la documentación sobre cómo :ref:`crear-filtro` :octicon:`report;1em;sd-text-info` para obtener más detalles y aplique los siguientes valores:

.. code-block::
   :caption: Guarde el filtro con el nombre **Autorizada**

   Campo = Estatus
   Condición = Igual a
   Valor = Autorizado

   // Este filtro mostrará todos los registros de las visitas autorizadas (candidato para recibir un pase de entrada)

Crear Pase de Entrada
---------------------

El proceso de crear un pase de entrada implica la emisión de una invitación formal para permitir el acceso de un visitante a las instalaciones. Durante este proceso, se asignan los permisos correspondientes al perfil del visitante, asegurando que cumpla con los requisitos necesarios antes de ingresar a las áreas designadas de la ubicación.

.. warning:: Antes de continuar con el proceso, asegúrese de contar con la instalación y registros necesarios del :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` y el :ref:`doc-employee` :octicon:`report;1em;sd-text-info`.

Observe el siguiente diagrama y revise las siguientes secciones para obtener más detalles sobre los elementos involucrados y cómo se configuran:

.. image:: /imgs/Modulos/Accesos/Accesos38.png

.. _tipos-vehiculos:

Catálogo: ``Tipos de Vehículos``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo contiene los diferentes tipos de vehículos que pueden ser registrados para las visitas. Revise las siguientes pestañas para obtener más detalles sobre la estructura del catálogo y ejemplos de registros.

.. tab-set::

   .. tab-item:: Estructura

      Este catálogo incluye los siguientes campos:

      - **Tipo de Vehículo**: Describe la categoría del vehículo, como automóvil, camioneta, moto, entre otros.
      - **Marca**: Indica la marca del vehículo, por ejemplo, Toyota, Ford, Honda, etc.
      - **Modelo**: Especifica el modelo del vehículo, proporcionando más detalles sobre la versión o variante de la marca.

      .. image:: /imgs/Modulos/Accesos/Accesos68.png

   .. tab-item:: Registros

      Cada registro representa información específica sobre un vehículo.

      .. image:: /imgs/Modulos/Accesos/Accesos69.png

      .. note:: Al instalar el módulo, se incluyen registros precargados que abarcan la mayoría de los vehículos existentes. Sin embargo, considere agregar más registros según lo requiera.

.. _form-pase-entrada:

Forma: ``Pase de Entrada``
^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta forma gestiona la creación y administración de los pases de entrada para visitantes. Al generar un pase, se asigna un perfil al visitante, que incluye permisos con requisitos que deben cumplirse para ingresar. El perfil seleccionado determina las áreas permitidas dentro de la ubicación, asegurando que el visitante solo acceda a los espacios autorizados según su rol y cumplimiento de los permisos establecidos.

Esta forma permite configurar toda la información relevante para autorizar el pase, como a quién visitará, el propósito, la duración, el por qué y para qué necesita acceder a las instalaciones.

.. warning:: Asegúrese de contar con los procesos y registros necesarios mencionados anteriormente en esta documentación.

Para responder la forma, revise las siguientes pestañas que detallan los campos necesarios para generar un pase de entrada. Asegúrese de prestar atención a la información proporcionada y las notas importantes.

.. tab-set::

   .. tab-item:: Selección de Visitante

      **Selección de Visitante**: Persona para la cual se generará el pase de entrada.

      Una vez que haya seleccionado al visitante y el pase esté en estado **Activo**, consulte el siguiente flujo que ilustra las acciones involucradas en la creación del pase de entrada. Para más detalles sobre las opciones, consulte el menú desplegable a continuación.

      .. image:: /imgs/Modulos/Accesos/Accesos65.png

      .. dropdown:: Opciones


         .. tab-set::

            .. tab-item:: Alta de Nuevo Visitante

               .. grid:: 2
                  :gutter: 0

                  .. grid-item-card::
                     :columns: 6

                     **Alta de Nuevo Visitante**: Permite registrar un nuevo visitante que aún no está en el catálogo de `visitas autorizadas <#catalog-visita-autorizada>`_ :octicon:`report;1em;sd-text-info`. Al seleccionar esta opción, llene los siguientes campos:

                     .. hint:: Utilice esta opción para registrar visitas que no implican grandes responsabilidades, como visitas espontáneas o asuntos personales.

                     - **Nombre Completo**: Nombre del visitante.

                     - **Email**: Correo electrónico del nuevo visitante.
                     
                     - **Teléfono**: Número de teléfono del nuevo visitante.

                     - **Empresa**: Empresa a la que pertenece el visitante.

                     .. note:: Si la visita no corresponde a un trabajador de un contratista, deje este campo en blanco.

                     - **Fotografía**: Imagen de la persona que realiza la visita.

                     - **Identificación**: Documento de identificación oficial.

                  .. grid-item-card::   
                     :columns: 6

                     .. image:: /imgs/Modulos/Accesos/Accesos47.png

               .. attention:: Al registrar un nuevo visitante, este deberá completar su proceso de registro. Consulte y envíe la documentación del **proceso registro visitantes** :octicon:`report;1em;sd-text-info` a quien corresponda, para más detalles sobre cómo finalizar el registro.

               .. hint:: Considere ajustar la estructura de la forma según el nivel de detalle de los datos que necesite recopilar.

            .. tab-item:: Buscar Visitantes Registrados

               .. grid:: 2
                  :gutter: 0

                  .. grid-item-card::
                     :columns: 6

                     **Buscar visitantes registrados**: Muestra la lista de visitas autorizadas definidas en el catálogo `visita autorizada <#catalog-visita-autorizada>`_ :octicon:`report;1em;sd-text-info`.

                     .. note:: Si anteriormente registró una visita y no aparece en la lista, revise el catálogo y verifique que el estatus de la visita sea **Autorizada**

                     - **Pase a Nombre de**: Visitante autorizado candidato para el pase de entrada. 
                     
                     .. hint:: Verifique los datos proporcionados, especialmente el email y si es necesario, modifique la información en la forma correspondiente.

                  .. grid-item-card::
                     :columns: 6

                     .. image:: /imgs/Modulos/Accesos/Accesos48.png
                        :width: 372 px

               .. attention:: Al seleccionar una visita registrada y solo si el pase de entrada está **Activo**, el visitante recibirá un correo electrónico con la información de la ubicación, los documentos necesarios para su ingreso y un código QR, el cual será escaneado por el personal de seguridad al llegar a la caseta, facilitando su entrada a la ubicación.
                  
                  Observe el siguiente ejemplo de correo para un pase de entrada activo.

                  .. image:: /imgs/Modulos/Accesos/Accesos49.png
                     :width: 600 px

   .. tab-item:: Ubicación

      **Ubicación**: Ubicación a la que se invita al visitante.

      .. seealso:: Revise el catálogo **ubicaciones** del :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` para más detalles.

      .. image:: /imgs/Modulos/Accesos/Accesos50.png

   .. tab-item:: Tipo de Pase

      **Tipo de Pase**: Perfil del visitante. El perfil seleccionado determina los permisos o certificaciones que el visitante debe cumplir para acceder a la ubicación. 
         
      .. attention:: Si selecciona un perfil diferente a **Visita General**, el contratista del empleado deberá completar el proceso de :ref:`carga-permisos-visitas` :octicon:`report;1em;sd-text-info`.

      .. admonition:: Ejemplo
         :class: pied-piper

         Observe los siguientes ejemplos que ilustran la diferencia entre perfiles. Mientras que el perfil **Visita General** no requiere permisos, un perfil como **Técnico de Telecomunicaciones** sí los exige.

         .. image:: /imgs/Modulos/Accesos/Accesos51.png
            
         .. image:: /imgs/Modulos/Accesos/Accesos52.png

   .. tab-item:: Visita a

      **Visita a**: Personas a la que visitará (opcionalmente).

      .. seealso:: Revise el catálogo **configuración áreas y empleados** del :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` para más detalles.

      .. image:: /imgs/Modulos/Accesos/Accesos53.png

      .. hint:: Si observa que en el catálogo muestra empleados pertenecientes a otra ubicación, asegúrese de que, en la forma, el catálogo esté correctamente relacionado con el catálogo **Ubicaciones** para filtrar correctamente a las personas según su ubicación.
         
         Consulte el :ref:`campo-catalogo` :octicon:`report;1em;sd-text-info`, específicamente el menú desplegable **Relacionar**, para obtener más información sobre como relacionar catálogos.

   .. tab-item:: Autorizado por

      **Autorizado por**: Empleado responsable de aprobar el pase de entrada.

      .. seealso:: Consulte el catálogo **Configuración de Áreas y Empleados de Apoyo** en el :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` para más detalles.

      .. image:: /imgs/Modulos/Accesos/Accesos54.png
      
      .. hint:: Si observa que en el catálogo muestra empleados de otra ubicación, asegúrese de que, en la forma, el catálogo esté correctamente relacionado con el catálogo **Ubicaciones** para filtrar correctamente a las personas según su ubicación.
         
         Consulte el :ref:`campo-catalogo` :octicon:`report;1em;sd-text-info`, específicamente el menú desplegable **Relacionar**, para obtener más información sobre como relacionar catálogos.

   .. tab-item:: Visita de

      **Visita de**: Este campo permite configurar la vigencia y acceso para la visita.

      .. .. image:: /imgs/Modulos/Accesos/Accesos55.png

      **Fecha Fija**: El pase es válido para un solo día, útil para visitas espontaneas. 
                  
      .. warning:: Si selecciona esta opción, deberá especificar la **fecha de vigencia** y la **hora límite** del pase. Esto significa que el pase será válido desde el inicio del día seleccionado hasta la hora indicada. Por ejemplo, si establece la hora límite a las 7:56 p.m., el pase será válido hasta esa hora y luego se considerará vencido.

      .. image:: /imgs/Modulos/Accesos/Accesos56.gif
      
      **Rango de fechas**: El pase es válido durante un rango de fechas, ideal para visitas recurrentes.

      Si selecciona esta opción, debe especificar lo siguiente:

      1. Especifique la fecha inicial y fecha final del pase.
      2. Seleccione los días de acceso entre las siguientes opciones:

      - **Cualquier dia**: La visita puede acceder cualquier día dentro del rango de fechas seleccionado.
      - **Limitar Días de Acceso**: Especifica los días y las veces permitidas dentro del rango en los que el visitante tendrá acceso.

      .. grid:: 2
         :gutter: 0

         .. grid-item-card::
            :columns: 6

            - **Limitar número de accesos a**: Define cuántas veces por día la visita puede ingresar.

            .. attention:: Si no se especifica una cantidad, se asume que no hay límite de entradas por día.

            - **Seleccione los días de acceso**: Días específicos en los que la visita tendrá permiso para acceder.

            .. warning:: Aunque el pase tenga un rango de fechas vigente, si no selecciona los días de acceso, podría causar problemas en la caseta de seguridad, ya que el sistema indicaría que en esos días la visita no debe estar en las instalaciones.

         .. grid-item-card::
            :columns: 6

            .. image:: /imgs/Modulos/Accesos/Accesos57.gif

   .. tab-item:: Areas de Acceso

      **Áreas de Acceso**: Áreas a las que el visitante tendrá permiso de ingresar.

      .. image:: /imgs/Modulos/Accesos/Accesos58.png

      .. seealso:: Consulte el catálogo **áreas de las ubicaciones** del :ref:`doc-ubicaciones` :octicon:`report;1em;sd-text-info` para más detalles.

      .. hint:: Si el catálogo muestra áreas de otra ubicación, verifique que en la forma el catálogo esté correctamente relacionado con el catálogo **Ubicaciones** para que solo se muestren las áreas correspondientes.
         
         Consulte el :ref:`campo-catalogo` :octicon:`report;1em;sd-text-info`, específicamente el menú desplegable **Relacionar**, para obtener más información sobre como relacionar catálogos.

   .. tab-item:: Vehículos

      **Vehículos**: Grupo repetitivo que permite registrar los vehículos asociados con la visita.

      .. image:: /imgs/Modulos/Accesos/Accesos59.png

      .. attention:: Generalmente, este grupo repetitivo se deja vacío. Si se conoce el vehículo que traerá la visita, puede registrarlo aquí. En la mayoría de los casos, esta forma se utiliza para almacenar los datos obtenidos de la aplicación web :ref:`doc-soter` :octicon:`report;1em;sd-text-info`. Regularmente, el campo se completa cuando el guardia de seguridad revisa los datos de la visita y registra el vehículo con el que ingresa.

      Los campos que componen al grupo repetitivo son:

      - **Tipo de Vehículo**, **Marca** y **Modelo**.

      .. seealso:: Consulte el catálogo `Tipos de Vehículos <#tipos-vehiculos>`_ :octicon:`report;1em;sd-text-info` para más detalles.

      - **Estado del Vehículo**

      .. seealso:: Consulte el catálogo **Estados** del :ref:`doc-base` :octicon:`report;1em;sd-text-info` para más detalles.

      - **Placas**
      - **Color**

   .. tab-item:: Equipos

      **Equipos**: Grupo repetitivo que permite registrar los equipos que el visitante llevará consigo durante su estancia.

      .. image:: /imgs/Modulos/Accesos/Accesos60.png

      - **Tipo de Equipo**: Clasificación del equipo o dispositivo.
      - **Nombre del Artículo**: Descripción o denominación específica del equipo.
      - **Marca**: Marca o fabricante del equipo (opcionalmente).
      - **Número de Serie**: Identificador único del equipo (opcionalmente).
      - **Color**

      .. attention:: Normalmente, este grupo repetitivo se deja vacío. Si se conoce con anticipación los equipos que el visitante traerá, puede registrarlo aquí. En la mayoría de los casos, esta sección se utiliza para almacenar la información proporcionada posteriormente por el guardia de seguridad, quien registra los equipos que el visitante lleva consigo al ingresar.

   .. tab-item:: Comentarios/Instrucciones

      **Comentarios/Instrucciones para la Visita**: Añada comentarios o instrucciones importantes según el tipo seleccionado.

      .. image:: /imgs/Modulos/Accesos/Accesos61.png
      
      - **Instrucción o comentario**: Detalles relacionados con la visita.

      - **Tipo de comentario**: 
         - **Pase**: El comentario será dirigido al visitante.
         - **caseta**: El comentario estará dirigido al guardia de seguridad.

   .. tab-item:: Estatus

      **Estatus del Pase**: Define el estado actual del pase de entrada para la visita.
      
      .. grid:: 2
         :gutter: 0

         .. grid-item-card::
            :columns: 6

            - **Proceso**: El pase está en espera o aún no ha sido autorizado.
            - **Activo**: El pase ha sido aprobado y está vigente, permitiendo el acceso del visitante.
            - **Vencido**: El pase ha expirado y ya no es válido para ingresar.

         .. grid-item-card::
            :columns: 6

            .. image:: /imgs/Modulos/Accesos/Accesos62.png

      .. attention:: Cuando el estado del pase de entrada es **Activo**, se enviará automáticamente un aviso y el gafete con un código QR del pase de entrada al correo electrónico del visitante. Este código deberá presentarse en la caseta de seguridad para permitir el acceso.

         Observe el siguiente ejemplo:
            
         .. image:: /imgs/Modulos/Accesos/Accesos64.png
            :width: 600px

   .. tab-item:: QR
      
      Los siguientes campos se generan automáticamente a través de un script. Estos permanecen ocultos ya que no requieren interacción del usuario. 

      .. image:: /imgs/Modulos/Accesos/Accesos63.png

      - **QR**: Código QR generado para el pase de entrada.
      - **QR Code**: Identificador del pase de entrada.

.. attention::

   Los registros de esta forma son utilizadas en otras formas, por lo que es necesario que estén disponibles también en un catálogo. Los registros de esta forma deben estar sincronizados con el `catálogo pase de entrada <#catalog-pase-entrada>`_ :octicon:`report;1em;sd-text-info`. Para más detalles, consulte el catálogo y revise los siguientes ejemplos de registros:

   .. image:: /imgs/Modulos/Accesos/Accesos66.png
      :width: 880px

.. _catalog-pase-entrada:

Catálogo: ``Pase de Entrada``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Este catálogo contiene los mismos registros que de la forma `pase de entrada <#form-pase-entrada>`_ :octicon:`report;1em;sd-text-info`. 

Su estructura es similar a la de la forma, pero a diferencia de esta, los catálogos no pueden incluir campos de grupo repetitivo. Sin embargo, es posible sincronizar registros entre la forma y el catálogo, omitiendo la información de los grupos repetitivos. Por lo tanto, no es necesario completar el catálogo manualmente; simplemente complete la forma para crear un pase de entrada y LinkaForm se encargará de sincronizar automáticamente el registro en este catálogo.

.. note:: Para asegurarse de que la sincronización funcione correctamente, si se agregan nuevos campos (que no sean grupos repetitivos) en la forma, asegúrese de incluirlos también en el catálogo.

Para más detalles de la estructura consulte la forma y observe los registros que se presentan a continuación:

.. image:: /imgs/Modulos/Accesos/Accesos67.png
   :width: 880px

.. LIGAS EXTERNAS

.. |linkaform| raw:: html

   <a href=**https://www.linkaform.com/** target=**_blank**>LinkaForm</a>