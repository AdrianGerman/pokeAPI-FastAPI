from fastapi import FastAPI, Body, Path, Query, status
from fastapi.responses import HTMLResponse, JSONResponse
from pokemon_list import pokemons
from pydantic import BaseModel, Field
from typing import Optional, List

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


@app.get('/pokemons', tags=['pokemon'], response_model=List[Pokemon])
def get_pokemon() -> JSONResponse:
    return JSONResponse(content=pokemons, status_code=status.HTTP_200_OK)


@app.get('/pokemons/{id}', tags=['pokemon'], response_model=Pokemon)
def get_pokemon_id(id: int = Path(ge=0, le=2000)) -> Pokemon:
    for item in pokemons:
        if item['id'] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])


@app.get('/pokemons/by_type/{type}', tags=['pokemon'], response_model=List[Pokemon])
def get_pokemon_by_type(type: str) -> List[Pokemon]:
    data = list(filter(lambda pokemon: type in pokemon['type'], pokemons))
    return JSONResponse(content=data)


@app.post('/pokemons', tags=['pokemon'], response_model=dict, status_code=201)
def create_pokemon(pokemon: Pokemon) -> dict:
    pokemons.append(pokemon.model_dump())
    return JSONResponse(status_code=201, content={'message': 'Se ha registrado el pokémon'})


@app.put('/pokemons/{id}', tags=['pokemon'], response_model=dict, status_code=200)
def update_pokemon(id: int, pokemon: Pokemon) -> dict:
    for item in pokemons:
        if item['id'] == id:
            item['name'] = pokemon.name
            item['type'] = pokemon.type
            item['description'] = pokemon.description
            item['category'] = pokemon.category
            item['height'] = pokemon.height
            item['weight'] = pokemon.weight
            return JSONResponse(status_code=200, content={'message': 'Se ha modificado el pokémon'})


@app.delete('/pokemons/{id}', tags=['pokemon'], response_model=dict, status_code=200)
def delete_pokemon(id: int) -> dict:
    for item in pokemons:
        if item['id'] == id:
            pokemons.remove(item)
            return JSONResponse(status_code=200, content={'message': 'Se ha eliminado el pokémon'})
