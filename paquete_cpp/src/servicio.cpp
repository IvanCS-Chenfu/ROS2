#include "rclcpp/rclcpp.hpp"

#include "paquete_cpp/srv/var_servicio.hpp"      //#include "interfaces_paquete_python/srv/varservicio.hpp"
#include <geometry_msgs/msg/twist.hpp>

class Clase_Servicio : public rclcpp::Node
{
    public:
        Clase_Servicio() : rclcpp::Node("nombre_servicio_cpp")
        {
           objeto_servicio = this->create_service<paquete_cpp::srv::VarServicio>
           ("Nombre_Servicio", std::bind(&Clase_Servicio::servicio_callback, this, std::placeholders::_1, std::placeholders::_2, std::placeholders::_3));
        }
    private:

    void servicio_callback(
        const std::shared_ptr<rmw_request_id_t>,
        const std::shared_ptr<paquete_cpp::srv::VarServicio::Request> request,
        std::shared_ptr<paquete_cpp::srv::VarServicio::Response> response)
    {
        response->media_twist = (request->twist.linear.x + request->twist.linear.y + request->twist.linear.z 
                                 + request->twist.angular.x + request->twist.angular.y + request->twist.angular.z) / 6.0;

        RCLCPP_INFO(this->get_logger(), "Se ha recibido: (l_x = %f, l_y = %f, l_z = %f, a_x = %f, a_y = %f, a_z = %f)\nLa media: (media = %f)",
                                        request->twist.linear.x, request->twist.linear.y, request->twist.linear.z,
                                        request->twist.angular.x, request->twist.angular.y, request->twist.angular.z,
                                        response->media_twist);
        
        response->new_twist.linear.x  = request->a * request->twist.linear.x;
        response->new_twist.linear.y  = request->a * request->twist.linear.y;
        response->new_twist.linear.z  = request->a * request->twist.linear.z;
        response->new_twist.angular.x = request->a * request->twist.angular.x;
        response->new_twist.angular.y = request->a * request->twist.angular.y;
        response->new_twist.angular.z = request->a * request->twist.angular.z;
        
        RCLCPP_INFO(this->get_logger(), "Se ha recibido: (a = %ld)", request->a);
    }

    rclcpp::Service<paquete_cpp::srv::VarServicio>::SharedPtr objeto_servicio;

};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto objeto_nodo = std::make_shared<Clase_Servicio>();
    rclcpp::spin(objeto_nodo); 

    rclcpp::shutdown(); 
    return 0;
}