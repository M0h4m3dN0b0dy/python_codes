from doc import Doc
from triangulation import Triangulation
from site_ import Site
from codage_site import Codage_site
from general import *
import math
import copy
# 1: 34077294
"""
a.ajoute_sommet([675, 340], 1, 50) # c
a.ajoute_sommet([715, 0], 2, 22)   # m7
a.ajoute_sommet([425, 240], 2, 20) # n1
a.ajoute_sommet([715, 241], 2, 21) # n7
a.ajoute_sommet([890, 189], 1, 52) # m6
a.ajoute_sommet([802, 290], 1, 51) # n6
a.ajoute_sommet([980, 381], 3, 32) # m4, m5



a.ajoute_sommet([797, 380], 3, 31) # n5
a.ajoute_sommet([797, 515], 3, 30) # n4
a.ajoute_sommet([540, 522], 3, 29) # n3
a.ajoute_sommet([520, 450], 1, 49) # n2
a.ajoute_sommet([540, 705], 3, 28) # m3
a.ajoute_sommet([435, 670], 1, 48) # m1, m2
"""
"""
a.ajoute_sommet([715, 0], 2, 22)   # m7
a.ajoute_sommet([425, 240], 2, 20) # n1
a.ajoute_sommet([775, 341], 2, 21) # n7
a.ajoute_sommet([675, 340], 1, 50) # c

#a.ajoute_sommet([890, 189], 1, 52) # m6
#a.ajoute_sommet([802, 290], 1, 51) # n6
a.ajoute_sommet([580, 551], 3, 35) # m4, m5
a.ajoute_sommet([980, 681], 3, 32) # m4, m5
"""
""""


#print (angle([890, 189], [900, 189], [715,0 ], no_inv=False))
"""
"""
import sys
sys.exit()


a.ajoute_sommet([291, 24], 1, 50)   # m7
a.ajoute_sommet([447, 18], 1, 51) # n1
a.ajoute_sommet([378.5, 81], 1, 52) # n7
a.ajoute_sommet([282, 108], 1, 53) # m6
a.ajoute_sommet([235, 142.5], 1, 54) # n6
a.ajoute_sommet([451, 101], 2, 32) # m4, m5

a.ajoute_sommet([376, 145], 2, 33) # c

a.ajoute_sommet([289, 170], 2, 34) # n5
a.ajoute_sommet([222, 253], 3, 20) # n4
a.ajoute_sommet([357, 212], 3, 21) # n3
a.ajoute_sommet([399, 253], 3, 22) # n2
a.ajoute_sommet([442, 210], 3, 23) # m3
a.ajoute_sommet([543, 124], 3, 24) # m1, m2


a.ajoute_sommet([715, 0], 22, 22)   # m7
a.ajoute_sommet([425, 240], 22, 20) # n1
a.ajoute_sommet([715, 241], 22, 21) # n7
a.ajoute_sommet([890, 189], 11, 52) # m6
a.ajoute_sommet([802, 290], 11, 51) # n6
a.ajoute_sommet([980, 381], 33, 32) # m4, m5

a.ajoute_sommet([675, 340], 11, 50) # c

a.ajoute_sommet([797, 380], 33, 31) # n5
a.ajoute_sommet([797, 515], 33, 30) # n4
a.ajoute_sommet([540, 522], 33, 29) # n3
a.ajoute_sommet([520, 450], 11, 49) # n2
a.ajoute_sommet([540, 705], 33, 28) # m3
a.ajoute_sommet([435, 670], 11, 48) # m1, m2
"""

#tri = Triangulation(a)
#print(tri.triangles.values())

"""s = Site(tri, ([797, 380], 3, 31))
print('\n')
print(s.sommet_centrale)
print('\n')
print(s.voisins)
print('\n')
print(s.miroires)
print('\n')

print('2 = {}'.format(a))


del s

ss = Site(tri, ([797, 515], 3, 30))
print('\n')
print(ss.sommet_centrale)
print('\n')
print(ss.voisins)
print('\n')
print(ss.miroires)
print('\n')"""

"""ss = Site(tri, ([435, 670], 1, 48))
print('\n')
print(s.sommet_centrale)
print('\n')
print(s.voisins)
print('\n')
print(s.miroires)
print('\n')"""

"""print(s.voisins)

print('\n')

print(s.miroires)

print('\n')

print(s.sommet_centrale)

print('\n')

c = Codage_site(s)

print(c.M)

print(c.Mp)

print('\n')

print(c.checksum_site())

print(selection_site(c.checksum_site(), "NASSIM", 6))

print(barycentre(s))

print(distance(s.sommet_centrale, barycentre(s)))

print('\n')

#cercle = Cercle([425, 240], [715, 241], [715, 0])
cercle = Cercle([715, 241], 300)
print(cercle.apartient_au_cercle([675, 340]))

print('\n')

test = test_preservation(s,  ([700, 400], 1, 50), 100)
print(test)"""
""""
sites = []

for i in range(len(a)):
    print ("Start running ", i+1 , " ... ")
    s = Site(tri, a.get(i))
    sites.append(s)
    s.print_voisins(s.voisins)
    print('\n')
    print("Mirroires : ", s.miroires)
    print('\n')
"""

"""print(angle([715, 241], [425, 240], [675, 340]))
print(a[6])
bg = bouger(a.get(6), [715, 241], 10, distance(a.get(6), [715, 241]), -1)
print(bg)
print(angle([715, 241], [425, 240], bg[0]))"""

"""
#--------- Error ici (24/02) ---------------
print ("=========== Modification =======")
for site in sites :
    print("\n-------------------------------")
    print('sommet_centrale = {}'.format(site.sommet_centrale))
    res = forcer_a_ne_pas_satisfait(site, 10)
    print('sommet_bouger = {}'.format(res.sommet_centrale[0]))
    print('distance = {}'.format(distance(res.sommet_centrale, site.sommet_centrale[0])))

    res = forcer_a_satisfait(site, 10)
    print('sommet_bouger = {}'.format(res.sommet_centrale[0]))
    print('distance = {}'.format(distance(res.sommet_centrale, site.sommet_centrale[0])))
"""
# ---------------------------------------------------------------
import shapefile
from tatouage import *

a = Doc([])

"""a.ajoute_sommet([7, 0], 1, 50) # c
a.ajoute_sommet([715, 0], 2, 22)   # m7
a.ajoute_sommet([425, 240], 2, 20) # n1
a.ajoute_sommet([715, 241], 2, 21) # n7
a.ajoute_sommet([890, 189], 1, 52) # m6
a.ajoute_sommet([802, 290], 1, 51) # n6
a.ajoute_sommet([980, 381], 3, 32) # m4, m5

a.ajoute_sommet([797, 380], 3, 31) # n5
a.ajoute_sommet([797, 515], 3, 30) # n4
a.ajoute_sommet([540, 522], 3, 29) # n3
a.ajoute_sommet([520, 450], 1, 49) # n2
a.ajoute_sommet([540, 705], 3, 28) # m3
a.ajoute_sommet([435, 670], 1, 48) # m1, m2"""

class shp_reader:
    def __init__(self, shp_name):
        rf = shapefile.Reader(shp_name)
        self.shapes = rf.shapes()

r2 = shp_reader("map/map1")
shapes = r2.shapes

for obj in range(0, len(shapes)):
    for pt in range(0, len(shapes[obj].points)):
        print(shapes[obj].points[pt])
        a.ajoute_sommet(shapes[obj].points[pt], obj, pt)

def sous_doc(shapes, point_from, point_to):
    sd = Doc([])
    for obj in range(0, len(shapes)):
        for pt in range(0, len(shapes[obj].points)):
            if point_from[0] <= shapes[obj].points[pt][0] and \
                point_to[0] >= shapes[obj].points[pt][0] and \
                point_from[1] <= shapes[obj].points[pt][1] and \
                point_to[1] >= shapes[obj].points[pt][1]:
                sd.ajoute_sommet(shapes[obj].points[pt], obj, pt)
                sd.set(len(sd)-1, sd.get(len(sd)-1))
    return sd

aa = sous_doc(shapes, [149, -40], [150, -30])

cle = "12345"
delta = 1
echelle = 34077294 #10
delta = (delta*100)/echelle

print("echelle = ", echelle)
print("delta = ", delta)
print("max = ", a.max_pos)
print("min = ", a.min_pos)

aaa = tatouage(aa, delta, cle, 3)

#for i in range(len(a)):
#    print(a.get(i))

print('\n')
for i in range(len(aaa)):
    print(aaa.get(i))

print('nombre de site bouger = {}'.format(len(nombre_de_site_bouger)))

from detection import *

res = detection(aaa, "12345", 0.5, delta, 2)

print("detecte = ", res)
