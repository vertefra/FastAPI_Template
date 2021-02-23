from tortoise import Tortoise


async def init():

    await Tortoise.init()
