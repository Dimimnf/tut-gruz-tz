from typing import List
from pydantic import BaseModel, Field


class Container(BaseModel):
    id: str = Field(
        ...,
        description="Уникальный идентификатор контейнера",
        example="20ft-001",
    )
    type: str = Field(
        ...,
        description="Тип контейнера (20ft, 40ft_hc, 40ft_reefer)",
        example="20ft",
    )
    slug: str = Field(
        ...,
        description="URL-идентификатор контейнера",
        example="20ft-001",
    )
    price: int = Field(
        ...,
        description="Цена контейнера",
        example=2200,
        gt=0,
    )
    currency: str = Field(
        ...,
        description="Валюта цены",
        example="EUR",
        min_length=3,
        max_length=3,
    )
    short_description: str = Field(
        ...,
        description="Краткое описание для карточки в каталоге",
        example="20-футовый контейнер, б/у",
        max_length=255,
    )
    description: str = Field(
        ...,
        description="Полное описание контейнера",
        example="Надёжный контейнер для хранения и перевозки грузов",
    )
    images: List[str] = Field(
        ...,
        description="Список URL изображений (первое — превью)",
        example=[
            "/static/images/20ft/001_preview.jpg",
            "/static/images/20ft/001_inside.jpg",
            "/static/images/20ft/001_outside.jpg",
        ],
        min_items=1,
    )

    class Config:
        json_schema_extra = {
            "example": {
                "id": "20ft-001",
                "type": "20ft",
                "slug": "20ft-001",
                "price": 2200,
                "currency": "EUR",
                "short_description": "20-футовый контейнер, б/у",
                "description": "Стандартный 20-футовый контейнер в хорошем состоянии",
                "images": [
                    "/static/images/20ft/001_preview.jpg",
                    "/static/images/20ft/001_inside.jpg",
                    "/static/images/20ft/001_outside.jpg"
                ]
            }
        }
