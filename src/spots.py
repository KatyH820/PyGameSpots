# spots.py -model for the Spots game
import random
import math


class Spot:
    def __init__(self, center: (float, float), radius: float):
        self._center = center
        self._radius = radius
        # Choose a random number between -0.005 and 0.005
        self._delta_x = (random.random() * 0.01) - 0.005
        self._delta_y = (random.random() * 0.01) - 0.005

    def center(self) -> (float, float):
        return self._center

    def radius(self) -> float:
        return self._radius

    def move(self) -> None:
        x, y = self.center()
        self._center = (self._delta_x+x, self._delta_y+y)

    def contains(self, point: (float, float)) -> bool:
        px, py = point
        cx, cy = self.center()
        distance = math.sqrt((px-cx)**2 + (py-cy)**2)
        return distance <= self._radius


class SpotsState:
    def __init__(self) -> None:
        self._spots = []

    def all_spots(self) -> [Spot]:
        return self._spots

    def move_all_spots(self) -> None:
        for spot in self._spots:
            spot.move()

    def handle_action(self, action_point: (float, float)) -> None:
        for spot in reversed(self._spots):
            if spot.contains(action_point):
                self._spots.remove(spot)
                return

        radius = (random.random() * 0.06) + 0.01
        self._spots.append(Spot(action_point, radius))
