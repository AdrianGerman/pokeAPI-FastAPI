from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from pokemon_list import pokemons
from routers.pokemon import pokemon_router
from routers.user import user_router


app = FastAPI()
app.title = 'PokeAPI from FastAPI'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)

app.include_router(pokemon_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello Germán</h1>')
