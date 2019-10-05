# def printCat():
#     # this function just print a cat
#     txt = r'''
# |\---/|
# | o_o |
#  \_^_/'''
#     print(txt)
#     return
#
# print(printCat())

# def EndYear():
#     from datetime import date
#     date_today = date.today()
#     current_year = date_today.year
#     date_end_year = date(current_year, 12, 31)
#     delta = date_end_year - date_today
#     print(delta.days)
#     return

# def printAnimal(animal):
#     txt_cat = r'''
# |\---/|
# | o_o |
#  \_^_/'''
#     txt_bear = r'''
# /  \.-"""-./  \
# \    -   -    /
#  |   o   o   |
#  \  .-'"'-.  /
#   '-\__Y__/-'
#      `---`'''
#     txt_bat = r'''
#    /\                 /\
#   / \'._   (\_/)   _.'/ \
#  /_.''._'--('.')--'_.''._\
#  | \_ / `;=/ " \=;` \ _/ |
#   \/ `\__|`\___/`|__/`  \/
#           \(/|\)/
#      '''
#
#     if animal == "cat":
#         print(txt_cat)
#     elif animal == "bear":
#         print(txt_bear)
#     elif animal == "bear":
#         print(txt_bat)
#     else:
#         print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" %animal)
#     return
#
# printAnimal("cos")