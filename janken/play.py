HANDS = (' ', 'グー', 'チョキ', 'パー')


def select_hand():
    '''
    コンピュータの手をランダムに決める
    :return:  HANDSの中でいずれか。
    '''
    import random

    b = random.randint(1, 3)

    return b


def judgement(player, computer):
    '''

    じゃんけんの勝敗を判定する。
    :param player: HANDSの中のどれか
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1,あいこは0、負けは-1を返す。
    '''
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
    '''
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:
    :return: None
    '''
    dic = {"win": 0, "lose": 0, "draw": 0}
    with open('score.txt', 'w') as f:
        if result == 1:
            dic["win"] = dic["win"] + 1
        elif result == -1:
            dic["lose"] = dic["lose"] + 1
        elif result == 0:
            dic["draw"] = dic["draw"] + 1
        f.write(str(dic))

if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字): '))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示
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
