from car import Car
import random


class UnreliableCar(Car):
    """A Car that might not always drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if it's reliable."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
