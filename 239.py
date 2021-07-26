from collections import deque
def maxSlidingWindow(nums,k):
    result = []
    deq = deque()
    for i in range(k):
        deq.append(nums.pop(0)) #최초의 윈도우 설정
    maximum = max(deq)#최초의 maximum
    while nums != []: #조건을 이렇게 준 부분이 에러사항일듯
        if deq.popleft() == maximum and nums != []:#나간게 최댓값이냐 아니냐로 나눔
            deq.append(nums.pop(0)) #nums로부터 새로 추가해줌
            maximum = max(deq)
            result.append(maximum)#새로운 maximum 설정됨
        elif deq.popleft() != maximum and nums != []:
            if nums[0] > maximum and nums != []:#나간게 최댓값이 아닌 경우에는 기존의 maximum값보다 들어온거 사이의 대소비교가 필요함.
                maximum = nums.pop(0)
                deq.append(maximum)
                result.append(maximum)
            elif nums[0] <= maximum and nums != []:
                deq.append(nums.pop(0))
                result.append(maximum)
    return result#출력값은 result에 담겨있음

print(maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))


#데큐는 pop(0)이 아니라 popleft가 존재한다.