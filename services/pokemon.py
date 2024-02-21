from models.pokemon import Pokemon as PokemonModel
from schemas.pokemon import Pokemon


class PokemonService():
    def __init__(self, db) -> None:
        self.db = db

    def get_pokemons(self):
        result = self.db.query(PokemonModel).all()
        return result

    def get_pokemon(self, id):
        result = self.db.query(PokemonModel).filter(
            PokemonModel.id == id).first()
        return result

    def get_pokemon_by_type(self, type):
        result = self.db.query(PokemonModel).filter(
            PokemonModel.type == type).all()
        return result

    def create_pokemon(self, pokemon: Pokemon):
        new_pokemon = PokemonModel(**pokemon.model_dump())
        self.db.add(new_pokemon)
        self.db.commit()
        return

    def update_pokemon(self, id: int, data: Pokemon):
        result = self.db.query(PokemonModel).filter(
            PokemonModel.id == id).first()
        result.name = data.name
        result.type = data.type
        result.description = data.description
        result.category = data.category
        result.height = data.height
        result.weight = data.weight
        self.db.commit()
        return

    def delete_pokemon(self, id: int):
        self.db.query(PokemonModel).filter(PokemonModel.id == id).delete()
        self.db.commit()
        return
