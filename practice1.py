# practice1.py

'''
    입력 함수 => input(출력할내용):입력된값
        ex name = input("이름 입력 : ")
'''


# 1. 이름, 성별, 나이, 키 입력받아 출력
#  * 출력 형식 : 이름: xxx, 성별: xx, 나이: xx, 키: xx.xxcm
name = input("이름 입력 : ")
gender = input("성별 입력 : ")
age = input("나이 입력 : ")
height = input("키 입력 : ")
s1 = f" 이름: {name}, 성별: {gender}, 나이: {age}, 키: {height}cm"
print(s1)   

# 2. 두 정수 입력받아 합, 차, 곱, 몫, 나머지 계산 후 출력
n1 = int(input("첫 정수 : "))
n2 = int(input("두번째 정수 : "))
sum = n1 + n2
minus = n1 - n2
double = n1 * n2
seperate = n1 / n2
rest = n1 % n2

s2 = f"합:{sum}, 차:{minus}, 곱:{double}, 몫:{seperate}, 나머지:{rest}"
print(s2)

# 3. 영어 문자열 입력받아 앞 세 글자 출력
eng = input("영어 문자 입력 : ")
print(eng[0:3])

# 4. 실수 2개 입력받아 합, 차, 곱, 나누기 출력
d1 = float(input("첫 실수 : "))
d2 = float(input("두번째 실수 : "))
sum = d1 + d2
minus = d1 - d2
double = d1 * d2
seperate = d1 / d2
rest = d1 % d2
s2 = f"합:{sum}, 차:{minus}, 곱:{double}, 몫:{seperate}, 나머지:{rest}"
print(s2)

# 5. 두 수 입력받아 제곱과 제곱근 계산
d1 = float(input("첫 실수 : "))
d2 = float(input("두번째 실수 : "))
double = d1**d2
d3 = d1**(1/2)
d4 = d2**(1/2)
s2 = f"제곱 : {double}, {d1}의제곱근 : {d3},{d2}의 제곱근 : {d4}"
print(s2)

# 6. 문자열 입력받아 대문자/소문자/글자 수 출력
str = input("문자열 입력: ")

print("대문자로 변환 : ", str.upper())   # Java 문자열.toUpperCase()
print("소문자로 변환 : ", str.lower())   # Java 문자열.toLowerCase()
print("길이 : ", len(str))

# 7. 좋아하는 음식 3개 입력받아 리스트처럼 저장 후 출력
food = []
food.append(input("첫번째 음식 : "))
food.append(input("두번째 음식 : "))
food.append(input("세번째 음식 : "))
print("좋아하는 음식 리스트:",food )
print("첫 번째 음식:",food[0] )
print("마지막 음식:" ,food[-1] )
food.sort()
print("오름차순 정렬 : ",food )
food.reverse()
print("내림차순 정렬 : ",food )
print()

# 8. 세 개의 숫자 입력받아 합과 평균 계산 후 출력
n1 = int(input("첫 정수 : "))
n2 = int(input("두번째 정수 : "))
n3 = int(input("세번째 정수 : "))
sum = n1 + n2 + n3
avg = (n1 + n2 + n3)/3

s8 = f"합 : {sum}, 평균 : {avg}"
print(s8)

# 9. 문자열 입력받아 앞 3글자 + 뒤 2글자 합쳐서 출력
str = input("문자열 입력: ")
p1 = str[0:3]
p2 = str[-2] + str[-1]
print(p1+p2)

# 10. 문자열 입력받아 대문자로 변환 후, 앞 5글자만 출력
str = input("문자열 입력: ")
str = str.upper()
print(str[0:6])