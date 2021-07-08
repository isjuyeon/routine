import collections
def findItinerary(tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    # 다시 뒤집어 어휘순 결과로
    return route[::-1]

print(findItinerary([['MUC','LHR'],['JFK','MUC'],['SFO','SJC'],['LHR','SFO']]))