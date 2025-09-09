# 4_data_list.py

# 리스트 -> 배열 / ArrayList
# 특징 => 중복 허용, 순서 유지, 가변(수정 가능)

fruits = ["사과", "배", "딸기", "복숭아", "바나나"]

# 인덱싱
print("첫번째 과일 : ", fruits[0])
print("마지막 과일 : ", fruits[-1]) # 리스트 끝에서부터 접근!

# 슬라이싱
print("두번째, 세번째 과일 : ", fruits[1:3]) # 1, 2 인덱스로 접근

# 리스트에 데이터 추가
fruits.append("무화과")
print(fruits)

fruits.insert(3, "두리안")
print(fruits)

fruits.extend(["메론", "수박"])
print(fruits)

# 데이터 삭제 : remove, pop
fruits.pop() # 리스트 끝의 데이터를 삭제
print(fruits)
item = fruits.pop()
print(item) # 리스트 끝의 데이터를 삭제하며 해당 값을 리턴

fruits.remove("두리안")
print(fruits)

#정렬
nums = [5, 3, 9, 1]

nums.sort() #오름차순 정렬
print(nums) # [1,3,5,9]
nums.reverse() # 내림차순 정렬
print(nums) # [9,5,3,1]

nums = [5,3,9,1]
nums.sort(reverse=True) # sort 메소드에 reverse 옵션 추가
print(nums) # 내림차순 정렬

words = ["apple", "banana", "cat"]
words.sort(key=len) # 데이터 길이를 기준으로 정렬
print(words)

words.sort(key=len, reverse=True)
print(words)