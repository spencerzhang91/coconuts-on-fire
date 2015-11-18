class Life:
    def __init__(self, name):
        print('Hello, %s' % name)
        self.name = name
    def live(self):
        print(self.name)

    def __del__(self):
        print('Goodbye, %s' % self.name)

if __name__ == "__main__":
    brain = Life('Brain')
    brain.live()
    brain = 'lorrita'
    sue = Life('Sue')
    
