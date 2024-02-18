from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse
from pokemon_list import pokemons
from pydantic import BaseModel, Field
from typing import Optional

from typing import List, Optional

app = FastAPI()

app.title = 'PokeAPI from FastAPI'
app.version = '0.0.1'


class Pokemon(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="Pokémon", max_length=15)
    type: list = Field(default=["Normal", "Fuego", "Agua"])
    description: str = Field(default="Un pokémon salvaje")
    category: str = Field(default="Animal")
    height: float = Field(default=1.2)
    weight: float = Field(default=0.35)

    # este tipo de modelo dejo de funcionar hace años
    # lo dejo aquí por si algún día vuelve a funcionar

    # model_config = {
    #     "json_schema_extra": {
    #         "examples": [
    #             {
    #                 "id": 7,
    #                 "name": "Pokémon",
    #                 "type": ["Normal", "Fuego", "Agua"],
    #                 "description": "Un pokémon salvaje",
    #                 "category": "Animal",
    #                 "height": 1.2,
    #                 "weight": 0.35,
    #             }
    #         ]
    #     }
    # }


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello Germán</h1>')


@app.get('/pokemons', tags=['pokemon'])
def get_pokemon():
    return pokemons


@app.get('/pokemons/{id}', tags=['pokemon'])
def get_pokemon_id(id: int = Path(ge=1, le=2000)):
    for item in pokemons:
        if item['id'] == id:
            return item
    return []


@app.get('/pokemons/by_type/{type}', tags=['pokemon'])
def get_pokemon_by_type(type: str):
    return list(filter(lambda pokemon: type in pokemon['type'], pokemons))


@app.post('/pokemons', tags=['pokemon'])
def create_pokemon(pokemon: Pokemon):
    pokemons.append(pokemon)
    return pokemons


@app.put('/pokemons/{id}', tags=['pokemon'])
def update_pokemon(id: int, pokemon: Pokemon):
    for item in pokemons:
        if item['id'] == id:
            item['name'] = pokemon.name
            item['type'] = pokemon.type
            item['description'] = pokemon.description
            item['category'] = pokemon.category
            item['height'] = pokemon.height
            item['weight'] = pokemon.weight
            return pokemons


@app.delete('/pokemons/{id}', tags=['pokemon'])
def delete_pokemon(id: int):
    for item in pokemons:
        if item['id'] == id:
            pokemons.remove(item)
            return pokemons
