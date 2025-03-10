===============
Carga Universal
===============

La carga universal es una funcionalidad que LinkaForm ofrece para importar registros masivamente a una forma a través de un archivo **.xlsx**.  

.. _estructura-xlsx:

Estructura del Archivo
======================

Para asegurar una correcta importación, siga las siguientes recomendaciones para preparar el archivo según los campos de la forma.  

.. Cada columna del archivo **.xlsx** debe corresponder a un campo de la forma.
.. .. warning:: El nombre de la columna en el archivo debe coincidir exactamente con el nombre del campo en la forma para evitar errores en la carga.

Campos Individuales (Primer Nivel)
----------------------------------

Son aquellos campos que **no** están dentro de grupos repetitivos o catálogos. Para este tipo de campos, simplemente ingrese el nombre del campo tal como aparece en la forma. Por ejemplo:
    
.. code-block::
    
    Nombre del Propietario  

Campos dentro de Catálogos 
--------------------------

Si el campo es un **catálogo**, el nombre de la columna debe seguir la siguiente estructura:  

.. code-block::

    [Nombre del Catálogo en la Forma]: [Nombre del Campo]  

    Tipo: Tipo de vehículo

.. image:: /imgs/Registros/Registros68.png

.. hint:: Solo debe incluir los campos seleccionables dentro del catálogo. Los campos de **solo lectura** no deben agregarse, ya que LinkaForm los identificará automáticamente y asignará el valor correspondiente por defecto. Esto funciona de la misma manera que al seleccionar una opción de un catálogo en una forma, donde ciertos campos solo aparecen como referencia y no pueden ser seleccionados.

Campos dentro de Grupos Repetitivos
-----------------------------------

Si un **grupo repetitivo** contiene campos que no pertenecen a un catálogo, utilice la siguiente estructura:

.. code-block::

    [Nombre del Grupo Repetitivo]: [Nombre del Campo]

    Mantenimiento Realizado: Descripción del Mantenimiento Realizado

.. image:: /imgs/Registros/Registros83.png

.. seealso:: Consulte :ref:`multiples-registros-gp` :octicon:`report;1em;sd-text-info` para conocer la estructura de los datos.

Catálogos dentro de Grupos Repetitivos
--------------------------------------

Si dentro del grupo repetitivo hay un catálogo, siga la siguiente estructura:  

.. code-block::

    [Nombre del Grupo Repetitivo]: [Nombre del Catálogo]: [Nombre del Campo dentro del Catálogo] 

    Mantenimiento Realizado: Mecánico Encargado: Nombre completo

.. image:: /imgs/Registros/Registros75.png

.. error:: Si los datos ingresados no coinciden con los registros del catálogo, el registro no se guardará y será descartado.

Formato de Datos  
================

Los registros deben cumplir con los estándares permitidos por LinkaForm.

Correo Electrónico
------------------

Debe cumplir con el formato estándar de correos electrónicos, por ejemplo:  

.. code-block::

    ✔️ marcela@gmail.com
    x marcela@gmail
    x pati

.. image:: /imgs/Registros/Registros66.png

.. error:: El registro será descartado si la estructura del correo no es correcta.

Respuesta Única
---------------

Debe ser exactamente una de las opciones disponibles en la forma.  

.. image:: /imgs/Registros/Registros71.png

.. error:: Si la opción ingresada no está dentro de las opciones del campo, el registro será descartado.

Respuesta Múltiple 
------------------

Si el campo permite múltiples selecciones, ingrese los valores separados por comas y sin espacios. Por ejemplo:  

.. code-block::
    
    ✔️ Opción 1,Opción 2,Opción 3
    x Opción 1, Opción 2, Opción 3
    x Opción 2, Opción 1, Opción 3

.. image:: /imgs/Registros/Registros72.png

.. error:: El registro será rechazado si las opciones ingresadas no coinciden con las establecidas en el campo o no cumplen con la estructura establecida.

Respuesta Sí/No
---------------

Debe contener exclusivamente: **Sí** o **No**  

.. code-block::

    ✔️ Sí
    ✔️ No
    x si
    x no

.. image:: /imgs/Registros/Registros67.png

.. error:: El registro solo será válido si las opciones ingresadas son **Sí** o **No** y solo si cumplen con la estructura correcta; de lo contrario, será descartado.

Respuesta Selecciona un Campo
-----------------------------

Funciona igual que la respuesta única. Debe ser una de las opciones disponibles.  

.. code-block::

    ✔️ Opción A

.. image:: /imgs/Registros/Registros73.png

.. error:: Si la opción ingresada no está dentro de las opciones del campo, el registro será descartado.

Números Enteros
---------------

Solo se permiten valores numéricos enteros.  

.. code-block::
    
    ✔️ 123
    x 12.3

.. image:: /imgs/Registros/Registros70.png

.. note:: El valor numérico debe tener menos de 10 dígitos. Para números telefónicos, se recomienda usar un campo de tipo texto.

Números Decimales
-----------------

Debe incluir el punto decimal para separar decimales.  

.. code-block::
    
    ✔️ 12.50
    x 12. 50
    x 12,50

.. image:: /imgs/Registros/Registros77.png

Fecha y Hora
------------

Debe seguir la estructura:  

.. code-block::
    
    ✔️ YYYY-MM-DD HH:MM:SS
    ✔️ 2025-02-28 13:47:47

    x DD/MM/YYYY SS:MM:HH
    x 28/02/2025 47:25:15

.. image:: /imgs/Registros/Registros74.png

Para campos de solo fecha o solo hora: 

.. code-block::

    ✔️ YYYY-MM-DD
    ✔️ 2025-02-28

    ✔️ HH:MM:SS
    ✔️ 13:47:47

.. note:: Si los segundos no se ingresan, se registrarán como “00“.  

.. image:: /imgs/Registros/Registros76.png

.. seealso:: Descargue la plantilla del ejemplo desde |archivoxlsx| :octicon:`report;1em;sd-text-info`.

.. _multiples-registros-gp:

Múltiples Registros en un Grupo repetitivo
==========================================

Para cargar múltiples registros dentro de un **grupo repetitivo**, siga estas reglas en el archivo **.xlsx** para que los datos sean interpretados correctamente:

**Columnas fuera del grupo repetitivo:**  

- Se ingresan **una sola vez** en la primera fila del registro.  
- No es necesario repetir la información en las filas siguientes del mismo registro.  

**Campos dentro del grupo repetitivo:**  

- Cada fila representa **un elemento dentro del grupo repetitivo**.  
- Los campos del grupo repetitivo deben llenarse en las filas adicionales, dejando vacíos los campos principales.  

.. warning:: Si un campo principal se llena nuevamente en una fila que ya pertenece a un registro existente, **se interpretará como un nuevo registro**.  

.. admonition:: Ejemplo
    :class: pied-piper

    - La columna **Nombre del Propietario** tiene datos en la primera fila del registro.  
    - La columna **Fecha de Último Mantenimiento** también se llena solo en la primera fila del registro.  
    - En las filas siguientes, esos campos quedan **vacíos**, indicando que pertenecen al mismo registro.  
    - Las columnas del grupo repetitivo (**Mantenimiento Realizado**) sí tienen valores en todas las filas necesarias.  

    .. image:: /imgs/Registros/Registros78.png
        :width: 780px
    
    .. image:: /imgs/Registros/Registros79.png
        :width: 780px

.. _alta-forma: 

Alta de Forma
=============

Antes de realizar la carga universal, primero debe registrar la forma donde se cargará la información. Para ello, siga estos pasos:  

1. Acceda a ``Catálogos > Catálogos`` desde el menú lateral.  
2. Ubique el catálogo **Catálogo de Formas**, dentro de la carpeta **Base**.  
3. Complete los siguientes campos:  

   - **Nombre de la forma**: Especifique el nombre de la forma.  
   - **ID de la forma**: Identificador único de la forma.  
   - **Tipo de ítem**: Seleccione “Form“.  

   .. image:: /imgs/Registros/Registros80.png  

4. Haga clic en ``Mandar respuestas`` o utilice el botón flotante de envío para finalizar el registro.  

   .. image:: /imgs/Registros/Registros81.png  

Carga Universal
===============

Para cargar registros en la forma, siga estos pasos:

.. note:: Verifique que su `archivo .xlsx <#estructura-xlsx>`_ :octicon:`report;1em;sd-text-info` esté preparado y que la `forma <#alta-forma>`_ :octicon:`report;1em;sd-text-info` correspondiente haya sido dada de alta.

1. Acceda a ``Formas > Mis Formas`` desde el menú lateral.  
2. Ubique la forma **Carga Universal Module** dentro de la carpeta **Base**.  
3. Complete la forma con los siguientes campos:  

   - **Excel de relaciones campo-documento**: Cargue el archivo **.xlsx** previamente preparado.  
   - **Forma**: Seleccione el nombre de la forma donde se cargarán los registros.  

   .. warning::  

        No ingrese o modifique datos en los campos de estatus, errores o comentarios. Al enviar el registro, estos campos se actualizarán automáticamente según el resultado de la carga.

4. Haga clic en ``Mandar respuestas`` o utilice el botón flotante de envío para finalizar el registro.
5. Una vez enviada la carga, regrese al registro presionando ``Ver Registro``.

.. image:: /imgs/Registros/Registros82.png  

.. hint:: Espere entre 2 - 4 minutos, dependiendo de la cantidad de registros, y luego recargue la página del detalle del registro para visualizar los resultados.

.. .. hint:: Si no encuentra la forma, repórtelo a soporte técnico.

.. Revisión de Carga
.. =================
.. 
.. Para verificar que los registros se hayan cargado correctamente, siga estos pasos:
.. 
.. 1. Diríjase a ``Registros > Registros`` en el menú lateral.  
.. 2. Ingrese **Carga Universal Module** en el buscador para localizar la forma. De manera predeterminada, se mostrarán todos los registros ingresados.  
.. 
..    .. hint:: Puede aplicar filtros opcionales para refinar la búsqueda y luego presionar ``Filtrar`` para visualizar los registros.  
.. 
.. 3. Ubique el registro que desea revisar y ábralo para ver los detalles.  
.. 
..    .. hint:: Para acceder al registro, presione el segundo ícono para abrirlo en la misma página o el tercer ícono para abrirlo en una pestaña nueva.
.. 
..    .. image:: /imgs/Registros/Registros84.png

Interpretación de Errores
-------------------------

Para revisar la interpretación de errores, ubíquese en el registro correspondiente y verifique el estatus:

**Carga terminada**: La importación fue exitosa. Podrá ver el número total de registros creados en la sección de comentarios.
**Error**: Hubo problemas en la carga. Se mostrará la cantidad de registros creados y los errores detectados

.. note:: En caso de error, se adjuntará un archivo **.xlsx** con los registros que no se importaron correctamente.

**Cómo revisar los errores**

1. Descargue el archivo adjunto con los errores detectados.
2. En cada fila encontrará únicamente los registros que no se cargaron correctamente.
3. Al final de cada fila, dentro del archivo .xlsx, encontrará mensajes que indican la causa del error en cada campo.

A continuación, tomaremos como ejemplo el siguiente registro detectado con errores:

.. list-table::  
   :header-rows: 1  

   * - Nombre del Propietario  
     - Email  
     - ¿Cuenta con Seguro?  
     - Tipo: Tipo de Vehículo  
     - Tipo: Marca  
     - Tipo: Modelo  
     - Año de Fabricación  
     - Consumo de Combustible (km/l)  
     - Tipo de Combustible  
     - Equipamiento Adicional  
     - Color  
     - Fecha de Último Mantenimiento  
     - Mantenimiento Realizado: Descripción  
     - Mantenimiento Realizado: Mecánico Encargado: Nombre Completo  
     - Hora de Entrega  
   * - Patricia Fernández  
     - pati  
     - No sé  
     - Camión  
     - GMC  
     - Canyn  
     - 3  
     - 54  
     - Gasolia  
     - SSensor de Revrsa
     - Verde  
     - 2024-12-04  
     - Cambio de llantas  
     - SN  
     -

- **La estructura del email no es correcta**:

El valor *“pati“* no cumple con el formato válido de correo electrónico (debe contener “@“ y un dominio válido).  

- **La opción no esta dentro de los valores definidos: “¿Cuenta con Seguro?“**:

La opción *“No sé“* no está dentro de los valores definidos (ebe ser, por ejemplo: *Sí* / *No*).  

- **La opción no esta dentro de los valores definidos: “Tipo de Combustible“**:

La opción *“Gasolia“* no coincide con los valores definidos en el catálogo (debe ser, por ejemplo: *Gasolina* / *Diésel* / *Eléctrico* / *Híbrido*).  

- **Alguna de las opciones no esta dentro de los valores definidos: “Equipamiento Adicional“**:

*“Sensor de Revrsa“* no se encuentra dentro de las opciones válidas del catálogo (está mal escrito).

- **La opción no esta dentro de los valores definidos: “Color“**:

*“Verde“* no coincide con los valores definidos (debe ser, por ejemplo: *Azul* / *Blanco* / *Negro* / *Rojo*).  

- **No se encontró información en el catalogo “Tipo“**:

Alguno de los valores en *Tipo de Vehículo*, *Marca* o *Modelo* no se encontró en el catálogo correspondiente (en este caso el modelo).  

- **No se encontró información en el catalogo “Mecánico Encargado“**:

No se encontró el nombre *“SN“* en el catálogo de mecánicos registrados.  

.. hint:: Para corregir estos errores, revise y actualice los datos ingresados asegurándose de que los valores coincidan exactamente con los definidos en los catálogos y que el formato de los campos sea el adecuado.

.. LIGAS DE INTERÉS EXTERNO 

.. |archivoxlsx| raw:: html

    <a href="https://f001.backblazeb2.com/file/app-linkaform/public-client-126/71202/6650c41a967ad190e6a76dd3/67c5e6681821fbe43611f1ef.xlsx" target="_blank">aquí</a>

