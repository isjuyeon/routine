def maxareaofisland(grid):
    result=0
    count = 0
    def dfs(a,b):
        nonlocal count
        if a>len(grid)-1 or b>len(grid[0])-1 or a<0 or b<0 or grid[a][b]==0:
            return 0
        grid[a][b]=0
        count+=1
        dfs(a+1,b)
        dfs(a,b+1)
        dfs(a-1,b)
        dfs(a,b-1)
        return count

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                count = 0
                a=dfs(i,j)
                result = max(result,a)
    return result

print(maxareaofisland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
'''
count가 최종 출력 값이고 dfs는 배경 지식이니 count의 전역/지역 변수 설정 및 위치 선정에 주의를 기울여야 한다. 제일 큰 함수에서 먼저 count가 선언이 되어야 다음에 쓸 수가 있으므로 거기다가 적었고, 
후에 0이 1로 바뀔때마다 +1을 해주고 이걸 재귀로 걸어서 자식들이 했던 것 까지 싹다 누적 시켜서 dfs(a,b)로 최종 값을 return 할 수 있게 만들어줌(변수를 dfs(i,j)로 써도 전혀 상관이 없긴하다. 
대신에 for문이 돌때마다 count 값은 0으로 초기화 해야 개별 경우 중 max를 구할 수가 있으므로 if문 바로 밑에 초기화를 해둠/그리고 이중 for문은 세로, 가로 순이다. 
가로가 이중으로 들어간거라서 그럼/grid, count를 매개변수로 부르기가 귀찮아서 종속으로 적어준다.
'''
