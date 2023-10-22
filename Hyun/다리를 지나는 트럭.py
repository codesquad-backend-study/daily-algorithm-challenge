import collections


def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    time = 0
    current_weight = 0

    bridge = collections.deque([0] * bridge_length)

    while truck_weights:
        time += 1

        current_weight -= bridge.popleft()

        if truck_weights and truck_weights[-1] + current_weight > weight:
            bridge.append(0)
        else:
            current_weight += truck_weights[-1]
            bridge.append(truck_weights.pop())

    return time + bridge_length
