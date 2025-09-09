#_variable_scope.py

#변수의 스코프
# - 전역변수 : 함수 외부에 선언된 변수. 자바에서는 멤버 변수(필드)처럼 함수 어디서든 접근 가능
# - 지역변수 : 함수 내부에 선언된 변수. 해당 함수 내에서만 접근 가능

# -> global 키워드 사용 : 함수 내부에서 전역 변수의 값을 변경 가능

# 전역 변수 선언
count = 0

def ex1():
    count = 10
    print("ex1() :", count)

def ex2():
    global count
    print("ex2")    


ex1()
print("ex1()호출 후 count: ", count)

ex2()
print("ex2()호출 후 count: ", count)