#include "rclcpp/rclcpp.hpp"

class Clase_Nodo : public rclcpp::Node
{
    public:
        Clase_Nodo() : rclcpp::Node("nombre_parametros_cpp")
        {
            // Declarar parámetro (tipo, nombre, valor por defecto)
            this->declare_parameter<std::string>("nombre_parametro", "valor_por_defecto_cpp");

            // Obtener parámetro (decir tipo)
            std::string valor = this->get_parameter("nombre_parametro").as_string();

            // Mostrarlo
            RCLCPP_INFO(this->get_logger(), "nombre_parametro = '%s'", valor.c_str());
        }
    private:
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv); 

    auto objeto_nodo = std::make_shared<Clase_Nodo>();
    rclcpp::spin(objeto_nodo);

    rclcpp::shutdown();
    return 0;
}