import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

card_list = deque([i for i in range(1,T+1)])

def cardGame(card_list):
    while len(card_list) != 1:
        card_list.popleft()
        move_card = card_list.popleft()
        card_list.append(move_card)

    return print(card_list[0])


cardGame(card_list)

