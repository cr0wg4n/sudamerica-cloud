# Nube de Palabras (Paises)
![](https://raw.githubusercontent.com/cr0wg4n/sudamerica-cloud/master/sudamerica_word/bolivia_words.png)
## Instalación

```bash
pip3 install -r requirements.txt
```

__Docker__

In the folder of the project create a .env file :

example:

```
PASSWORD_DB=password
USER_DB=root
```

build a docker container

```
docker-compose up 
```
or 

```
docker compose --env-file .env up
```

**Important** cloudwords:0.1 the app will terminate first but created the image(png) will be in sudamerica_word folder.

__next_step__ gitlab and ci/cd
