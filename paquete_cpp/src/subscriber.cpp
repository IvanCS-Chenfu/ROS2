#include "rclcpp/rclcpp.hpp"
#include <geometry_msgs/msg/twist.hpp>
#include <chrono>                       // Necesario para poner 500ms
using namespace std::chrono_literals;   // <-- habilita 500ms, 1s, etc.

class Clase_Subscriber : public rclcpp::Node
{
    public:
        Clase_Subscriber() : rclcpp::Node("nodo_subscriber_cpp")
        {
            // Al crear el objeto del subscriptor, a parte de lo añadido en el publicador, deberemos añadir la función callback.
            // Esta función se llamará siempre que alguien publique algo en el tópico dado.
            objeto_subscriber = this->create_subscription<geometry_msgs::msg::Twist>
            ("/nombre_topico", 10, std::bind(&Clase_Subscriber::subscriber_callback, this, std::placeholders::_1));
        }
    private:
        void subscriber_callback(const geometry_msgs::msg::Twist msg)
        {
            RCLCPP_INFO(this->get_logger(), "%f,%f,%f,%f,%f,%f",msg.linear.x,msg.linear.y,msg.linear.z,msg.angular.x,msg.angular.y,msg.angular.z);
        }

        
        rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr objeto_subscriber;   // Creamos el objeto del subscriptor.
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto objeto_nodo = std::make_shared<Clase_Subscriber>();
    rclcpp::spin(objeto_nodo);

    rclcpp::shutdown();
    return 0;
}