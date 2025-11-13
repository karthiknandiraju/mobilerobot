import time
import pygame

class PlanExecutor:
    def __init__(self, environment, robots, packages, gui=None):
        self.env = environment
        self.robots = {r.id: r for r in robots}
        self.packages = {p.id: p for p in packages}
        self.gui = gui  # reference to pygame (optional)

    def execute_action(self, action_name, params):
        try:
            if action_name == "move":
                robot_id, from_zone, to_zone = params
                robot = self.robots[robot_id]
                fx, fy = self._parse_zone(from_zone)
                tx, ty = self._parse_zone(to_zone)
                direction = self._get_direction((fx, fy), (tx, ty))
                robot.move(direction)
                return True

            elif action_name == "pickup":
                robot_id, pkg_id, location = params
                robot = self.robots[robot_id]
                pkg = self.packages[pkg_id]
                robot.pickup(pkg)
                pkg.is_carried = True
                pkg.carrier_id = robot_id
                return True

            elif action_name == "drop":
                robot_id, pkg_id, location = params
                robot = self.robots[robot_id]
                pkg = self.packages[pkg_id]
                robot.drop(pkg)
                pkg.is_carried = False
                pkg.position = robot.position
                return True

        except Exception as e:
            print(f"Error executing action {action_name}: {e}")
            return False

    def _parse_zone(self, name):
        parts = name.split("_")
        return int(parts[1]), int(parts[2])

    def _get_direction(self, from_pos, to_pos):
        fx, fy = from_pos
        tx, ty = to_pos
        if tx > fx:
            return "right"
        elif tx < fx:
            return "left"
        elif ty > fy:
            return "down"
        elif ty < fy:
            return "up"

    def execute_plan(self, plan_file="plan.txt"):
        try:
            with open(plan_file) as f:
                lines = [l.strip().strip("()") for l in f if l.strip() and not l.startswith(";")]
        except FileNotFoundError:
            print("File not found plan.txt")
            return

        print("Executing plan...")
        for line in lines:
            parts = line.split()
            action, params = parts[0], parts[1:]
            print(f"→ {action} {' '.join(params)}")

            # Executing action
            self.execute_action(action, params)

            # Redrawing GUI
            if self.gui:
                self.gui.draw()

            # Small pause between actions
            time.sleep(0.7)

        print("Plan executed completely.")

