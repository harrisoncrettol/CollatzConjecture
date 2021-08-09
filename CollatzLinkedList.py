from math import log
from matplotlib import pyplot as plt

plt.figure(figsize=(8, 8))

class CollatzLinkedList:
    def __init__(self, num):
        self.num = num

    def generate_sequence(self, num) -> list:
        # returns [x, y] where x=length of sequence and y=sequence
        n = num
        stack = []
        
        while n != 1:

            # stack.append(n)     # represnt smaller numbers
            stack.append(log(n, 100))  # represent very large numbers

            if n % 2 != 0:
                n = n * 3 + 1
            else:
                n /= 2
        
        stack.append(n)
        x = list(range(len(stack)))
        return [x, stack]

    def show_sequence(self):
        x, y = self.generate_sequence(self.num)

        plt.title(str(self.num))
        plt.plot(x, y)
        plt.show()

    def show_sequences(self):
        for i in range(2, self.num + 1):
            x, y = self.generate_sequence(i)
            plt.plot(x, y)
            # plt.show()  # show one by one
        plt.show()     # show all at once


def main():
    c = CollatzLinkedList(100)
    x = c.show_sequences()


if __name__ == '__main__':
    main()
