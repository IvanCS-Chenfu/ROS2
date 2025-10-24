#include "rclcpp/rclcpp.hpp"
#include <geometry_msgs/msg/twist.hpp>
#include <chrono>                       // Necesario para poner 500ms
using namespace std::chrono_literals;   // <-- habilita 500ms, 1s, etc.

class Clase_Publisher : public rclcpp::Node
{
    public:
        Clase_Publisher() : rclcpp::Node("nodo_publisher_python")
        {
            // Le damos al objeto del publicador el tipo de mensaje, el tópico en el que se publicará y el tamaño del buffer.
            objeto_publisher = this->create_publisher<geometry_msgs::msg::Twist>("/nombre_topico",10);
            
            // Cada 0.5 segundos se llama a la función "enviar_twist".
            objeto_timer = this->create_wall_timer(500ms, std::bind(&Clase_Publisher::enviar_twist, this));
        }
    private:

        void enviar_twist()
        {
            geometry_msgs::msg::Twist msg;      // Creamos el mensaje tipo Twist.

            // Damos valores
            msg.linear.x = -1;
            msg.linear.y = -2;
            msg.linear.z = -3;
            msg.angular.x = -4;
            msg.angular.y = -5;
            msg.angular.z = -6;

            objeto_publisher->publish(msg);     // Publicamos el mensaje tipo Twist en el tópico dicho anteriormente.
        }
        
        rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr objeto_publisher;   // Creamos el objeto del publicador.
        rclcpp::TimerBase::SharedPtr objeto_timer;                                  // Creamos el objeto del timer.
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    rclcpp::spin(std::make_shared<Clase_Publisher>());

    rclcpp::shutdown();
    return 0;
}