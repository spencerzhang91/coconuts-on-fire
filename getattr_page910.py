class Empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)


if __name__ == '__main__':
    x = Empty()
    print(x.age)
    print(x.name)
