from covid.api import CovId19Data
import telebot

#Это что типа init
api = CovId19Data(force=True)
#TOKEN бота
bot = telebot.TeleBot('5316073591:AAGEMvSnOIBQLUD6T3Di98x-2NcreO7mdWw')
#команда старт и другие ну короче как всегда
@bot.message_handler(commands=['start'])
def welcome(message):

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name},предоставляю всю информацию о заболевших 🤒\n Введите,пожалуйста страну🤗\n /commands".format(message.from_user, bot.get_me()),
		parse_mode='html')

@bot.message_handler(commands=['commands'])
def command(message):
	bot.send_message(message.chat.id, "\n/list: Список доступных стран\n""/author: Автор проекта \n")

@bot.message_handler(commands=['list'])
def ldl(message):
	bot.send_message(message.chat.id, "Все страны🌍 \n Главное напишите,пожалуйста, название страны правильно😊\n 1)Казахстан\n 2)Россия\n 3)США\n 4)Корея и тд\n\n Если хотите увидеть статистику по всему миру - напишите слово 'Мир' ")


@bot.message_handler(commands=['author'])
def author(message):
	bot.send_message(message.chat.id,"Мама великолепного бота :\n Нурдаулет Жанель (16.00-18.00)😅")


@bot.message_handler(content_types=['text'])
def mess(message):

	good_bye_message = ""
	a = message.text
	test = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Diamond Princess', 'Cuba', 'Cyprus', 'Czechia', 'Denmark', 'Djibouti', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Guatemala', 'Guinea', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea', 'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon', 'Liberia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malaysia', 'Maldives', 'Malta', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Taiwan*', 'Tanzania', 'Thailand', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'US', 'Uzbekistan', 'Venezuela', 'Vietnam', 'Zambia', 'Zimbabwe', 'Dominica', 'Grenada', 'Mozambique', 'Syria', 'Timor-Leste', 'Belize', 'Laos', 'Libya', 'West Bank and Gaza', 'Guinea-Bissau', 'Mali', 'Saint Kitts and Nevis', 'Kosovo', 'Burma', 'MS Zaandam', 'Botswana', 'Burundi', 'Sierra Leone', 'Malawi', 'South Sudan', 'Western Sahara', 'Sao Tome and Principe', 'Yemen', 'Comoros', 'Tajikistan']

	if a == "США" or a == 'Америка' or a == 'сша':
		res = api.filter_by_country("US")
	elif a == "Украина":
		res = api.filter_by_country("Ukraine")
	elif a == "Россия":
		res = api.filter_by_country("Russia")
	elif a == "Беларусь":
		res = api.filter_by_country("Belarus")
	elif a == "Казахстан":
		res = api.filter_by_country("Kazakhstan")
	elif a == "Италия":
		res = api.filter_by_country("Italy")
	elif a == "Франция":
		res = api.filter_by_country("French")
	elif a == "Германия":
		res = api.filter_by_country("Germany")
	elif a == "Япония":
		res = api.filter_by_country("Japan")
	elif a == "Узбекистан":
		res = api.filter_by_country('Uzbekistan')
	elif a == "Китай":
		res = api.filter_by_country('China')

	elif a == 'Афганистан':
		res = api.filter_by_country(test[0])

	elif a == "Албания":
		res = api.filter_by_country(test[1])

	elif a == "Алжир":
		res = api.filter_by_country(test[2])

	elif a == "Андорра":
		res = api.filter_by_country(test[3])

	elif a == "Ангола":
		res = api.filter_by_country(test[4])

	elif a == "Антигуа и Барбуда":
		res = api.filter_by_country(test[5])
	elif a == "Аргентина":
		res = api.filter_by_country(test[6])
	elif a == "Армения":
		res = api.filter_by_country(test[7])
	elif a == "Австралия":
		res = api.filter_by_country(test[8])
	elif a == "Австрия":
		res = api.filter_by_country(test[9])
	elif a == "Азербайджан":
		res = api.filter_by_country(test[10])

	elif a == "Багамские о-ва" or a == "Багамские острова" or a == "Багамские Острова":
		res = api.filter_by_country(test[11])

	elif a == "Бахрейн":
		res = api.filter_by_country(test[12])

	elif a == "Бангладеш":
		res = api.filter_by_country(test[13])
	elif a == "Барбадос":
		res = api.filter_by_country(test[14])
	elif a == "Беларусь":
		res = api.filter_by_country(test[15])
	elif a == "Бельгия":
		res = api.filter_by_country(test[16])
	elif a == "Бенин":
		res = api.filter_by_country(test[17])
	elif a == "Бутан":
		res = api.filter_by_country(test[18])
	elif a == "Боливия":
		res = api.filter_by_country(test[18])
	elif a == "Босния и Герцеговина":
		res = api.filter_by_country(test[19])
	elif a == "Бразилия":
		res = api.filter_by_country(test[20])
	elif a == "Бруней":
		res = api.filter_by_country(test[21])
	elif a == "Болгария":
		res = api.filter_by_country(test[22])
	elif a == 'Буркина-Фасо':
		res = api.filter_by_country(test[23])
	elif a == 'Кабо-Верде':
		res = api.filter_by_country(test[24])
	elif a == "Камбоджа":
		res = api.filter_by_country(test[25])
	elif a == "Камерун":
		res = api.filter_by_country(test[26])
	elif a == "Канада":
		res = api.filter_by_country(test[27])
	elif a == "Центральноафриканская Республика":
		res = api.filter_by_country(test[28])
	elif a == "Чад ":
		res = api.filter_by_country(test[29])
	elif a == "Чили ":
		res = api.filter_by_country(test[30])
	elif a == "Китай":
		res = api.filter_by_country(test[31])
	elif a == "Колумбия":
		res = api.filter_by_country(test[32])
	elif a == "Конго":
		res = api.filter_by_country(test[33])
	elif a == "Коста-Рика":
		res = api.filter_by_country(test[34])
	elif a == "Кот-д Ивуар":
		res = api.filter_by_country(test[35])
	elif a == "Хорватия":
		res = api.filter_by_country(test[36])
	elif a == "Алмазная принцесса":
		res = api.filter_by_country(test[37])
	elif a == "Куба":
		res = api.filter_by_country(test[38])
	elif a == "Кипр":
		res = api.filter_by_country(test[39])
	elif a == "Чехия":
		res = api.filter_by_country(test[40])
	elif a == "Дания":
		res = api.filter_by_country(test[41])
	elif a == "Корея":
		res = api.filter_by_country(test[42])
	elif a == "":
		res = api.filter_by_country(test[43])
	elif a == "":
		res = api.filter_by_country(test[44])
	elif a == "":
		res = api.filter_by_country(test[45])
	elif a == "":
		res = api.filter_by_country(test[46])
	elif a == "":
		res = api.filter_by_country(test[47])
	elif a == "":
		res = api.filter_by_country(test[48])
	elif a == "":
		res = api.filter_by_country(test[48])
	elif a == "":
		res = api.filter_by_country(test[49])
	elif a == "":
		res = api.filter_by_country(test[50])
	elif a == "":
		res = api.filter_by_country(test[51])
	elif a == "":
		res = api.filter_by_country(test[52])
	elif a == "":
		res = api.filter_by_country(test[53])
	elif a == "":
		res = api.filter_by_country(test[54])
	elif a == "":
		res = api.filter_by_country(test[55])
	elif a == "":
		res = api.filter_by_country(test[56])
	elif a == "":
		res = api.filter_by_country(test[57])
	elif a == "":
		res = api.filter_by_country(test[58])
	elif a == "":
		res = api.filter_by_country(test[59])
	elif a == "":
		res = api.filter_by_country(test[60])
	elif a == "":
		res = api.filter_by_country(test[61])
	elif a == "":
		res = api.filter_by_country(test[62])
	elif a == "":
		res = api.filter_by_country(test[63])
	elif a == "":
		res = api.filter_by_country(test[64])
	elif a == "":
		res = api.filter_by_country(test[65])
	elif a == "":
		res = api.filter_by_country(test[66])
	elif a == "":
		res = api.filter_by_country(test[67])
	elif a == "":
		res = api.filter_by_country(test[68])
	elif a == "":
		res = api.filter_by_country(test[69])
	elif a == "":
		res = api.filter_by_country(test[70])
	elif a == "":
		res = api.filter_by_country(test[71])
	elif a == "":
		res = api.filter_by_country(test[72])
	elif a == "":
		res = api.filter_by_country(test[73])
	elif a == "":
		res = api.filter_by_country(test[74])
	elif a == "":
		res = api.filter_by_country(test[75])
	elif a == "":
		res = api.filter_by_country(test[76])
	elif a == "":
		res = api.filter_by_country(test[77])
	elif a == "":
		res = api.filter_by_country(test[78])
	elif a == "":
		res = api.filter_by_country(test[79])
	elif a == "":
		res = api.filter_by_country(test[80])
	elif a == "":
		res = api.filter_by_country(test[81])
	elif a == "":
		res = api.filter_by_country(test[82])
	elif a == "":
		res = api.filter_by_country(test[83])
	elif a == "":
		res = api.filter_by_country(test[84])
	elif a == "":
		res = api.filter_by_country(test[85])
	elif a == "":
		res = api.filter_by_country(test[86])
	elif a == "":
		res = api.filter_by_country(test[87])
	elif a == "":
		res = api.filter_by_country(test[88])
	elif a == "":
		res = api.filter_by_country(test[89])
	elif a == "":
		res = api.filter_by_country(test[90])
	elif a == "":
		res = api.filter_by_country(test[91])
	elif a == "":
		res = api.filter_by_country(test[92])
	elif a == "":
		res = api.filter_by_country(test[93])
	elif a == "":
		res = api.filter_by_country(test[94])
	elif a == "":
		res = api.filter_by_country(test[95])
	elif a == "":
		res = api.filter_by_country(test[96])
	elif a == "":
		res = api.filter_by_country(test[97])
	elif a == "":
		res = api.filter_by_country(test[98])
	elif a == "":
		res = api.filter_by_country(test[99])
	elif a == "":
		res = api.filter_by_country(test[100])
	elif a == "":
		res = api.filter_by_country(test[101])
	elif a == "":
		res = api.filter_by_country(test[102])
	elif a == "":
		res = api.filter_by_country(test[103])
	elif a == "":
		res = api.filter_by_country(test[104])
	elif a == "":
		res = api.filter_by_country(test[105])
	elif a == "":
		res = api.filter_by_country(test[106])
	elif a == "":
		res = api.filter_by_country(test[107])
	elif a == "":
		res = api.filter_by_country(test[108])
	elif a == "":
		res = api.filter_by_country(test[109])
	elif a == "":
		res = api.filter_by_country(test[111])
	elif a == "":
		res = api.filter_by_country(test[112])
	elif a == "":
		res = api.filter_by_country(test[113])
	elif a == "":
		res = api.filter_by_country(test[114])
	elif a == "":
		res = api.filter_by_country(test[115])
	elif a == "":
		res = api.filter_by_country(test[116])
	elif a == "":
		res = api.filter_by_country(test[117])
	elif a == "":
		res = api.filter_by_country(test[118])
	elif a == "":
		res = api.filter_by_country(test[119])
	elif a == "":
		res = api.filter_by_country(test[120])
	elif a == "":
		res = api.filter_by_country(test[121])
	elif a == "":
		res = api.filter_by_country(test[122])
	elif a == "":
		res = api.filter_by_country(test[123])
	elif a == "":
		res = api.filter_by_country(test[124])
	elif a == "":
		res = api.filter_by_country(test[125])
	elif a == "":
		res = api.filter_by_country(test[126])
	elif a == "":
		res = api.filter_by_country(test[127])
	elif a == "":
		res = api.filter_by_country(test[128])
	elif a == "":
		res = api.filter_by_country(test[129])
	elif a == "":
		res = api.filter_by_country(test[130])
	elif a == "":
		res = api.filter_by_country(test[131])
	elif a == "":
		res = api.filter_by_country(test[132])
	elif a == "":
		res = api.filter_by_country(test[133])
	elif a == "":
		res = api.filter_by_country(test[134])
	elif a == "":
		res = api.filter_by_country(test[135])
	elif a == "":
		res = api.filter_by_country(test[136])
	elif a == "":
		res = api.filter_by_country(test[137])
	elif a == "":
		res = api.filter_by_country(test[138])
	elif a == "":
		res = api.filter_by_country(test[139])
	elif a == "":
		res = api.filter_by_country(test[140])
	elif a == "":
		res = api.filter_by_country(test[141])
	elif a == "":
		res = api.filter_by_country(test[142])
	elif a == "":
		res = api.filter_by_country(test[143])
	elif a == "":
		res = api.filter_by_country(test[144])
	elif a == "":
		res = api.filter_by_country(test[145])
	elif a == "":
		res = api.filter_by_country(test[146])
	elif a == "":
		res = api.filter_by_country(test[147])
	elif a == "":
		res = api.filter_by_country(test[148])

	elif a == "":
		res = api.filter_by_country(test[149])
	elif a == "":
		res = api.filter_by_country(test[150])
	elif a == "":
		res = api.filter_by_country(test[151])
	elif a == "":
		res = api.filter_by_country(test[152])
	elif a == "":
		res = api.filter_by_country(test[153])
	elif a == "":
		res = api.filter_by_country(test[154])
	elif a == "":
		res = api.filter_by_country(test[155])
	elif a == "":
		res = api.filter_by_country(test[156])
	elif a == "":
		res = api.filter_by_country(test[157])
	elif a == "":
		res = api.filter_by_country(test[158])
	elif a == "":
		res = api.filter_by_country(test[159])
	elif a == "":
		res = api.filter_by_country(test[160])
	elif a == "":
		res = api.filter_by_country(test[161])
	elif a == "":
		res = api.filter_by_country(test[162])
	elif a == "":
		res = api.filter_by_country(test[163])
	elif a == "":
		res = api.filter_by_country(test[164])
	elif a == "":
		res = api.filter_by_country(test[165])
	elif a == "":
		res = api.filter_by_country(test[166])
	elif a == "":
		res = api.filter_by_country(test[167])
	elif a == "":
		res = api.filter_by_country(test[168])
	elif a == "":
		res = api.filter_by_country(test[169])
	elif a == "":
		res = api.filter_by_country(test[170])
	elif a == "":
		res = api.filter_by_country(test[171])
	elif a == "":
		res = api.filter_by_country(test[172])
	elif a == "":
		res = api.filter_by_country(test[173])
	elif a == "":
		res = api.filter_by_country(test[174])
	elif a == "":
		res = api.filter_by_country(test[175])
	elif a == "":
		res = api.filter_by_country(test[176])
	elif a == "":
		res = api.filter_by_country(test[177])
	elif a == "":
		res = api.filter_by_country(test[178])
	elif a == "":
		res = api.filter_by_country(test[179])
	elif a == "":
		res = api.filter_by_country(test[180])
	elif a == "":
		res = api.filter_by_country(test[181])
	elif a == "":
		res = api.filter_by_country(test[182])
	elif a == "":
		res = api.filter_by_country(test[183])
	elif a == "":
		res = api.filter_by_country(test[184])
	elif a == "":
		res = api.filter_by_country(test[185])
	elif a == "":
		res = api.filter_by_country(test[186])
	elif a == "":
		res = api.filter_by_country(test[187])
	else:
		res = api.get_stats()
		good_bye_message = f"Во всем мире:\n     Последнее обновление: {res['last_updated']}\n<b>     Выздоровевших:</b> {res['recovered']:,} \n     <b>Заболевших: </b>{res['confirmed']:,} \n     <b>Смертей: </b>{res['deaths']:,} людей "

	if good_bye_message == "":
		good_bye_message = f"Данные по стране:\n     Последние данные были обновлены: {res['last_updated']}\n   <b> Выздоровевших:</b> {res['recovered']:,}\n    <b> Заболевших: </b>{res['confirmed']:,}\n    <b> Смертей:</b> {res['deaths']:,}"

	bot.send_message(message.chat.id, good_bye_message, parse_mode='html')

bot.polling(none_stop=True)
