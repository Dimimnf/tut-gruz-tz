from fastapi import APIRouter, Depends
from src.dao import container_dao
from src.params import ContainerParams
from src.dependencies import verify_user

router = APIRouter(prefix="/containers", tags=["Контейнеры"])


@router.get("")
async def get_containers(
    params: ContainerParams = Depends(), user_id: str = Depends(verify_user)
):
    res = container_dao.get_all(params=params)
    return res


@router.get("/{id}")
async def get_container(id: str, user_id: str = Depends(verify_user)):
    res = container_dao.get_by_id(id)
    return res
