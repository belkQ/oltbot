import pyowm
owm = pyowm.OWM('e6910af1fedcad1885a807ec3a1b3a6f', language = "ru")

import telebot
bot = telebot.TeleBot("835963570:AAHpP0Nb5JCEcIeVk2HnY3wEUH3PgqhfKNY")





@bot.message_handler(content_types =['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
	answer += "В городе " + message.text + " сейчас " + str(temp) + "\n\n"
	
	if temp < 10:
		answer += "Сейчас прохладненько, время для теплого пальтишона!" 
	elif temp <20:
		answer += "Погодка норм, время для легкого пальтишона или курточки!" 
	else:
		answer += "Отличная погодка! Можно примерять юбочку!" 

	#bot.reply_to(message, message.text)
	bot.send_message (message.chat.id, answer)
bot.polling( none_stop = True )
