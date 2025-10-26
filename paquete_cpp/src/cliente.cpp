#include "rclcpp/rclcpp.hpp"

#include "paquete_cpp/srv/var_servicio.hpp"      // Añadir interfaz usada en el servicio.
#include <geometry_msgs/msg/twist.hpp>           // Añadir dependencia de la interfaz.

#include <chrono>                       // Necesario para poner 500ms
using namespace std::chrono_literals;   // <-- habilita 500ms, 1s, etc.

class Clase_Cliente : public rclcpp::Node 
{
    public:
        Clase_Cliente() : rclcpp::Node("nombre_cliente_cpp")  
        {
            // Creamos el objeto del cliente añadiendo el tipo de interfaz a utilizar, el nombre del servicio al que llamar.
            objeto_cliente = this->create_client<paquete_cpp::srv::VarServicio>("Nombre_Servicio");

            // Bucle del que no sale hasta que el cliente encuentre al servidor querido. Se repite cada 1 segundo.
            while (!objeto_cliente->wait_for_service(1s)) 
            {
                RCLCPP_INFO(this->get_logger(), "Servicio no disponible");
            }

            request = std::make_shared<paquete_cpp::srv::VarServicio::Request>();   // Creamos el objeto de la datos a enviar.
        }

        auto enviar_datos(int64_t a, double twist_1, double twist_2)
        {
            RCLCPP_INFO(this->get_logger(), "Datos obtenidos");

            // Declaramos los valores a enviar al servicio
            request->a = a;
            request->twist.linear.x = twist_1;
            request->twist.linear.y = twist_1;
            request->twist.linear.z = twist_1;

            request->twist.angular.x = twist_2;
            request->twist.angular.y = twist_2;
            request->twist.angular.z = twist_2;

            // Enviar petición asíncrona
            auto future_result = objeto_cliente->async_send_request(request);

            // Esperar la respuesta
            rclcpp::spin_until_future_complete(this->get_node_base_interface(), future_result);
      
            return future_result.get();
        }
    private:
        
        rclcpp::Client<paquete_cpp::srv::VarServicio>::SharedPtr objeto_cliente;
        std::shared_ptr<paquete_cpp::srv::VarServicio::Request> request;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto objeto_nodo = std::make_shared<Clase_Cliente>();

    auto response = objeto_nodo->enviar_datos(std::stoll(argv[1]), std::stod(argv[2]), std::stod(argv[3]));

    RCLCPP_INFO(objeto_nodo->get_logger(), "Resultado del Servicio: (Media = %f) y (Nuevo Twist = [%f, %f, %f], [%f, %f, %f])",
      response->media_twist,
      response->new_twist.linear.x, response->new_twist.linear.y, response->new_twist.linear.z,
      response->new_twist.angular.x, response->new_twist.angular.y, response->new_twist.angular.z);

    rclcpp::spin(objeto_nodo);  

    rclcpp::shutdown();
    return 0;
}