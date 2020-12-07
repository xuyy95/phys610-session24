import numpy as np
import matplotlib.pyplot as plt
from calculator import Cannonball


ball = Cannonball(planet='Earth', m=1.0, C=0.47, R=0.08, theta=30.0, v0=100)
x, y = ball.RK()

plt.plot(x, y)

plt.show()