# file classtools.py(new)
"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provides an inheritable display overload method that show instances with
    their class name and a name=value pair for each attribute stored on the
    instance itself(but not attributes inherited from its classes). Can be
    mixed into any class, and will work on any instances.
    """
    def getherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
            # above can alse be: (key, self.__dict__[key])
        return ', '.join(attrs)

    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.getherAttrs())

if __name__ == '__main__':
    class Toptest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = Toptest.count
            self.attr2 = Toptest.count + 1
            Toptest.count += 20

    class Subtest(Toptest):
        pass

    x, y = Toptest(), Subtest()
    print(x)
    print(y)

    
