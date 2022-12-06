def get_hidden_card(card_num, stars=4):
    return "*" * stars + card_num[12:16]


print(get_hidden_card('4576528637598225'))
print(get_hidden_card('4335789642315369', 1))
print(get_hidden_card('4853127786521321', 2))
print(get_hidden_card('4785665375472125', 5))
print(get_hidden_card('5257566532156785', 7))
