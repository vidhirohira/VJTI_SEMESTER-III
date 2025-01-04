# Violation of LSP
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        # Sparrow flying logic
        pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguins can't fly")  # Violates LSP

# Following LSP
class Bird:
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        # logic for flying
        pass

class Penguin(Bird):
    def move(self):
        # logic for swimming
        pass
