.. _doc-manual-soter:

============
Manual Soter
============

Este manual es una guía detallada sobre el uso de las funcionalidades de **Soter**, proporciona ejemplos, tutoriales paso a paso y soluciones a problemas comunes para facilitar su uso.  

La siguiente información está dirigida principalmente a **guardias de seguridad** y **personal administrativo**, quienes gestionan las entradas y salidas de visitantes, así como todos los aspectos relacionados con la **seguridad física** de las instalaciones.  

.. hint:: Para una mejor comprensión, el manual sigue una estructura **cronológica**, presentando las funcionalidades en el orden en que se utilizan dentro del sistema. Se recomienda seguir la lectura en secuencia para familiarizarse progresivamente con cada funcionalidad y su aplicación.

Requisitos previos
==================

Para utilizar el sistema **Soter** de manera óptima, es importante cumplir con los siguientes requisitos previos:

**Navegador compatible**

El sistema es compatible con los navegadores más utilizados, incluyendo:

- Google Chrome (versión más reciente)
- Mozilla Firefox (versión más reciente)
- brave web browser (versión más reciente)

**Resolución de pantalla** 

Aunque **Soter** es adaptable a cualquier dispositivo, se recomienda una resolución mínima de 1024x768 píxeles para una visualización adecuada en computadoras de escritorio y tablets. 

En dispositivos móviles, la interfaz se ajusta automáticamente para facilitar la navegación. 

.. warning:: Actualmente, la versión responsiva presenta algunos detalles de ajuste menores, que **no** comprometen la funcionalidad general del sistema.

**Conexión a internet**

Se requiere una conexión a internet estable para acceder a las funcionalidades de **Soter** y garantizar que los datos se registren y sincronicen correctamente.

**Conocimientos básicos de computación**

Se recomienda que los guardias de seguridad tengan conocimientos básicos en el uso de computadoras y navegación web. Sin embargo, **Soter** ha sido diseñado con una interfaz intuitiva y fácil de usar, por lo que incluso aquellos usuarios que no estén familiarizados con la tecnología encontrarán el sistema accesible y sencillo de manejar. 

.. _soter-notificacion-cuenta:

Notificación de Activación de Cuenta  
====================================

Para acceder a **Soter**, recibirá un correo de notificación con los detalles de su cuenta. Siga estos pasos para revisar la notificación:  

1. Ingrese a su |gmail| :octicon:`report;1em;sd-text-info`.
2. Revise el correo con el asunto “📢 ¡Bienvenido! Empieza a usar Soter hoy mismo”.

.. hint:: Si no encuentra el correo en su bandeja de entrada, revise la carpeta de **Spam** o **Correo no deseado**.  

3. Lea las instrucciones del correo.

   - El mensaje indicará que su cuenta ha sido activada y está lista para usarse.
   - También incluirá su usuario y un enlace para acceder a **Soter**.

   .. important:: La contraseña de su cuenta será enviada por su administrador.

   .. image:: /imgs/Soter/Soter111.png
    :width: 600px

.. warning::  

   - Solo podrá ingresar a **Soter** si su cuenta ha sido activada por el administrador.  
   - Si no recibe el correo, contacte a su administrador para confirmar su registro.

Iniciar Sesión
==============

Para iniciar sesión, siga los siguientes pasos:

1. En el navegador de su preferencia, ingrese al siguiente enlace: 

.. code-block::
    
    https://app.soter.mx

.. seealso:: Haga clic en el botón proporcionado en el correo de notificación de su cuenta o acceda directamente |aqui| :octicon:`report;1em;sd-text-info`.

2. Escriba el username y la contraseña en los campos correspondientes.

.. warning:: En caso de no disponer de credenciales, solicítelas al administrador de su empresa y revise la `notificación de activación <#soter-notificacion-cuenta>`_ :octicon:`report;1em;sd-text-info` de su cuenta.

3. Presione el botón ``Continuar``. Será redirigido automáticamente al menú principal.

   .. image:: /imgs/Soter/Soter1.png
    :width: 600px

Menú Principal
==============

El menú principal de **Soter** proporciona acceso a diversas funcionalidades, dependiendo del **rol del usuario** y la **configuración establecida por el administrador**.  

Cada usuario verá y podrá utilizar únicamente las funciones autorizadas para su perfil. En este ejemplo, se muestran todas las funcionalidades disponibles en el sistema, pero el acceso a cada una dependerá de los permisos asignados.  

Las opciones del menú pueden incluir:  

- **Pases de Entrada**: Gestión y creación de accesos para visitantes.  
- **Turnos / Accesos**: Administración de turnos.  
- **Bitácoras**: Registro de entradas y salidas.
- **Objetos Perdidos**: Control y seguimiento de artículos extraviados.  
- **Artículos Concesionados**: Gestión de objetos entregados en custodia o préstamo.  
- **Incidencias**: Reporte y seguimiento de eventos que afecten la seguridad.  
- **Notas**: Registro de información relevante para el personal de seguridad.  

.. image:: /imgs/Soter/Soter112.png

.. note::

    - Si un usuario no visualiza una función en el menú, significa que no tiene los permisos correspondientes.  
    - Los administradores pueden modificar los accesos desde la configuración del sistema.  
    - Para solicitar permisos adicionales, contacte al administrador del sistema.  

.. toctree::
    :maxdepth: 1
    :titlesonly:
    :hidden:

    Turnos
    Notas
    Accesos
    Bitacoras
    Incidencias
    Fallas
    Pases
    
.. LIGAS DE INTERÉS EXTERNO 

.. |Soter| raw:: html

    <a href="https://app.soter.mx/" target="_blank">Soter</a>
    
.. |aqui| raw:: html

    <a href="https://app.soter.mx/" target="_blank">aquí</a>

.. |linkaform| raw:: html

   <a href="https://www.linkaform.com/" target="_blank">LinkaForm</a>

.. |gmail| raw:: html

   <a href="https://mail.google.com//" target="_blank">correo electrónico</a>
   