a=list('cat')
print(a)

tuple_a=('ready','fire','aim')
b=list(tuple_a)
print(b)
print(b[::-1])

# 리스트 항목 끝에 추가하기
b.append('start')
print(b)

# 원하는 위치에 항목 추가하기
b.insert(1,'set')
print(b)

# 리스트 병합하기
c=['3','2','1','done']
b.extend(c)
print(b)

# 항목 바꾸기
b[2]='aim'
b[3]='fire'
print(b)

