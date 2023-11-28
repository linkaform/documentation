===========
Bibliotecas
===========

El frontend consiste en el desarrollo de la interfaz gráfica de un sitio o aplicación web, usando herramientas como HTML, CSS y JavaScript. Linkaform hace uso de estas herramientas y de librerías para agilizar el desarrollo de los reportes. En esta sección se brindaran los conocimientos necesarios para la implementación de reportes en el frontend y todo lo necesario respecto a las librerías utilizadas.

.. _card-boostrap.txt:
.. card:: **Boostrap** 

	Es una biblioteca de estilos, cuenta con una variedad de complementos de UI agilizando el desarrollo de la estructura y el diseño. Esta hace uso principalmente de clases que definen los estilos a implementar. Si desea conocer a mayor profundidad esta librería puede acceder a su sitio oficial en el siguiente enlace `bootstrap <https://getbootstrap.com/docs/5.0/getting-started/introduction/>`_ :octicon:`report;1em;sd-text-info`.

	Para hacer uso de esta biblioteca se hace uso de un CDN, esto permite obtener todos los estilos de la biblioteca a partir de un enlace, esto se hace porque el proyecto se encuentra alojado en un docker y por cada actualización seria necesario descargar el archivo, esto no es mantenible para agilizar el proceso,  se usa el siguiente CDN.

.. tab-set::

    .. tab-item:: Ejemplo

		.. code-block:: html

			<!doctype html>
			<html>
			<head>
				<meta charset="utf-8">
				<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
				<!-- Bootstrap CSS -->
				<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
				<title>Hola Mundo</title>
			</head>
			<body>
				<div class="container" style="background-color:#ccc"> 
				<h1>Hola Mundo!</h1>
				</div>
				
				<!-- Si utilizamos componentes de Bootstrap que requieran Javascript agregar estos tres archivos -->
				<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
				<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
				<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
			</body>
			</html>

    .. tab-item:: Código

		.. code-block:: html

			<!doctype html>
			<html>
			<head>
				<meta charset="utf-8">
				<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
				<!-- Bootstrap CSS -->
				<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
				<title>Hola Mundo</title>
			</head>
			<body>
				<div class="container" style="background-color:#ccc"> 
				<h1>Hola Mundo!</h1>
				</div>
				
				<!-- Si utilizamos componentes de Bootstrap que requieran Javascript agregar estos tres archivos -->
				<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
				<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
				<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
			</body>
			</html>



.. _card-vanilla.txt:

.. card:: **Vanilla JS** 
	
	Vanila JS hace uso de JavaScript puro, está orientada en mejorar el rendimiento del cliente, a partir de ECMAScript 6, se puede hacer tareas que normalmente se hacen con librerías más pesadas con JQuery.
	
	Si desea conocer a profundidad de esta librería, puede visitar su sitio oficial `vanilaJs <http://vanilla-js.com/>`_ :octicon:`report;1em;sd-text-info`.

.. _card-jquery.txt:
.. card:: **JQuery** 
	
	Es una librería de código abierto, esta permite controlar eventos, crear animaciones de manera menos verbosa que JavaScript puro. Si desea conocer más respecto a la librería puede visitar su sitio oficial `jQuery <https://jquery.com/>`_ :octicon:`report;1em;sd-text-info`.
	
	Para desarrollar reportes, se usa JQuery para agilizar el manejo de elementos en el DOM y crear animaciones de forma sencilla.

	Para acceder a la librería utilice el siguiente CDN: 

.. code-block:: html

	<!DOCTYPE html>
	<html lang="es">
	<head>
		<meta charset="UTF-8">
		<!-- Incluye jQuery desde un CDN -->
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
	</head>
	<body>
		<h1>Mi Página con jQuery</h1>
		<p>Haz clic en el botón para cambiar el texto de este párrafo.</p>
		
		<button id="cambiarTexto">Cambiar Texto</button>

		<!-- El código jQuery -->
		<script>
			// Espera a que el documento esté listo
			$(document).ready(function(){
				// Agrega un controlador de evento al botón
				$("#cambiarTexto").click(function(){
					// Cambia el texto del párrafo
					$("p").text("El texto ha sido cambiado con jQuery.");
				});
			});
		</script>
	</body>
	</html>

.. _card-charjs.txt:
.. card:: **Charjs** 

	ChartJs es una librería basada en JavaScript, esta cuenta con un conjunto de gráficos que permiten personalizarlos, agregar complementos y agregar ciertas funcionalidades, los gráficos más comunes son los de pie, barras y de tendencia. 
	Si desea conocer más acerca de ChartJs puede acceder a su sitio oficial `Chartjs <https://www.chartjs.org/>`_ :octicon:`report;1em;sd-text-info`.

	Puede encontrar algunos ejemplos en el siguiente enlace `Ejercicios de Chartjs <https://tobiasahlin.com/blog/chartjs-charts-to-get-you-started/#8-grouped-bar-chart/>`_ :octicon:`report;1em;sd-text-info`.

	Los reportes hacen uso de los gráficos para brindar a los clientes un resumen visual de sus datos, a continuación se muestra un ejemplo para entender su estructura y uso.
	Para acceder a la librería utilice el siguiente CDN:

.. tab-set::

    .. tab-item:: Ejemplo

		.. code-block:: html

			<!DOCTYPE html>
			<html lang="es">
			<head>
				<meta charset="UTF-8">

				<!-- Incluye Chart.js desde un CDN -->
				<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
			</head>
			<body>
				<h3>Gráfico de Barras con Chart.js</h3>

				<!-- Contenedor del gráfico -->
				<div style="width: 80%; max-width: 600px; margin: 0 auto;">
					<canvas id="miGrafico"></canvas>
				</div>

				<!-- El código para crear el gráfico -->
				<script>
					// Datos del gráfico
					var data = {
						labels: ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
						datasets: [{
							label: "Ventas Mensuales",
							backgroundColor: "rgba(75, 192, 192, 0.2)",
							borderColor: "rgba(75, 192, 192, 1)",
							borderWidth: 1,
							data: [12, 19, 3, 5, 2]
						}]
					};

					// Opciones del gráfico
					var options = {
						scales: {
							y: {
								beginAtZero: true
							}
						}
					};

					// Obtén el contexto del lienzo (canvas) donde se dibujará el gráfico
					var ctx = document.getElementById("miGrafico").getContext("2d");

					// Crea el gráfico de barras
					var myChart = new Chart(ctx, {
						type: 'bar',
						data: data,
						options: options
					});
				</script>
			</body>
			</html>

    .. tab-item:: Código

		.. code-block:: html

			<!DOCTYPE html>
			<html lang="es">
			<head>
				<meta charset="UTF-8">

				<!-- Incluye Chart.js desde un CDN -->
				<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
			</head>
			<body>
				<h3>Gráfico de Barras con Chart.js</h3>

				<!-- Contenedor del gráfico -->
				<div style="width: 80%; max-width: 600px; margin: 0 auto;">
					<canvas id="miGrafico"></canvas>
				</div>

				<!-- El código para crear el gráfico -->
				<script>
					// Datos del gráfico
					var data = {
						labels: ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
						datasets: [{
							label: "Ventas Mensuales",
							backgroundColor: "rgba(75, 192, 192, 0.2)",
							borderColor: "rgba(75, 192, 192, 1)",
							borderWidth: 1,
							data: [12, 19, 3, 5, 2]
						}]
					};

					// Opciones del gráfico
					var options = {
						scales: {
							y: {
								beginAtZero: true
							}
						}
					};

					// Obtén el contexto del lienzo (canvas) donde se dibujará el gráfico
					var ctx = document.getElementById("miGrafico").getContext("2d");

					// Crea el gráfico de barras
					var myChart = new Chart(ctx, {
						type: 'bar',
						data: data,
						options: options
					});
				</script>
			</body>
			</html>


.. _card-tabulator.txt:
.. card:: **Tabulator**

	Es una librería basada en JavaScript, cuenta con una amplia variedad de tablas, además de un grupo de complementos que agilizan la construcción de tablas. Esta tiene ciertas funcionalidades que permiten descargar los registros en distintos formatos como: pdf, excel, csv, JSON, entre otros.
	Si desea conocer más  a detalle esta librería; consulte su página oficial `Tabulator <https://tabulator.info/>`_ :octicon:`report;1em;sd-text-info`.

