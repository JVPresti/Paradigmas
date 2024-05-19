# Introducción a Git

    En esta guía, se describe el proceso para comenzar a utilizar Git, desde la creación de una cuenta hasta la realización de commits y push a un repositorio remoto en GitHub.

## Comando utiles en la terminal

    - mkdir crea un repositorio de manerea local
    - cd <direccion> te lleva a un lugar
    - git status se usa para ver el estatus del repositorio
    - git clone <url> copia un repositorio
    - git checkout -b <branch> crea una rama y cambia a ella
    - git restore te deja restaurar un archivo antes de hacerle commit
    - git diff te muestra los cambios de los archivos
    - git log te muestra los commits realizados
    - git merge es para hacer un merge entre ramas
    - git push sube los cambios a un repositorio en la nube
    - git pull obtiene la version mas reciente en la nube

 ## Creación de cuenta y llave SSH

    - Se comienza creando y verificando una cuenta de Git.
    - Se genera una llave de seguridad del tipo SSH con el comando $ssh-keygen, lo cual produce archivos locales con la key.
    - En la página oficial de GitHub, se procede a agregar la llave pública y establecer una contraseña.

## Configuración del repositorio

    - Para crear un repositorio local se tiene que realizar el comado $mkdir <nombre>
    - Se crea un proyecto con el comando $git remote add origin <url>, una vez se ha creado un repositorio en la página de GitHub.
    - Para asegurar que los push se realicen correctamente, se utiliza $git push -u origin <branch>.

## Inicialización del repositorio local

    - Se inicializa un repositorio local con el comando git init.
    - Una vez iniciado el repositorio, se puede comenzar a trabajar en él.

## Gestión de cambios y commits

    - Para añadir archivos al área de preparación, se utiliza el comando git add <nombre del archivo> para cada archivo.
    - Se verifica el estado del proyecto con git status.
    - Si se desean subir todos los archivos al área de preparación, se emplea git add ..
    - Una vez que todos los archivos están preparados, se realiza un commit con el mensaje descriptivo utilizando git commit -m "mensaje".

## Conclusiones

    - Después de realizar un commit, los cambios permanecen en el repositorio local. Para sincronizarlos con el repositorio remoto, se requiere realizar un push.