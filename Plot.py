## @file Plot.py
#  @author Abdullah Abdullah
#  @brief Contains a small function which plots the motion of a shape
#  @date 02/19/2021
#  @details Imports matplotlib to plot the motion of a shape
import matplotlib.pyplot as plt


## @brief plots the values of the motion in 3 different graphs
#  @details The following method plots 3 graphs which are x vs t, y vs t and x vs y.
#  @return No return type
def plot(wsol, t):

	mon = [(wsol[i][0]) for i in range(len(wsol))]
	con = [(wsol[i][1]) for i in range(len(wsol))]

	plt.subplot(3, 1, 3)
	plt.plot(mon, con)
	plt.ylabel("y(m)")
	plt.xlabel("x(m)")

	plt.subplot(3, 1, 1)
	plt.plot(t, mon)
	plt.ylabel("x(m)")

	plt.subplot(3, 1, 2)
	plt.plot(t, con)
	plt.ylabel("y(m)")

	plt.show()

