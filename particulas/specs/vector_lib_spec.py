import unittest
from should_dsl import *

from numpy import array, allclose

from vector_lib import *

X=0
Y=1
Z=2

@matcher
def be_an_array_like():
    from numpy import allclose
    return (allclose, "%s is %san array like %s")

class VectorLibSpec(unittest.TestCase):

    def it_should_return_the_absolute_value_of_a_vector(self):
        vector = array([2, 1, -2])
        absolute(vector) |should| equal_to(3)

        vector = array([-3, 4])
        absolute(vector) |should| equal_to(5)

    def it_should_return_the_versor_of_a_vector(self):
        vector = array([2, 1, -2])
        _versor = versor(vector)
        _versor[X] |should| equal_to(2/3.0)
        _versor[Y] |should| equal_to(1/3.0)
        _versor[Z] |should| equal_to(-2/3.0)

    def it_should_return_the_projection_of_u_upon_v(self):
        u = array([2,3,4])
        v = array([1,-1,0])
        _projection = projection(u,v)
        _projection[X] |should| equal_to(-1/2.0)
        _projection[Y] |should| equal_to(1/2.0)
        _projection[Z] |should| equal_to(0)

    def it_should_return_a_vector_define_by_two_points(self):
        a = array([-2,3,1])
        b = array([1,4,6])
        allclose(vector_by(a,b), array([3,1,5])) |should| be(True)
        allclose(vector_by(b,a), array([-3,-1,-5])) |should| be(True)

    def should_return_the_future_point_of_intersection_between_a_straight_and_a_particle(self):
        a = array([1,2,-1])
        b = array([-1,0,-1])
        c = array([2,1,2])
        vertex = [b,c]
        f = future_intersection(vertex, a)
        allclose(f, array([5/19.0, 8/19.0, 5/19.0])) |should| equal_to(True)

    def should_return_the_distance_between_tow_points(self):
        a = array([4,1,1])
        b = array([2,0,3])
        distance(a,b) |should| equal_to(3)
        distance(b,a) |should| equal_to(3)

