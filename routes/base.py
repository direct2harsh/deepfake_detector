from fastapi import APIRouter


router = APIRouter(prefix="/base",tags=["base"])


@router.get("/")
def base():
    return {"Response":"You are at the base"}
