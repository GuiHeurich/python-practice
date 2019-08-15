from timer_last import ranges, times
from timer_reverse import reverse_times
from timer_shuffle import shuffle_times
from pylab import *

x = ranges()
last_times = times()
reverse_times = reverse_times()
shuffle_times = shuffle_times()

plot(x, last_times, color="blue", label="last()")
plot(x, reverse_times, color="red", label="reverse()")
plot(x, shuffle_times, color="green", label="shuffle()")

title('Algorithmic Complexity: timing last, reverse, shuffle')
xlabel('range')
ylabel('time')
legend(loc=2)
grid(True)

savefig("./graphs/last_reverse_shuffle(after_refactoring).png")
