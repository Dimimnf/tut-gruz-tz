from typing import Optional
from pydantic import BaseModel, Field


class ContainerParams(BaseModel):
    type: Optional[str] = Field(None, description="Тип контейнера")
    price_min: Optional[int] = Field(None, description="Минимальная цена")
    price_max: Optional[int] = Field(None, description="Максимальная цена")
