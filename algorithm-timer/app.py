import flask
from flask import Response
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.patches as mpatches
from plot import main
from timer_last import ranges, times
from timer_reverse import reverse_times
from timer_shuffle import shuffle_times
from timer_duplicates import times as duplicate_times

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return '''<center><h1>Algorithmic Timer</h1><br><br><a href='/functions'>Graph for last(), reverse(), shuffle(), and find_duplicate()</a></center>'''

@app.route('/functions', methods=['GET'])
def image():
    return '''<img src="/functions.png" alt="my plot">'''

@app.route('/functions.png')
def plot():
    fig = plot_functions()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def plot_functions():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    x = ranges()
    last = times()
    reverse = reverse_times()
    shuffle = shuffle_times()
    duplicate = duplicate_times()

    axis.plot(x, last, color="blue", label="last()")
    axis.plot(x, reverse, color="red", label="reverse()")
    axis.plot(x, shuffle, color="green", label="shuffle()")
    axis.plot(x, duplicate, color="yellow", label="find_duplicate()")

    axis.set_title('Algorithmic Complexity: timing last')
    axis.set_xlabel('Ranges in number of elements')
    axis.set_ylabel('Time in seconds')

    last_patch = mpatches.Patch(color='blue', label='last()')
    reverse_patch = mpatches.Patch(color='red', label='reverse()')
    shuffle_patch = mpatches.Patch(color='green', label='shuffle()')
    duplicate_patch = mpatches.Patch(color='yellow', label='find_duplicate()')
    axis.legend(handles=[last_patch, reverse_patch, shuffle_patch, duplicate_patch])
    return fig

app.run()
