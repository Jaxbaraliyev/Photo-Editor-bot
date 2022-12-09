from aiogram import Bot, Dispatcher, executor, types
import logging
from config import TOKEN
from api import api_requests


logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    ism = message.from_user.full_name
    await message.answer(f"Assalomu alaykum <i>{ism}</i> <b>Image Editor</b> botimizga xush kelibsiz\n"
                         f"Iltimos o`zgartirmoqchi bo`lgan rasmingizni kiriitng", parse_mode="HTML"
                         )


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_image(message:types.Message):
    message_id = (await message.answer("Yuklanmoqda...🚀"))
    photo_id = message.photo[-1].file_id
    photo_info = await bot.get_file(photo_id)
    file_path = photo_info["file_path"]
    photo_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

    data = await api_requests(photo_url)

    if data is not None:
        await bot.delete_message(chat_id=message_id.from_user.id, message_id=message_id)
        await message.answer_photo(photo=data)
    else:
        await message.answer("Iltimos yuz qiyofasi aniq aks etgan rasm yuboring!")


if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)