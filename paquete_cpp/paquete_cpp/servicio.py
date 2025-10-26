#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from paquete_cpp.srv import VarServicio       # Añadir interfaz usada en el servicio.
from geometry_msgs.msg import Twist           # Añadir dependencia de la interfaz

class Clase_Servicio(Node):

    def __init__(self):
        super().__init__("nombre_servicio_python")
        
        # Creamos el objeto del servidor añadiendo el tipo de interfaz a utilizar, el nombre del servicio el cual
        # el cliente debe llamar para acceder a él, y el nombre de la función callback.
        # Esta función se llamará siempre que alguien llame al servicio
        self.objeto_servicio = self.create_service(VarServicio, 'Nombre_Servicio', self.servicio_callback)

    # Función Callback
    def servicio_callback(self, request, response):
        
        # Recibe los datos "twist" dados por el cliente y hace la media).
        response.media_twist = (request.twist.linear.x + request.twist.linear.y + request.twist.linear.z 
                                + request.twist.angular.x + request.twist.angular.y + request.twist.angular.z)/6.0
        
        self.get_logger().info("Se ha recibido: (l_x = %f, l_y = %f, l_z = %f, a_x = %f, a_y = %f, a_z = %f)\nLa media: (media = %f)" %
                               (request.twist.linear.x, request.twist.linear.y, request.twist.linear.z,
                                request.twist.angular.x, request.twist.angular.y, request.twist.angular.z,
                                response.media_twist))
        
        # Recibe los datos dados por el cliente y multiplica a * twist).
        response.new_twist = Twist()
        response.new_twist.linear.x = request.a * request.twist.linear.x
        response.new_twist.linear.y = request.a * request.twist.linear.y
        response.new_twist.linear.z = request.a * request.twist.linear.z
        
        response.new_twist.angular.x = request.a * request.twist.angular.x
        response.new_twist.angular.y = request.a * request.twist.angular.y
        response.new_twist.angular.z = request.a * request.twist.angular.z
        
        self.get_logger().info("Se ha recibido: (a = %d)" % (request.a))
        
        return response     # Devuelve al cliente la respuesta.

def main(args=None):
    rclpy.init(args=args)
    
    objeto_nodo = Clase_Servicio()
    rclpy.spin(objeto_nodo)
    
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()