
from registrador import Registrador
import os

class User:

    def __init__(self, idU, name):

        self.name = name
        self.id = idU

class Message:

  def __init__(self, idM, mensaje):
    self.idM = idM
    self.mensaje=mensaje

class TipoRegistro:

  def __init__(self, idR, tipo):
    self.idR = idR
    self.tipo = tipo

class Register:

  def __init__(self, u, m):
    self.u = u
    self.m = m


  def register(self):

    propiedadRegistro = Registrador.properties()
    if propiedadRegistro == "consola":
        print("Se registro en consola el mensaje: {}".format(self.m))
    elif propiedadRegistro == "texto":
        print("Se registro en texto el mensaje: {}".format(self.m))
        
        file = open("{}/ficheroSalida.txt".format(os.getcwd()), "w")
        file.write("{}".format(self.m))
        
        file.close()
    elif propiedadRegistro == "base de datos":
        print("Se registro en base de datos el mensaje: {}".format(self.m))



nombre = input("Ingrese Nombre de Usuario: ")
mensaje = input("Ingrese mensaje: ")

x = User(1,nombre)
y = Message(1, mensaje)
w = Register(x.name,y.mensaje)

w.register()