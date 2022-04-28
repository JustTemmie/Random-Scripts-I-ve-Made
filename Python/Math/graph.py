from pylab import *
import random

matplotlib.use("Qt5Agg")

# https://coolors.co/palette/ff0000-ff8700-ffd300-deff0a-a1ff0a-0aff99-0aefff-147df5-580aff-be0aff
colours = ["#FF0000", "#FF8700", "#FFD300", "#DEFF0A", "#A1FF0A",
           "#0AFF99", "#0AEFFF", "#147DF5", "#580AFF", "#BE0AFF"]

def f(x):
    return x**1.1

def rand():
    return random.randrange(0,200)

fig, ax = plt.subplots(figsize=(10, 8))

xlabel("x")
ylabel("y")
ax.set_xlim(0, 200)
ax.set_ylim(0, 200)
grid()

for x in range(0, len(colours)):
    x_verdier = linspace(-200, 200, 100)
    y_verdier = f(x_verdier)
    axhline(y=0, color="000000")
    axvline(x=0, color="000000")
    plot(x_verdier, y_verdier, color=colours[x])
    
show()