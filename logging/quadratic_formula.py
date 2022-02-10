"""Quadratic formula"""

import math
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= "./logging/quad_formula.log", level= logging.DEBUG, format= LOG_FORMAT, filemode= 'w')

logger = logging.getLogger()

def quadratic_formula(a, b, c):
    """Returns sol to the equation ax^2 + bx + c =0"""
    logger.info(f"Quadratic formal for {a}, {b} and {c}")

    #compute the discriminant
    logger.debug("#Compute the discriminant")
    disc = b**2 - 4*a*c
    print(disc)

    #compute two roots
    logger.debug("#compute two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    #return the roots
    logger.debug("#Return the roots")
    return (root1, root2)

print(quadratic_formula(1, 0 , -4))