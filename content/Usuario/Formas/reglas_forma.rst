.. _reglas-form:

===============
Reglas de Forma
===============

Las reglas de forma son configuraciones que posibilitan:

- Mostrar campos
- Deshabilitar campos
- Requerir campos
- Ocultar campos

.. important:: La configuración de las reglas de forma es independiente para cada forma. En otras palabras, si duplica la misma forma, es necesario crear las reglas de forma de manera independiente, ya que no se duplicarán automáticamente.

Siga los siguientes pasos, que son requeridos para cada regla de campo:

1. Ubíquese en la forma a la que desea aplicar la regla de campo.
2. Seleccione ``Opciones > Reglas de Forma``.

.. image:: /imgs/Formas/Formas62.jpg

3. Haga clic en el botón verde con el icono de más para ``Agregar Regla``.

.. image:: /imgs/Formas/Formas63.jpg

4. Asigne un nombre descriptivo que diferencie su regla, haciendo doble clic en el nombre predeterminado ``Regla N``.

5. En el campo ``Deseo``, seleccione una opción.

.. seealso:: Opciones

  - **Mostrar**: Se utiliza para que, al cumplir una validación configurada, se muestren uno o más campos.
  - **Deshabilitar**: Funciona para que, al cumplir una validación configurada, se deshabiliten uno o más campos.
  - **Requerir**: Es útil para que, al cumplir una validación configurada, se requieran de manera obligatoria uno o más campos.
  - **Ocultar**: Se utiliza para que, al cumplir una validación configurada, se oculten uno o más campos.

6. Seleccione el o los campos que serán afectados por la regla, presionando el botón ``Campos``. Observe que aparecerán los campos de su forma.

.. image:: /imgs/Formas/Formas66.jpg

7. Escriba el nombre del campo que hará la condición que se debe cumplir para la ejecución de la regla de forma.  Observe que aparecerá un recuadro verde con el tipo de campo que representa dicho campo.

.. tip:: Si no recuerda el nombre del campo, teclee dos puntos ``(:)`` y Linkaform mostrará todos los campos de la forma.

  .. image:: /imgs/Formas/Formas67.jpg

8. Seleccione una condición para que se cumpla la regla. 

.. seealso:: Opciones

  - **No está vacío**: Esta opción valida si el campo no está vacío, es decir, si contiene algún valor.
  - **Está vacío**: Verifica si el campo está vacío, sin contener ningún valor.
  - **No contiene opción**: Comprueba si el campo no contiene una opción específica.
  - **Contiene opción**: Evalúa si el campo contiene una opción específica.
  - **No es igual a**: Esta opción verifica si el campo no es igual al valor especificado.
  - **Igual a**: Verifica si el campo es igual al valor especificado.

La elección de las últimas cuatro opciones permitirá seleccionar o escribir contenido para realizar la validación. Puede incluir más de una validación para un campo; sin embargo, debe aplicar una relación lógica ``AND`` o ``OR``.

.. image:: /imgs/Formas/Formas68.1.png

9. Opcionalmente, seleccione el botón ``Duplicar`` para replicar la regla exactamente como está configurada en ese momento (esta opción es útil cuando se desean crear reglas muy similares).
10. Opcionalmente, seleccione ``Condiciones de usuario`` con el ícono de un solo usuario para incluir o excluir usuarios de esta regla de forma.
11. Opcionalmente, seleccione ``Condiciones de grupo`` con el ícono de grupo para incluir o excluir un grupo de usuarios de esta regla de forma.
12. Guarde sus cambios.

Consulte el video a continuación para obtener ejemplos visuales.

.. youtube:: N-eQmvPNo40
  :aspect: 16:9
  :width: 100%
  :height: 480
  :align: center
  :privacy_mode: enable_privacy_mode
  :url_parameters: ?start=23