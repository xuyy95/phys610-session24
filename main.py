import numpy as np
import matplotlib.pyplot as plt
from calculator import Cannonball


# plot setup
plt.rc('font',**{'family':'sans-serif','sans-serif':['DejaVu Sans']}) # sans-serif
plt.rc('mathtext',**{'default':'regular'})
plt.rc('xtick', labelsize=12, direction='in')
plt.rc('ytick', labelsize=12, direction='in')
plt.rc('axes', labelsize=14)

plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams['axes.linewidth'] = 1
plt.rcParams['xtick.major.width'] = 1
plt.rcParams['xtick.major.size'] = 6
plt.rcParams['ytick.major.width'] = 1
plt.rcParams['ytick.major.size'] = 6


# part a
if False:
	fig, ax = plt.subplots(figsize=(6,4.5))

	planet = 'Mars'

	for m in [0.25,0.5,1,2,4]:
		ball = Cannonball(planet=planet, m=m, C=0.47, R=0.08, theta=30.0, v0=100)
		x, y = ball.RK()
		ax.plot(x, y, label='m = '+str(m)+' kg')
		ax.set_xlabel("x [m]")
		ax.set_ylabel('y [m]')
		ax.legend(loc='upper left', frameon=False, prop={'size':12})

	plt.savefig('../plot/{0}_part_a.pdf'.format(planet), transparent=True)
	plt.show()


# part b
if False:
	ball = Cannonball(planet='Mars', m=1, C=0.47, R=0.08, theta=30.0, v0=100)
	x, y = ball.RK()
	print(x[-1])


# part c
xmax = 0
v1 = 0
v2 = 2000
if True:
	while not(xmax > 600000 and xmax < 601000):
		v0 = (v1 + v2)/2
		print('velocity = {0:.2f}'.format(v0))
		ball = Cannonball(planet='Mars', m=1, C=0.47, R=0, theta=30, v0=v0)
		x, y = ball.RK()
		xmax = x[-1]
		print('xmax = {0:.2f}'.format(xmax))
		if xmax < 600000:
			v1 = v0
		else:
			v2 = v0
print(np.max(y))
