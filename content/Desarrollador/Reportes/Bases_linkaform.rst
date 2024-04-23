.. _bases-linkaform-reportes:

==================
Bases de Linkaform
==================

Los reportes son una funcionalidad que brinda a los clientes de Linkaform una perspectiva visual, resumida y agradable de los datos recopilados de las **formas** a través de elementos como filtros, gráficos y tablas.

A lo largo de la documentación, encontrará orientación sobre los aspectos necesarios para la creación de sus propios reportes personalizados.

.. important:: Tenga en cuenta que el desarrollo de reportes se basa en la información recopilada de las formas (formularios digitales), por lo que es importante que comprenda su funcionamiento. Consulte el siguiente :ref:`section-forms` :octicon:`report;1em;sd-text-info` para más información.

Subdominios
===========

Linkaform cuenta con una serie de subdominios que le serán útiles al momento de desarrollar reportes.

Producción
----------

Es la versión que está en línea y disponible para los clientes finales en tiempo real. Para acceder, siga los pasos:

1. Ingrese a la plataforma web en |Producción| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales habituales.

.. note:: En caso de no contar con credenciales, solicite asistencia a soporte técnico.

Preproducción
-------------

Es una copia de producción en su estado más reciente, utilizada para realizar pruebas sin riesgos en caso de cometer errores. Para acceder, siga los pasos:

1. Ingrese a la plataforma web en |Preproducción| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con su correo habitual, pero solicite a soporte la contraseña necesaria.

.. warning:: Tenga en cuenta que cada proceso que realice en **producción** y **preproducción** es similar. Sin embargo, es importante que considere que todo lo que se haga en **preproducción** será reemplazado por los datos de **producción** en cargas que se realizan cada semana. 

FAQ
---

Es la página donde podrá encontrar preguntas frecuentes sobre funcionalidades especificas de LinkaForm. Aquí podrá realizar sus preguntas a través de publicaciones o consultas con otros usuarios relacionados. 

Para acceder, ingrese a |faq| :octicon:`report;1em;sd-text-info`.

Acceder a reportes
==================

Para acceder a los ``Reportes``, siga los pasos:

1. Ingrese a la plataforma web en |Producción| :octicon:`report;1em;sd-text-info` o |Preproducción| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales.
3. Seleccione la opción ``Reportes`` en el menú lateral. 

.. tip:: Presione el símbolo ``>`` para visualizar el nombre de las opciones del menú lateral.

.. image:: /imgs/Reportes/Reportes1.png

Ver reporte
===========

Para examinar un reporte en detalle, siga los siguientes pasos:

1. Inicie sesión en la plataforma web en |Producción| :octicon:`report;1em;sd-text-info` o |Preproducción| :octicon:`report;1em;sd-text-info`.
2. Seleccione la opción ``Reportes`` en el menú lateral. 
3. Identifique el reporte de su interés.
4. Presione el icono de engrane, seguido de ``Ver reportes`` o elija el tercer icono. Será redirigido al reporte correspondiente. 

.. image:: /imgs/Reportes/Reportes2.png

En términos generales, observe la siguiente imagen que describe los elementos básicos presentes en un reporte.

.. image:: /imgs/Reportes/Reportes3.png

Crear carpeta
=============

Crear una carpeta le permitirá almacenar uno o más reportes dentro de ella. Siga los siguientes pasos:

1. Inicie sesión en la plataforma web en |Producción| :octicon:`report;1em;sd-text-info` o |Preproducción| :octicon:`report;1em;sd-text-info`.
2. Diríjase y seleccione la opción ``Reportes``.
3. Haga clic en el icono sobre ``Carpeta`` ubicada en el menú superior derecho.

.. image:: /imgs/Reportes/Reportes6.png

4. Escriba el nombre de la ``Carpeta``.
5. Presione ``Crear``.

Compartir Carpeta/Reporte
=========================

Compartir una carpeta o un reporte es un proceso sencillo. Siga los pasos:    

1. Inicie sesión en la plataforma web en |Producción| :octicon:`report;1em;sd-text-info` o |Preproducción| :octicon:`report;1em;sd-text-info`.
2. Diríjase y presione la opción ``Reportes`` en el menú lateral.
3. Identifique la carpeta o reporte de su interés.
4. Presione el icono de engrane, seguido de la opción ``Compartir`` o haga clic en el segundo ícono de compartir.

.. image:: /imgs/Reportes/Reportes4.png

5. Ingrese el nombre del usuario con el que desea compartir la carpeta o el reporte y presione ``Enter``. Observe que el nombre del usuario aparecerá en la parte inferior de la ventana.

.. attention:: Compartir un reporte es útil para que otros usuarios puedan visualizar y consultar datos de una o varias formas, según la finalidad del reporte. Sin embargo, al compartir un reporte, también es necesario compartir los elementos que lo componen, es decir, la forma, catálogos o cualquier otro recurso del cual el reporte consulte la información.
    
    Revise :ref:`compartir` :octicon:`report;1em;sd-text-info` y :ref:`compartir-cat` :octicon:`report;1em;sd-text-info` para más detalles. 

.. image:: /imgs/Reportes/Reportes5.png

.. note:: Observe la diferencia entre los permisos permitidos para diferentes usuarios: 

    Cuando comparte cualquier elemento con algún miembro perteneciente a la misma cuenta padre que la suya, puede otorgarle el permiso de ``Admin``. Sin embargo, al compartir un elemento con un usuario perteneciente a otra cuenta padre diferente a la suya pero dentro del mismo sistema de Linkaform, se establece una **conexión**, lo que significa que se limita a otorgarle permisos que puedan afectar al elemento compartido.

6. Establezca al usuario el permiso que requiera. Tenga en cuenta las descripciones:

- **Lectura**: El usuario puede ver todos los reportes dentro de la carpeta. 
- **Compartir**: El usuario puede ver y compartir la carpeta o el reporte con otros usuarios. 
- **Admin**: El usuario tiene los mismos privilegios que los perfiles anteriores, pero puede modificar y eliminar los reportes o la carpeta.
- **Borrar registros**: Al activar esta opción, el usuario puede eliminar los reportes. Si no se activa, el usuario no puede eliminar los reportes, incluso si tiene el perfil de ``Admin``.

.. warning:: Cuando comparte una carpeta, los reportes que contiene heredan automáticamente los permisos. Sin embargo, tenga cuidado al compartir un reporte e intentar moverlo a una carpeta diferente, ya que esto puede causar problemas con los permisos y otras acciones inesperadas.

.. tip:: 
    
    Si necesita mover un reporte a una carpeta, simplemente arrástrelo al lugar necesario. 
    
    Si necesita mover un reporte fuera de alguna carpeta, a la raíz, simplemente arrástrelo a la columna principal.

Para editar el nombre de un carpeta o reporte, siga los siguientes pasos:

.. grid:: 2
    :gutter: 0
    :padding: 0
    :margin: 0

    .. grid-item-card:: 
        :columns: 3
        :padding: 0
        :margin: 0

        .. image:: /imgs/Reportes/Reportes9.png
            :width: 400
            :height: 200

    .. grid-item-card:: 
        :columns: 9
        :padding: 0
        :margin: 0

        1. Identifique la carpeta o reporte de su interés.
        2. Presione el icono de engrane, seguido de ``Editar``.
        3. Ingrese el nuevo nombre.
        4. Haga clic en ``Renombrar``.

.. _config-reporte:

Crear reporte
=============

Crear un reporte en Linkaform es un proceso sencillo. Siga el siguiente procedimiento teniendo en cuenta las notas y recomendaciones:

.. warning:: Tenga en cuenta que estos son los pasos que debe seguir para configurar el reporte (previamente preparado) en su cuenta de Linkaform; sin embargo, **no** constituyen la totalidad del proceso.

1. Inicie sesión en la plataforma web en |Producción| :octicon:`report;1em;sd-text-info` o |Preproducción| :octicon:`report;1em;sd-text-info`.

.. important:: El proceso de configuración en producción y preproducción es idéntico. Sin embargo, se recomienda iniciar el proceso de creación de reportes en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

2. Seleccione la opción ``Reportes`` en el menú lateral. 
3. Presione el icono de archivo, ubicado en la parte superior.

.. image:: /imgs/Reportes/Reportes7.png

.. tip:: Pase el cursor sobre las opciones para conocer las funcionalidades que ofrecen.

4. Configure el reporte teniendo en cuenta lo siguiente:

- **Nombre del Reporte**: Identificador del reporte, no necesariamente es el mismo que se visualiza al consultar el reporte.
- **URL**: Dirección del reporte. 

.. note:: En la siguiente figura, observe que se está asignando la ``URL`` de servido. Consulte la sección :ref:`url-acceso` :octicon:`report;1em;sd-text-info`, específicamente :ref:`link-servido` :octicon:`report;1em;sd-text-info` para más detalle.
 
- **Script**: Nombre del script previamente desarrollado en lenguaje Python. 

.. attention:: Asegúrese de `cargar el script <#cargar-script>`_ :octicon:`report;1em;sd-text-info`. Automáticamente, el ``ID`` del **script** se enviará como parámetro en la ``URL``, especificando al reporte en dónde deberá consultar la data. 
    
    Por esta razón, la **URL** solo incluye la estructura del reporte ya que el script es dinámico.

.. image:: /imgs/Reportes/Reportes8.png

5. Presione el botón ``Cargar``.

Si necesita editar las configuraciones de su reporte, simplemente presione el icono de engranaje, seguido de ``Editar`` y modifique su reporte según las instrucciones anteriores.

.. image:: /imgs/Reportes/Reportes9.png

.. _cargar-script:

Cargar script
=============

Para cargar un script en la plataforma de Linkaform, siga los siguientes pasos y lea las recomendaciones necesarias.

.. caution:: Tenga en cuenta que los siguientes pasos son necesarios para configurar el script previamente desarrollado.

    Antes de realizar esta configuración, asegúrese de haber creado el script de acuerdo a sus requerimientos. Revise la sección :ref:`crear-script` :octicon:`report;1em;sd-text-info` para más detalles.

1. Inicie sesión en la plataforma web en |Producción| :octicon:`report;1em;sd-text-info` o |Preproducción| :octicon:`report;1em;sd-text-info`.

.. important:: El proceso de configuración en producción y preproducción es idéntico. Sin embargo, se recomienda iniciar el proceso de creación de reportes en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

2. Seleccione ``Formas > Scripts`` en el menú lateral.
3. Seleccione el icono de documento ubicado en la parte superior derecha.

.. image:: /imgs/Reportes/Reportes31.png

Complete el formulario de acuerdo a los siguientes pasos:

1. Seleccione el archivo correspondiente al script. Automáticamente, se rellenará el nombre del script.
2. Seleccione la imagen de Docker (versión del contenedor de scripts):

- ``python3_lkf:latest`` es la imagen que actualmente se utiliza; usa la version 3 de python.
- ``python:development`` **no** se usa para scripts actuales; utiliza la version 2 de python.

.. hint:: Ingrese el número 3, automáticamente aparecerá la opción utilizada.

    .. image:: /imgs/Reportes/Reportes32.1.png

3. Seleccione los bullets que considere:

- **Activity**: Active el bullet si desea que la actividad (ejecuciones exitosas o fallas) del script le sea notificada por correo electrónico a la cuenta padre.
- **Pública**: Active el bullet si desea consultar el script a través de un ``fetch``, sino está indicando que desea consultar el script a través del ``JWT`` del usuario que hace la consulta del script. 
Es decir, verifica a través del ``token`` si el usuario tiene los permisos necesarios para consultar el script. 

Active el bullet si deasea que 

.. image:: /imgs/Reportes/Reportes32.png

.. _visualizar-id-script:

Ver ``ID`` del script
---------------------

Hay dos maneras para consultar el id de un script.

**Log de script**

Para consultar a través del log de flujo, siga los siguientes pasos:

1. Ubíquese en la interfaz de scripts.
2. Identifique el script del cual necesita conocer el ``id``.
3. Seleccione el icono ``Ejecutar script`` para generar el log del script.

.. note:: Solo ejecute si aún no tienen ningún log.

4. Presione el icono ``Log de script``.

.. image:: /imgs/Reportes/Reportes35.png

5. Seleccione ``Log``.
6. Presione ``Ctrl + f`` para abrir el buscador de la página.
7. Escriba:

.. code-block::

    script_id.

8. Copie y pegue el ``script_id`` según lo requiera. 

.. image:: /imgs/Reportes/Reportes36.png

**Herramientas de desarrollador**

Para utilizar las herramientas de desarrollador, siga los pasos:

1. Ubíquese en la interfaz de scripts.
2. Presione ``Clic derecho > Inspeccionar`` o bien presione ``F12``.
3. Ubíquese en la pestaña ``Network``.
4. Recargue la página sin cerrar la ventana de inspección.
5. Identifique el script que necesite saber el ``id``.
6. Seleccione la opción ``Compartir``. 

.. image:: /imgs/Reportes/Reportes33.png

7. Identifique la línea ``file_shared_email/?file_shared=`` en el inspector de código.
8. Copie y pegue el ``id``.

.. image:: /imgs/Reportes/Reportes34.png

.. _log-script:

Log de script
=============

El registro de script es una funcionalidad útil que se utiliza para depurar y verificar la correcta ejecución de los scripts.

Para visualizar el log de un script, siga los siguientes pasos:

.. grid:: 2
    :gutter: 0
    :padding: 0
    :margin: 0

    .. grid-item-card:: 
        :columns: 8
        :padding: 0
        :margin: 0

        1. Inicie sesión en la plataforma web de Linkaform en |Producción| :octicon:`report;1em;sd-text-info` o en |Preproducción| :octicon:`report;1em;sd-text-info`.
        2. Seleccione ``Formas > Scripts`` en el menú lateral. Podrá observar todos los scripts cargados en la cuenta.
        3. Identifique el script de su interés.

    .. grid-item-card:: 
        :columns: 4
        :padding: 0
        :margin: 0

        .. image:: /imgs/Reportes/Reportes24.png

4. Presione el icono play para ejecutar el script.

.. image:: /imgs/Reportes/Reportes25.png

5. Presione el último icono, ``Log de Script``. Esto abrirá un modal donde encontrará el historial e información útil, como fechas de ejecución y estado del script. Preste mucha atención al estado, ya que le indicará si la ejecución del script fue exitosa o no.

.. image:: /imgs/Reportes/Reportes25.1.png

6. Presione la opción ``log`` para más detalles.

.. seealso:: Consulte la siguiente sección sobre la `interpretación del log <#interpretacion-log-script>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. image:: /imgs/Reportes/Reportes26.png

.. _interpretacion-log-script:

Interpretación log de script
----------------------------

El registro del script le proporciona información util de la ejecución del script.

Regularmente, en la interpretación del log se analizan las consultas a la base de datos (querys), errores de ejecución, peticiones y otros datos relevantes relacionados con el script.

Toda la información en el log del registro se genera gracias a la línea de código ``print(sys.argv)`` del script. Esta línea imprime una cadena de objetos JSON con los argumentos de la línea de comandos, lo cual es útil para debuggear código en Python.

La variable sys.argv es una lista que contiene los argumentos pasados al script en la línea de comandos. Al imprimir sys.argv, se puede verificar si los argumentos que esperaba están siendo pasados correctamente al script y entender la estructura y valores de esos argumentos.

Regularmente, lo que imprime ``sys.argv`` son tres argumentos, de los cuales el tercero o de la ``posición [2]`` es la más importante:

- El primer elemento es la ruta del script Python que se está ejecutando (línea 10).
- El segundo elemento representa objetos JSON, como el ``jwt`` y ``data`` (línea 12 y 14).

.. important:: El objeto ``data`` es el más importante, ya que contiene los filtros y parámetros utilizados en la ``URL`` que se utilizan para tratar la información. 

    .. code-block:: python
        :linenos:
        
        "data": {"promotor": "", "script_id": 123, "date_from": "2023-11-29", "option": 1, "date_to": "2023-12-29"},
       
    En la mayoría de scripts, los filtros más utilizados corresponden a las fechas (``date_to``, ``date_from`` o alguna otra fecha específica). Dependerán de los requerimientos del reporte.

.. code-block:: python
    :linenos:
    :emphasize-lines: 10, 12, 14

    ==== LOG FOR SCRIPT reporte_visitas.py ==== 
    Host: swarm1.lkf.cloud 
    Running on Image: linkaform/python3_lkf:latest 
    Start Date: 2023-12-29 16:04:24.796816+00:00 
    End Date: 2023-12-29 16:04:26.348783+00:00 
    =========== TRACEBACK ============= 
    =========== END ============= 

    =========== OUTPUT ============= 
    ['/srv/backend.linkaform.com/infosync-api/backend/media/uploads/public-client-11702/scripts/reporte_visitas.py', '{}', 

    '{"jwt": "Bearer zI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI0X2lkIjoxMTcwMiwiaXNfbW9iaWxlIjFpbCI6InZhcmVua2FzZkBnbWFpbC5jb20ifQ.b-xZSl8i1EsoCTIf8Oi1Cj8lcg0_79URc6S94UO_pvd20NmG_Ome71vd6pAULSfjxlLjirYHRIwl1w4VzSOumTipN2wVp5JWeFKJ8-hAKCSoSW8CQi9PgSxnlT0UK-pOt6R7olvIbQVE_vWJbQqL4n8r5_FsTXW4jLiRVyQ9AIcmIL_IFfBZtRKAr5dTabTAjfq1wSJtW-3CWPdR_0IcvOlavjPNWfAdlq5R1e6_-Q6rjDyLDzUyXup5N35gHAsLgafZXqybXm_jvSoS30cDpJexnKpTmQ2BOHYd4f4oSVKpcUhC1O_yiOFQ_lSMbOGfzg2-MFW2lsbeMXEz0__IA9eg9HnpkJNDJ-QIi9lO7YbYZX5IN1cIVu41b4fABbbKlXiJ-0IcdfjsRQde_z9JNttdaaZLEp1bGdksoBy-B6y2CALHIjhjcnqOmXLFbL6OSKQGyoVB2hcg-2nA1WXx1yAwddrqix-bBmRPhL0JgVDeMBDmVTd9XRO0Af9qs-AAFJoz3RTJf2X3sZLuFZ0ASmOaVDxCJZ-G5ycLLQ-cs", 

    "data": {"promotor": "", "script_id": 123, "date_from": "2023-11-29", "option": 1, "date_to": "2023-12-29"}, "account_id": 11702, "docker_image": "linkaform/python3_lkf:latest", "name": "reporte_visitas.py"}', 'False'
    ]

Si experimenta errores durante la ejecución del script, la impresión de ``sys.argv`` puede ayudarle a identificar rápidamente si hay problemas con los argumentos (líneas 6-17).

.. code-block:: python
    :linenos:
    :emphasize-lines: 6-17

    ==== LOG FOR SCRIPT reporte_encuestas.py ==== 
    Host: swarm0.lkf.cloud 
    Start Date: 2023-09-04 17:29:43.132755+00:00 
    End Date: 2023-09-04 17:29:44.578959+00:00 
    =========== TRACEBACK ============= 
    Traceback (most recent call last):
    File "/srv/backend.linkaform.com/infosync-api/backend/media/uploads/public-client-11702/scripts/reporte_encuestas.py", line 737, in <module>
        response = get_query_visita(date_from, date_to)
    File "/srv/backend.linkaform.com/infosync-api/backend/media/uploads/public-client-11702/scripts/reporte_encuestas.py", line 604, in get_query_visita
        match_query.update(get_date_query(date_from=date_from, date_to=date_to))
    File "/srv/backend.linkaform.com/infosync-api/backend/media/uploads/public-client-11702/scripts/reporte_encuestas.py", line 27, in get_date_query
        date_to = datetime.strptime('%s 23:59:59'%(date_to), "%Y-%m-%d %H:%M:%S") - timedelta(seconds=tz_offset)
    File "/usr/local/lib/python3.7/_strptime.py", line 577, in _strptime_datetime
        tt, fraction, gmtoff_fraction = _strptime(data_string, format)
    File "/usr/local/lib/python3.7/_strptime.py", line 359, in _strptime
        (data_string, format))
    ValueError: time data ' 23:59:59' does not match format '%Y-%m-%d %H:%M:%S'
    =========== END ============= 

    =========== OUTPUT ============= 
    es un error del tipo lkf
    ['/srv/backend.linkaform.com/infosync-api/backend/media/uploads/public-client-11702/scripts/reporte_encuestas.py', '{}', 
    
    '{"jwt": "Bearer I1NiIsInR5cCI6IkpXVCJ9.eX2lkIjoxMTcwMiwicGFyjoxNjk0NDUzMzua2FzZkBnbWFpbC5jb20ifQ.Rcoxv3nR3vWJf1S_2ZVdjM12qEeVEWeLkSxVtI8ou_t6MX5F4J2Q4eX6Ot6Y64_MeZji4JILDhynUTsxYn_b5mkm3Adfgq-KVwOG5K_scDloTDsxV_UDzcxWsC7LsadaASNd4D2OyTGqUI0JM5sz3z3xQFel8gsztLE1yHHQoVgDYQ2y0lYzsZCWY0l_Oi8Pa3R9-ONCy5UtVC8V73xMKCrV4uHuUL9XhZ_8ObJdebRErlRihMvUsxI2j2ipEQgM7tRU9q3zLNAws0tTdULne7mKLbrxYqpdV_r-PBR16KEmXpkm-tdmBs0zISy8HunAaQgtuYtaWp-k5R6fiJ-is4UQ8thy67cRaBqQumlDn5inUcTMZFjfwDd1XynNZfDPFos_tdeZILJ-6o03CGpkUORxDvlVzcS9kKyw7xq7VD0T_q8A89R1FVMqpXAhV-zcq1YYd-6YPeop_urvVrRe4STP5ZhdBBn8epWrYIxgNNXQAnsXQZaWCz85kwCiV80z4B1C_VCAA2i5eKezpNsV8W4zkUEfPhGIUP90NjXC-yZKCMRZSjM", 
    
    "data": {"script_id": 123, "date_from": "2023-08-28", "option": 0, "date_to": ""}, "account_id": 11702, "name": "reporte_encuestas.py"}', 'False'
    ]

.. _generar-api-key:

Generar API key
===============

Una ``API Key`` (clave de API) es un código alfanumérico único que se utiliza para autenticar y autorizar el acceso a toda la información de la cuenta.

.. warning:: El usuario con perfil de administrador es el único que puede generar una ``API Key``.

Para generar una ``API Key``, siga las instrucciones:

1. Inicie sesión en la plataforma web de Linkaform en |Producción| :octicon:`report;1em;sd-text-info` o en |Preproducción| :octicon:`report;1em;sd-text-info`.
2. Seleccione ``Grupos > Usuarios`` ubicado en el menú lateral.
3. Identifique y seleccione su cuenta. Observe la información que le proporciona. 
4. Identifique el campo ``ApiKey``.

- Presione el icono en forma de rueda para generar una nueva key.
- Presione el icono de la papelera para eliminar la key actual.
- Presione el icono del portapapeles para copiar la key.

.. image:: /imgs/Reportes/Reportes23.png

.. warning:: En caso de que ya exista una ``API Key``, no es necesario crear una nueva, ya que probablemente esté siendo utilizada para otras operaciones. Cambiarla podría provocar acciones inesperadas.

    En el desarrollo de reportes, utilizará esta ``API Key`` en el :ref:`account-settings` :octicon:`report;1em;sd-text-info`.

.. _informacion-cuenta:

Ver información de la cuenta
============================

Para visualizar la información completa de su cuenta, siga los siguientes pasos:

1. Ingrese a la aplicación web de |Linkaform| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales.

.. note:: En caso de no contar con credenciales, solicite asistencia a soporte técnico.

3. Presione la burbuja ubicada en la parte superior izquierda.
4. Seleccione la opción ``Cuenta``.

.. image:: /imgs/Reportes/Reportes18.png

Observe el contenido de su cuenta; por privacidad, cierta información se oculta. Tenga en cuenta el ``ID`` de la cuenta padre.

.. image:: /imgs/Reportes/Reportes19.png

.. _ver-id-forma:

Ver ``ID`` de la forma
======================

Para poder visualizar el ``ID`` de la forma siga los pasos:

1. Ingrese a la aplicación web de |Linkaform| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales.

.. note:: En caso de no contar con credenciales, solicite asistencia a soporte técnico.

3. Presione ``Formas > Mis Formas`` ubicado en el menú lateral.
4. Identifique la forma y seleccione la opción ``Editar``.

.. image:: /imgs/Reportes/Reportes28.png

5. Observe el ``ID`` ubicado en la parte superior.

.. image:: /imgs/Reportes/Reportes29.png

Si desea crear su propio reporte personalizado, le sugerimos revisar las siguientes secciones de la documentación que explican cómo crear reportes. En caso contrario, le recomendamos contactar a soporte técnico para que el equipo de Linkaform pueda elaborar una propuesta a la medida.

.. LIGAS EXTERNAS

.. |Linkaform| raw:: html

   <a href="https://app.linkaform.com/" target="_blank">Linkaform</a>

.. |Producción| raw:: html

   <a href="https://app.linkaform.com/" target="_blank">producción</a>

.. |Preproducción| raw:: html

   <a href="https://preprod.linkaform.com/" target="_blank">preproducción</a>

.. |faq| raw:: html

   <a href="https://faq.linkaform.com/" target="_blank">FAQs de Linkaform</a>
   