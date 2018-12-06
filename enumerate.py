
#cf.day8-4

#cf.enumerate()와 _기호(뜻:삭제)
myName=['Kim','Park','Lee']
for i, name in enumerate(myName):
# for _, name in enumerate(myName): #i안쓰고 name에 해당하는 것만 출력
    print(i,name)
v=[name for _, name in enumerate(myName)]
print(v)