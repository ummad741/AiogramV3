import asyncio
import sys
import logging
from aiogram import Bot, Dispatcher
from handlers import bot_cmd, user_cmds
from callbacks import pagination
from config import config


async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(
        user_cmds.router,
        bot_cmd.router,
        pagination.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# projectni strukturasi va run qiladigan functionlari
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
