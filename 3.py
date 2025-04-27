print("Попов Олег Михайлович 09.03.01ПОВа-o24")

import time
from collections import deque

def solve_with_array(A):
    n = len(A)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and A[i] > A[stack[-1]]:
            idx = stack.pop()
            result[idx] = A[i]
        stack.append(i)
    return result

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        return None

    def is_empty(self):
        return self.top is None

def solve_with_linked_list(A):
    n = len(A)
    result = [0] * n
    stack = LinkedListStack()
    for i in range(n):
        while not stack.is_empty() and A[i] > A[stack.top.value]:
            idx = stack.pop()
            result[idx] = A[i]
        stack.push(i)
    return result

def solve_with_deque(A):
    n = len(A)
    result = [0] * n
    stack = deque()
    for i in range(n):
        while stack and A[i] > A[stack[-1]]:
            idx = stack.pop()
            result[idx] = A[i]
        stack.append(i)
    return result

if __name__ == "__main__":
    A = [1, 3, 2, 5, 3, 4]
    print("\nИсходный массив:")
    print(A)

    start_time = time.time()
    result_array = solve_with_array(A)
    time_array = time.time() - start_time

    start_time = time.time()
    result_linked_list = solve_with_linked_list(A)
    time_linked_list = time.time() - start_time

    start_time = time.time()
    result_deque = solve_with_deque(A)
    time_deque = time.time() - start_time

    print("\nРезультат через массив:")
    print(result_array)
    print(f"Время выполнения: {time_array:.6f} секунд")

    print("\nРезультат через связанный список:")
    print(result_linked_list)
    print(f"Время выполнения: {time_linked_list:.6f} секунд")

    print("\nРезультат через deque:")
    print(result_deque)
    print(f"Время выполнения: {time_deque:.6f} секунд")

    assert result_array == result_linked_list == result_deque, "Результаты не совпадают!"
    print("\nВсе реализации дают одинаковый результат.")
