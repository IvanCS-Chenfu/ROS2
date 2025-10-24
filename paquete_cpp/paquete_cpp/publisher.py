#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Clase_Publisher(Node):
    def __init__(self):
        super().__init__("nodo_publisher_python")
        
        # Creamos el objeto del publicador añadiendo el tipo de mensaje, el tópico en el que se publicará y el tamaño del buffer.
        self.objeto_publisher = self.create_publisher(Twist,"/nombre_topico",10) 
        
        self.timer_ = self.create_timer(0.5,self.enviar_twist)  # Cada 0.5 segundos se llama a la función "enviar_twist".
        
    def enviar_twist(self):
        msg = Twist()   # Creamos el mensaje tipo Twist.
        
        # Damos valores
        msg.linear.x = 1.0
        msg.linear.y = 2.0
        msg.linear.z = 3.0
        msg.angular.x = 4.0
        msg.angular.y = 5.0
        msg.angular.z = 6.0
        
        self.objeto_publisher.publish(msg)  # Publicamos el mensaje tipo Twist en el tópico dicho anteriormente.
    
def main(args=None):
    rclpy.init(args=args)
    
    objeto_nodo = Clase_Publisher()
    rclpy.spin(objeto_nodo) 
    
    rclpy.shutdown() 

if __name__ == '__main__':
    main()