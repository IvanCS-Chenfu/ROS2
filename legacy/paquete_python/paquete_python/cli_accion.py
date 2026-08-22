#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient       # Librería necesaria para crear la acción.

from interfaces_paquete_python.action import VarAction      # Añadir interfaz usada en el servicio.
from geometry_msgs.msg import Vector3                         # Añadir dependencia de la interfaz
  

import sys         # Para el Ejemplo

class Clase_Cliente_Accion(Node):

    def __init__(self):
        super().__init__("nombre_cliente_accion_python")
        
        # Creamos el objeto del cliente de la acción añadiendo el tipo de interfaz a utilizar y el nombre de la acción al que llamar.
        self.objeto_cliente_accion = ActionClient(self, VarAction, "Nombre_Accion")

        # Bucle del que no sale hasta que el cliente encuentre la acción querida. Se repite cada 1 segundo.
        while not self.objeto_cliente_accion.wait_for_server(timeout_sec=1.0):
            self.get_logger().info("Servicio no disponible")
            
        self.goal_msg = VarAction.Goal()    # Creamos el objeto de la datos a enviar.

    def enviar_datos(self, goal_0, goal_fin):
        self.get_logger().info("Datos Obtenidos")
        
        # Declaramos los valores a enviar al servicio
        self.goal_msg.a = goal_0
        self.goal_msg.b = goal_fin
        
        # Enviamos los valores al servicio de la acción y obtenemos el feedback en la función callback.
        self.future = self.objeto_cliente_accion.send_goal_async(self.goal_msg, feedback_callback=self.feedback_callback)  
        
        # Este callback nos dice si el servidor de la acción ha aceptado nuestra petición o no.
        self.future.add_done_callback(self.goal_response_callback)
    
    def feedback_callback(self, feedback_msg):
        self.get_logger().info("Feedback: [%f,%f,%f]" % (feedback_msg.feedback.entre.x, feedback_msg.feedback.entre.y, feedback_msg.feedback.entre.z))
    
    def goal_response_callback(self, future):
        
        goal_handle = future.result()
        
        if not goal_handle.accepted:
            self.get_logger().warn("Goal rechazado")
            return
        
        # Si acepta la petición obtenemos el resultado en el siguiente feedback
        self.get_logger().info("Goal aceptado, esperando resultado…")
        
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)
        
    def result_callback(self, future):
        result = future.result().result
        
        self.get_logger().info("Resultado: [{0}]".format(result.valores))
        
        
def main():
    rclpy.init()
    
    objeto_nodo = Clase_Cliente_Accion()
    
    objeto_nodo.enviar_datos(int(sys.argv[1]), int(sys.argv[2]))
    
    rclpy.spin(objeto_nodo)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()