# This is an example of applying the notion of inheritance
class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)
        self.reader.close()
        self.writer.close()

    def converter(self, data):
        assert False, 'converter must be defined'


class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

class HTMLize:
    def write(self, line):
        print('<p>%s</p>' % line.rstrip())


if __name__ == '__main__':
    import sys
    obj = Uppercase(open('sometext.txt'), open('output.txt', 'w'))
    obj.process()
    
