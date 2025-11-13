class Environment:
    def __init__(self, width=7, height=7):
        self.width = width
        self.height = height
        # 0 = libre, 1 = obstáculo
        self.grid = [[0 for _ in range(height)] for _ in range(width)]

    def is_valid_position(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and not self.is_obstacle(x, y)

    def is_obstacle(self, x, y):
        return self.grid[x][y] == 1

    def toggle_obstacle(self, x, y):
        """Cambia entre celda libre y obstáculo"""
        if self.is_obstacle(x, y):
            self.grid[x][y] = 0
        else:
            self.grid[x][y] = 1
