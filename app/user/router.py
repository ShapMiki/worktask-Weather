from fastapi import APIRouter, Request, Depends, Response


router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.delete("/")
async def delete_history(request: Request, response: Response):
    response.delete_cookie(key="user_id", path="/")