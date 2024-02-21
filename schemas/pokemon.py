from pydantic import BaseModel, Field
from typing import Optional


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
