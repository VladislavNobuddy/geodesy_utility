from math import degrees, radians
import math

from numpy.ma.core import arctan, arcsin, sin, sqrt, cos


def to_get_result(x1, y1, x2, y2, gamma, an, bn):
    # print(y2, y1, x2, x1)
    # print(an, bn, gamma)

    alpha_ab = degrees(arctan((y2 - y1) / (x2 - x1)))
    alpha_ba = 180.00 + alpha_ab

    # print(alpha_ab)
    # print(alpha_ba)

    tau = sqrt((x2-x1)**2 + (y2-y1)**2)

    # print("\n")
    # print(bn * sin(gamma))
    # print("\n")
    # print(bn)
    # print(tau)
    # print((bn * sin(gamma)) / tau)

    sigma = degrees(arcsin((bn * sin(radians(gamma)))/tau))

    #print(sigma)

    psi = degrees(arcsin((an * sin(radians(gamma)))/tau))

    print(sigma, psi)

    control = sigma + psi + gamma

    print(control)

    temp = control - 180
    print(temp, temp/3)
    if temp > 0:
        temp = abs(temp)
        sigma = sigma - temp/3
        psi = psi - temp/3

    elif temp < 0:
        temp = abs(temp)
        sigma = sigma + temp/3
        psi = psi + temp/3

    else:
        pass
    
    print(sigma, psi)

    alpha_an = alpha_ab + sigma
    alpha_bn = alpha_ba - psi

    print(alpha_ab, sigma)
    print(alpha_ba, psi)

    x1n = x1 - (an*cos(radians(180 - alpha_an)))
    x2n = x2 - (bn*sin(radians(alpha_bn - 90)))

    y1n = y1 + (an*sin(radians(180 - alpha_an)))
    y2n = y2 + (bn*cos(radians(alpha_bn - 90)))

    xn = (x1n+x2n)/2
    yn = (y1n+y2n)/2

    return round(xn, 2), round(yn, 2)