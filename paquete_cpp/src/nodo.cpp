#include "rclcpp/rclcpp.hpp"

class Clase_Nodo : public rclcpp::Node      // Clase que creamos heredando una clase de rclcpp
{
    public:
        Clase_Nodo() : rclcpp::Node("nombre_nodo_cpp")      // Aquí insertamos el nombre del nodo
        {
            RCLCPP_INFO(this->get_logger(), "Bamboleirlo");
            // Inicializar Variables
        }
    private:
        // Funciones Implementables
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);       // Inicia ROS2

    rclcpp::spin(std::make_shared<Clase_Nodo>());   // Hace  que al llamar al nodo en la terminal, este no se cierre a menos que se pulse ctr+c

    rclcpp::shutdown();             // Cierra ROS2
    return 0;
}