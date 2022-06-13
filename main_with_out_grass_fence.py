import sys, pygame 
from pygame.locals import * 
from pygame.constants import * 
from OpenGL.GL import * 
from OpenGL.GLU import * 
from camera import Camera 
from Loader.objloader import * 
import numpy as np 
from OpenGL.GL.shaders import * 
import os 
from PIL import * 
 
def getFileContents(filename): 
    p = os.path.join(os.getcwd(), "shaders", filename) 
    return open(p, 'r').read() 
 
pygame.init() 
cam = Camera() 
vport = (800,600) 
height = vport[0]/2 
width = vport[1]/2 
pygame.display.set_mode(vport, OPENGL | DOUBLEBUF) 
 
vertexes = np.array([ 
     
]) #to be filled  
vertexShader = compileShader(getFileContents( 
        "triangle.vertex.shader"), GL_VERTEX_SHADER) 
fragmentShader = compileShader(getFileContents( 
    "triangle.fragment.shader"), GL_FRAGMENT_SHADER) 
 
program = glCreateProgram() 
glAttachShader(program, vertexShader) 
glAttachShader(program, fragmentShader) 
glLinkProgram(program) 
 
glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0)) 
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0)) 
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0)) 
glEnable(GL_LIGHT0) 
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 
                          8 * vertexes.itemsize, ctypes.c_void_p(0)) 
glEnableVertexAttribArray(0) 
 
# colorLocation = glGetAttribLocation(program, "color"); 
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 
                        8 * vertexes.itemsize, ctypes.c_void_p(12)) 
glEnableVertexAttribArray(1) 
 
# texLocation = glGetAttribLocation(program, "texCoord"); 
glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE,  
    8*vertexes.itemsize, ctypes.c_void_p(24)) 
glEnableVertexAttribArray(2) 
glEnable(GL_LIGHTING) 
glEnable(GL_COLOR_MATERIAL) 
glEnable(GL_DEPTH_TEST) 
glShadeModel(GL_SMOOTH)  
 
obj = OBJ("mesh/of3.obj", swapyz=True) 
obj.generate() 
 
clock = pygame.time.Clock() 
 
glMatrixMode(GL_PROJECTION) 
glLoadIdentity() 
width, height = vport 
gluPerspective(90.0, width/float(height), 1, 100.0) 
glEnable(GL_DEPTH_TEST) 
glMatrixMode(GL_MODELVIEW) 
 
 
while 1: 
    clock.tick(30) 
    for e in pygame.event.get(): 
        if e.type == QUIT: 
            sys.exit() 
        cam.takeAc(e) 
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
 
    glTranslate(cam.transX/20., cam.transY/20., - cam.zpos) 
    glRotate(cam.rotx, 1, 0, 0) 
    glRotate(cam.rotx, 0, 1, 0) 
    glScale(cam.sx, cam.sy, cam.sz) 
    obj.render() 
 
    pygame.display.flip()