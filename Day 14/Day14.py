class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        for i in self.__elements:
            for j in self.__elements:
                
                d = abs(i - j)
                
                if d > self.maximumDifference:
                    self.maximumDifference = d

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)