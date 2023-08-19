class Square():

    def __init__(self, max):
        self.max = max

        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):

        if (self.number <= self.max):

            sonuc = self.number ** 2
            self.number += 1
            return sonuc
        else:
            self.number = 1
            raise StopIteration


square = Square(5)
for i in square:
    print(i)
