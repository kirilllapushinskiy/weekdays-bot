from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from loader import dp
from markups.text import menu, buttons
from states import Menus


@dp.message_handler(Text(equals=buttons.go_back_btn.text), state=Menus.calendar)
@dp.message_handler(Text(equals=buttons.settings_btn.text), state=[Menus.main_menu, None])
async def settings_submenu(message: Message):
    await Menus.settings_submenu.set()
    await message.answer(f"Вы пережли в настройки. Что хотите сделать?", reply_markup=menu.settings_submenu)
