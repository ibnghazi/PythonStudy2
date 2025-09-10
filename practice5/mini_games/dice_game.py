#practice5/mini_games/dice_game.py
import random
'''
3. 주사위 게임
   - dice_game.py 모듈
   - 함수명: play_dice_game()
   - 기능:
       * 사용자와 컴퓨터 각각 1~6 사이 랜덤 수 생성
       * 주사위 값 비교 후 결과 출력 (이김, 짐, 비김)
'''

def play_dice_game():
    player = random.randint(1,6)
    computer = random.randint(1,6)

    print(f"당신의 주사위 : {player}")
    print(f"컴퓨터의의 주사위 : {computer}")

    if player > computer :
        print("이김")
    elif computer > player :
        print("짐")
    else:
        print("비김")