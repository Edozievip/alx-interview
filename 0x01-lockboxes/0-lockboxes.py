def canUnlockAll(boxes):
    visited = [False] * len(boxes)  # Keep track of visited boxes
    visited[0] = True  # The first box is unlocked initially
    stack = [0]  # Start DFS with the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    # If all boxes are visited, return True. Otherwise, return False.
    return all(visited)

