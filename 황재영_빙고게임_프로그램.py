import random
import copy

# 난수 리스트 생성
temp = [0]*25
count = 1  #들어갈 숫자(1~25)
while count < 26:
    x = random.randint(0,24)
    if temp[x] == 0:
        temp[x] = count
        count += 1
#플레이어1에 숫자 입력
grid = [[0]*5 for _ in range(5)]
for i in range(0, 5):
    for j in range(0, 5):
        grid[i][j] = temp[i* 5 + j]
temp = copy.deepcopy(grid)                       #deepcopy는 이미 copy된 list는 더 이상 원본 list에 영향을 미치지 않는다



# 플레이어1,2 게임 시작
playCount1 = 0
playCount2 = 0   # 게임 플레이 횟수
bingo = True
print()
print('**Player1 bingo game start**')
print()
while bingo:
    num1 = random.randint(1,25)
    for i in range(0,5):
        for j in range(0,5):
           # 플레이어1 보드에서 사용자가 입력한 값이 있는 곳을 X 표시로 바꾸기
           if grid[i][j] == num1:
                grid[i][j] = 'X'
                playCount1 += 1

    num2 = random.randint(1, 25)
    for i in range(0,5):
        for j in range(0,5):
           # 플레이어2 보드에서 사용자가 입력한 값이 있는 곳을 X 표시로 바꾸기
           if grid[i][j] == num2:
                grid[i][j] = 'X'
                playCount2 += 1

    for i in range(0,5):
        # X로 가로줄이 만들어지면 bingo를 False로 바꿔 루프 종료
        if grid[i][0]=='X' and grid[i][1]=='X' and grid[i][2]=='X'\
                and grid[i][3]=='X'and grid[i][4]=='X':
            bingo = False
        # X로 세로줄이 만들어지면 bingo를 False로 바꿔 루프 종료
        if grid[0][i]=='X' and grid[1][i]=='X' and grid[2][i]=='X'\
                and grid[3][i]=='X'and grid[4][i]=='X':
            bingo = False
        # X로 우대각선이 만들어지면 bingo를 False로 바꿔 루프 종료
        if grid[0][0]=='X' and grid[1][1]=='X' and grid[2][2]=='X'\
                and grid[3][3]=='X' and grid[4][4]=='X':
            bingo = False
        # X로 좌대각선이 만들어지면 bingo를 False로 바꿔 루프 종료
        if grid[0][4]=='X' and grid[1][3]=='X' and grid[2][2]=='X'\
                and grid[3][1]=='X'and grid[4][0]=='X':
            bingo = False



print('--Player1 플레이 전--')
for i in temp:
    for j in i:
        print(j, end='\t')
    print()
print()

print(f'--Player1 bingo --')
print(f'Player1은 {playCount1}번 플레이했습니다.')
print()


print('--Player1 플레이 후--')
for i in grid:
    for j in i:
        print(j, end='\t')
    print()

print("==========================================")

print('--Player2 플레이 전--')
for i in temp:
    for j in i:
        print(j, end='\t')
    print()
print()

print(f'--Player2 bingo --')
print(f'Player2은 {playCount2}번 플레이했습니다.')
print()


print('--Player2 플레이 후--')
for i in grid:
    for j in i:
        print(j, end='\t')
    print()

def playerWin(): #빙고게임 승자 결정
    if playCount1 > playCount2:
        print("Player2 WIN 축하합니다.")
    elif playCount1 == playCount2:
        print("비겼습니다.")
    else:
        print("Player1 WIN 축하합니다.")
print()
playerWin()