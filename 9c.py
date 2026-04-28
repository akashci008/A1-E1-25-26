grid_size = 4

agent = [0, 0]
goal = [3, 3]
pit = [1, 2]

def move(direction):
    if direction == "UP" and agent[0] > 0:
        agent[0] -= 1
    elif direction == "DOWN" and agent[0] < grid_size - 1:
        agent[0] += 1
    elif direction == "LEFT" and agent[1] > 0:
        agent[1] -= 1
    elif direction == "RIGHT" and agent[1] < grid_size - 1:
        agent[1] += 1
    else:
        print("Invalid move!")

while True:
    print("\nAgent position:", agent)

    if agent == goal:
        print("Reached Goal!")
        break
    elif agent == pit:
        print("Fell into Pit!")
        break

    direction = input("Enter move (UP/DOWN/LEFT/RIGHT): ").upper()
    move(direction)