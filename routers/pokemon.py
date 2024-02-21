from fastapi import APIRouter
from fastapi import Path, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from pydantic import BaseModel, Field
from typing import List, Optional
from models.pokemon import Pokemon as PokemonModel
from config.database import Session
from services.pokemon import PokemonService

pokemon_router = APIRouter()


class Pokemon(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="Pokémon", max_length=15)
    type: str = Field(default="Normal")
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


@pokemon_router.get('/pokemons', tags=['pokemon'], response_model=List[Pokemon], dependencies=[Depends(JWTBearer())])
def get_pokemon() -> JSONResponse:
    db = Session()
    result = PokemonService(db).get_pokemons()
    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@pokemon_router.get('/pokemons/{id}', tags=['pokemon'], response_model=Pokemon)
def get_pokemon_id(id: int = Path(ge=0, le=2000)) -> Pokemon:
    db = Session()
    result = PokemonService(db).get_pokemon(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@pokemon_router.get('/pokemons/by_type/{type}', tags=['pokemon'])
def get_pokemon_by_type(type: str):
    db = Session()
    # type_list = type.split(', ')
    result = db.query(PokemonModel).filter(PokemonModel.type == type).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@pokemon_router.post('/pokemons', tags=['pokemon'], response_model=dict, status_code=201)
def create_pokemon(pokemon: Pokemon) -> dict:
    db = Session()
    new_pokemon = PokemonModel(**pokemon.model_dump())
    db.add(new_pokemon)
    db.commit()
    # pokemons.append(pokemon.model_dump())
    return JSONResponse(status_code=201, content={'message': 'Se ha registrado el pokémon'})


@pokemon_router.put('/pokemons/{id}', tags=['pokemon'], response_model=dict, status_code=200)
def update_pokemon(id: int, pokemon: Pokemon) -> dict:
    db = Session()
    result = db.query(PokemonModel).filter(PokemonModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    result.name = pokemon.name
    result.type = pokemon.type
    result.description = pokemon.description
    result.category = pokemon.category
    result.height = pokemon.height
    result.weight = pokemon.weight

    db.commit()
    return JSONResponse(status_code=200, content={'message': 'Se ha modificado el pokémon'})


@pokemon_router.delete('/pokemons/{id}', tags=['pokemon'], response_model=dict, status_code=200)
def delete_pokemon(id: int) -> dict:
    db = Session()
    result = db.query(PokemonModel).filter(PokemonModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})

    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={'message': 'Se ha eliminado el pokémon'})
