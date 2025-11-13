class Robot:
    def __init__(self, robot_id, position=(0, 0), capacity=1):
        self.id = robot_id
        self.position = position
        self.capacity = capacity
        self.carrying = []

    def move(self, direction):
        x, y = self.position
        moves = {
            "up": (x, y - 1),
            "down": (x, y + 1),
            "left": (x - 1, y),
            "right": (x + 1, y)
        }

        if direction not in moves:
            return False

        self.position = moves[direction]
        return True

    def pickup(self, package):
        if len(self.carrying) < self.capacity:
            self.carrying.append(package)
            return True
        return False

    def drop(self, package):
        if package in self.carrying:
            self.carrying.remove(package)
            return True
        return False
