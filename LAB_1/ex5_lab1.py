import itertools


def cross(a, b):
    return {item_a + item_b for item_a in a for item_b in b}


THREE_OF_A_KIND_CONST = 3
three_of_a_kind = []
type_card = 'SCDH'
value_card = '123456789TJQK'  # T mean 10
value_key = 1  # 0 is type, 1 is index

deck = cross(type_card, value_card)
poker_5 = list(itertools.combinations(deck, 5))
len_poker_5 = len(poker_5)

for poker_5_item in poker_5:
    value = sorted(card[value_key] for card in poker_5_item)
    if THREE_OF_A_KIND_CONST in [value.count(value[0]), value.count(value[1]), value.count(value[2])]:
        three_of_a_kind.append(poker_5_item)

len_three_of_a_kind = len(three_of_a_kind)

print('len_poker_5:', len_poker_5)  # len_poker_5: 2598960
print('len_three_of_a_kind:', len_three_of_a_kind)  # len_three_of_a_kind: 58656

