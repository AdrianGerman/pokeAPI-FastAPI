from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = 'PokeAPI from FastAPI'
# app.version = '0.0.1'

pokemon = [
    {
    'id': 1,
    'title': 'Bulbasaur',
    'type': 'Planta, Veneno',
    'description': 'Lleva un bulbo en el lomo desde que nace. A medida que el Pokémon crece, el bulbo también va haciéndose más grande.',
    'category': 'Semilla',
    'height': 0.7,
    'weight': 6.9,
    }
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello Germán</h1>')

@app.get('/pokemon', tags=['pokemon'])
def get_pokemon():
    return pokemon