# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 15:35:03 2023

@author: austi
"""

import numpy as np

def point(a, b):
    return np.array((a, b))

def modgroup(a, n):
    # creates cyclic group of a % mod
    i = 0
    group = []
    m = 0
    i = 0
    while True:
        val = (a*m)%n
        if i >= 1 and val == 0:
            break
        group.append(val)
        i+= 1
        m+= 1
    return group

def modinverse(a, n, r = 1):
    # finds the inverse an integer a mod n
    # uses the index (integer) of the cyclic group that 
    # produces a value of 1 as that corresponds to 
    # a*a_inverse mod n = 1
    inv = 0
    group = modgroup(a, n)
    for k, val in enumerate(group):
        if val == 1:
            inv = k
            break
        else:
            # inv = "no inv for a:{}, n:{}".format(a, n)
            inv = 'none'
    # print("inv: {}".format(inv))
    return inv

def slope(n, P, Q):
    # n: modulus 

    A = -7
    xp, yp = P
    xq, yq = Q
    if xp == xq and yp != yq or xp != xq and yp == yq:
        m = "none"
        inv = 'none'
        # print('1st if')
    elif xp == xq and yp == yq:
        # print('2nd if')
        inv = modinverse(2*yp, n)
        if inv == 'none':
            m = 'none'
        else:
            m = (3*xp**2+A)*inv
            m = m%n
           
    else:
        # print('else')
        inv = modinverse(xq-xp, n)
        if inv == 'none':
            m = 'none'
        else:
            m = (yq-yp)*inv
            m = m%n
    # print("m: {}, inv: {}".format(m, inv))
    return m

# P = point(1, 2)
P = point(2, 2)
n = 19
mult = 10
def nP(mult, P, n):
    # n = modulus
    # mult = multiplier (nP)
    # P = a tuple representing a point: (a, b)
    i = 2
    j = 0
    pts = [P]
    
    stop = False
    while stop == False: #i <= mult:
        # print('i:{}'.format(i))
        # print(pts[-1])  
        if i%2 == 0:
            # if we are multiplying by an even number, we will add the same p
            k = int(i/2) - 1# if even, we use half and add. EX 6P = 3P + 3P
            # print("i:{}, k: {}".format(i, k))
            # print(pts[k])
            m = slope(n, pts[k], pts[k])
            if m == 'none':
                neg_R = np.array((float('inf'), float('inf')))
                stop = True
            else:
                xp, yp = pts[k]
                # xq, yq = pts[k]
                xr = (m**2 - 2*xp)%n
                # print('m: {}, xr: {}, xp: {}'.format(m, xr, xp))
                yr = (yp + m*(xr-xp))%n
                neg_R = np.array((xr, (-1*yr)%n))
            
            
        if i%2 == 1:
            m = slope(n, P, pts[j])
            if m == 'none':
                neg_R = np.array((float('inf'), float('inf')))
                stop = True
            else:
                xp, yp = P
                xq, yq = pts[j]
                xr = (m**2 - xp - xq)%n
                yr = (yp + m*(xr-xp))%n
                neg_R = np.array((xr, (-1*yr)%n))
        pts.append((neg_R))
        j += 1
        i += 1
        
    points = np.array(pts)
    return points

points = nP(mult, P, n)

print(points)
Q_check = point(16, 2)
for i, val in enumerate(points):
    xq, yq = Q_check
    x, y = val
    if x == xq and y == yq:
        print("multiple: {}".format(i+1))

        
        
        
        
        
        
        
        
        
        
        