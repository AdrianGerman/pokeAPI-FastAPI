# PokeAPI con FastAPI

API sencilla de pokémones creada con FastAPI

## Ejecución del proyecto

Para correr el proyecto **PokeAPI** debes seguir las siguientes instrucciones.

1. crear el archivo **.env** y creamos nuestra key (tomando de ejemlo el archivo **.env.example**)

2. Instalamos las dependencias necesarias para correr el proyecto, seguimos los siguientes pasos en la terminal.
   ```sh
   pip freeze > requirements.txt
   ```
3. Y listo, tines 2 maneras de ejecutar el proyecto, de manera manual.

   ```sh
   uvicorn main:app --reload
   ```

   o de la manera automatica que es corriendo el archivo run.py

   > windows

   ```sh
   python run.py
   ```

   > linux

   ```sh
   python3 run.py
   ```
