from numpy import sqrt, inner

X=0
Y=1
Z=2

def absolute(vector):
    """
    Return the absolute of the given vector.
    """

    if len(vector) == 3:
        absolute = sqrt(pow(vector[X], 2) +
                        pow(vector[Y], 2) +
                        pow(vector[Z], 2) )
    elif len(vector) == 2:
        absolute = sqrt(pow(vector[X], 2) +
                        pow(vector[Y], 2) )
    return absolute

def versor(vector):
    """
    Return the versor of the given vector. That is a unit vector indicating the
    orientation of the original vector.

    versor = vector / |vector|
    """

    versor = vector / float(absolute(vector))
    return versor

def projection(u, v):
    """
    Return the projection of u upon v.
    """

    projection = ( inner(u,v) / float(inner(v,v)) ) * v
    return projection

def vector_by(origin, extremity):
    """
    Return a vector shaped by two given points.
    """

    vector = extremity - origin
    return vector

def future_intersection(vertex, particle):
    """
    Return the future point of intersection between a straight and a particle.
    """

    straight = vector_by(vertex[0],vertex[1])
    straight_particle = vector_by(vertex[0], particle)

    intersection_point = projection(straight_particle, straight) + vertex[0]
    return intersection_point

def distance(a, b):
    """
    Return distance between two points.
    """

    vector = vector_by(a,b)
    _distance = absolute(vector)
    return _distance

