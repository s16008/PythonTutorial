import json

HANDS = (' ', 'グー', 'チョキ', 'パー')


def select_hand():
    import random

    b = random.randint(1, 3)

    return b


def judgement(player, computer):
    if player == computer:
        return 0
    elif player == 1 and computer == 2:
        return 1
    elif player == 2 and computer == 3:
        return 1
    elif player == 3 and computer == 1:
        return 1
    else:
        return -1


def save_score(result):
    rec = {"win": 0, "lose": 0, "draw": 0}

    with open("score.txt", "r") as f:
        rec = json.load(f)

    with open('score.txt', 'w') as f:

        if result == 1:
            rec["win"] += 1
        if result == -1:
            rec["lose"] += 1
        if result == 0:
            rec["draw"] += 1
        strlist = json.dumps(rec)
        f.write(strlist)

    return None


if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)
    if result == 0:
        print('あなたの手は', HANDS[player], end=',')
        print('コンピュータは', HANDS[computer])
        print("あいこです")
    elif result == 1:
        print('あなたの手は', HANDS[player], end=',')
        print('コンピュータは', HANDS[computer])
        print("あなたの勝ちです")
    elif result == -1:
        print('あなたの手は', HANDS[player], end=',')
        print('コンピュータは', HANDS[computer])
        print("あなたの負けです。")
    save_score(result)
