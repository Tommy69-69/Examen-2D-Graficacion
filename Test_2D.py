"""
@author Francisco Emanuel Grijalva Ramirez
@Date 14/Dic/2020
Circulo cuyo radio es igual a la mitad de el rectangulo
 y que se encuentra centrado en un rectangulo, siendo que,
 el segundo rectangulo tenga su esquina que vaya desde el
 centro del circulo
"""
#Notas_finales
"""
Dado que los rectangulos tienen que ser iguales, no use sx ni sy, aunque entiendo que son
para cambiar la escala de dichos rectangulos, a su vez, Rz que lo puedo entender como valor
de rotacion tampo lo estoy usando porque no puedo rotar ningun rectangulo
"""

import matplotlib.pyplot as plt
import numpy as np

plt.axis([20,80,20,80])
plt.axis()
plt.grid()
plt.title('Test 2D')

xc=50
yc=50
plt.scatter(xc,yc,s=10,color='k')
#   Color segun mis ultimos 3 digitos de N. Control
Colour=(0,3/10,1/10)

#   Variables que no sé pa que sirven
#   Y que tampo use, perdon profe
rz=3*6
sx=1/5
sy=3/5

#   Draw circle
rad=5
p1=np.radians(0)
p2=np.radians(360)
dp=np.radians(1)

xlast = rad*np.sin(p1)+xc
ylast = rad*np.cos(p2)+yc

for p in np.arange(p1,p2+dp,dp):
    x= rad*np.sin(p)+xc
    y= rad*np.cos(p)+yc
    plt.plot([xlast,x],[ylast,y],color=Colour)
    xlast=x
    ylast=y

#   Draw cuadrado pero largo
#   Rectangulo con circulo dentro
x1=xc-2*rad
x2=x1+4*rad
y1=yc+rad
y2=y1-2*rad

plt.plot([x1,x1],[y1,y2],color=Colour)
plt.plot([x2,x2],[y1,y2],color=Colour)
plt.plot([x1,x2],[y1,y1],color=Colour)
plt.plot([x1,x2],[y2,y2],color=Colour)

#   Rectangulo desde el centro del circulo
xr=np.array([xc,xc,(xc+4*rad),(xc+4*rad),xc])
yr=np.array([yc,(yc-2*rad),(yc-2*rad),yc,yc])
plt.plot(xr,yr,color=Colour)

plt.gca().set_aspect('equal')
plt.show()
