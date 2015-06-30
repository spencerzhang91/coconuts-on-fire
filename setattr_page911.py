class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value + 10
            #self.age = value + 10  //causes infinite loop
            #object.__setattr__(self, attr, value + 10)  //a new style way
        else:
            raise AttributeError(attr + ' not allowed')

    def __repr__(self):
        return str(self.value)

if __name__ == '__main__':
    
    x = Accesscontrol()
    x.age = 40
    print(x.age)
