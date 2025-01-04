# Violation of ISP
class Worker:
    def work(self):
        pass

    def manage(self):
        pass

class Developer(Worker):
    def work(self):
        # coding work
        pass

    def manage(self):
        raise NotImplementedError("Developers don't manage")  # Violates ISP

# Following ISP
class Workable:
    def work(self):
        pass

class Manageable:
    def manage(self):
        pass

class Developer(Workable):
    def work(self):
        # coding work
        pass

class Manager(Workable, Manageable):
    def work(self):
        # management work
        pass

    def manage(self):
        # manage team
        pass
