__author__ = 'Matteo'
import copy

d=dict(a=3,b=4,c=5)
e=d.copy().keys()
f=d.keys()
print e,f
e[1]='P'
print e,f,d
f[0]='CCC'
print e,f,d