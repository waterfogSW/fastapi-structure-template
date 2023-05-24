from fastapi import APIRouter, status

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
async def get_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
