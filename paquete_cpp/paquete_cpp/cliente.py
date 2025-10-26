#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import sys              # Es solo para el ejemplo, sirve para enviar datos por la terminal.
from paquete_cpp.srv import VarServicio       # Añadir interfaz usada en el servicio.
from geometry_msgs.msg import Twist                         # Añadir dependencia de la interfaz

class Clase_Cliente(Node):

    def __init__(self):
        super().__init__("nombre_cliente_python")
        
        # Creamos el objeto del cliente añadiendo el tipo de interfaz a utilizar, el nombre del servicio al que llamar.
        self.objeto_cliente = self.create_client(VarServicio, 'Nombre_Servicio')  

        # Bucle del que no sale hasta que el cliente encuentre al servidor querido. Se repite cada 1 segundo.
        while not self.objeto_cliente.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Servicio no disponible")
            
        self.request = VarServicio.Request()    # Creamos el objeto de la datos a enviar.
        
    def enviar_datos(self, a, twist_1, twist_2):
        self.get_logger().info("Datos Obtenidos")
        
        # Declaramos los valores a enviar al servicio
        self.request.a = a
        
        self.request.twist = Twist()
        self.request.twist.linear.x = twist_1
        self.request.twist.linear.y = twist_1
        self.request.twist.linear.z = twist_1
        
        self.request.twist.angular.x = twist_2
        self.request.twist.angular.y = twist_2
        self.request.twist.angular.z = twist_2
        
        self.future = self.objeto_cliente.call_async(self.request)  # Enviamos los valores al servicio y obtenemos una respuesta.
        
        rclpy.spin_until_future_complete(self,self.future)  # Nos quedamos en bucle esperando hasta recibir la respuesta.
        
        return self.future.result()
        

def main():
    rclpy.init()
    
    objeto_nodo = Clase_Cliente()
    
    response = objeto_nodo.enviar_datos(int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    objeto_nodo.get_logger().info("Resultado del Servicio: (Media =  %f) y (Nuevo Twist = [%f, %f, %f], [%f, %f, %f])" % 
                                  (response.media_twist, 
                                   response.new_twist.linear.x, response.new_twist.linear.y, response.new_twist.linear.z,
                                   response.new_twist.angular.x, response.new_twist.angular.y, response.new_twist.angular.z))
    rclpy.spin(objeto_nodo)
    
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()