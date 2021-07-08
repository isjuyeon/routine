import collections
def networkDelayTime(times,N,src,dst,K):
    graph1= collections.defaultdict(list)
    graph2= collections.defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v,w in times:
        graph1[u].append(v,w)

print(networkDelayTime(times=[[0,1,100],[1,2,100],[0,2,500]],N=3,src=0,dst=2,K=0))
