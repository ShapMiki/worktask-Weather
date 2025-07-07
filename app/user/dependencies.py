from fastapi import Request, HTTPException, Depends, status

def get_user_id(request: Request):
    user_id = request.cookies.get("user_id")
    if not user_id:
        print("New user")
        return None
    return user_id


