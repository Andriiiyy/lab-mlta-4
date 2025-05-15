from  math import inf
from typing import List, Tuple

def kangaro(n_pods: int, step_size: list[int]) -> int:
    memory: dict[int, int] = {0: 1}
    for i in range(1, n_pods + 1):
        memory[i] = 0
        for step in step_size:
            problem: int = i - step
            if problem < 0:
                continue

            memory[i] += memory[problem]

    return memory[n_pods]



def max_sand_value(n: int, piles: List[Tuple[int, int]]) -> float:
    # Sort piles by value per kg in descending order (greedy strategy)
    piles.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0.0
    remaining_capacity = n
    
    for weight, value in piles:
        if remaining_capacity == 0:
            break
        # Take as much as possible from the current pile
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            # Take a fraction if not enough capacity remains
            total_value += value * (remaining_capacity / weight)
            remaining_capacity = 0
    return total_value
