#!/usr/bin/python3
"""module that defines canUnlockAll functionn"""
from collections import deque


def canUnlockAll(boxes):
    """this functions finds a key to unlock some boxes"""
    n = len(boxes)
    visited = [False] * n
    queue = deque([0])
    visited[0] = True
    unlocked_count = 1

    while queue:
        box_index = queue.popleft()

        for key in boxes[box_index]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)
                unlocked_count += 1

    return unlocked_count == n
