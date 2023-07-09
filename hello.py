# # ===================1-1 숫자열 자료형 =====================

# # int : 정수 
# # float : 실수
 
# a = 3
# b = 4

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# print(a%b)
# print(a**b)
# print(a//b)








# # ===================2-1 문자열 자료형==================


# # str : 문자열 자료형

# a = 'python\'s is good program tool'
# print(a)

# a = 'Life is short\nyou need Python' #이스케이프문자
# print(a)

# a = """Life is 
#         short
#   you need Python""" # """ 는 줄바꿈 인식함
# print(a)


# a = "Life "

# print(a*10)









# # =====================2-2 인덱싱(indexing)===================



# a = "Life is short you need Python"

# print(a[0])  #글자의 순서에 숫자를 매김
# print(a[1])
# print(a[2])
# print(a[3])

# # 슬라이싱(slicing)  # a[이상:미만:간격]

# a = "Life is short you need Python"

# print(a[0:4]) # 0 <= X < 4

# print(a[:4]) #비워 놓으면 처음부터 시작

# print(a[::2]) # 2칸씩 끝까지 간다
# print(a[::-1]) #-1씩 끝까지 간다 (결론' 역순)

# print(a[5:])


# # 문자열 포매팅

# a = "I eat %d Apple" %3
# b = "I eat "+str(3)+" Apple" # 따옴표등 귀찮기 때문에 위에걸 쓰자

# print(a)
# print(b)

# # 문자열 포매팅 활용

# number = 10
# day = "three"

# a = "I ate %d Apple. So i was sick for %s days." %(number,day)

# a = "I ate %s Apple. So i was sick for %s days." %(number,day)  #%s 는 다 됨

# print(a)
# # %s 문자열 %d 정수 %f 실수

# a = "%0.2f" %3.141592 #소수점 2자리 까지 쓰겠다
# print(a)

# a = "Life is {} you need Python".format("short")
# print(a)

# a = "My name is {name}.Im {age} years old. Nice to meet you".format(name ="KIM", age=21)
# print(a)

# #바로 위 코드 활용
# name = "KIM"
# a= f"My name is {name}"
# print(a)

# #함수

# a = "hobby"
# print(a.count("b")) #b가 몇개인지 세어줘

# a = "Python"
# print(a.find("h")) #h가 0부터 몇번째에 있는지 찾아줘

# a = "Python"
# print(a.find("x")) #찾고싶은 글자가 없을때는 -1 출력

# a = ",".join("abcde")
# print(a)

# a = ",".join(["a","b","c","d","e"])
# print(a)

# a = "python"
# print(a.upper()) #대문자로 바꿔줌

# a = "PYTHON"
# print(a.lower()) #소문자로 바꿔줌

# a = "     python     "
# print(a.strip()) #공백을 없애줌

# a = "Life is short you need Python"
# print(a.replace("Python","Javascript")) #(이 문자를,이 문자로 변환)

# a = "Life is short you need Python"
# print(a.split()) #문자열 자료형을 () 별로 자른다

# a = "LifexisxshortxyouxneedxPython"
# print(a.split("x")) #문자열 자료형을 (x) 별로 자른다










# #========== 2-3 리스트 자료형==============



# a = [1,2,3,4,5]
# print(a) #리스트 전체 출력

# a = ["one","two","three","four"]
# print(a[2]) #리스트 안에 몇번째 값만 출력

# a = ["one","two","three","four",[5,6,7]] # 리스트 안에 리스트를 또 만들수 있음
# print(a[4]) 

# a = ["one","two","three","four",[5,6,7]] 
# print(a[4][2]) # 리스트 안의 리스트에서 몇번째 값만 출력

# a = [1,2,3]
# b = [4,5,6]
# print(a+b) #리스트 더하기

# a = ["one","two","three","four"]
# a[0] = "1" # [번쨰]리스트를 바꾼다
# print(a)

# a = ["one","two","three","four"]
# a[0:2] = ["1","2"] # 0 <= x < 2 번째 리스트를 바꾼다
# print(a)

# a = ["one","two","three","four"]
# del a[0] # 0번째 리스트를 지운다
# print(a)

# a = ["one","two","three","four"]
# a.remove("two") # 특정 값을 지운다
# print(a)

# a = ["one","two","two","three","four"]
# a.remove("two") # 첫번째로 걸리는 것만 지운다. #다 지우려면 for문 해서 if남아있으면 또 지우고 해야함
# print(a)

# a = ["one","two","three","four"]
# a.append("five") # 리스트를 추가한다
# print(a)

# a = ["one","two","three","four"]
# a.append(["five","six"]) # 리스트에 리스트를 추가한다
# print(a)

# a = ["one","two","three","four"]
# a.extend(["five","six"]) # 리스트안의 값만을 추가한다
# print(a)

# a = ["one","two","three","four"]
# a.insert(0,"zero") #(x번째,이걸 추가)
# print(a)

# a = [1,4,3,2]
# a.sort() #숫자의 경우 크기순으로 정렬
# print(a)

# a = ["one","two","three","four"]
# a.sort() #글자의 경우 첫알파벳 abc순으로 정렬 
# print(a)

# a = ["one","two","three","four"]
# a.reverse() #리스트를 뒤집는다
# print(a)

# a = ["one","two","three","four"]
# print(a.pop()) #리스트의 마지막걸 빼냄
# print(a) #빼낸 나머지 리스트 









# # ==========2-4 튜플 자료형 (자물쇠가 잠긴 리스트같은 느낌 수정을 못함) ==============


# t1 = (1,2,"three","four")
# print(t1[0]) # 보는건 가능함

# t1 = (1,2,"three","four")
# t2 = (5,6)
# print(t1+t2) # t1과t2를 합한 새로운 튜플을 만듬 *수정한게 아님









# # ===================2-5 딕셔너리 자료형=======================

# # {Key : Value} 로 만들어져 있다

# dic = {"name": "KIM", "age":21} 
# print(dic["name"])  #네임 키에 있는 벨류를 뽑음


# dic = {"name": "KIM"} 
# dic["age"] = 21 #딕셔너리에 새로운 키와 벨류를 넣는다
# print(dic)


# dic = {"name": "KIM", "age":21}
# del dic["age"]   # 지우고 싶은 Key를 넣는다
# print(dic)


# dic = {"name": "KIM", "age":21, "Country": "korea"}

# print(dic.keys()) #　Key만을 뽑아서 리턴

# print(dic.values()) # Value만을 뽑아서 리턴

# print(dic.items()) # 각각의 키벨류를 튜플형태로 리턴

# dic.clear() # 딕셔너리 안의 모든 키벨류를 지운다
# print(dic)


# a = {1:"a", 2:"b", 3:"c"}

# # print(a[4])  #없는 키는 에러발생

# print(a.get(4)) # 없는 키는 None으로 리턴

# print(a.get(4,"없음")) #없는 키면 "없음" 을 리턴
# print(a.get(3,"없음")) #있다면 그대로 벨류값 리턴

# print(1 in a)
# print(4 in a)#a라는 사전에 해당 Key 가 있는지. boolean형태인 True, False값으로 리턴







# # ======================2-6 집합 자료형========================

# #중복된 값은 집합 안에 넣을 수 없다.
# #집합 자료형에 순서는 없다

# s1 = set([1,2,5]) # set : 집합
# print(s1)

# s2 = {3,4,5} # 중괄호 안에 넣어도 집합
# print(s2)



# # 집합 자료형 활용

# #중복 된걸 없애고 싶을때
# l = [1, 2, 2, 3, 4, 4, 5] 
# NewList = list(set(l))
# print(NewList)

# s1 = set("Hello") #문자열 형태는 집합에 들어가면 쪼개진다. 중복된 값을 제거
# print(s1)


# s1 = set([1,2,3,5])
# s2 = set([3,4,5,6])

# print(s1 & s2) #교집합을 리턴
# print(s1.intersection(s2)) #intersection : 교집합 

# print(s1 | s2) #합집합을 리턴
# print(s1.union(s2)) #union : 합집합

# print(s1 - s2) #차집합을 리턴
# print(s1.difference(s2)) #difference : 차집합


# s1 = set([1,2,3,5])
# s1.add(4) # 값 한개 추가
# print(s1)

# s1.update([6,7,8]) # 값 여러개 출력
# print(s1)

# s1.remove(7) # 값 한개 지우기
# print(s1)







# ==============2-7 boolean자료형===============

b = True
print(b)
print(type(b))

# "Python"  ""안에 문자가 있으면 True 없으면 False

# [1,2,3,4] 리스트 안에 값이 있으면 True 없으면 False

# () 튜플 자료형에 값이 없으면 False

# {} 딕셔너리 자료형에 값이 없으면 False

# 1은 True, 0은 False, None은 False

a = [1,2,3,4]
while a: #a 안에 값이 있기때문에 트루
    a.pop() # .pop함수로 마지막 값을 꺼내서 제거 
    print(a)








# ================2-8 자료형의 값을 저장하는 공간, 변수====================


