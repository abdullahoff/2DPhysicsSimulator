## @file Scene.py
#  @author Abdullah Abdullah
#  @brief Creates a scene which a simulation can be done
#  @date 02/16/2021
#  @details extends the Shape interface and imports the Scipy library


from scipy.integrate import odeint
from Shape import Shape


## @brief Scene is responsible for simulating a scene for a specified shape
class Scene(Shape):

	## @brief constructor method for Scene
	#  @param s is the shape object ie TriangleT, CircleT or BodyT
	#  @param Fx is the unbalanced force in the x axis
	#  @param Fy is the unbalanced force in the y axis
	#  @param vx is the velocity in the x axis
	#  @param vy is the velovity in the y axis
	def __init__(self, s_, Fx_, Fy_, vx_, vy_):
		self.s = s_
		self.Fx = Fx_
		self.Fy = Fy_
		self.vx = vx_
		self.vy = vy_

	## @brief getter method for the shape of the object in the simulation
	#  @details indicates the shape along with the properties of the shape
	#  @return the shape object that is currently being passed into the simulation
	def get_shape(self):
		return self.s

	## @brief getter method for the unbalanced forces
	#  @details the unbalanced forces are functions with respect
	#  to time that are specified in the input
	#  @return Fx, Fy which are the function for the unbalanced forces on the shape
	def get_unbal_forces(self):
		return self.Fx, self.Fy

	## @brief getter method for the inital velocities in the x and y direction
	#  @return vx, vy are the inital velocities in the x and y axes
	def get_init_velo(self):
		return self.vx, self.vy

	## @brief setter method for the shape that is used in the scene class
	#  @details The shape can be changed to any interface that is a subclass of the Shape object
	#  @return none
	def set_shape(self, s_):
		self.s = s_

	## @brief setter method for the unbalanced forces of the shape
	#   being passed into scene
	#  @details the unbalanced forces are functions with respect to time
	#  that are specified in the input
	#  @return none
	def set_unbal_forces(self, Fx_, Fy_):
		self.Fx = Fx_
		self.Fy = Fy_

	## @brief setter method for the inital velocities for the x and y axes
	#  @return none
	def set_init_velo(self, vx_, vy_):
		self.vx = vx_
		self.vy = vy_

	## @brief Complies the simulation
	#  @param t_final is the final time at which the simulation ends
	#  @param nsteps is the amount of steps taken in the time
	#  @return time which is a sequence of times of corresponding data points
	#  @return arr which is a nested sequence that contains x and y
	#   points for corresponding times
	def sim(self, t_final, nsteps):

		def ode(w, t):
			return [w[2], w[3], self.Fx(t) / self.s.mass(), self.Fy(t) / self.s.mass()]
		time = [(i * t_final / (nsteps - 1)) for i in range(0, nsteps - 1)]
		tao = [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy]
		arr = odeint(ode, tao, time)
		return time, arr
