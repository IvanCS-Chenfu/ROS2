#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Clase_Nodo(Node):             # Clase que creamos heredando una clase de rclpy

    def __init__(self):
        super().__init__("nombre_nodo")     # Aquí insertamos el nombre del nodo
        
        self.get_logger().info("Bamboleiro")

def main(args=None):
    rclpy.init(args=args)       # Inicia ROS2
    
    objeto_nodo = Clase_Nodo()  # Creamos el objeto del Nodo
    rclpy.spin(objeto_nodo)     # Hace  que al llamar al nodo en la terminal, este no se cierre a menos que se pulte ctr+c
    
    rclpy.shutdown()            # Cierra ROS2
