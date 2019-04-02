_n = input()
card_list = list(map(int, input().split()))
card_list.sort(reverse=True)

Alice_card_list = card_list[0::2]
Bob_card_list =  card_list[1::2]

print(sum(Alice_card_list)-sum(Bob_card_list))
