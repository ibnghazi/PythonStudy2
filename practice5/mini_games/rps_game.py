#practice5/mini_games/rps_game.py
import random

'''
2. 가위바위보 게임
   - rps_game.py 모듈
   - 함수명: play_rps_game()
   - 기능:
       * 사용자 입력: "가위", "바위", "보"
       * 컴퓨터 랜덤 선택
       * 결과 출력 (이김, 짐, 비김)
'''

def play_rps_game():
    player = (input("가위, 바위, 보\n"))
    print()
    rpc = ["가위", "바위", "보"]
    compu = random.choice(rpc)

    print(f"컴퓨터의 값: {compu}")
    
    if(player == compu):
        print("비김")
    
    elif(player == "가위" and compu == "보") or (player == "바위" and compu == "가위") or (player == "보" and compu == "바위"):
        print("이김")
    else:
        print("짐")