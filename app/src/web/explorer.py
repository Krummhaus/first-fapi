# There is a new routrer in town
from fastapi import APIRouter

router = APIRouter(prefix="/explorer")


@router.get("/")
def top():
    return "top explorer endpoint"


# app.include_router(explorer.router)
