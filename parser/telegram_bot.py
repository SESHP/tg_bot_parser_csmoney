import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from parser import collect_data
from aiogram.utils.markdown import hbold, hlink
import asyncio
bot = Bot(token='5216367344:AAESEBbJMnNLYeTjUak94ZNwFvDRgTeUSv8', parse_mode=types.ParseMode.HTML)
dp= Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
	start_buttons = ['Knife', 'Gloves', 'Sniper Rifles']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*start_buttons)


	await message.answer('Select a category', reply_markup=keyboard)


@dp.message_handler(Text(equals='Knife'))
async def get_discount_knives(message: types.Message):
	await message.answer('Please waiting...')

	collect_data(cat_type=2)

	with open('result.json', encoding="utf-8") as file:
		data = json.load(file)

	for index, item in enumerate(data):
		card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
			f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
			f'{hbold("Цена: ")}{item.get("item_price")}'

		if index%20 == 0:
			await asyncio.sleep(3)
		await message.answer(card)


@dp.message_handler(Text(equals='Gloves'))
async def get_discount_gloves(message: types.Message):
	await message.answer('Please waiting...')

	collect_data(cat_type=13)

	with open('result.json', encoding="utf-8") as file:
		data = json.load(file)

	for index, item in enumerate(data):
		card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
			f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
			f'{hbold("Цена: ")}{item.get("item_price")}'

		if index%20 == 0:
			await asyncio.sleep(3)
		await message.answer(card)



@dp.message_handler(Text(equals='Sniper Rifles'))
async def get_discount_sniper(message: types.Message):
	await message.answer('Please waiting...')

	collect_data(cat_type=4)

	with open('result.json', encoding="utf-8") as file:
		data = json.load(file)

	for index, item in enumerate(data):
		card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
			f'{hbold("Скидка: ")}{item.get("overprice")}%\n' \
			f'{hbold("Цена: ")}{item.get("item_price")}'

		if index%20 == 0:
			await asyncio.sleep(3)
		await message.answer(card)




def main():
	executor.start_polling(dp)



if __name__ == '__main__':
	main()