

class Task:

    def __init__(self, description):
        self.description = description
        self.completed = False
    
    def complete(self):
        self.completed = True
        
    def isCompleted(self):
        return self.completed
        
    def taskDescription(self):
        return self.description