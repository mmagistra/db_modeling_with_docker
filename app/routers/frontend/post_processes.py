from starlette.requests import Request

from routers.api.views import templates


async def post_process_handler(
        request: Request,
        context: dict,
        level: int = 4,
        template_name: str = 'model_update.html',
        placement: str = 'tables'
):
    is_light_theme = request.cookies.get('theme', 'dark') == 'light'

    context = {
        **context,
        'level': level,
        'is_light_theme': is_light_theme,
        f'is_{placement}_active': True
    }
    return templates.TemplateResponse(
        request=request,
        name=template_name,
        context=context
    )
