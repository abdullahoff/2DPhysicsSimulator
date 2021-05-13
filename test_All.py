## @file test_All.py
#  @author Abdullah Abdullah
#  @brief Tests CircleT.py, TriangleT.py, BodyT.py and Scene.py
#  @date 02/16/2021
#  @details 


'''
import pytest
from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import *
from Scene import Scene
import math

g = 9.81  # accel due to gravity (m/s^2)
n = 1  # mass (kg)


def Fx(t):
    return 5 if t < 5 else 0


def Fy(t):
    return -g * n if t < 3 else g * n

def Fx1(t):
    return 5 if t < 6 else 0


def Fy1(t):
    return -g * n if t < 4 else g * n

def Fx2(t):
    return 0

def Fy2(t):
    return -g * n

def vx(v, theta):
	return v * math.cos(theta)

def vy(v, theta):
	return v * math.sin(theta)

c = CircleT(1.0, 10.0, 0.5, 1.0)

t = TriangleT(1.0, 10.0, 0.5, 1.0)

x = [1.0, 2.0, 3.0]
y = [1.0, 2.0, 3.0]
m = [1.0, 2.0, 3.0]

b = BodyT(x, y, m)

Sc1 = Scene(c, Fx, Fy, 0, 0)
Sc2 = Scene(t, Fx2, Fy2, 0, 0)
Sc3 = Scene(c, Fx2, Fy2, vx(3, math.pi / 2), vy(3, math.pi / 2) )

def test_except_Cmass():
	with pytest.raises(ValueError):
		circle = CircleT(1.0, 10.0, 0.5, -1.0)

def test_except_Cradius():
	with pytest.raises(ValueError):
		circle = CircleT(1.0, 10.0, -0.5, 1.0)

def test_except_Cboth():
	with pytest.raises(ValueError):
		circle = CircleT(1.0, 10.0, -0.5, -1.0)

def test_Circle_cm_x():
	expected = 1.0
	assert c.cm_x() == expected

def test_Circle_cm_y():
	expected = 10.0
	assert c.cm_y() == expected

def test_Circle_mass():
	expected = 1.0
	assert c.mass() == expected

def test_Circle_m_inert():
	expected = ((1.0)*((0.5**2)))/2
	assert c.m_inert() == expected

def test_except_Tmass():
	with pytest.raises(ValueError):
		Triangle = TriangleT(1.0, 10.0, 0.5, -1.0)

def test_except_Tside():
	with pytest.raises(ValueError):
		Triangle = TriangleT(1.0, 10.0, -0.5, 1.0)

def test_TriangleT_cm_x():
	expected = 1.0
	assert t.cm_x() == expected

def test_TriangleT_cm_y():
	expected = 10.0
	assert t.cm_y() == expected

def test_TriangleT_mass():
	expected = 1.0
	assert t.mass() == expected

def test_m_inert():
	expected = (1.0*((0.5)**2))/2
	assert t.m_inert() == expected

def test_exception_Bmass():
	with pytest.raises(ValueError):
		body = BodyT([1, 1, 1], [1, 1, 1], [-1, 0, 1])

def test_exception_Bdiffsize():
	with pytest.raises(ValueError):
		body = BodyT([1, 1], [1, 1, 1], [1, 1, 1])

def test_sum():
	expected = 4
	assert sum([1,1,1,1]) == expected

def test_sum_neg():
	expected = 2
	assert sum([1,1,1,-1]) == expected

def test_sum_random():
	expected = 17
	assert sum([15, 1, 1]) == expected

def test_cm():
	expected = 1
	assert cm([1,1,1], [2,2,2]) == expected

def test_cm_random():
	expected = 2
	assert cm([1,2,3], [1,1,1]) == expected

def test_mmom():
	expected = 6
	assert mmom([1, 1, 1], [1,1,1], [1,1,1]) == expected

def test_cm_x_BodyT():
	expected = 14/6
	assert b.cm_x() == expected

def test_cm_y_BodyT():
	expected = 14/6
	assert b.cm_y() == expected

def test_mass_BodyT():
	expected = 6
	assert b.mass() == expected

def test_m_inert_BodyT():
	assert 6.6666666 < b.m_inert() <6.666667

def test_get_shape_circleScene():
	expected = [1.0, 10.0, 0.5, 1.0]
	assert Sc1.get_shape().cm_x() == expected[0] and Sc1.get_shape().cm_y() == expected[1] and Sc1.get_shape().r == expected[2] and Sc1.get_shape().mass() == expected[3]

def test_get_unbal_forces():
	assert Fx, Fy == Sc1.get_unbal_forces

def test_init_velo():
	assert (0,0) == Sc1.get_init_velo() 

def test_set_shape_cm_x():
	Sc1.set_shape(t)
	assert Sc1.get_shape().cm_x()  == t.cm_x()

def test_set_shape_cm_y():
	Sc1.set_shape(t)
	assert Sc1.get_shape().cm_y()  == t.cm_y()

def test_set_shape_mass():
	Sc1.set_shape(t)
	assert Sc1.get_shape().mass()  == t.mass()

def test_set_shape_m_inert():
	Sc1.set_shape(t)
	assert Sc1.get_shape().m_inert()  == t.m_inert()

def test_set_unbal_forces():
	Sc1.set_unbal_forces(Fx1, Fy1)
	assert Fx1, Fy1 == Sc1.get_unbal_forces

def test_set_init_velo():
	Sc1.set_init_velo(1, 1)
	assert (1,1) == Sc1.get_init_velo()

def test_sim_time():
	expectedt, expectedn = Sc1.sim(10, 100)
	assert [(i * 10 / (100 - 1)) for i in range(0, 100 - 1)]  == expectedt

def test_sim_wsol1():
	expectedt, expectedn = Sc1.sim(10, 100)
	pass

def test_sim_wsol2():
	expectedt, expectedn = Sc2.sim(10, 100)
	pass

def test_sim_wsol3():
	expectedt, expectedn = Sc3.sim(10, 100)
	pass





expectedt, expectedn = Sc1.sim(10, 100)
print(expectedn)'''

