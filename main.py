from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pokemon_list import pokemon

app = FastAPI()

app.title = 'PokeAPI from FastAPI'
# app.version = '0.0.1'


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello Germán</h1>')

@app.get('/pokemon', tags=['pokemon'])
def get_pokemon():
    return pokemon

@app.get('/pokemon/{id}', tags=['pokemon'])
def get_pokemon_id(id: int):
    for item in pokemon:
        if item['id'] == id:
            return item
    return []