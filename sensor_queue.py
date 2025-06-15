class SensorQueue():
    def __init__(self):
        self.items = []
    
    def push(self, item):
        if item in self.items:
            return
        self.items.insert(0, item)
    
    def pop(self):
        if len(self.items) != 0:
            return self.items.pop()
        return None
    
    def has(self, item):
        if item in self.items:
            return True
        return False
    
    def peek(self):
        if len(self.items) != 0:
            return self.items[-1]
        return None
    
    def remove(self, item):
        if item in self.items: 
            self.items.remove(item)