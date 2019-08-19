# Algorithm Timer

Times the execution of the following bespoke python methods:

1. last()
2. reverse()
3. shuffle()
4. find_duplicate()

## How to use

Clone this repo. Make sure you have python3 installed.

To run timers for each function on the command line, type:

```
import timer_<function>
python3 timer_<function>.py
```

It will print the name of the function and run a timer for each range. The ranges start as a list of 10000 elements and increase by 5000 for each run.

To plot a graph for last, reverse, and shuffle, type:

```
python3 plot.py
```

To plot a graph for find_duplicate, type:

```
python3 plot_duplicate.py
```

Each of these will save a new PNG file inside the graphs folder.

They should look something like this:

[](<./graphs/last_reverse_shuffle(after_refactoring).png>)
[](<./graphs/find_duplicate(second_attempt).png>)

_The reason the plots are separated is because, at the moment, find_duplicate() takes much longer (it's quadratic) than the other three functions, which are all constant time._

If you have patience to wait, you can see them also together by running `python3 app.py` and opening your browser on `localhost:5000`. _It will take about three minutes to load...sorry [working on it]_
