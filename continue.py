# # # # # firstRow = 1
# # # # # # lastRow = 31
# # # # # # currentRow = firstRow
# # # # # # while currentRow <= lastRow:
# # # # # #     print("row number",currentRow)
# # # # # #     currentRow+=1
# # # # # # firstNumber = 1
# # # # # # lastNumber = 13
# # # # # # i = firstNumber
# # # # # # while i <= lastNumber:
# # # # # #     print(i, i**2, i**3)
# # # # # #     i+=1
# # print('x'*10)
# # # # # # minNumber = 0
# # # # # # maxNumber = 16
# # # # # # i = minNumber
# # # # # # while i <= maxNumber:
# # # # # #     print("2 do potęgi",i,"równa się",2**i)
# # # # # #     i+=1
# # # # # # minHafts = 0
# # # # # # maxHafts = 10
# # # # # # i = minHafts
# # # # # # while i <= maxHafts:
# # # # # #     print("x"*i)
# # # # # #     i+=1
# # print('x'*10)
# # # # # numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
# # # # # i =0
# # # # # number = len(numbers)-2
# # # # # while i < number:
# # # # #     print(i,"-",numbers[i], numbers[i+1], numbers[i+2])
# # # # #
# # # # #     if numbers[i]**2 == numbers[i+1] and numbers[i+1]**2 ==numbers[i+2]:
# # # # #         print("\tFOUND")
# # # # #     i+=1
#
# # print('x'*10)
#
# # # # texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
# # # # i=0
# # # # wordsInText = len(texts)-1
# # # # while i < wordsInText :
# # # #     print(texts[i], texts[i+1])
# # # #     if len(texts[i]) == len(texts[i+1]):
# # # #         print("\tfound", texts[i], texts[i+1])
# # # #     i+=1
# # # # number = 1
# # # # previousNumber = 0
# # # #
# # # # while number <= 50:
# # # #     print(number + previousNumber)
# # # #     previousNumber = number
# # # #     number += 1
# # print('x'*10)
# # # import random
# # # my_number = random.randint(0,20)
# # # trails = 0
# # #
# # # guess=-1
# # #
# # # print("zgadnij liczbę: ")
# # #
# # # while guess != my_number:
# # #     guess =(int(input()))
# # #     trails +=1
# # #     if guess == my_number:
# # #         print("gratulacje, żeby zgadnąc potrzebowałeś", trails,"prób")
# # #     elif guess < my_number:
# # #         print("zgaduj większa liczba")
# # #     else:
# # #         print("zgaduj mniejsza liczbe")
# # # number = 1
# # # previus_number = 0
# # #
# # # while number<50:
# # #     print(number + previus_number)
# # #     previus_number=number
# # #     number+=1
# # print('x'*10)
# # text = ''
# # number = 10
# # condition = True
# #
# # while condition:
# #
# #     text+='x'
# #     print(text)
# #
# #     if len(text)>number:
# #         condition=False
# # data = ['Error:File cannot be open',
# #         'Error:No free space on disk',
# #         'Error:File missing',
# #         'Warning:Internet connection lost',
# #         'Error:Access denied']
# #
# # for i in data:
# #     elements = i.split(":")
# #     if elements[0] == "Error":
# #         print(elements[1].upper())
# #     else:
# #         print(elements[1])
#
# # print('x'*10)
#
# # string_A = '+---+---+---+---+'
# # string_B = '|   |   |   |   |'
# #
# # for i in range(1,5):
# #     print(string_A)
# #     print(string_B)
# #
# # s=1
# # for i in range(1,5):
# #     print("o"*s)
# #     print("x"*s)
# #     s+=1
#
# # print('x'*10)
#
# # text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
# # newText = ' '
# # words = text.split()
# # counter = 0
# # for word in words:
# #     newText += word+' '
# #     counter +=1
# #     if counter > 20:
# #         print(newText)
# #         break
# # print('x'*20)
#
# # definitions = [
# #     'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
# #     'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
# #     'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
# #     'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
# # ]
# #
# # for definition in definitions:
# #     words = definition.split()
# #     newText = ' '
# #     counter = 0
# #     for word in words:
# #         newText += word+' '
# #         counter +=1
# #         if counter > 20:
# #             print(newText)
# #             break
# # # print('x'*20)
# menu = '''
# Choose what you want me to do for you:
# 1 - COFFEE
# 2 - TEA
# 3 - MAKE ME SMILE
# ---------------
# To stop this script select 0
# '''
#
# smile = '''
#
#                           oooo$$$$$$$$$$$$oooo
#                       oo$$$$$$$$$$$$$$$$$$$$$$$$o
#                    oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
#    o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
# oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
# "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
#   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
#   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
#    "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
#     $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
#    o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
#    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
#   o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
#   $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
#  """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
#             "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
#               $$$o          "$$""$$$$$$""""           o$$$
#                $$$$o                                o$$$"
#                 "$$$$o      o$$$$$$o"$$$$o        o$$$$
#                   "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
#                      ""$$$$$oooo  "$$$o$$$$$$$$$"""
#                         ""$$$$$$$oo $$$$$$$$$$
#                                 """"$$$$$$$$$$$
#                                     $$$$$$$$$$$$
#                                      $$$$$$$$$$"
#                                       "$$$""""
# '''
# while True:
#     print(menu)
#     letter = input('Enter your choice: ')
#
#     if "1" in letter:
#         print("Function COFFEE not implemented")
#         input("please, press enter")
#         continue
#     if "2" in letter:
#         print("Function TEA not implemented, please, press enter")
#         input("please, press enter")
#         continue
#     if "3" in letter:
#         print(smile)
#         input("please, press enter")
#
#     if "0" in letter:
#         break
#     else:
#         print("You need to make a valid choice.")
#         continue
#
# print('x'*10)
# initialCapital = 20000
# percent = 0.03
# maxTimeYears = 10
# years = 0
# capital = initialCapital
# while years < maxTimeYears:
#     years += 1
#     capital=round((1+percent)*capital,2)
#     print("year ", years,"\t", capital)
# else:
#     print("the total revenue is", capital - initialCapital)
#
# print("x"*10)
# number= 20730906
# newNumber = number
# sumofDigits = 0
# while newNumber>0:
#     digit = newNumber % 10
#     sumofDigits += digit
#     newNumber = newNumber //10
# else:
#     print("the sum of digit of ", number, 'is', sumofDigits)
# print("x" * 10)
# text = '''United Space Alliance: This company provides major support to NASA for
#  various projects, such as the space shuttle. One of its projects is to
# create Workflow Automation System (WAS), an application designed to
# manage NASA and other third-party projects. The setup uses a central
# Oracle database as a repository for information. Python was chosen over
# languages such as Java and C++ because it provides dynamic typing and
# pseudo-code–like syntax and it has an interpreter. The result is that
# the application is developed faster, and unit testing each piece is easier'''
#
# wordLength = 6
# listOfWord = text.split(' ')
# longWords = 0
# shortWords = 0
# i = 0
# while i < len(listOfWord):
#     if len(listOfWord[i])>wordLength:
#         longWords += 1
#     else:
#         shortWords +=1
#
#     i+=1
# print("Words shourter than ",wordLength,":",shortWords)
# print("Words longer than ",wordLength,":", longWords)
# print("x"*20)
# fibonacciIterations = 20
# a1 = 0
# a2 = 1
# a3 = 0
# for i in range (1,21):
#     print('step',i,'value',a3)
#     a1=a2
#     a2=a3
#     a3=a1+a2
# print('x'*10)
dictionary = """Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t."""
# #
# # listOfWords = text.split(" ")
# # for word in listOfWords:
# #     if word.lower().find('p')>=0:
# #         print(word)
#
# # print('x'*10)
#
# # dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
# # for word in dictionary.keys():
# #     print(word, '-', dictionary[word])
# # print('x'*10)
wordDictionary = {}
listOfWords = dictionary.split()
for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word]+1
    else:
        wordDictionary.setdefault(word,1)
print(wordDictionary)
#print('x'*10)















































