import heapq


def is_solvable(state):
    inversion_count = 0
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                inversion_count += 1
    return inversion_count % 2 == 0


def manhattan_distance(current_state, goal_state):
    """
    A* heuristic function which calculates the manhattan distance
    """
    distance = 0
    for i in range(16):
        current_value = current_state[i]
        goal_value = goal_state[i]
        if current_value != 0 and current_value != goal_value:
            current_x, current_y = i % 4, i // 4
            goal_x, goal_y = (goal_state.index(current_value) % 4, goal_state.index(current_value) // 4)
            distance += abs(current_x - goal_x) + abs(current_y - goal_y)
    return distance


def solution(position):
    if not is_solvable(position):
        return "No solution found"
    # Define the goal state
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]
    # Define the possible moves for the blank tile
    moves = ["left", "right", "up", "down"]
    # Create a set to store the visited states
    visited = set()
    # Create a priority queue for the A* algorithm
    heap = []
    # Push the initial state onto the queue with a priority of 0
    heapq.heappush(heap, (0, position, [], 0))
    while heap:
        # Pop the state with the lowest priority
        priority, state, path, cost = heapq.heappop(heap)
        # If the state is the goal state, return the path
        if state == goal:
            return path
        # Mark the state as visited
        visited.add(tuple(state))
        # Find the location of the blank tile
        blank_tile = state.index(0)
        # Iterate through the possible moves
        for move in moves:
            # Make a copy of the current state
            new_state = state.copy()
            # Move the blank tile in the specified direction
            if move == "left" and blank_tile % 4 != 0:
                new_state[blank_tile], new_state[blank_tile-1] = new_state[blank_tile-1], new_state[blank_tile]
            elif move == "right" and blank_tile % 4 != 3:
                new_state[blank_tile], new_state[blank_tile+1] = new_state[blank_tile+1], new_state[blank_tile]
            elif move == "up" and blank_tile > 3:
                new_state[blank_tile], new_state[blank_tile-4] = new_state[blank_tile-4], new_state[blank_tile]
            elif move == "down" and blank_tile < 12:
                new_state[blank_tile], new_state[blank_tile+4] = new_state[blank_tile+4], new_state[blank_tile]
            else:
                continue
            # if state is not visited yet
            if tuple(new_state) not in visited:
                # Add the new state to the queue with the appropriate priority
                priority = cost + 1 + manhattan_distance(new_state, goal)
                heapq.heappush(heap, (priority, new_state, path + [move], cost + 1))


# Test

position = [1, 2, 3, 4, 6, 5, 7, 0, 9, 8, 11, 10, 13, 14, 15, 12]

print(solution(position)) 