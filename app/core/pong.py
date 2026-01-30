from fastapi import APIRouter
router = APIRouter( prefix="/ping",tags=["Ping"])


@router.get("", summary="Retourne Pong")
def route_get_ping():
    return {"message":"Pong"}
