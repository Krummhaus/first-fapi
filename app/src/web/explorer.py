# There is a new routrer in town
from fastapi import APIRouter
from model.explorer import Explorer
import fake.explorer as service


router = APIRouter(prefix="/explorer")


@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

# app.include_router(explorer.router)
