# Instalación y configuración de Wordpress
----

----
## 1. Configuración de la base de datos

* Accedemos a `mysql server` y nos logueamos como root

![image](images/Selección_001.png)

* Creamos la base de datos y añadimos los privilegios.

![image](images/Selección_002.png)

![image](images/Selección_003.png)

![image](images/Selección_004.png)

## 2. Descarga de código

* Descargamos el codigo fuente de Wordpress desde la web utilizando el comando `curl`

![image](images/Selección_005.png)

![image](images/Selección_006.png)

* Ahora descomprimimos el fichero zip que nos hemos descargado y lo metemos en `/usr/share`. Si no tenemos instalado la utilidad `unzip`, la instalamos.

![image](images/Selección_007.png)

![image](images/Selección_008.png)

![image](images/Selección_009.png)

* A continuación le damos permisos al usuario `www-data` para controlar estos ficheros.

![image](images/Selección_010.png)

## 3. Editando los ficheros de Configuración

* Copiamos el fichero plantilla `wp-config-sample.php`, del directorio `/usr/share/wordpress/` y lo llamamos `wp-config.php` de la siguiente forma:

```console

sudo cp wp-config-sample.php wp-config.php

```

* Una vez hecho esto, tenemos que modificar una serie de líneas en ese fichero.

![image](images/Selección_011.png)

  - `define('DB_NAME', 'wpdatabase');` Identifica el nombre

  - `define('DB_USER', 'dbuser');` Identifica el usuario

  - `define('DB_PASSWORD', 'XXXXXXXXX');` Indica cual es la contraseña

  - `define('DB_CHARSET', 'utf8mb4');` Define el charset a utilizar

## 4. Acceso mediante Nginx

* Para que nuestro Wordpress sea accesible desde un navegador, tenemos que crear un virtual host en la ruta `/etc/nginx/sites-available/wordpress` con la siguiente configuración

![image](images/Selección_013.png)

* Ahora enlazamos con el directorio `sites-enabled`

![image](images/Selección_012.png)

* Recargamos el servicio de Nginx

![image](images/Selección_014.png)

## 5. Configuración del sitio web

* Una vez hecho lo anterior correctamente deberíamos poder acceder sin problemas desde un navegador a nuestro wordpress, donde nos aparecerá una especie de asistente de instalación. En principio elegimos el idioma `Español`

![image](images/Selección_015.png)

* Luego nos pedirá que rellenemos los siguientes campos

![image](images/Selección_016.png)

* Una vez acabado esto, ya podemos empezar

![image](images/Selección_017.png)

![image](images/Selección_018.png)

* Aquí vemos la interfaz de Wordpress por primera vez

![image](images/Selección_019.png)

## 6. Ajuste de permalinks y personalización de la página

* Para acceder al menu de personalización de los permalinks tenemos que acceder a ajustes (marcado con una pequeña cajetilla roja en la imagen)

![image](images/Selección_020.png)

* Una vez abierta dicha pestaña, de damos a la opción `Enlaces permanentes` y nos debería aparecer lo siguiente, donde en nuestro caso seleccionamos `Día y nombre`

![image](images/Selección_022.png)

* Vamos de nuevo a la pestaña `Escritorio`, desde donde accederemos a la pestaña `Personaliza tu sitio`

![image](images/Selección_027.png)

* Una vez ahí, si seleccionamos `Temas de wordpress.org` nos aparecerán muchos temas para elegir. Elegimos uno cualquiera

![image](images/Selección_028.png)

* Le damos a instalar

![image](images/Selección_029.png)

* Y aquí tenemos la vista previa de lo que sería nuestra página ahora mismo

![image](images/Selección_030.png)

* Si vamos a `Escritorio` y luego accedemos a la pestaña `Entradas` podemos incluir noticias a nuestra web. Como prueba haremos la siguiente entrada

![image](images/Selección_032.png)

![image](images/Selección_031.png)

* La agregamos y aparecerá en nuestra web tal que así

![image](images/Selección_033.png)

![image](images/Selección_034.png)
