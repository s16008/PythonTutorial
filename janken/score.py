# 'score.txt'のデータを読み取り、現状の戦績を表示するだけ。
f = open('score.txt', 'r')
for line in f:
    print(line)
f.close
