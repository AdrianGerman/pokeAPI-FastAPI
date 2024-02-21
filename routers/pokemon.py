from fastapi import APIRouter
from fastapi import Path, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from typing import List
from models.pokemon import Pokemon as PokemonModel
from config.database import Session
from services.pokemon import PokemonService
from schemas.pokemon import Pokemon

pokemon_router = APIRouter()


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
    result = PokemonService(db).get_pokemon_by_type(type)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@pokemon_router.post('/pokemons', tags=['pokemon'], response_model=dict, status_code=201)
def create_pokemon(pokemon: Pokemon) -> dict:
    db = Session()
    PokemonService(db).create_pokemon(pokemon)
    # pokemons.append(pokemon.model_dump())
    return JSONResponse(status_code=201, content={'message': 'Se ha registrado el pokémon'})


@pokemon_router.put('/pokemons/{id}', tags=['pokemon'], response_model=dict, status_code=200)
def update_pokemon(id: int, pokemon: Pokemon) -> dict:
    db = Session()
    result = db.query(PokemonModel).filter(PokemonModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    PokemonService(db).update_pokemon(id, pokemon)
    return JSONResponse(status_code=200, content={'message': 'Se ha modificado el pokémon'})


@pokemon_router.delete('/pokemons/{id}', tags=['pokemon'], response_model=dict, status_code=200)
def delete_pokemon(id: int) -> dict:
    db = Session()
    result: PokemonModel = db.query(PokemonModel).filter(
        PokemonModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'No encontrado'})
    PokemonService(db).delete_pokemon(id)
    return JSONResponse(status_code=200, content={'message': 'Se ha eliminado el pokémon'})
