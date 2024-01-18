import math

class Trap:
    Ax: 0
    Ay: 0
    Bx: 0
    By: 0
    Cx: 0
    Cy: 0
    Dx: 0
    Dy: 0

    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.Ax = ax
        self.Ay = ay
        self.Bx = bx
        self.By = by
        self.Cx = cx
        self.Cy = cy
        self.Dx = dx
        self.Dy = dy

    def AB(self):
        return math.sqrt((self.Bx - self.Ax) **2 + (self.By - self.Ay) ** 2)

    def BC(self):
        return math.sqrt((self.Bx - self.Cx) **2 + (self.By - self.Cy) ** 2)

    def CD(self):
        return math.sqrt((self.Cx - self.Dx) **2 + (self.Cy - self.Dy) ** 2)

    def AD(self):
        return math.sqrt((self.Ax - self.Dx) ** 2 + (self.Ay - self.Dy) ** 2)

    def check(self):
        return self.AB == self.CD

    def Perimetr(self):
        return self.AB() + self.BC() + self.CD() + self.AD()

    def Height(self):
        '''
        x = (self.AD() - self.BC()) / 2
        AH = math.sqrt((self.AB()) ** 2 + x ** 2)
        return AH
        '''
        a = self.AD()
        b = self.BC()
        c = self.AB()
        d = self.CD()

        h = math.sqrt(c ** 2 - (((a - b) ** 2 + c ** 2 - d ** 2) / (2 * (a - b))) ** 2)
        return h

    def Square(self):
        return ((self.AD() + self.BC()) / 2) * self.Height()


A = []
N = int(input('введите количество трапеций: '))
avg = 0

for i in range(N):
    A.append(Trap(5, 1, 2, 2, 3, 6, 4 + i, 9))

for i in range(N):
    avg += A[i].Square()
    print(i + 1, A[i].Square())

avg = avg / N
print('avg', avg)

for i in range(N):
    if A[i].Square() > avg:
        print(A[i].Square())

