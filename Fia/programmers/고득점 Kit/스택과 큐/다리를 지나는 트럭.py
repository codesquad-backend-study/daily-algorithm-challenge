import collections


def solution(bridge_length, weight, truck_weights):
    bridge_current_state = collections.deque([0 for _ in range(bridge_length)]);
    waiting_trucks = collections.deque(truck_weights)

    total_weight_on_bridge = 0
    answer = 0

    while waiting_trucks:
        total_weight_on_bridge -= bridge_current_state.popleft()

        if total_weight_on_bridge + waiting_trucks[0] <= weight:
            truck = waiting_trucks.popleft()
            bridge_current_state.append(truck)
            total_weight_on_bridge += truck
        else:
            bridge_current_state.append(0)

        answer += 1

    answer += bridge_length

    return answer
