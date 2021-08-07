from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from markups.text import menu, buttons
from loader import dp


@dp.message_handler(Text(equals=buttons.first_view_btn.text), state=None)
async def representation_one(message: Message):
    await message.answer(f"ВИД1", reply_markup=menu.default_submenu)