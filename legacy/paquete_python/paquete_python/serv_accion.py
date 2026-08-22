#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer       # Librería necesaria para crear la acción.

from interfaces_paquete_python.action import VarAction      # Añadir interfaz usada en el servicio.
from geometry_msgs.msg import Vector3                       # Añadir dependencia de la interfaz
  

import time         # Para el Ejemplo

class Clase_Servicio_Accion(Node):

    def __init__(self):
        super().__init__("nombre_servicio_accion_python")
        
        # Creamos el objeto del servidor de la acción añadiendo el tipo de interfaz a utilizar, el nombre de la acción el cual
        # el cliente de la acción debe llamar para acceder a él, y el nombre de la función callback.
        # Esta función se llamará siempre que alguien llame al servicio de la acción
        self.objeto_servicio_accion = ActionServer(self, VarAction, "Nombre_Accion", self.accion_callback)

    # Función Callback
    def accion_callback(self, goal):
        
        feedback_msg = VarAction.Feedback()     # Creamos el objeto de nuestra interfaz que utilizaremos como feedback de la acción
        feedback_msg.entre = Vector3()          # Hacemos de tipo "Vector3" la variable "entre" de nuestra interfaz.
        
        result = VarAction.Result()             # Creamos el objeto de nuestra interfaz que devolveremos al cliente al final del callback.
        result.valores = []                     # Hacemos de tipo "array" la variable "valores" de nuestra interfaz
        
        x = float(goal.request.a)
        b = goal.request.b
        
        # En nuestro feedback devolveremos una variable "Vector3" con los 3 ultimos valores actuales del bucle.
        while x <= b:
            
            feedback_msg.entre.x = x-0.2
            feedback_msg.entre.y = x-0.1
            feedback_msg.entre.z = x
            
            goal.publish_feedback(feedback_msg)     # Envía periódicamente los valores al tópico /feedback
            
            result.valores.append(x)
            
            x += 0.1
            
            time.sleep(0.5)     # Delay para verlo más claro en el tópico feedback
            
        goal.succeed()       # Se ha cumplido el objetivo
        
        return result       # Devuelve result al cliente de la acción
            
        
    
def main(args=None):
    rclpy.init(args=args)
    
    objeto_nodo = Clase_Servicio_Accion()
    rclpy.spin(objeto_nodo)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()