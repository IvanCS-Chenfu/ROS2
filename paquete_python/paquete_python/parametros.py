#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Clase_Nodo(Node):

    def __init__(self):
        super().__init__("nombre_parametros_python")    
        
        # Declarar parámetro (nombre, valor por defecto)
        self.declare_parameter("nombre_parametro", "valor_por_defecto_py")

        # Obtener parámetro
        valor = self.get_parameter("nombre_parametro").value

        # Mostrarlo
        self.get_logger().info(f"nombre_parametro = '{valor}'")
        
def main(args=None):
    rclpy.init(args=args)
    
    objeto_nodo = Clase_Nodo()
    rclpy.spin(objeto_nodo)
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()