########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################### 정현희 선생님 ###############################################################
# #########################################section2) print()함수 서식####################################################
#cf.정현희 p.63 {중요} print()
# # print("\nIt\'s")
# print("%d" % 123)
print("%5d" % 123) #총 5자리로 만들기+ 빈칸 포함
print("%05d" % 123) #총 5자리 만들기 + 빈칸은 0으로 채워
#
# print("%f" % 123.45) #소수점 이하 6자리까지 출력
# print("%7.1f" % 123.45) #총 7자리, 소수점은 1자리까지
# print("%7.3f" % 123.45) # 총 7자리, 소수점은 3자리까지
#
# print("%s" % "Python") #"Python"의 자릿수만큼 출력
# print("%10s" % "Python") #총 10자리 만들기 + 빈칸 포함
# print("%s10" % "Python") #옆에 10붙이기


#############################################Section 3) 중첩 for 문 ####################################################
# #1.중첩 for 문의 개념
# #2. 활용
# 2)구구단-가로(p.155)
# 전역 변수
# i, k, guguLine = 0, 0, ""
#
# 메인 코드
# for i in range(2, 10):
#     guguLine = guguLine + ("# %d단 #" % i) #{중요}모두 모은 후 한번에 all 출력(각 하나씩 출력x)
#
# print(guguLine)
#
# for i in range(1, 10):
#     guguLine = "" #Q)쓰임?
#     for k in range(2, 10):
#         guguLine = guguLine + str("%2dX %2d= %2d" % (k, i, k*i))
#     print(guguLine)


#############################################Section 4) while 문 #######################################################
# # # 2. 무한 루프(loop)(=무한반복)를 하는 while 문
# while True :
#     print("무한 루프", end="")

# # p.161 숫자 2개 입력, 연산자 1개 입력
# ch=""
# a,b=0,0
#
# while True :
#     a = int(input("a의 숫자 입력 : "))
#     b = int(input("b의 숫자 입력 : "))
#     ch = input("연산자 입력 : ")
#
#     if(ch == "+") :
#         print("%d + %d = %d" % (a,b,a+b))
#     elif(ch == "-") :
#         print("%d - %d = %d" % (a,b,a-b))
#     elif(ch == "*") :
#         print("%d * %d = %d" % (a, b, a * b))
#     elif (ch == "/"):
#         print("%d / %d = %d" % (a, b, a / b))
#     elif (ch == "%"):
#         print("%d %% %d = %d" % (a, b, a % b)) #{조심} %%
#     elif (ch == "//"):
#         print("%d // %d = %d" % (a, b, a // b))
#     elif (ch == "**"):
#         print("%d ** %d = %d" % (a, b, a ** b))
#     else :
#         print("연산자를 잘못 입력했습니다.")

######################################## Section2) 리스트의 기본 ########################################################
#{중요} 리스트끼리 연산(+,*)
# aa = [10,20,30]
# bb = [40,50,60]
# print(aa+bb) #붙이기 #=>[10, 20, 30, 40, 50, 60]
# print(aa*30) #30번 반복 #=>[10, 20, 30, 10, 20, 30,....]

# aa=[10,20,30,40,50,60,70]
# print(aa[::2]) #2칸씩 건너뛰라
# print(aa[::-2]) #뒤에서부터 2칸씩 건너뛰라
# print(aa[::-1]) #뒤에서부터 1칸씩 건너뛰라
# print(aa[1::2]) #1번째부터 2칸씩 건너뛰라

# myList = [[1,2,[0,3]],  [4,5], [6]]
# print(myList)
# print(myList[0])
# print(myList[1][1])
# print(myList[0][2][0])


# # ## 6. 리스트 값 변경하기
# aa=[10,20,30]
# aa[1:2]=[200,201] #연속된 범위의 값을 변경하기
# print(aa) #=>[10, 200, 201, 30]
# #{주의}
# aa=[10,20,30]
# aa[1]=[200,201]
# print(aa) #=>[10, [200, 201], 30]


# #cf.정현희 cf7 p.189
# # #sort() : 오름차순 정렬
# myList = [30,0,20,0,-12]
# newList = [5,6,7]
# print("myList : ", myList)
# print("newList : ", newList)
#
# myList.sort()
# print("sort() 이렇게 작성하기 :", myList) #=>[-12, 0, 0, 20, 30]
#
# a=myList.sort()
# print("sort() 오류 :", a) #=>None


# # ## 7.리스트 조작 함수 (p.189) {중요}
# #count() :리스트에서 해당 값의 개수를 센다->반환한다
# #정답{중요}
# print("count() : ", newList.count(5))
#
# # cnt=newList.count(5)
# # print("count() : ", cnt)
#
# # #오답
# # # newList.count(5)
# # newList.count(newList) #count(newList) 작성하면 안됨
# # print("count() : ", newList)

# # ## 7.리스트 조작 함수 (p.189) {중요}
# #
# myList = [30,0,20,0,-12]
# newList = [5,6,7]
# print("myList : ", myList)
# print("newList : ", newList)
#
# #clear() : 리스트 내용 모두 지우기
# # myList.clear()
# # print("clear() : ", myList)
#
# #copy() : 리스트의 내용을 새로운 리스트에 복사한다
# newLsit = myList.copy()
# print("copy() : ", myList)
# print("copy() : ", newLsit)
#
# #del() : 리스트에서 해당 위치의 '항목을 삭제((리스트 자체를 삭제x))'한다
# del(myList[1])
# print("del() : ", myList)
#
# #len() : 리스트에 포함된 전체 항목의 개수를 센다=리스트의 개수 확인하기=리스트 내 요소의 개수를 돌려주는 함수
# print("len() : ", len(myList))
#
# #count() :리스트에서 해당 값의 개수를 센다->반환한다
# #정답{중요}
# print("count() : ", newList.count(5))
#
# # cnt=newList.count(5)
# # print("count() : ", cnt)
#
# # #오답
# # # newList.count(5)
# # newList.count(newList) #count(newList) 작성하면 안됨
# # print("count() : ", newList)
#
# #extend() : 리스트 뒤에 리스트를 추가한다. 리스트의 더하기(+) 연산과 기능이 동일하다.
# # myList.extend([1,2,3])
# # print("extend() 1 : ", myList)
# # myList.extend(newList)
# # print("extend() 2 : ", myList)
# #
# # nnewList = myList + newList
# # myList.extend([1,2,3])
# # myList.extend(newList)
# # print("extend() 3 : ", nnewList)
#
# myList.extend([1,2,3])
# myList.extend(newList)
# print("extend() 4 : ", myList)
#
# #remove() : 리스트에서 지정한 값을 삭제한다. 단 지정한 값이 여러 개면 첫번째 값만 지운다.
# myList = [30,10,0,20,0,-12]
# print("remove() 전 : ", myList)
# myList.remove(0) #remove() : 앞에 있는 0만 지움
# print("remove() 후 : ", myList)
#
# #insert(): 지정된 위치에 값을 '삽입'한다
# myList.insert(1,50) #1번째 위치에 50이란 값을 삽입
# print("insert() : ",myList)
#
# #index() : 지정한 값을 찾아 해당 '위치'를 반환한다
# print(myList)
# a=myList.index(0)
# print("index() 0 위치 찾기 : ", a)
# print("index() 10 위치 찾기 : ", myList.index(10))
#
# #reverse() : 거꾸로 뒤집기
# myList.reverse()
# print("reverse() : ", myList)
#
# #sorted() : 리스트의 항목을 정렬해서 새로운 리스트에 대입한다(오름차순 정렬+대입)
# newList=sorted(myList)
# print(myList)
# print("sorted()",newList)
# #to do 대입해보기!
#
#
# # #sort() : 오름차순 정렬
# myList.sort()
# print("sort() 이렇게 작성하기 :", myList) #=>[-12, 0, 0, 20, 30]
#
# a=myList.sort()
# print("sort() 오류 :", a) #=>None
# #
# # #append() : 리스트의 '맨 마지막'에 항목을 추가
# # myList.append(20)
# # print("append()", myList)
# #
# # #pop() :리스트 맨 뒤의 항목을 빼낸다(리스트에서 해당 항목이 삭제된다)
# print("pop() 전 : ", myList)
# print("pop() 빼내기 : ", myList.pop())
# print("pop() 후 : ", myList)
# print("-"*50)
# print("pop() 전 : ", myList)
# print("pop() 빼내기 : ", myList.pop())
# print("pop() 후 : ", myList)

######################################## Section2) 리스트의 기본 ########################################################
#{중요} 리스트끼리 연산(+,*)
# aa = [10,20,30]
# bb = [40,50,60]
# print(aa+bb) #붙이기 #=>[10, 20, 30, 40, 50, 60]
# print(aa*30) #30번 반복 #=>[10, 20, 30, 10, 20, 30,....]


######################################## Section4) 튜플 ########################################################
#3){중요} 연산(+,*)가능
tt2=('A','B')
print(tt1 + tt2) #덧붙이기
print(tt2 * 3) # 3번 반복하기


######################################## Section5) 딕셔너리 ########################################################
# 1. 딕셔너리 생성(p.199)
# 삭제하기 : del(딕셔너리명[키])
del(student1['이름'])
# del(student1['안철수']) #값으로 지정해 지우려면 오류
print(student1)

# 키-유일함
student1={'학번':1000,'이름':'홍길동', '학번':2000}
print(student1) #{중요} 동일한 키일 경우 마지막에 있는 키가 적용됨

# 2. 딕셔너리 사용 {중요}
# #딕셔너리명.get(키): 없는 키 호출 시 오류x(#=>None)
# #딕셔너리명[키]:없는 키 호출 시 오류o(#=>KeyError)
# student1={'학번':1000,'이름':'홍길동'}
# print(student1.get('회장'))
#
# student1={'학번':1000,'이름':'홍길동'}
# print(student1['회장'])



# 출력 관련
student1={'학번':1000,'이름':'홍길동'}
print(student1.keys()) #딕셔너리명.keys() : 모든 키 반환
print(list(student1.keys()))#list(딕셔너리명.keys()) : 출력 결과에서 dict_keys 지우고 출력

print(student1.items()) #딕셔너리명.items() : 키와 값의 쌍을 튜플 형태로 반환

print(student1.values()) # 딕셔너리명.values() : 딕셔너리의 모든 값을 리스트로 반환
print(list(student1.values())) # list(딕셔너리명.values()) : 출력 결과에서 dict_values 지우고 출력

# in : 해당 키 유무 확인 : 있으면 T, 없으면 F.
print('이름' in student1)
print('전공' in student1)



#ex)p.204
ab=[]
dic1 = {'반장':'황미나', '부반장':'이하림', '총무':'곽소희'}

print(dic1['총무'])
print(dic1.get('부반장')) #{중요} get() : key에 대응되는 value를 돌려준다
print(dic1.get('회장','회장:안철수')) #{중요} get(찾으려는 키, '디폴트 값') : 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에사용.
# print(dic1.keys()) #키만 출력

ab=dic1.keys()
# print(ab)
abList=list(ab)#ab는 리스트임. 일반 문자열 변수가 아님. 즉, 리스트로 키를 담고자 할 때.
# print(abList)
abList.append('부총무') # 새 키 삽입
# print(abList)

cd=dic1.values()
cdList = list(cd) # 값만 리스트로 담아 출력
# print(cdList)



#p.205 Self Study 7-5
#변수 선언
animals = {"닭":"병아리","개":"강아지","곰":"능소니","고등어":"고도리","명태":"노가리","말":"망아지","호랑이":"개호주"}; #Q); 왜 썼어?

#메인 코드
while(True) :
    myanimal = input(str(list(animals.keys())) + "중 새끼 이름을 알고 싶은 동물은?")
    if myanimal in animals :
        print("<%s>의 새끼는<%s>입니다." % (myanimal, animals.get(myanimal))) #{중요}

    elif myanimal == "끝" :
        break

    else :
        print("아이구, 그런 동물은 없네요. 확인해 보세요.")

######################################## Section6) 심화내용 ########################################################
#여기서부터 복습하기

# # #1. 세트(set)(p.206)
#중복된 키는 자동으로 하나만 남는다(정렬x)
# mySet1={1,2,3,3,3,4}
# print(mySet1)

# #{중요}리스트, 튜플, 딕셔너리 등을 세트로 변경시켜 준다.
# saleList=['삼각김밥','바나나','도시락','삼각김밥','도시락','삼각김밥']
# print(set(saleList))

# #{중요}집합
# mySet1={1,2,3,4,5}
# mySet2={4,5,6,7}
#
# # #방법1)
# # #교집합(두 세트에 공통으로 들어 있는 값) : &
# # print(mySet1 & mySet2)
# # #합집합(두 세트의 값을 모두 모은 것) : |
# # print(mySet1 | mySet2)
# # #차집밥(첫 번째 세트에만 있고 두 번째 세트에는 없는 값) : -
# # print(mySet1 - mySet2)
# # #대칭차집합(한 쪽 세트에만 포함되어 있는 값) : ^
# # print(mySet1 ^ mySet2)
#
# #방법2)
# print(mySet1.intersection(mySet2)) #교집합
# print(mySet1.union(mySet2)) #합집합
# print(mySet1.difference(mySet2)) #차집합
# print(mySet1.symmetric_difference(mySet2)) #대칭차집합

# # #방법3)
# my1=mySet1 & mySet2
# my1=mySet1 | mySet2
# my1=mySet1 - mySet2
# my1=mySet1 ^ mySet2
# print(my1)
#
# # #방법4)
# my1=mySet1.intersection(mySet2)
# my1=mySet1.union(mySet2)
# my1=mySet1.difference(mySet2)
# my1=mySet1.symmetric_difference(mySet2)
# print(my1)



# # #2.컴프리헨션(Comprehension.함축)(p.207)
# 리스트 컴프리헨션(많이 사용)과 딕셔너리 컴프리헨션(적게 사용)으로 나뉜다.
# 리스트 컴프리헨션의 형식 :
# 리스트=[수식 for 항목 in range() if 조건식]
# 해석순서 : if 조건식->for 항목 in range()->수식

# # #ex) 1~5까지 저장된 리스트 만들기
# #컴프리헨션 사용해 만들기
# numList=[num for num in range(1,6)]
# print(numList)
# #컴프리헨션 사용하지 않고 만들기
# numList=[]
# for num in range(1,6):
#     numList.append(num)
# print(numList)


# # #ex) 1~5의 제곱으로 구성된 리스트 만들기
# numList = [num * num for num in range(1,6)]
# print(numList)
# #=>[1, 4, 9, 16, 25]
# #해석 : 1x1=1, 2x2=4, 3x3=9, 4x4=16, 5x5=25

# # #ex) 1~100까지 숫자에서 5의 배수만 리스트에 넣기
# #컴프리헨션 사용해 만들기
# numList = [num for num in range(1,101) if num % 5 ==0]
# print(numList)
# #컴프리헨션 사용하지 않고 만들기
# numList=[]
# for i in range(1,101):
#     if i % 5 == 0:
#         numList.append(i)
#         print(numList)


# # #3.동시에 여러 리스트에 접근 가능(p.208)
### zip : 자료들을 묶어주는 함수
#작은 개수 기준으로 묶는다 : 피자,맥주-zip(x)
# foods = ['떡볶이','짜장면','라면','피자','맥주']
# sides = ['오뎅','단무지','김치']
# for food, side in zip(foods, sides):
#     print(food,'-->',side)

# #리스트,튜플,딕셔너리로 묶기 가능
# foods = ['떡볶이','짜장면','라면','피자','맥주']
# sides = ['오뎅','단무지','김치']
# #튜플+리스트로 묶기
# tupList=list(zip(foods,sides))
# print(tupList)
# #튜플
# print(tuple(zip(foods,sides)))
# # tuple=zip(foods,sides)
# # print(tuple) #=><zip object at 0x0000028703389948>
# #딕셔너리
# dic=dict(zip(foods,sides))
# print(dic)


# # #4.리스트의 복사(p.209)
# 얕은 복사(Shallow Copy) : 메모리 공간 1개 공유 ex)나와 너 - 냉장고 1대 공유
# 깊은 복사(Deep Copy)(리스트명[:] or 리스트명.copy()) : 메모리 공간 각자 소유 ex)나-내 냉장고 1대, 너-네 냉장고 1대 각각 소유

# # 1) 얕은 복사
# oldList=['짜장면','탕수육','군만두']
# newList=oldList
# print(oldList)
# print(newList)
#
# oldList[0]='짬뽕'
# print(oldList)
# print(newList)
#
# oldList.append('깐풍기')
# print(oldList)
# print(newList)


# # 2) 깊은 복사 :  리스트명[:] or 리스트명.copy() 로 싸용
# oldList=['짜장면','탕수육','군만두']
# newList=oldList[:]
# # newList=oldList.copy()
# print(oldList)
# print(newList)
#
# oldList[0]='짬뽕'
# print(oldList)
# print(newList) # 변경되지 않음
#
# oldList.append('깐풍기')
# print(oldList)
# print(newList) # 변경되지 않음


# # #5.{중요}리스트를 이용한 스택(stack) 구현(p.210)
#리스트를 이용해 초기화함
parking=[]
top=0

#push : 데이터 넣기. append()함수 사용
parking.append('자동차A') #자동차 한대 넣기
top += 1 #자동차A는 top의 위치에 들어감->top은 0에서 1로 바뀜
print(parking)
parking.append('자동차B')
top += 1
print(parking)
parking.append('자동차C')
top += 1
print(parking)

#pop : 데이터 빼기
top -= 1
outCar=parking.pop() # 자동차 한대(C) 빼기
print(outCar)
top -= 1
outCar=parking.pop() # 자동차 한대(B) 빼기
print(outCar)
top -= 1
outCar=parking.pop() # 자동차 한대(A) 빼기
print(outCar)
outCar=parking.pop()
print(outCar) #=>IndexError: pop from empty list(뺄 차 없다)


########################################################################################################################
####################################################8장 문자열(String)###################################################
########################################################################################################################

################################################# Section2) 문자열 기본 #################################################
####{중요}프로그램1(p.227) : 문자열 거꾸로 출력하기
#내 풀이) 전체 문자열의 개수에서 하나씩 빼나가며(가감) 뒤에서부터 앞으로 계속토록 한다.
#변수 선언
inStr, outStr = "", "" #inStr : 문자열 입력 받을 변수 #outStr : 문자열 거꾸로 저장하는 변수
count, i = 0, 0 #count : 문자열 개수 저장

#메인 코드
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)

for i in range(0, count) :
    # print(inStr[i],end='')
    outStr += inStr[count - (i + 1)] #{중요. 핵심임)
    # print(outStr)

print("내용을 거꾸로 출력 --> %s" % outStr)

# #요약)
# outStr = ""
# inStr=input("문자열을 입력하세요 : ")
# count=len(inStr)
# for i in range(0,count) :
#     outStr += inStr[count-i-1]
# print(outStr)

################################################# Section3) 문자열 함수 #################################################
# #3. 문자열 공백 삭제, 변경하기 : strip(), rstrip(), lstrip(), replace()
# ss = '  파 이 썬  '
# print(ss)
# #1){중요} 변수명.strip() : '앞뒤' 공백 삭제
# print(ss.strip())
# print(type(ss.strip()))
#
# #2){중요} 변수명.rstrip() : '오른쪽' 공백 삭제
# print(ss.rstrip())
# print(type(ss.strip()))
#
# #3){중요} 변수명.lstrip() : '왼쪽' 공백 삭제
# print(ss.lstrip())
# print(type(ss.strip()))
#
# # #4){중요} 문자열 '중간' 공백 삭제하기(#p.231 Code 8-4)
# inStr = "  문자열 중간 공백 삭제 전 "
# outStr = ""
#
# for i in range(0, len(inStr)):
#     if inStr[i] != ' ':
#         outStr += inStr[i]
#
# print(outStr)

# print("중간 공백 삭제 전 : " + '[' + inStr+ ']')
# print("중간 공백 삭제 후 : " + '[' + outStr+ ']')

# # # Ex) p.231 Self Study 8-2 :'<<<파<<이>>썬>>>' -> '파이썬'으로 출력하기
# inStr="<<<파<<이>>썬>>>"
# outStr = ""
#
# for i in range(0,len(inStr)) :
#     if inStr[i] != '<' and inStr[i] !='>':
#         outStr += inStr[i]
# print(outStr)

# # 5){중요} 변수명.replace('기존문자열', '새문자열') : 문자열 변경
# ss = '열심히 파이썬 공부 중~'
# print(ss)
# print(ss.replace('파이썬', 'Py'))
# # print(type(ss.replace('파이썬', 'Py')))
#
# # #Ex) p.232 code8-5 : 영문자 'o'를 찾아 '$'로 변경
# inStr = input("입력받을 문자열 : ")
# outStr = ''
#
# print(inStr.replace('o','$'))
#
# # 만약 print(inStr.replace('o','$')) 문장을 쓰지 않으면 아래와 같이 길어진다.
# # for i in range(0,len(inStr)) :
# #     if inStr[i] != 'o':
# #         print(inStr[i], end='')
# #     else:
# #         print('$', end='')


# # #4. 문자열 분리, 결합하기 : split(), splitlines(). join()
# #1){중요} 변수명.split() : 문자열을 공백/다른 문자로 분리해 리스트로 반환함.
# ss = 'Python을 열심히 공부 중'
# print(ss.split()) #공백 기준으로 분리
#
# ss = 'Python:열심히:공부: 중'
# # print(ss.split(':')) #:기준으로 분리

##2)변수명.splitlines() : 행 단위로 분리시켜줌
# ss = '하나\n둘\n셋'
# print(ss.splitlines())
# print(ss.split('\n'))
#
# #3){중요} 구분자.join('문자열') : 문자열 결합하기
# ss = '%'
# print(ss.join('파이썬'))
# print(type(ss.join('파이썬')))

# Ex) p.233 Code 08-06 : 연/월/일 형식의 문자열을 입력 -> 10년 후 날짜를 출력
# 내 답안)
# # 얼거리 : /제거->리스트화->연에 10 더하기
# inStr = input("연/월/일 형식 날짜 입력 : ")
# # inStr = "2010/01/01"
# outStr = ""
#
# chList=inStr.split('/')
# # print(chList)
# print("10년 후 날짜 출력 : ", str(int(chList[0])+10) + '년' + chList[1] + '월' + chList[2] + '일')

# # 책 답안)
# ss = input("연/월/일 형식 날짜 입력 : ")
#
# ssList=ss.split('/')
# print("입력한 날짜의 10년 후 ==>", end='')
# print(str(int(ssList[0])+10) + '년', end='')
# print(ssList[1] + '월', end='')
# print(ssList[2] + '일', end='')


# # #5. 함수명에 대입하기
# # map(함수명, 리스트명) : ("리스트명"에 있는)리스트값 하나하나를 "함수명"에 대입
# before = ['2019', '12', '31']
# after = list(map(int, before)) #문자->숫자 변환->리스트로 변환
# print(after)
# # print(type(after))
#
# before = [2019, 12, 31]
# after = list(map(str, before)) #숫자->문자 변환->리스트로 변환
# print(after)


# # #6. 문자열 정렬하기, 채우기 : center(). ljust(), rjust(), zfill()
ss = '파이썬'
# #1) 변수명.center(숫자) : 숫자만큼 전체 자릿수를 잡은 후 문자열을 가운데 배치
print(ss.center(10))
#변수명.center(숫자,'문자') : 앞뒤 빈 공간에 문자로 채워 넣음
print(ss.center(10,'-'))
# print(type(ss.center(10,'-')))


# #2) 변수명.ljust(숫자) : 왼쪽에 붙여서 출력
print(ss.ljust(10))
# print(type(ss.ljust(10)))

# #3) 변수명.rjust(숫자) : 오른쪽에 붙여서 출력
print(ss.rjust(10))
# print(type(ss.rjust(10)))

# #4) 변수명.zfill(숫자) : 오른쪽에 붙여 쓰고, 왼쪽 빈 공간은 0으로 채움
print(ss.zfill(10))
# print(type(ss.zfill(10)))


# #7. 문자열 구성 파악하기 : isdigit(), isalpha(), isalnum(), islower(), isupper(), isspace()
# 개념 : 문자열의 구성을 확인한 후 T/F로 반환
# 방식(2) :
# 1) ss='1234'
# 2) '1234'.메서드()
# (반환 시)자료구조 : bool

# # 1) 변수명.isdigit() : 숫자로만 구성되었나 확인
ss='1234'
# print(ss.isdigit())
# print(type(ss.isdigit())) #=>bool
#
# print('1234'.isdigit())
#
# # 2) 변수명.isalpha() : 글자(한글, 영어)로만 구성되었나 확인
print(ss.isalpha())
# print('1234'.isalpha())
# print('ab가나'.isalpha())

# print(type(ss.isalpha()))

# # 3) 변수명.isalnum() : 글자+숫자 섞여 있나 확인
# print(ss.isalnum())
# print('12rk가나'.isalnum())
# print('12rk가나#$#$'.isalnum())
# print(type(ss.isalnum()))

# # 4) 변수명.islower() : 전체가 소문자로만 구성되었는지 확인
# ss="abvf"
# print(ss.islower())

# print("abvf".islower())
#
# ss="abvf가나"
# print(ss.islower()) #소문자 영문+한글 섞일 때 True
#
# ss="가나"
# print(ss.islower()) # 순 한글일 때는 False

# # 5) 변수명.isupper() : 대문자로만 구성되었는지 확인
# ss = "AAFF"
# print(ss.isupper())

# print("AAFF".isupper())
#
# ss = "AabbB"
# print(ss.isupper())
#
# ss = "AAFF가나"
# print(ss.isupper()) # 대문자 영문+한글 섞일 때 True
#
# ss = "가나"
# print(ss.isupper()) # 순 한글일 때는 False

# # 6) 변수명.isspace() : 공백 문자로만 구성되었는지 확인
# ss = '    '
# print(ss.isspace())
#
# print('    '.isspace())


########################################################################################################################
############################################9장 함수와 모듈(Function, module)############################################
########################################################################################################################

################################################# Section2) 문자열 기본 #################################################
# # ex) p.251 : plus()함수 작성하기
# #전역 변수
# hap = 0
#
# #함수 선언 = 함수를 정의함 = 요리하자
# def plus(c,d,e,f=1) : #{중요} f=1->f=50으로 바뀜
#     hap=c+d+e+f
#     return hap
#
# def pp() :
#     print("다른 함수")
#
# #메인 코드 = 함수를 실행함 = 요리 먹자
# a=int(input("숫자1 "))
# b=int(input("숫자2 "))
# dap = plus(a,b,30,50)
# print(dap)


######################################## Section 4) 함수의 반환값과 매개변수 #############################################
# ex) 3)개수 지정 않고 전달
## 함수 선언 부분 ##
def para_func(*para) : #{조심}*:튜플로 만듦, para :매개변수명
     result = 0
     for num in para :
          result = result + num

     return result

## 전역 변수 선언 부분 ##
hap = 0

## 메인 코드 부분 ##
hap = para_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
# print(type("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap))
hap = para_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)

############################################# Section 6) 함수의 심화 내용 ###############################################
# ## 3.{중요}람다함수
# 형식 : 함수명=lambda 매개변수:함수내용
# 1)개념
# 1-1)람다 사용 전
# def hap(num1, num2):
#     res = num1 + num2
#     return res
# print(hap(10, 20))
#
# 1-2)람다 사용 후
# hap2 = lambda num1, num2 : num1 + num2 #lamda함수를 이용해 매개변수(num1, num2)를 계산(num1 + num2)해 hap2에 넣겠다
# print(hap2(10,20))
#
# 1-3)매개변수에 기본값 설정해 사용하기도 가능
# hap3 = lambda num1 = 10, num2 = 20 : num1 + num2 ## 매개변수에 기본값 설정해 사용하기도 가능
# # print(hap3) #이렇게 작성하면 출력 안됨 #Q)어떤 형식이라고 하나?
# print(hap3())
# print(hap3(100,200)) #기본값을 설정해도 매개변수를 넘겨주면 기본값은 무시됨.

# 2){중요}람다 + map 함수 사용(p.274)
# #2-1)람다 사용 전
# myList = [1,2,3,4,5]
# # 함수 선언
# def add10(num) :
#     return num + 10
# # 메인 코드
# for i in range(len(myList)):
#     myList[i] = add10(myList[i])
#
# print(myList)
#
# #2-2){중요}람다+map 함수 표현 방법
# myList = [1,2,3,4,5]
# add10 = lambda num : num + 10
# myList = list(map(add10, myList)) # map(함수명, 리스트명) : 리스트(muList)의 모든 내용을 하나씩 함수(add10)에 적용 {num으로 들어감}
# print(myList)
#
# #2-3){중요}람다+map 함수 표현 방법
# myList = [1,2,3,4,5]
# myList = list(map(lambda num : num+10, myList))
# print(myList)

# #2-4){중요}람다+map 함수 표현 방법-리스트가 2개 이상 있을 경우
# list1 = [1,2,3,4]
# list2 = [10,20,30,40]
#
# #람다함수 -> 일반함수
# def hapfunc(n1,n2) :
#     return n1+n2
#
# haplist = list(map(hapfunc,list1,list2))
# print(haplist)

########################################################################################################################
########################################################################################################################
########################################################################################################################
############################################# 박길식 선생님 #############################################################
# pi=3.14
# print("{0:10.4f}".format(pi)) #pi를 0으로 넣어 10 + 소수자리 4까지 출력 =>10은 10진수?

################################################# Day 2-2 ##############################################################
# #8. 비교-계산, 리턴값
# # 1)
# def two_times(num):
#     res=[] #[2,4,6]
#     for n in num:
#         res.append(n*2)
#     return res #[2,4,6]
#
# res=two_times([1,2,3])
# print(res)#[2,4,6]
# # 2)
# def two_times(num):
#     res=[] #3번 반복됨 [[1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3]]
#     for n in num: #n:2
#         # print(n)
#         res.append(num*2) #[1,2,3]이 2번 반복돼 [1,2,3,1,2,3]
#         # return res #리턴 위치에 따라 다른 결과값
#     return res
#
# print(two_times([1,2,3])) #(출력 시)None:함수를 호출하여 수행한 결과가 리턴되지 않았다. 즉, 리턴문 빠짐
#
# # 3)
# def two_times(num):
#     res=[] #3번 반복됨 [[1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3]]
#     for n in num: #n:2
#         # print(n)
#         res.append(num*2) #[1,2,3]이 2번 반복돼 [1,2,3,1,2,3]
#         return res #리턴 위치에 따라 다른 결과값
#     # return res
#
# print(two_times([1,2,3])) #(출력 시)None:함수를 호출하여 수행한 결과가 리턴되지 않았다. 즉, 리턴문 빠짐


################################################# Day 2-3 ##############################################################
# #1.출력값-sorted/sort 차이
# # # 1)sorted 함수 : 값을 "정렬" -> 결과를 "리스트"로 리턴해주는 함수. 순차 자료형으로 반환. 오름차순. 출력값은 리스트 형식.
# print(sorted("seoul")) #=>['e', 'l', 'o', 's', 'u']
# # #혹은
# # #ss = sorted([5,3,4])
# # #print(ss) #=>[3, 4, 5]
# # # 2)sort 함수 : 리턴값이 없음.아래 처럼 작성. 오름차순.
# myList=[31,10,20]
# myList.sort()
# # myList.sorted() #=>오류
# print(myList) #=>[10, 20, 31]

# ########cf. 배열 VS 리스트
# #공통점 : 여러개 값이 나열되는 측면이 같다
# #차이점 : 배열-저장되는 타입이 모두 동일해야함.
# #        리스트-타입 달라도 됨(문자 ,숫자 섞여있어도 괜찮음)
# print(sorted([5,3,4])) #정렬! 공통점 답이 다 리스트로 나옴. #=>[3, 4, 5]
# print(sorted(['k','i','m'])) #=>['i', 'k', 'm']
# print(sorted("seoul")) #=>['e', 'l', 'o', 's', 'u']
# ss = sorted([5,3,4])
# print(ss) #=>[3, 4, 5]

# ex) sorted
data=[5,3,4]
sorted(data)
print(data) #=>[5, 3, 4]

data=[5,3,4]
data=(sorted(data))
print(data) #=>[3, 4, 5] #Q) 왜 이렇게 출력될까?

# ex)sort
data2 =[5,3,4]
print(data2.sort()) #=>None

data2 =[5,3,4]
data2.sort()
print(data2)#=>[3, 4, 5]
