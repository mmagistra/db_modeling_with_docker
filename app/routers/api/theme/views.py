from fastapi import Request, APIRouter, Response
from starlette import status

router = APIRouter(prefix='/theme',
                   tags=['theme']
                   )


@router.post(path='/change_theme/', status_code=status.HTTP_200_OK)
async def change_theme(response: Response, request: Request):
    theme = 'light' if request.cookies.get('theme', 'dark') == 'dark' else 'dark'
    response.set_cookie(key="theme", value=theme)
    return status.HTTP_200_OK
