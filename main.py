from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pokemon_list import pokemons

from typing import List, Optional

app = FastAPI()

app.title = 'PokeAPI from FastAPI'
# app.version = '0.0.1'


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello Germán</h1>')

@app.get('/pokemons', tags=['pokemon'])
def get_pokemon():
    return pokemons

@app.get('/pokemons/{id}', tags=['pokemon'])
def get_pokemon_id(id: int):
    for item in pokemons:
        if item['id'] == id:
            return item
    return []

@app.get('/pokemons/by_type/{type}', tags=['pokemon'])
def get_pokemon_by_type(type: str):    
    return list(filter(lambda pokemon: type in pokemon['type'], pokemons))


@app.post('/pokemons', tags=['pokemon'])
def create_pokemon(id: int = Body(), name: str = Body(), type: list = Body(...), description: str = Body(), category: str = Body(), height: float = Body(), weight: float = Body()):
    pokemons.append({
        'id': id,
        'name': name,
        'type': type,
        'description': description,
        'category': category,
        'height': height,
        'weight': weight
    })
    return pokemons

@app.put('/pokemons/{id}', tags=['pokemon'])
def update_pokemon(id: int, name: str = Body(), type: list = Body(...), description: str = Body(), category: str = Body(), height: float = Body(), weight: float = Body()):
    for item in pokemons:
        if item['id'] == id:
            item['name'] = name,
            item['type'] = type,
            item['description'] = description,
            item['category'] = category,
            item['height'] = height,
            item['weight'] = weight,
            return pokemons
            
            
            
@app.delete('/pokemons/{id}', tags=['pokemon'])
def delete_pokemon(id: int):
    for item in pokemons:
        if item['id'] == id:
            pokemons.remove(item)
            return pokemons
            

