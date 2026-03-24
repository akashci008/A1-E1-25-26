import heapq

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

class Puzzle:
    def __init__(self, board, g=0, parent=None, move="Start"):
        self.board = board
        self.g = g
        self.h = self.heuristic()
        self.f = self.g + self.h
        self.parent = parent
        self.move = move

    def heuristic(self):
        dist = 0
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val != 0:
                    x = (val-1)//3
                    y = (val-1)%3
                    dist += abs(i-x) + abs(j-y)
        return dist

    def is_goal(self):
        return self.board == GOAL

    def get_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def generate(self):
        children = []
        x, y = self.get_blank()
        moves = [(-1,0,"Up"),(1,0,"Down"),(0,-1,"Left"),(0,1,"Right")]

        for dx, dy, m in moves:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                new = [row[:] for row in self.board]
                new[x][y], new[nx][ny] = new[nx][ny], new[x][y]
                children.append(Puzzle(new, self.g+1, self, m))
        return children

    def __lt__(self, other):
        return self.f < other.f


def print_board(b):
    for row in b:
        print(row)
    print()


def print_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    path.reverse()

    for i, p in enumerate(path):
        print(f"Move {i}: {p.move}")
        print_board(p.board)


def A_star(start):
    open_list = []
    visited = set()

    heapq.heappush(open_list, Puzzle(start))

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            print("Solution Found:\n")
            print_path(current)
            return

        visited.add(str(current.board))

        for child in current.generate():
            if str(child.board) not in visited:
                heapq.heappush(open_list, child)

    print("No solution")

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

print("Initial State:")
print_board(start)

A_star(start)