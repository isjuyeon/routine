N,M,background,result= *map(int, input().split()),[],[]#입력값

def dfs(path):# 함수설정
    if len(path) == 3 and sorted(path) not in result:
        result.append(sorted(path))
        return
    for i in background:
        if i in path:
            continue
        else:
            l = path[:]
            l.append(i)
            dfs(l)
for x in range(M): # 출력을 위한 전체 반복문
    a, b = map(int, input().split()) #a,b를 각각 받은 다음에 in논리를 써서 예외 처리된 집합을 만들기 위하여 밑에 조건문에서는 [a,b]라고 적어둠
    for i in range(1,N+1):
        if i not in [a,b]:#이렇게 1부터 N까지의 모든 수 중에서 a,b만 제외되도록 한 집합을 background에 저장함. 단 입력문의 줄이 바뀔때마다 새로운 background가 형성되므로 dfs이후에 pop처리해줌
            background.append(i) #제외된 집합은 세팅 완료됨

    dfs([]) #알아서 돌고 다끝나면
    background=[]# 초기화 후 입력문항의 밑에 줄 실행

print(len(result))# 중복없는 집합의 개수는 len으로 처리