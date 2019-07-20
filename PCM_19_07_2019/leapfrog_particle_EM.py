import numpy
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

# Función para sacar la proyección de un vector con otro
def projection(A, B):
    paral = numpy.dot(A, B) * B / (numpy.linalg.norm(B) ** 2)
    perp = A - paral
    return paral, perp

# Función para actualizar la velocidad en medio paso de tiempo
def update_velocity(vel, dt):
    v_new = vel + (charge / mass * numpy.cross(vel, B)) * dt
    return v_new

# Función para actualizar la posición en un paso de tiempo
def update_position(pos, vel, dt):
    r_new = pos + vel * dt
    return r_new

# Función para utilizar el método de leapfrog
def leapfrog(pos, vel, dt):
    v_new = update_velocity(vel, dt)
    r_new = update_position(pos,v_new, dt)
    return r_new, v_new

# Definición de parámetros
B = numpy.array([0.0, 0.0, 1.0])
vel = numpy.random.uniform(2.0, size=3)
v_paral, v_perp = numpy.linalg.norm(projection(vel, B), axis=1)
charge = 1.0
mass = 1.0
omega = (abs(charge) / mass) * numpy.linalg.norm(B)
rL = v_perp / omega

# Generar un arreglo de tiempos
T = 2 * numpy.pi / omega  
dt = 0.1
steps = int(5 * T / dt)
t = numpy.linspace(0, steps * dt, steps)

# Definir condiciones iniciales
x0, y0, z0 = 0.0 , 0.0, 0.0

# Definir ecuaciones de movimiento 
x_th = x0 + rL * numpy.sin(omega * t)
y_th = y0 + (abs(charge) / charge) * rL * numpy.cos(omega * t)
z_th = z0 + v_paral * t

# Inicializar variables que se dasarrollaran de manera numérica
r_num = numpy.zeros((steps, 3)) 
v_num = numpy.zeros((steps, 3)) 

# Condiciones iniciales
r_num[0] = x0, y0 + (abs(charge) / charge) * rL, z0
v_num[0] = v_perp, 0, v_paral

# Primer paso de leapfrog
v_num[0] = update_velocity(v_num[0], -0.5 * dt)

for i in range(steps - 1):
    r_num[i + 1], v_num[i + 1] = leapfrog(r_num[i], v_num[i], dt)

x_num = r_num[:, 0]
y_num = r_num[:, 1]
z_num = r_num[:, 2]

# Creamos la figura
fig = pyplot.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_th, y_th, z_th, color='violet', label='Theoretical', marker='*')
ax.plot(x_num, y_num, z_num, color='deeppink', label='Numerical')
ax.legend(loc='best')
ax.set_xlabel(r'$x$', fontsize=10)
ax.set_ylabel(r'$y$', fontsize=10)
ax.set_zlabel(r'$z$', fontsize=10)
ax.set_title('Particle in an electromagnetic field', fontsize=20)
pyplot.savefig('image.pdf')
pyplot.close()

