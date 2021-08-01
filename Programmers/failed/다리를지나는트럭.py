from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    passed_bridge = []
    passing_bridge = deque([0 for _ in range(bridge_length)])
    tmp = [0 for _ in range(bridge_length)]
    wait_bridge = truck_weights

    while sum(passing_bridge) == 0:

        wait_truck = wait_bridge[0]
        print("대기 중인 트럭: ", wait_truck)

        if sum(passing_bridge) + wait_truck < weight:
            passing_bridge.append(wait_truck)
            wait_bridge.pop(0)

        else:
            first = passing_bridge.popleft()
            if first == 0:
                passing_bridge.append(first)
            else:
                passed_bridge.append(first)

        print("다리를 지난 트럭: ", passed_bridge)
        print("다리를 지나는 트럭: ", passing_bridge)
        print("대기 트럭: ", wait_bridge)
        print()
        print("tmp = ", tmp)
        answer += 1

    return answer


bridge_length = 100
weight = 100
truck_weights = [10]
s = solution(bridge_length, weight, truck_weights)
print(s)