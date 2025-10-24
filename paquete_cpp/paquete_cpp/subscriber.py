#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Clase_Subscriber(Node):
    def __init__(self):
        super().__init__("nodo_subscriber_python_c")
        
        # Al crear el objeto del subscriptor, a parte de lo añadido en el publicador, deberemos añadir la función callback.
        # Esta función se llamará siempre que alguien publique algo en el tópico dado.
        self.objeto_subscriber = self.create_subscription(Twist,"/nombre_topico", self.subscriber_callback, 10) 
        
    # Función Callback
    def subscriber_callback(self, msg: Twist):
        self.get_logger().info(str(msg))
        
def main(args=None):
    rclpy.init(args=args) 
    
    objeto_nodo = Clase_Subscriber() 
    rclpy.spin(objeto_nodo) 
    
    rclpy.shutdown() 

if __name__ == '__main__':
    main()