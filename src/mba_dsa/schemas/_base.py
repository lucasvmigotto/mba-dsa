from pydantic import BaseModel, ConfigDict


class _BaseSchema(BaseModel):
    model_config: ConfigDict = ConfigDict(
        use_enum_values=True,
        validate_by_name=True,
        validate_by_alias=True,
        extra="ignore",
    )
