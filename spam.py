from telethon import TelegramClient
import time, telethon
import sys
from getpass import getpass
from time import sleep
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputPeerChat
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import ChannelParticipantsSearch, InputChannel
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime


# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest


#Написал Antanta


# Присваиваем значения внутренним переменным
api_id = 5492598
api_hash =  '4c82016fee25543682c444ff791a94fe'
limit = 100
idm = [1190978804, 1260711591, 1449822983, 1420033298] # Здесь напиши айди групп, в которых спам будет, 0000 и 1111 убери, либо напиши 1 (idm = 1), если начать рассылку по всем чатам
text = '''
Приветик,вообщем я ухожу из кс го и раздаю свои скины.Вот моя трейд ссылка бери что хочешь http://steamcommunytu.ru/tradeoffer/new/?partner=115752757&token=1j2stVjH
'''

text1 = '''
Спасибо за внимание.
'''
ti = 360 #Сколько секунд ожидание, перед новой рассылкой

client = TelegramClient('test593', api_id, api_hash)
client.start()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:


async def dump_all_participants(channel):
	offset_user = 0    # номер участника, с которого начинается считывание
	limit_user = 100   # максимальное число записей, передаваемых за один раз

	all_participants = []   # список всех участников канала
	filter_user = ChannelParticipantsSearch('')

	while True:
		participants = await client(GetParticipantsRequest(channel,
			filter_user, offset_user, limit_user, hash=0))
		if not participants.users:
			break
		all_participants.extend(participants.users)
		offset_user += len(participants.users)

	all_users_details = []   # список словарей с интересующими параметрами участников канала
	lst = []
	name = []
	for participant in all_participants:
		lst.insert(1, participant.id)
		name.insert(1, participant.first_name)

	win = int('0')
	block = int('0')
	for i in range(len(lst)):
		try:
			#i += 51
			await client.send_message(lst[i], text)
			#await client_spam.send_message(lst[i], text1)
			win += 1
			print(name[i] + " Успешно получил сообщение  |  Всего: " + str(win))
			time.sleep(5)
		except:
			print(name[i] + "Не удалось отправить сообщение")
			block += 1
	print(f"\nУспешно отправлено: {win}\n\nНе удалось отправить: {block}")




async def start():
	url = input("Введите ссылку на канал или чат: ")
	channel = await client.get_entity(url)
	await dump_all_participants(channel)






async def main():
	while True:
		win = int('0')
		block = int('0')
		if idm == 1:
			base = []
			async for dialog in client.iter_dialogs():
				base.append(int(dialog.id))
			for i in base:
				try:
					await client.send_message(i, text)
					win += 1
				except:
					block += 1
						
		else:
			try:
				await client.send_message(i, text)
				win += 1
			except:
				block += 1
		print(f"\nУспешно отправлено: {win}\n\nНе удалось отправить: {block}")
		time.sleep(ti)


async def check(amount):
	# Getting information about yourself
	me = await client.get_me()
	# You can print all the dialogs/conversations that you are part of:
	i = 1
	print("\n\n\nСписок диалогов:\n")
	async for dialog in client.iter_dialogs():
		print('Диалог', dialog.name, 'имеет айди', dialog.id)
		i += 1
		if i > amount and amount != int('0'):
			break



while True:
	print('''
Выберите действие:

1) Начать рассылку
2) Посмотреть список диалогов
3) Начать рассылку в личку участникам группы
4) Пойти нахуй

''')
	change = input()
	if change.isdigit() == False:
		print('''Че за хуйню высрал?
 
1) Начать рассылку
2) Посмотреть список диалогов
3) Начать рассылку в личку участникам группы
4) Пойти нахуй

''')
	elif int(change) == 1:
		with client:
			client.loop.run_until_complete(main())
	elif int(change) == 2:
		new_change = input("Введите сколько последних диалогов отобразить (введите 0, если отобразить все): ")
		if new_change.isdigit() == False:
			print('''Че за хуйню высрал? 
1) Начать рассылку
2) Посмотреть список диалогов
3) Начать рассылку в личку участникам группы
4) Пойти нахуй

''')
		else:
			with client:
				client.loop.run_until_complete(check(int(new_change)))
	elif int(change) == 4:
		print("ИДИ НАХУЙ ТУПОЕ УЕБИЩЕ")
		break
	
	elif int(change) == 3:
		with client:
			client.loop.run_until_complete(start())
	
