Documentacion de LinkaForm


Para hacer el build

1. Para realizar el build es necesario levantar el contendor de lkf-documenation donde vive el proyecto.
```
docker compose up -d
```

2. Una vez con el contenedor corriendo entrar al contenedor 
```
docker exec -it lkf-documentation bash
```

3. Ya dentro del contenedor ejecutar

```
local_build
```
el cual es un pequeño ejecutable que realizamos para hacer las coas mas facil, o bien puedes 
```
cd /srv/docs/
rm -rf /srv/docs/build
sphinx-build -c /srv/docs/ content/ build/
```

## Build Documentation

### Ambiente

Para crear tu ambiente de produccion, primero tienes que hacer un build del `docker` dentro del cual se van a compliar los archivos. Para garantizar que los archivos que se compilen, se creen con el usaurio correcto y tengas permisos para lees y escribir en dichos archivos, es ncesario correr el build con el mismo usuario que usas en tu computadora, para ello, vamos a generar el build con este comando.

```
docker-compose build --build-arg UID=$UID
```

Esto es necesario solo correrlo cada vez que quieras actualizar tu ambiente de produccion. Posteriormente solo correr la compliacion de la documentacion.

### Compliar Documentacion


Para hace el build de la documentación, colocate en la carpeta padre del proyecto y corre el comando

```
docker-compose up 
```
o si tienes la version mas acutal de docker correr
```
docker compose up 
```

Entrar al contenedor y hacer el build local
```
```

una vez realizada la compilacion hacer un tar de la carpeta build

```
tar -czvf documentacion.tar.gz build
```
copiar tar  a server
```
scp documentacion.tar.gz docs.linkaform.com:
```

En el servidor correr estos comandos
```
tar xzvf documentacion.tar.gz 
cp -a build/* /srv/docs/
```

https://www.sphinx-doc.org/en/master/