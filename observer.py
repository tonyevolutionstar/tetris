class Observer:
    def on_notify(self, entity, event):
        print("Entity: ", entity , event)

class Subject(Observer):
    def __init__(self):
        self.observers = []
    def add_observer(self, obs: Observer):
        self.observers.append(obs)
    
    def notify(self, entity, event):
        for obs in self.observers:
            obs.on_notify(entity, event)