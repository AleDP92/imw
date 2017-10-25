# UT1-A4: Sirviendo aplicaciones Php y Python

## Propósito de la actividad

La actividad consiste en configurar 2 sitios web (virtual hosts) en nuestro servidor web Nginx.

## Comienzo de la actividad

### Sitio web 1

Tenemos que crear un sitio web denominado `http://php.alu2302.me`, que lea el contenido PHP de un fichero descargado con anterioridad.

* Para ello, como llevamos haciendo hasta ahora, lo primero que tenemos que hacer es crear el virtualhost para la práctica, asi que nos vamos a la siguiente ruta y ejecutamos "nano":

```console

alu2302@cloud:/etc/nginx/sites-available$ sudo nano php

```

* Dentro del fichero de nuestro virtualhost especificamos la ruta en la cual se buscarán los ficheros, así como también debemos especificar que sea PHP quien se encargue de procesar la información, cosa que especificaremos en la directiva que tenemos abajo.

![image](img/000035.png)

* Como siempre, creamos el enlace

```console

alu2302@cloud:/etc/nginx/sites-enabled$ sudo ln -s ../sites-available/php .

```

* Una vez hecho esto, nos vamos a nuestro directorio home y creamos el directorio php.

```console

alu2302@cloud:~$ mkdir php

```

* Una vez descargado y realizada la copia remota del fichero zip a descargar por medio del comando `scp`, colocamos al mismo dentro del directorio php.

![image](img/000039.png)

* Por último, reiniciamos el servicio.

```console

alu2302@cloud:~$ sudo systemctl reload nginx.service

```

* Al acceder a la dirección http://php.alu2302.me nos debe aparecer lo siguiente:

![image](img/000041.png)

---

## Sitio web 2
