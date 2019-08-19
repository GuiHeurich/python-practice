from timer_duplicates import ranges, times
from pylab import *

def main():
    x = ranges()
    y = times()

    plot(x, y, color="blue", label="find_duplicate()")

    title('Algorithmic Complexity: timing find_duplicate')
    xlabel('range')
    ylabel('time')
    legend(loc=2)
    grid(True)

    savefig("./graphs/find_duplicate.png")

if __name__ = '__main__':
    main()
