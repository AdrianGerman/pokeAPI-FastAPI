from models.pokemon import Pokemon as PokemonModel


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
