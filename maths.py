# # percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
# #            2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
# #            3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
# #            4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
# #            8.740978348,6.174819567]
# #
# # # countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
# # #              'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
# # #              'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
# # #              'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
# # #              'Cyprus','Italy']
# # #
# # # sumOfPoints = 4988
# # #
# # # print(min(percent), max(percent))
# # #
# # # for i in range(len(countries)):
# # #     print(percent[i], int(percent[i]), round(percent[i],2), int(round(percent[i]*sumOfPoints/100)), countries[i])
# #
# # percent.sort()
# # import statistics
# # print(statistics.median(percent))
# # print(statistics.median_low(percent))
# # print(statistics.median_high(percent))
# # print(percent)
# #
# # from statistics import *
# # print(median(percent))
# # print(median_low(percent))
# # print(median_high(percent))
#
# # import random
# # for i in range(10):
# #     print("zimportowana liczba to:",random.randint(1,100))
# # import random
# # number1 = (random.randint(1,100))
# # print("pierwsza wylosowana liczba to: %d" %(number1))
# # counter = 1
# # number2 = random.randint(1,100)
# # while number1 != number2:
# #     counter+=1
# #     number2=random.randint(1,100)
# #     print(counter, number2)
# # countries = [
# #     'Uruguay',
# #     'Russia',
# #     'Saudi Arabia',
# #     'Egypt',
# #     'Spain',
# #     'Portugal',
# #     'Iran',
# #     'Morocco',
# #     'France',
# #     'Denmark',
# #     'Peru',
# #     'Australia',
# #     'Croatia',
# #     'Argentina',
# #     'Nigeria',
# #     'Iceland',
# #     'Brazil',
# #     'Switzerland',
# #     'Serbia',
# #     'Costa Rica',
# #     'Sweden',
# #     'Mexico',
# #     'Korea Republic',
# #     'Germany',
# #     'Belgium',
# #     'England',
# #     'Tunisia',
# #     'Panama',
# #     'Colombia',
# #     'Japan',
# #     'Senegal',
# #     'Poland'
# # ]
# # random.shuffle(countries)
# #
# # groupNumber = 0
# #
# # for i in range(len(countries)):
# #     if i % 4 == 0:
# #         groupNumber +=1
# #         print("======== group %d ==========" % (groupNumber))
# #     print(countries[i])
# # import random
# # min = 1
# # max = 6
# # dice = random.randint(min, max)
# #
# # if dice == 1:
# #     print('   ')
# #     print(' o ')
# #     print('   ')
# # elif dice == 2:
# #     print('  o')
# #     print('   ')
# #     print('o  ')
# # elif dice == 3:
# #     print('  o')
# #     print(' o ')
# #     print('o  ')
# # elif dice == 4:
# #     print('o o')
# #     print('   ')
# #     print('o o')
# # elif dice == 5:
# #     print('o o')
# #     print(' o ')
# #     print('o o')
# # else:
# #     print('o o')
# #     print('o o')
# #     print('o o')
# #
# # print("x"*10)
# #
# # dice = []
# # for i in range(5):
# #     dice.append(random.randint(min,max))
# #
# # dice.sort()
# # print(dice)
#
# # poem = '''1.Runą i w łunach spłoną pożarnych
# # Krzyże kościołów, krzyże ofiarne
# # I w bezpowrotnym zgubi się szlaku
# # W lechickiej ziemi Orzeł Polaków.
# # 2.O, jasne słońce- wodzu Stalinie!
# # Niech sława twoja nigdy nie zginie
# # Niechaj jak orły powiedzie z gniazda
# # Rosja i z Kremla płonąca gwiazda.
# # 3.Na ziemskim globie flagi czerwone
# # Będą na wiatrach grały jak dzwony
# # Czerwona Armia i wódz jej Stalin
# # Odwiecznych wrogów na zawsze obali!
# # 4.Zaćmisz się rychło w czarnej godzinie
# # Polsko- Twe córy i syny,
# # Wiara i każdy krzyż na mogile,
# # U stóp am legą w prochu i pyle! '''
# #
# # lines= poem.split('\n')
# # for i in range(8):
# #     print(lines[i])
# #     print(lines[1+8])
# # import time
# # print(time.time())
# # print(time.localtime(time.time()))
# # import calendar
# # print(calendar.month(1997,2))
# # calendar.setfirstweekday(6)
# # print(calendar.month(1997,2))
# # print('2000 is leap: ', calendar.isleap(2000))
# # print(calendar.calendar(2019))
# #
# # print("x"* 10)
# #
# # inputdata = [0,1,2,3,5,8,13,21,34,55,89]
# # # factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]
# # #
# # import math
# # # print(len(inputdata))
# # # print(len(factortable))
# # #
# # # if len(inputdata) == len(factortable):
# # #     i=0
# # #     while i<len(inputdata):
# # #         minvalue=inputdata[i]-factortable[i]*inputdata[i]
# # #         maxvalue=inputdata[i]+factortable[i]*inputdata[i]
# # #         print("minvalue - ",minvalue,"maxvalue - ",maxvalue)
# # #
# # #         miniteger = math.floor(minvalue)
# # #         maxiteger = math.ceil(minvalue)
# # #         print(miniteger,"\t",inputdata[i],"\t",maxiteger)
# # #         i+=1
# # #
# # # else:
# # #     print("inputdata and factortable need to have equal number of elements")
# # # print("x"*10)
# #
# # import random
# # # i=0
# # # while i<len(inputdata):
# # #     minvalue=inputdata[i]-random.random()*inputdata[i]
# # #     maxvalue=inputdata[i]+random.random()*inputdata[i]
# # #     print("minvalue - ",minvalue,"maxvalue - ",maxvalue)
# # #
# # #     miniteger = math.floor(minvalue)
# # #     maxiteger = math.ceil(minvalue)
# # #     print(miniteger,"\t",inputdata[i],"\t",maxiteger)
# # #     i+=1
# # from datetime import datetime
# # print(datetime.today())
# # print(datetime.today().strftime("%Y-%m-%d"))
#
# colors = ['Hearts','Diamonds','Clubs','Spades']
#
# figures = ['Ace','King','Queen','Jack','10','9']
#
# allCards = []
# for c in colors:
#     for f in figures:
#         allCards.append("%s - %s" % (c, f))
# print(allCards)
#
# import random
#
# random.shuffle(allCards)
#
# player1 = []
# player2 = []
#
# max = len(allCards)
# for i in range(max):
#     if i % 2 == 0:
#         player1.append(allCards[i])
#     else:
#         player2.append(allCards[i])
#
# print('-------PLAYER 1--------')
# print(player1)
#
# print('-------PLAYER 1--------')
# print(player2)