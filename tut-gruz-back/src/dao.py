import json
from pathlib import Path
from typing import List, Optional

from src.models import Container
from src.params import ContainerParams


class ContainerDAO:
    def __init__(self, data_path: str):
        self._data_path = Path(data_path)
        self._containers: List[Container] = []
        self._load()

    def _load(self) -> None:
        with open(self._data_path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        self._containers = [Container(**item) for item in raw["containers"]]

    def get_all(self, params: Optional[ContainerParams] = None) -> List[Container]:
        if not params:
            return self._containers

        c_list = self._containers
        if params.type:
            c_list = [c for c in c_list if c.type == params.type]
        if params.price_min is not None:
            c_list = [c for c in c_list if c.price >= params.price_min]
        if params.price_max is not None:
            c_list = [c for c in c_list if c.price <= params.price_max]

        return c_list

    def get_by_id(self, container_id: str) -> Optional[Container]:
        return next((c for c in self._containers if c.id == container_id), None)

    def get_by_slug(self, slug: str) -> Optional[Container]:
        return next((c for c in self._containers if c.slug == slug), None)

    def get_by_type(self, container_type: str) -> List[Container]:
        """20ft | 40ft_hc | 40ft_reefer"""
        return [c for c in self._containers if c.type == container_type]


container_dao = ContainerDAO("src/containers.json")
