from config.settings import settings
from tortoise import Tortoise, run_async


async def init() -> None:
    await Tortoise.init(
        db_url=settings.get_db_uri(),
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()


run_async(init())
