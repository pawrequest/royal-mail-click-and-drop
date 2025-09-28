from pydantic import BaseModel, ConfigDict, AliasGenerator
from pydantic.alias_generators import to_pascal


class RMBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            alias=to_pascal,
        ),
        populate_by_name=True,
        use_enum_values=True,
    )
