==================
Bases de Linkaform
==================

En el módulo ``Reportes`` de Linkaform, tiene la capacidad de explorar visualmente los resultados extraídos de las :ref:`section-forms` :octicon:`report;1em;sd-text-info` a través de filtros, gráficos y tablas.

Para acceder a los ``Reportes``, siga los pasos:

1. Ingrese a la aplicación web de |Linkaform| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales.

.. note:: En caso de no contar con credenciales, solicite asistencia a soporte técnico.

3. Seleccione la opción ``Reportes`` en el menú lateral. 

.. image:: /imgs/Reportes/Reportes1.png

Ver reporte
===========

Para examinar un reporte en detalle, siga los siguientes pasos:

1. Seleccione la opción ``Reportes`` en el menú lateral. 
2. Presione el icono de engrane, seguido de ``Ver reportes`` o elija el tercer icono.

.. image:: /imgs/Reportes/Reportes2.png

En términos generales, observe la siguiente imagen que describe los elementos básicos presentes en un reporte.

.. image:: /imgs/Reportes/Reportes3.png

Crear carpeta
=============

Crear una carpeta le permitirá almacenar uno o más reportes dentro de ella. Siga los pasos para crear una carpeta:

1. Diríjase y seleccione la opción ``Reportes``.
2. Haga clic en el icono sobre ``Carpeta`` ubicada en el menú superior derecho.

.. image:: /imgs/Reportes/Reportes6.png

3. Escriba el nombre de la ``Carpeta``.
4. Presione ``Crear``.

Compartir Carpeta/Reporte
=========================

Compartir una carpeta o un reporte es un proceso sencillo. Siga los pasos:

1. Diríjase y presione la opción ``Reportes`` en el menú lateral.
2. Identifique la carpeta o la forma de su interés.
3. Presione el icono de engrane, seguido de ``Compartir`` o haga clic en el segundo ícono de compartir.

.. image:: /imgs/Reportes/Reportes4.png

4. Escriba el nombre del usuario con el que desea compartir la carpeta o el reporte y presione ``Enter``. Observe que el nombre del usuario aparecerá en la parte inferior de la ventana.

.. image:: /imgs/Reportes/Reportes5.png

.. seealso:: 

    La diferencia en las opciones de permisos se debe a que el usuario Omar Vázquez es una conexión. Es decir, pertenece a otra cuenta padre diferente a la suya.

    En cambio, el usuario Israel pertenece a la misma cuenta padre.

5. Establezca al usuario el permiso que requiera. Tenga en cuenta las descripciones:

- **Lectura**: El usuario puede ver todos los reportes dentro de la carpeta. 
- **Compartir**: El usuario puede ver y compartir la carpeta con otros usuarios. 
- **Admin**: El usuario tiene los mismos privilegios que los perfiles anteriores y puede modificar y eliminar los reportes.
- **Borrar registros**: Al activar esta opción, el usuario puede eliminar los reportes. Si no se activa, el usuario no puede eliminar los reportes, incluso si tiene el perfil de ``Admin``.

.. caution:: Cuando se comparte una carpeta, los reportes que contiene heredan automáticamente los permisos. Sin embargo, compartir un reporte e intentar moverlo a una carpeta puede causar problemas.

.. tip:: 
    
    Si necesita mover un reporte a una carpeta, simplemente arrástrelo al lugar necesario. 
    
    Si necesita mover un reporte fuera de alguna carpeta, a la raíz, simplemente arrástrelo a la columna principal.

Si necesita editar el nombre de su carpeta siga los siguientes pasos:

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

        1. Presione el icono de engrane, seguido de ``Editar``.
        2. Renombre a la carpeta.
        3. Haga clic en ``Renombrar``.

.. _config-reporte:

Crear reporte
=============

Crear un reporte en Linkaform es un proceso sencillo. Siga el siguiente procedimiento teniendo en cuenta las notas y recomendaciones:

.. caution:: Tenga en cuenta que estos son los pasos que debe seguir para configurar el reporte (previamente preparado) en su cuenta de Linkaform; sin embargo, NO constituyen la totalidad del proceso.

    Antes de realizar esta configuración, asegúrese de `cargar el script <#cargar-script>`_ :octicon:`report;1em;sd-text-info`.

1. Ingrese a la aplicación web de Linkaform en |Producción| :octicon:`report;1em;sd-text-info` o en otro caso, en |Preproducción| :octicon:`report;1em;sd-text-info`.

.. important:: El proceso de configuración en producción y preproducción es idéntico. Sin embargo, se recomienda iniciar el proceso de creación de reportes en preproducción. Una vez finalizado y seguro de sus cambios, puede transferirlo a producción.

2. Seleccione la opción ``Reportes`` en el menú lateral. 
3. Presione el icono de archivo, ubicado en la parte superior.

.. image:: /imgs/Reportes/Reportes7.png

.. note:: Pase el cursor sobre las opciones para conocer las funcionalidades que ofrecen.

4. Configure el reporte teniendo en cuenta lo siguiente:

- **Nombre del Reporte**: Identificador del reporte, no necesariamente es el mismo que se visualiza en el nombre del reporte.
- **URL**: Dirección del reporte. 

.. note:: En la siguiente figura, observe que se está asignando la ``URL`` de servido, indicando que es un reporte de demostración. Consulte la sección :ref:`url-acceso` :octicon:`report;1em;sd-text-info`, específicamente :ref:`link-servido` :octicon:`report;1em;sd-text-info`.
 
- **Script**: Nombre del script previamente desarrollado en lenguaje Python. 

.. important:: Automáticamente el ``ID`` del ``script`` se envía como parámetro en la ``URL``, especificando al reporte a dónde consultar la data. Por esta razón, el script no se coloca directamente en la ``URL``, ya que es dinámico.

.. image:: /imgs/Reportes/Reportes8.png

.. seealso:: Consulte :ref:`crear-script` :octicon:`report;1em;sd-text-info` para desarrollar su script personalizado. 
    
5. Presione el botón ``Cargar``.

Si necesita editar las configuraciones de su reporte, simplemente presione el icono de engranaje, seguido de ``Editar`` y modifique su reporte según las instrucciones anteriores.

.. image:: /imgs/Reportes/Reportes9.png

.. _generar-api-key:

Generar API key
===============

Una ``API Key`` (clave de API) es un código alfanumérico único que se utiliza para autenticar y autorizar el acceso a toda la información de la cuenta.

Para generar una ``API Key``, siga las instrucciones:

1. Ingrese a la aplicación web de |Linkaform| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión en la cuenta padre. 

.. caution:: El administrador de la cuenta padre es el único que puede asignar a los usuarios dependientes de él una ``API Key``.

3. Seleccione ``Grupos > Usuarios`` ubicado en el menú lateral.

.. image:: /imgs/Reportes/Reportes20.png

4. Identifique y seleccione al usuario que desea asignar una ``API Key``. Utilice el buscador.

.. image:: /imgs/Reportes/Reportes21.png

De manera detallada, podrá encontrar toda la información del usuario, desde permisos hasta dispositivos conectados, etc.

.. image:: /imgs/Reportes/Reportes22.png

5. Seleccione el menú desplegable ``API Keys``. Si no ha creado una ``API Key`` Simplemente haga clic en el enlace de color azul ``+ Crear api key de Linkaform``, que se muestra a continuación:

.. image:: /imgs/Reportes/Reportes23.png

.. caution:: En caso de tener una ``API Key`` previamente creada, ya no es necesario volver a crear una nueva, ya que es utilizada por el archivo ``account_settings`` y si cambia podría provocar acciones inesperadas. 

.. _log-script:

Log de script
=============

El ``log`` de script es una herramienta útil que se utiliza para depurar (*debuggear*) y verificar la correcta ejecución de los scripts.

Para visualizar el ``log`` de un script, siga los siguientes pasos:

1. Ingrese a la aplicación web de |Linkaform| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión utilizando sus credenciales.
3. Seleccione ``Formas > Scripts`` en el menú lateral. Podrá observar todos los scripts cargados en la cuenta.

.. image:: /imgs/Reportes/Reportes24.png

4. Identifique el script del cual desea conocer la información.
5. Presione el último icono ``Script log``.

.. image:: /imgs/Reportes/Reportes25.png

Observe la siguiente pantalla, que es el historial de los ``logs`` de script cada vez que se ejecuta. En esta ventana, puede ver la fecha y hora de ejecución, el nombre del script y su estatus, que es el más importante, ya que indica si se ejecutó exitosamente.

6. Presione la opción ``log`` para más detalles.

.. image:: /imgs/Reportes/Reportes26.png

.. seealso:: Consulte `la siguiente sección <#interpretacion-log-script>`_ :octicon:`report;1em;sd-text-info` para más detalles.

.. _interpretacion-log-script:

Interpretación log de script
----------------------------

La línea ``print(sys.argv)`` imprime una cadena de objetos JSON con los argumentos de la línea de comandos, lo cual es útil para depurar (*debuggear*) código en Python.

.. seealso:: Consulte :ref:`main` :octicon:`report;1em;sd-text-info` para más detalles.
    
La variable ``sys.argv`` es una lista que contiene los argumentos pasados al script en la línea de comandos. Al imprimir ``sys.argv``, puede verificar si los argumentos que esperaba están siendo pasados correctamente al script y entender la estructura y valores de esos argumentos.

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

.. _cargar-script:

Cargar script
=============

Para cargar un script en la aplicación web de Linkaform, siga los siguientes pasos y lea las recomendaciones necesarias.

.. caution:: Tenga en cuenta que los siguientes pasos son necesarios para configurar el script previamente desarrollado.

    Antes de realizar esta configuración, asegúrese de haber creado su script de acuerdo a sus necesidades. Revise la sección sobre :ref:`crear-script` :octicon:`report;1em;sd-text-info`.

1. Ingrese a la aplicación web de |Linkaform| :octicon:`report;1em;sd-text-info`.
2. Inicie sesión con sus credenciales.

.. note:: En caso de no contar con credenciales, solicite asistencia a soporte técnico.

3. Seleccione ``Formas > Scripts`` en el menú lateral.
4. Seleccione el icono de documento ubicado en la parte superior derecha para cargar el script.

.. image:: /imgs/Reportes/Reportes31.png

Complete el formulario de acuerdo a los siguientes pasos:

1. Seleccione el archivo correspondiente al script. Automáticamente, se rellenará el nombre del script.
2. Seleccione la imagen de Docker (versiones de las herramientas):

- ``python:development`` no se usa para scripts actuales; utiliza la version 2 de python.
- ``python3_lkf:latest`` es la imagen que actualmente se utiliza; usa la version 3 de python.

3. Seleccione los bullets que considere:

- **Activity**: Active el bullet si desea que la actividad (ejecuciones exitosas o fallas) del script le sea notificada por correo electrónico de la cuenta padre.
- **Pública**: Active el bullet si desea consultar el script a través de un ``fetch``, sino está indicando que desea consultar el script a través del ``JWT`` del usuario que hace la consulta del script. Es decir, verifica a través del ``token`` si el usuario tiene los permisos necesarios para consultar el script. 

.. note:: Regularmente, los bullet están desactivados.

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