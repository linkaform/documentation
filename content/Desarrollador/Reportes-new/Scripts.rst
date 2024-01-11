===================
Creación de Scripts
===================

.. note:: RECUERDE QUE ESTE ES UN ARCHIVO BASADO EN UN REPORTE EN ESPECIFICO, PUEDE CAMBIAR. 

El archivo ``py`` en el repositorio ``infosync_scripts`` contiene la lógica encargada de gestionar las solicitudes a la API de Linkaform, así como de procesar y presentar la información correspondiente en la estructura establecida.

En la siguiente pestaña desplegable, observe el bloque de código, el cual representa de manera general las variables y funciones principales que componen al ``archivo py``. Sin embargo, en contenido posterior podrá encontrar detalles sobre las funciones más relevantes, resaltando los elementos que puede personalizar.

.. dropdown:: Vista general

    .. code-block:: python
        :linenos:

        #-*- coding: utf-8 -*-
        import simplejson, sys
        from linkaform_api import settings, network, utils
        from bson import ObjectId
        import time, pytz, math
        from datetime import datetime, timedelta, date
        from account_settings import *
        from unicodedata import normalize

        table_data = []
        plants = {}
        WEEKS = []

        def get_date_query(date_from=None, date_to=None, date_field_id=None): ...

        def get_visitas(date_from, date_to, promotor): ...

        def get_format_minutes(checkout, checkin): ...

        def get_report(date_from, date_to, promotor): ... 

        def get_catalog_promotor(catalogo_id): ...

        if __name__ == "__main__":
            print(sys.argv)
            all_data = simplejson.loads(sys.argv[2])
            data = all_data.get("data", {})
            date_from = data.get("date_from")
            date_to = data.get("date_to")
            option = data.get("option")
            promotor = data.get("promotor")

            #--Report Model
            report_model = ReportModel()

            lkf_api = utils.Cache(settings)
            jwt_parent = lkf_api.get_jwt(api_key=config["API_KEY"])
            config["USER_JWT_KEY"] = jwt_parent
            
            settings.config.update(config)
            lkf_api = utils.Cache(settings)
            net = network.Network(settings)
            cr = net.get_collections()

            if option == 1:
                response = get_report(date_from, date_to, promotor)
                sys.stdout.write(simplejson.dumps(
                    {"firstElement":{
                        'tabledata':response
                        },
                    })
                )
            elif option == 0:
                response = get_catalog_promotor(95211)
                sys.stdout.write(simplejson.dumps(
                    {
                        "catalog":response,
                    })
                )

.. _main:

Main
====

Un ``Script`` comienza a ejecutarse a partir del ultimo bloque de código ``main``. Por favor, lea los comentarios dentro del código y considere las siguientes anotaciones.

Observe la línea de código 3, ``print(sys.argv)``, que se encarga principalmente de generar un ``log`` para depurar y obtener detalles sobre los argumentos del ``script``.

.. caution:: Por ningún motivo comente o elimine esta línea de código. Consulte :ref:`log-script` :octicon:`report;1em;sd-text-info` y revise la interpretación de la misma.

Identifique el bloque de código de la 6 a la 15, que procesa un objeto JSON presente en el tercer elemento de la lista ``sys.argv``. Revise :ref:`interpretacion-log-script` :octicon:`report;1em;sd-text-info`.

.. seealso:: El ``método get`` se utiliza para obtener el valor asociado con una clave en un diccionario. 

    - Si la clave existe en el diccionario, ``get`` devuelve el valor asociado con esa clave.
    - Si la clave no existe en el diccionario, ``get`` devuelve ``None`` por defecto.
    - Si se proporciona un valor por defecto como segundo argumento, ese valor se devuelve si la clave no está presente en el diccionario.

Ahora, considere que el código presente es un ejemplo básico y puede cambiar según sus necesidades. Por ejemplo, para procesar las ejecuciones, considere aplicar alguna condicional en caso de no recibir un valor, revise los siguientes casos.

.. tab-set::

    .. tab-item:: Caso 1
        :sync: key1
        
        .. code-block:: python
            :linenos:
            :emphasize-lines: 3, 6-15

            if __name__ == "__main__":
                # Log del script
                print(sys.argv)
                #---FILTROS
                # Carga el objeto JSON desde el tercer elemento de sys.argv. Por ejemplo, considere al objeto "data": {"promotor": "", "script_id": 123, "date_from": "2023-11-29", "option": 1, "date_to": "2023-12-29"}
                all_data = simplejson.loads(sys.argv[2])

                # Obtiene el diccionario asociado con la clave "data", o un diccionario vacío si no está presente
                data = all_data.get("data", {})

                # Obtiene valores específicos del diccionario "data" (puede ser None si la clave no está presente)
                date_from = data.get("date_from")
                date_to = data.get("date_to")
                option = data.get("option")
                promotor = data.get("promotor")

                lkf_api = utils.Cache(settings)
                jwt_parent = lkf_api.get_jwt(api_key=config["API_KEY"])
                config["USER_JWT_KEY"] = jwt_parent
                # print('jwot', jwt_parent)
                
                settings.config.update(config)
                lkf_api = utils.Cache(settings)
                net = network.Network(settings)
                cr = net.get_collections()

                if option == 1:
                    response = get_report(date_from, date_to, promotor)
                    sys.stdout.write(simplejson.dumps(
                        {"firstElement":{
                            'tabledata':response
                            },
                        })
                    )
                elif option == 0:
                    response = get_catalog_promotor(95211)
                    sys.stdout.write(simplejson.dumps(
                        {
                            "catalog":response,
                        })
                    )

    .. tab-item:: Caso 2
        :sync: key2

        El siguiente código contiene una condicional y solamente ejecutará su contenido si recibe una fecha desde (``date_to``) o una fecha hasta (``date_from``) en la línea 14. En caso de que el filtro no contenga ningún valor, lo que va a mostrar será una cadena vacía (línea 30).

        Concéntrese en el bloque 19-23, aquí, se están actualizando las configuraciones en el módulo ``settings`` con los valores del ``diccionario config``. Después de la actualización de la configuración, se utilizan las clases ``utils.Cache`` y ``network.Network`` para interactuar con la API de Linkaform.
        
        .. seealso:: Consulte el `archivo account settings <#account-settings>`_ :octicon:`report;1em;sd-text-info` para más detalles. 
        
        Si la autenticación se desea realizar a partir del ``token`` (26-27), se obtiene el ``token`` (``jwt_complete``) y luego lo asigna a la propiedad ``USER_JWT_KEY`` en el `diccionario de configuración <#account-settings>`_ :octicon:`report;1em;sd-text-info`.

        De otra manera, si la autenticación se realiza a partir de la ``API key`` (30-31), se llama al método ``get_jwt`` de la API de Linkaform, proporcionándole la ``API key`` almacenada en la configuración (``settings.config['API_KEY']``). 
        
        El método ``get_jwt`` genera un ``token`` a partir de la ``API key`` y devuelve ese ``token``, que luego se asigna a la propiedad ``USER_JWT_KEY`` en el `diccionario de configuración <#account-settings>`_ :octicon:`report;1em;sd-text-info`.

        .. caution:: Si requiere hacer la autenticación por el usuario que abre o ejecuta el reporte, deberá comentar el bloque correspondiente a la ``API key`` y habilitar el ``Token`` para recibirla en la petición.
        
        En el último bloque del script (línea 38), podrá encontrar las ejecuciones, que básicamente son las funciones encargadas de gestionar la consulta. En este caso, es un reporte con una sola función de consulta (``query_report_first``).

        .. code-block:: python
            :linenos:
            :emphasize-lines: 19, 22, 23, 26, 27, 30, 31, 38

            if __name__ == "__main__":
                # Log del script
                print(sys.argv)
                all_data = simplejson.loads(sys.argv[2])

                #--Filtros
                data = all_data.get("data", {})    
                date_to = data.get("date_to",'')
                date_from = data.get("date_from",'')
                buscador = data.get("buscador",'')
                variedad = data.get("variedad",'')

                #--Report Model
                report_model = ReportModel()

                if date_to or date_from :
                    #--CREDENCIAL
                    # Actualiza la configuración con los valores definidos en el diccionario "config"
                    settings.config.update(config)  

                    # Crea instancias de las clases utils.Cache y network.Network con la configuración actualizada
                    lkf_api = utils.Cache(settings)
                    net = network.Network(settings)

                    # Autenticación con Token JWT
                    #jwt_complete = simplejson.loads(sys.argv[2])
                    #config["USER_JWT_KEY"] = jwt_complete

                    # Autenticación con API Key
                    jwt_key = lkf_api.get_jwt(api_key=settings.config['API_KEY'])
                    config["USER_JWT_KEY"] = jwt_key

                    # Habilita el acceso a las colecciones de la consulta. 
                    cr = net.get_collections()

                    #--EJECUCIONES
                    # Llama a la función y envía parámetros
                    query_report_first(date_from, date_to, buscador, variedad)
                    sys.stdout.write(simplejson.dumps(report_model.print()))
                else:
                    sys.stdout.write(simplejson.dumps({"json": {}}))

Funciones
=========

Para definir las funciones encargadas de gestionar las peticiones a la base de datos, deben definirse siguiendo el estándar |snake_case| :octicon:`report;1em;sd-text-info` de Python.

.. code-block:: python
    :linenos:
    
    def nombre_funcion(parámetro1, parámetro2, parámetro3)

Para estructurar una ``query``, dependerá de los requerimientos que necesite. Sin embargo, tenga en cuenta los siguientes puntos que la mayoría de los reportes comparten:

- Cuando realiza un ``query`` para consultar datos reales de una forma, necesita forzosamente el identificador de la forma.

.. seealso:: Consulte :ref:`ver-id-forma` :octicon:`report;1em;sd-text-info` para más información.

- Se requiere el ``ID`` del campo para especificar que se necesita la data del mismo.

.. seealso:: Consulte la sección :ref:`menu-opciones-generales` :octicon:`report;1em;sd-text-info` en la documentación para el usuario y consulte específicamente :ref:`opciones-avanzadas` :octicon:`report;1em;sd-text-info`.

A continuación se detallan algunos ejemplos en base a los casos anteriores. 

.. tab-set::

    .. tab-item:: Caso 1
        :sync: key1

        Contenido 1

    .. tab-item:: Caso 2
        :sync: key2

        La siguiente función se utiliza para consultar datos de un formulario. Utilice este ejemplo como base para preparar su propia consulta personalizada, pero tenga mucho cuidado y preste atención a las notas para realizar modificaciones según lo requiera.

        Por favor, revise y lea los comentarios del código de la función al final de esta pestaña sincronizada y regrese aquí para seguir el flujo de la función.

        Se define la función ``query_report_first`` que recibe cuatro parámetros correspondientes a los filtros del punto de entrada principal del `script (main) <#main>`_ :octicon:`report;1em;sd-text-info`.

        .. code-block:: python
            :linenos:

            def query_report_first(date_from, date_to, buscador, variedad):

        La variable global ``report_model`` modifica su valor en base a esta función para presentar la estructura de los diccionarios. 

        .. code-block:: python
            :linenos:

            global report_model

        .. seealso:: consulte la `clase ReportModel <#class-reportModel>`_ :octicon:`report;1em;sd-text-info` para más detalles.

        En el siguiente bloque de código, se crea un diccionario denominado ``match_query`` que representa las condiciones iniciales de la consulta. Este diccionario actúa como filtros adicionales que especifican las condiciones de dónde y cómo extraer los datos.

        - Asegúrese de modificar el valor de la clave ``form_id`` de acuerdo al identificador del formulario al que desea extraer la información.

        .. seealso:: Revise :ref:`ver-id-forma` :octicon:`report;1em;sd-text-info` para más información.

        - La clave y valor ``"deleted_at":{"$exists":False}``, propio de ``MongoDB``, indica que no se desea consultar información previamente eliminada.

        .. code-block:: python
            :linenos:

            match_query = {
                    "form_id": 98116,
                    "deleted_at":{"$exists":False},
                }

        Por lo general, el diccionario ``match_query`` contiene las claves ``form_id`` y ``deleted_at``. Sin embargo, considere y agregue otros filtros a su consulta según lo requiera. En el siguiente bloque de código, se presentan dos nuevos filtros; por favor, lea detenidamente los comentarios para comprender su función.
        
        .. caution:: Asegúrese de que los nuevos filtros sean constantes, es decir que su valor no cambie. 

        .. code-block:: python
            :linenos:
            :emphasize-lines: 6, 9

            match_query = { 
                "form_id": 75791,
                "deleted_at":{"$exists":False},

                # Busca documentos en la colección donde el metadato "created_by_name" no contenga ninguno de los siguientes valores
                "created_by_name":{"$nin":['Luis Marquez', 'Andrea Lopez', 'Jose Chavez', 'Esteban Martinez']},

                # Busca todos los documentos que el campo contenga el valor de "montaje_terminado".
                "answers.11ci37d99a03dd17b1f6ff": "montaje_terminado",
            }

        .. note:: La palabra reservada ``answers`` seguido de la cadena alfanumérica (``ID``) se utiliza para indicar que se está accediendo a un campo especifico del formulario.  
        
            Consulte la sección :ref:`menu-opciones-generales` :octicon:`report;1em;sd-text-info` en la documentación para el usuario y consulte específicamente :ref:`opciones-avanzadas` :octicon:`report;1em;sd-text-info` para habilitar la visualización de los ``IDs`` de los campos. Copie y pegue según sea necesario. 

        Los siguientes filtros son opcionales, es decir, solo se aplican si están presentes ambas, uno o ninguno en la solicitud; de lo contrario, no afectan la condición de la consulta y se descartan. 

        .. code-block:: python
            :linenos:

            # Actualiza la consulta para incluir el filtro de 'buscador' y 'variedad' si está presente y no contiene '--'
            if buscador and '--' not in  buscador:
                match_query.update({"answers.": buscador})

            if variedad and '--' not in variedad:
                match_query.update({"answers.":variedad })

            #match_query.update(get_date_query(date_from, date_to))

        Considere el siguiente ejemplo, observe las condicionales que actualizan la consulta (``match_query``) según los valores de los filtros ``date_from`` y ``date_from``.

        .. code-block:: python
            :linenos:

            # Si "date_from" tiene algún valor y si no contiene la cadena '--', se actualiza la consulta (match_query) con una condición de rango utilizando $gte (mayor o igual) para el campo específico.
            if date_from and '--' not in  date_from:
                match_query.update({"answers.643d9b19b6b0dd38ef4cbdbc": {'$gte': date_from}})

            # Si "date_to" tiene algún valor y si no contiene la cadena '--', se actualiza la consulta (match_query) con una condición de rango utilizando $lte (menor o igual) para el campo específico.
            if date_to and '--' not in  date_to:
                match_query.update({"answers.643d9b19b6b0dd38ef4cbdbc": {'$lte': date_to}})

            # Si tanto "date_from" como "date_to" tienen valores y si ninguno de ellos contiene la cadena '--', se actualiza la consulta con una condición de rango utilizando $gte y $lte para abarcar un rango de fechas.
            if date_from and '--' not in  date_from and date_to and '--' not in  date_to:
                match_query.update({"answers.643d9b19b6b0dd38ef4cbdbc": {'$gte':date_from,'$lte':date_to}})

        .. note:: Se menciona que son filtros opcionales porque comúnmente se reciben fechas. Por ejemplo, si recibe ``date_from`` (fecha desde), la consulta comprende realizar búsquedas desde la fecha seleccionada hasta el día de la consulta. (Considere los otros casos).

        .. seealso:: Consulte la documentación oficial de los |mongo-operadores| :octicon:`report;1em;sd-text-info` o acceda al siguiente enlace que proporciona |tutorial-operadores| :octicon:`report;1em;sd-text-info` para preparar sus propios filtros.

        Con frecuencia, en la mayoría de los reportes, encontrará la función `get_date_query <#get_date_query>`_ :octicon:`report;1em;sd-text-info`. Esta función actualiza la consulta mediante condiciones de fecha. La razón detrás de esta práctica es que, como se mencionó anteriormente, la mayoría de los reportes incorporan tanto ``date_from`` como ``date_to`` como filtros.

        .. code-block:: python
            :linenos:

            match_query.update(get_date_query(date_from, date_to))

        .. seealso:: Consulte la `función get_date_query <#date-query>`_ :octicon:`report;1em;sd-text-info` para más detalles.

        El siguiente código es la estructura de una consulta muy sencilla. En términos generales, se están utilizando `operadores de agregación <#proceso-agregacion>`_ :octicon:`report;1em;sd-text-info` para filtrar  `documentos <#mongo-documento>`_ :octicon:`report;1em;sd-text-info` que cumplen con otros criterios. Por favor, revise los comentarios dentro del código.

        - Observe la línea de código 7. Es un ``documento`` apuntando a un ``metadato``. Los ``metadatos`` permiten mostrar información descriptiva del registro, los mas utilizados son los siguientes:

        +-----------------------+----------------------------------------------------------------+
        | Metadatos             | Descripción                                                    |
        +=======================+================================================================+
        | ``created_at``        | Fecha de creación de registro en formato 'YYYY-MM-DD HH:mm:ss'.|
        +-----------------------+----------------------------------------------------------------+
        | ``created_by_name``   | Nombre del usuario que creó el registro.                       |
        +-----------------------+----------------------------------------------------------------+
        | ``folio``             | Folio del registro.                                            |
        +-----------------------+----------------------------------------------------------------+
        | ``version``           | Versión del registro.                                          |
        +-----------------------+----------------------------------------------------------------+
        
        - Observe las líneas de código 9-13. La consulta selecciona a los campos para extraer la data de los formularios utilizando el ``ID`` del campo.

        .. note:: Recuerde que la palabra reservada ``answers`` seguido de la cadena alfanumérica (``ID``) se utiliza para indicar que se está accediendo a un campo especifico del formulario. 

            Si necesita acceder a un campo dentro de un :ref:`campo-catalogo` :octicon:`report;1em;sd-text-info` o :ref:`grupo_repetitivo` :octicon:`report;1em;sd-text-info`, primero coloque el ``ID`` del catálogo o grupo repetitivo seguido del ``ID`` del campo. Por ejemplo:

            .. code-block:: python
                :linenos:
                
                "tienda":"$answers.63dc0f1ec29b8336b7b72613.63dc0f1ec29b8336b7b72616",
                
            Consulte la sección :ref:`menu-opciones-generales` :octicon:`report;1em;sd-text-info` en la documentación para el usuario y consulte :ref:`opciones-avanzadas` :octicon:`report;1em;sd-text-info` para habilitar la visualización de los ``IDs`` de los campos. Copie y pegue según sea necesario. 

        .. code-block:: python
            :linenos:
            :emphasize-lines: 9-13

            query = [
                # Filtra el documento de acuerdo a los filtros aplicados en "match_query" (id de la forma y la especificación de que no se desea consultar información previamente eliminada.)
                {"$match": match_query},
                # Selecciona a los campos específicos para extraer la información de los campos del formulario a traves de su ID.
                {"$project": {
                    "_id":1,
                    # Metadato folio
                    "folio":"$folio",
                    # Campos
                    "nombre_usuario":"$answers.64d66dc5d738a20c816b5",
                    "paterno_usuario":"$answers.64d66dc5d738a20c816b6",
                    "materno_usuario":"$answers.64d66dc5d738a20c82416b7",
                    "cantidad":"$answers.64d66dc5d7a20c82416ba",
                    "fecha":"$answers.64d66dc5d738a20c82416bc",
                }},
                # Ordena los documentos resultantes en orden ascendente según el metadato "created_at"
                {"$sort": {"created_at":1}}
            ]

        .. caution:: Si desconoce de algunos elementos de mongodb, consulte la sección `query <#doc-query>`_ :octicon:`report;1em;sd-text-info` para obtener una breve descripción

        Las siguientes instrucciones son importantes y varían según lo requiera. 

        .. code-block:: python
            :linenos:

            result = cr.aggregate(query)
            get_format_firstElement(result)

        En este caso, ``result = cr.aggregate(query)`` ejecuta la consulta de `agregación <#proceso-agregacion>`_ :octicon:`report;1em;sd-text-info` y obtiene un `cursor <#mongo-cursor>`_ :octicon:`report;1em;sd-text-info` (``result``) que apunta a los resultados generados por el `pipeline de agregación <#pipeline-agregacion>`_ :octicon:`report;1em;sd-text-info`.

        Con el `método aggregate <#metodo-agregacion>`_ :octicon:`report;1em;sd-text-info` se accede a los *pipelines de agregación* de la consulta (``query``). En lugar de iterar sobre el *cursor* para procesar cada `documento <#mongo-documento>`_ :octicon:`report;1em;sd-text-info`, se pasa directamente el *cursor* como parámetro a la función `método aggregate <#funcion-get-format-firstElement>`_ :octicon:`report;1em;sd-text-info` para aplicar un nuevo formateo.
        
        En el siguiente caso, se crea una lista vacía llamada  ``data`` para almacenar los resultados obtenidos de la iteración del *cursor*. La expresión ``cr.aggregate(query)`` ejecuta una consulta de *agregación* y devuelve un *cursor* que apunta a los resultados de esa consulta. Luego, utilizando una comprensión de lista ``[x for x in result]``, se itera sobre el *cursor* para extraer todos los *documentos* y se almacenan en la lista `data`. En última instancia, data contiene una lista con la información consultada de la base de datos.

        .. code-block:: python
            :linenos:     

            data = []
            result = cr.aggregate(query)
            data = [x for x in result]
            return data;

        .. seealso:: Si tiene alguna duda respecto algún termino usado en las consultas, revise la sección `query <#doc-query>`_ :octicon:`report;1em;sd-text-info` para más información. 
       
        Para visualizar el código completo de la función ``query_report_first``, por favor, haga clic en el siguiente menú desplegable.

        .. dropdown:: Función ``query_report_first`` 

            .. code-block:: python
                :linenos:
                :emphasize-lines: 1, 2, 5-8, 11-15, 17, 20-32

                def query_report_first(date_from, date_to, buscador, variedad):
                    global report_model

                    # Construcción de la consulta inicial para MongoDB
                    match_query = { 
                        "form_id": 98116,
                        "deleted_at":{"$exists":False},
                    }

                    # Actualiza la consulta para incluir el filtro de 'buscador' y 'variedad' si está presente y no contiene '--'
                    if buscador and '--' not in  buscador:
                        match_query.update({"answers.": buscador})

                    if variedad and '--' not in variedad:
                        match_query.update({"answers.":variedad })

                    #match_query.update(get_date_query(date_from, date_to))

                    # Definición de la consulta de agregación para MongoDB
                    query = [
                        # Filtra el documento de acuerdo a los filtros aplicados en "match_query" (id de la forma y la especificación de que no se desea consultar información previamente eliminada.)
                        {"$match": match_query},
                        # Selecciona a los campos específicos para extraer la información de los campos del formulario a traves de su ID.
                        {"$project": {
                            "_id":1,
                            "folio":"$folio",
                            "nombre_usuario":"$answers.64d66dc5d738a20c816b5",
                            "paterno_usuario":"$answers.64d66dc5d738a20c816b6",
                            "materno_usuario":"$answers.64d66dc5d738a20c82416b7",
                            "cantidad":"$answers.64d66dc5d7a20c82416ba",
                            "fecha":"$answers.64d66dc5d738a20c82416bc",
                        }},
                        # Ordena los documentos resultantes en orden ascendente según el metadato "created_at"
                        {"$sort": {"created_at":1}}
                    ]
                    # Ejecución de la consulta en la colección usando el método aggregate
                    result = cr.aggregate(query)
                    # Llamada a la función para procesar el resultado de la consulta
                    get_format_firstElement(result)

.. _funcion-get-format-firstElement:

funciones de formateo
---------------------

Esta función toma el cursor de documentos de MongoDB, extrae información específica de cada documento y la estructura en un formato específico dentro del modelo de reporte (report_model).

La función recibe el cursor data como parámetro, que se espera que sea un cursor (o algo iterable) que contiene documentos de MongoDB.

global report_model: Indica que la función utilizará la variable global report_model.

for x in data:: Itera sobre cada documento (x) en el cursor data.

print(x): Imprime el documento actual para propósitos de depuración.

print('=============='): Imprime una línea divisoria para ayudar a distinguir entre los documentos durante la depuración.

record_id = str(x.get('_id', '')): Extrae el valor del campo "_id" del documento. Si el campo no existe, asigna una cadena vacía. Convierte el valor a cadena.

folio = x.get('folio', ''): Similar al paso anterior, pero para el campo "folio".

Resto de las líneas (nombre_usuario, paterno_usuario, materno_usuario, cantidad, fecha): Realizan la extracción de valores para los campos correspondientes.

La sección final agrega un diccionario con los valores extraídos al modelo de informe (report_model). Cada documento del cursor se representa como un diccionario dentro de la lista bajo la clave 'data' en la sección 'firstElement' del modelo de informe.

.. code-block:: python
    :linenos:
    :emphasize-lines: 1

    def get_format_firstElement(data):
        global report_model

        # Itera sobre cada documento en el cursor
        for x in data:
            print(x);
            print('==============');

            # Extrae valores específicos del documento (si no existen, se asigna un valor predeterminado)
            record_id = str(x.get('_id',''))
            folio = x.get('folio','')
            nombre_usuario = x.get('nombre_usuario','')
            paterno_usuario = x.get('paterno_usuario','')
            materno_usuario = x.get('materno_usuario','')
            cantidad = x.get('cantidad')
            fecha = x.get('fecha','')

            # Agrega un diccionario con los valores extraídos al modelo de informe
            report_model.json['firstElement']['data'].append({
                'record_id':record_id,
                'folio':folio,
                'nombre_usuario':nombre_usuario,
                'paterno_usuario':paterno_usuario,
                'materno_usuario':materno_usuario,
                'cantidad':cantidad,
                'fecha':fecha,
            })

.. _doc-query:

Query
-----

.. caution:: El siguiente contenido ofrece una visión rápida de los elementos básicos de una consulta en ``MongoDB`` útiles en los reportes, pero no constituye un tutorial completo. Por favor, consulte la documentación oficial de |mongodb-documentation| :octicon:`report;1em;sd-text-info` o visite |mongodb| :octicon:`report;1em;sd-text-info` si aún no está familiarizado.

Una ``query`` es una solicitud estructurada para recuperar información específica de la base de datos de |mongodb-documentation| :octicon:`report;1em;sd-text-info`. Una ``query`` puede ser tan simple o muy estructurada, según lo requiera. 

.. _mongo-documento:

Un ``documento`` es la representación en formato ``BSON`` de la información almacenada en la base de datos. Puede contener datos jerárquicamente estructurados, similar a un objeto ``JSON``, con una estructura de pares ``clave-valor``. Las claves son cadenas y los valores pueden ser de varios tipos.

Una ``colección`` es un conjunto lógico de documentos, comparable a una tabla en una base de datos relacional. A diferencia de una tabla, no impone un esquema fijo; cada documento puede tener campos diferentes sin necesidad de definir la estructura previamente.

En este ejemplo, cada clave (como nombre, edad, correo) representa un campo en el ``documento`` y los valores asociados son los datos almacenados. Además, el documento puede contener campos anidados (dirección) y un array (intereses).

.. important:: La clave ``_id`` actúa como identificador único del documento. 

.. code-block:: python
    :linenos:
    :emphasize-lines: 2

    {
    "_id": ObjectId("5f7a1efb89f6a74f8c3cf45a"),
    "nombre": "Juan Pérez",
    "edad": 30,
    "correo": "juan.perez@example.com",
    "direccion": {
        "calle": "123 Main Street",
        "ciudad": "Ciudad Ejemplo",
        "codigo_postal": "12345"
    },
    "intereses": ["lectura", "viajes", "tecnología"]
    }

.. _proceso-agregacion:

En MongoDB, existe un concepto llamado ``agregación``, donde se utilizan operadores que procesan ``documentos`` y devuelven resultados calculados. Cada etapa realiza una operación específica en los datos durante la ``agregación``. Algunas de las etapas más usadas en los reportes son:

+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Comando                                  | Descripción                                                                                                      |
+==========================================+==================================================================================================================+
| ``$match``                               | Filtra documentos que cumplen con ciertos criterios.                                                             |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``$group``                               | Agrupa documentos según un campo específico y realiza operaciones de agregación en esos grupos.                  |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``$sort``                                | Ordena los documentos según un campo especificado. Utilice 1 (orden ascendente) y -1 (orden descendiente).       |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``$limit``                               | Limita el número de documentos que pasan a la siguiente etapa.                                                   |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``$project``                             | Proyecta (selecciona) campos específicos para el resultado final.                                                |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``$count``                               | Cuenta el número de documentos que pasan a través de la etapa.                                                   |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``$set``                                 | Asigna un valor a un nuevo campo o modifica un campo existente.                                                  |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``$out``                                 | Escribe el resultado de la agregación en una nueva colección.                                                    |
+------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _pipeline-agregacion:

Un ``pipeline de agregación`` es una parte específica del ``proceso de agregación``. Es una serie secuencial de etapas (operadores) que se aplican a los documentos en una colección.

Aquí hay un ejemplo de un ``pipeline de agregación`` utilizando algunas de las etapas mencionadas. Este ``pipeline`` realiza una serie de operaciones en una ``colección`` para ``filtrar``, ``agrupar``, ``ordenar``, ``limitar`` y ``proyectar`` datos según las necesidades específicas.

.. code-block:: 
    :linenos:

    [
        { $match: { field1: value1 } },
        { $group: { _id: "$field2", total: { $sum: "$field3" } } },
        { $sort: { total: -1 } },
        { $limit: 10 },
        { $project: { _id: 0, groupName: "$_id", totalAmount: "$total" } }
    ]

.. seealso:: Para más información consulte |papeline| :octicon:`report;1em;sd-text-info`.

.. _metodo-agregacion:

Un ``método`` generalmente se refiere a una función o procedimiento que se puede invocar para realizar una operación específica en la base de datos. Considere los siguientes métodos:

+---------------------------------------+-------------------------------------------------------------------------------------------------+
| Método                                | Descripción                                                                                     |
+=======================================+=================================================================================================+
| ``db.collection.aggregate()``         | Proporciona acceso al canal de agregación.                                                      |
+---------------------------------------+-------------------------------------------------------------------------------------------------+
| ``db.collection.count()``             | Se ajusta count para devolver un recuento del número de documentos en una colección o vista.    |
+---------------------------------------+-------------------------------------------------------------------------------------------------+
| ``db.collection.dataSize()``          | Devuelve el tamaño de la colección. Envuelve el size campo en la salida de collStats.           |
+---------------------------------------+-------------------------------------------------------------------------------------------------+
| ``db.collection.drop()``              | Elimina la colección especificada de la base de datos.                                          |
+---------------------------------------+-------------------------------------------------------------------------------------------------+
| ``db.collection.find()``              | Realiza una consulta sobre una colección o una vista y devuelve un objeto de cursor.            |
+---------------------------------------+-------------------------------------------------------------------------------------------------+

.. seealso:: Revise todos los |mongodb-metotdos| :octicon:`report;1em;sd-text-info` que ``MongoDB`` ofrece.

.. _mongo-cursor:

Un ``cursor`` es un puntero que permite recorrer los resultados de una ``query`` (consulta) uno a uno. Es especialmente útil al trabajar con conjuntos de datos extensos, ya que no es necesario cargar todo en la memoria simultáneamente. Sin embargo, es importante tener en cuenta que si se cierra el cursor, ya no se podrá acceder a los datos a través de él.

.. seealso:: Consulte el siguiente enlace para ejemplos y más detalles sobre un |mongodb-cursores| :octicon:`report;1em;sd-text-info`. 

.. _class-reportModel:

Clase ``ReportModel``
---------------------

La clase ``ReportModel()`` es opcional, pero es utilizada para representar una estructura de los diccionarios de datos para formatear y enviar respuestas a alguna petición.

.. code-block:: python
    :linenos:

    class ReportModel():
        def __init__(self):
            # Estructura de datos predefinida
            self.json = {
                "firstElement":{
                    "data": [],
                },
                "secondElement":{
                    "data": [],
                },
                "thirdElement":[],
            }

        def print(self):
            # Nuevo diccionario para almacenar la estructura y datos
            res = {'json':{}}
            # Copia la estructura y datos de self.json al nuevo diccionario
            for x in self.json:
                res['json'][x] = self.json[x]
            return res

.. _date-query:

Función ``get_date_query``
--------------------------

Cuando un registro se almacena en los servidores de Linkaform, se utiliza la |utc| :octicon:`report;1em;sd-text-info`. Por ejemplo, si envía su registro el lunes 8 de enero a las 6:42 pm, el registro se almacenará considerando la zona horaria UTC+0, es decir, el martes 9 de enero a las 12:42 am. 

Por este motivo, se utiliza la función ``get_date_query()``, para convertir la fecha y hora a la zona horaria ``America/Monterrey.`` Esta función se encarga de construir y retornar un diccionario que representa una consulta basada en los parámetros ``date_from`` y ``date_to``.

.. caution:: Esta función ya está lista para su uso. Si pertenece a una zona horaria diferente o si así lo requiere, modifique la configuración de la zona horaria (``timezone``). Por favor, lea los comentarios.

.. code-block:: python
    :linenos: 5

    def get_date_query(date_from, date_to):
        # Inicializa un diccionario vacío para almacenar las condiciones de fecha
        res = {}
        # Define la zona horaria 
        timezone = pytz.timezone('America/Monterrey')
        # Convierte la fecha de 'date_from' a un objeto datetime y ajusta a la zona horaria UTC
        tz_date =  datetime.strptime('%s 00:00:00'%(date_from), "%Y-%m-%d %H:%M:%S")
        tz_date = tz_date.replace(tzinfo=pytz.utc)
        # Convierte a la zona horaria 'America/Monterrey' y normaliza el objeto de fecha
        tz_date = tz_date.astimezone(timezone)
        tz_date = timezone.normalize(tz_date)
        # Calcula el offset de la zona horaria en segundos
        tz_offset = tz_date.utcoffset().total_seconds()

        # Ajusta las fechas 'date_from' y 'date_to' restando el offset de la zona horaria
        date_from = datetime.strptime('%s 00:00:00'%(date_from), "%Y-%m-%d %H:%M:%S") - timedelta(seconds=tz_offset)
        date_to = datetime.strptime('%s 23:59:59'%(date_to), "%Y-%m-%d %H:%M:%S") - timedelta(seconds=tz_offset)
        
        # Construye las condiciones de fecha en el diccionario de consulta 'res'
        if date_from and date_to:
            res.update({
            'start_date': {
            '$gte':date_from,
            '$lt':date_to,
            }
            })
        elif date_from and not date_to:
            res.update({
            'start_date': {
            '$gte':date_from
            }
            })

        elif not date_from and date_to:
            res.update({
            'start_date': {
            '$lt':date_to
            }
            })
        # Retorna el diccionario de condiciones de fecha
        return res

Bibliotecas y módulos
=====================

El primer bloque de código corresponde a las importaciones de varias bibliotecas y módulos. 

.. note:: Por favor, lea los comentarios dentro del código para comprender su función.

.. code-block:: python
    :caption: Bibliotecas y módulos
    :linenos:

    # Biblioteca para trabajar con JSON (JavaScript Object Notation) en Python
    import simplejson, sys

    # Importa el módulo "settings", "network", "utils" de la Api de Linkaform
    from linkaform_api import settings, network, utils

    # Importa la clase "ObjectId" del módulo "bson". Esta clase se utiliza comúnmente en bases de datos NoSQL, como MongoDB, para representar identificadores únicos
    from bson import ObjectId

    # "time" se utiliza para trabajar con el tiempo, "pytz" para trabajar con zonas horarias y "math" para funciones matemáticas
    import time, pytz, math

    # Proporciona clases para trabajar con fechas y horas
    from datetime import datetime, timedelta, date

    # Importa configuraciones específicas de la cuenta
    from account_settings import *

    # Importa la función "normalize" del módulo "unicodedata", que se utiliza para normalizar cadenas de texto Unicode
    from unicodedata import normalize

.. _account-settings:

Archivo account settings
========================

Dentro de la carpeta ``infosync_scripts`` debe existir una carpeta por cada cliente que contenga scripts de sus reportes. Dentro de esta carpeta debe contener un archivo con el formato ``account_settings`` escrito en ``python`` por cliente.

.. caution:: Este archivo contiene información y configuraciones sensibles de la cuenta del cliente. Si requiere hacer actualizaciones en el archivo ``account_settings`` de algún cliente y no encuentra el archivo, lo podrá encontrar con el nombre del cliente seguido de ``settings``, por ejemplo: ``linkaform_settings``.

El contenido de un archivo ``account_settings`` varía dependiendo de lo que el cliente requiera. Sin embargo, lo que un reporte necesita de este archivo es el ``entorno de ejecución`` y lo que contiene el diccionario ``config``.

Identifique las líneas de código 4-5 y 8-9. Si desea apuntar y hacer la petición del script a producción, debe habilitar las líneas de código correspondientes a la misma. En caso contrario, si desea apuntar al script almacenado en preproducción, descomente las líneas de código de preproducción.

Ahora, localice la variable ``MONGODB_PASSWORD`` ubicada en línea de código 28, hace referencia a la contraseña de mongo.

.. note:: Solicite a soporte técnico apoyo para obtener la contraseña correspondiente a mongo.

Identifique las líneas de código 34-35, debe colocar el ``USER_ID`` y ``ACCOUNT_ID`` de la cuenta padre. 

.. seealso:: Consulte el siguiente enlace para :ref:`informacion-cuenta` :octicon:`report;1em;sd-text-info`.

Ubique la variable ``AUTHORIZATION_EMAIL_VALUE`` (línea 42) y ajuste de acuerdo al correo de la cuenta padre.

En la variable ``API_KEY`` (línea 43) copie y pegue la la clave alfanumérica generada. 

.. seealso:: Consulte: a :ref:`generar-api-key` :octicon:`report;1em;sd-text-info` para más información.

Revise la linea 46, ``settings.config.update(config)`` se utiliza para aplicar las configuraciones definidas en el diccionario ``config`` al módulo ``settings``. Esto es útil porque permite modificar dinámicamente las configuraciones de la aplicación sin tener que cambiar el código fuente directamente. 

.. code-block:: python
    :linenos:
    :emphasize-lines: 4, 5, 8, 9, 28, 34, 42, 43, 46

    from linkaform_api import settings # Configuraciones de la api

    # --------- ENTORNO PRODUCCIÓN ---------
    settings.mongo_hosts = 'db2.linkaform.com:27017,db3.linkaform.com:27017,db4.linkaform.com:27017'
    settings.mongo_port = 27017

    # --------- ENTORNO PREPRODUCCIÓN ---------
    # settings.mongo_hosts = 'dbs2.lkf.cloud:27918'
    # settings.mongo_port = 27918

    config = {
        # Correo de la cuenta padre
        'USERNAME' : 'correo.cuenta.padre@gmail.com',
        'PASS' : '',

        # Colección de MongoDB para almacenar las respuestas de los formularios
        'COLLECTION' : 'form_answer',

        # No cambiar
        'HOST' : 'app.linkaform.com',
        'PROTOCOL' : 'https', #http o https

        # Variables definidas para el entorno de ejecución 
        'MONGODB_PORT': settings.mongo_port,
        'MONGODB_HOST': settings.mongo_hosts,

        'MONGODB_USER': 'account_id',
        'MONGODB_PASSWORD': 'pass',

        'PORT' : settings.mongo_port,

        # Id de la cuenta padre
        'USER_ID' : 123,
        'ACCOUNT_ID' : 123,

        'KEYS_POSITION' : {},
        'IS_USING_APIKEY' : False,
        'USE_JWT' : True,
        'JWT_KEY':'',

        # Configuración de api key
        'AUTHORIZATION_EMAIL_VALUE' : 'correo.cuenta.padre@gmail.com'',
        'API_KEY':"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    }

    settings.config.update(config)

.. attention:: Cualquier cambio dentro de este archivo debe ser ejecutado solamente en su entorno local por ningún motivo son cambios que deben actualizarse en el repositorio.


.. LIGAS EXTERNAS

.. |mongodb| raw:: html

   <a href="https://learn.mongodb.com/learning-paths/introduction-to-mongodb" target="_blank">MongoDB University</a>

.. |mongodb-documentation| raw:: html

   <a href="https://www.mongodb.com/docs/" target="_blank">MongoDB</a>

.. |mongodb-python| raw:: html

   <a href="https://learn.mongodb.com/learning-paths/using-mongodb-with-python" target="_blank">MongoDB con Python</a>

.. |mongo-operadores| raw:: html

   <a href="https://www.mongodb.com/docs/manual/reference/operator/query/nin/" target="_blank">operadores relacionales de MongoDB</a>

.. |papeline| raw:: html

   <a href="https://www.mongodb.com/docs/manual/core/aggregation-pipeline/" target="_blank">conjunto de agregación</a>

.. |tutorial-operadores| raw:: html

   <a href="https://www.tutorialesprogramacionya.com/mongodbya/detalleconcepto.php?punto=9&codigo=9&inicio=0#google_vignette" target="_blank">ejemplos</a>

.. |mongodb-cursores| raw:: html

   <a href="https://www.mongodb.com/docs/v3.0/core/cursors/#read-operations-cursors" target="_blank">cursor</a>

.. |mongodb-metotdos| raw:: html

   <a href="https://www.mongodb.com/docs/manual/reference/method/" target="_blank">métodos</a>

.. |snake_case| raw:: html

   <a href="https://en.wikipedia.org/wiki/Snake_case" target="_blank">snake_case</a>

.. |utc| raw:: html

   <a href="https://time.is/UTC" target="_blank">zona horaria UTC+0 (GMT)</a>



