#include "rclcpp/rclcpp.hpp"
#include <rclcpp_action/rclcpp_action.hpp>                      // Librería necesaria para crear la acción.
#include <memory>
#include <thread>

#include "paquete_cpp/action/var_action.hpp"        // Añadir interfaz usada en el servicio.
#include <geometry_msgs/msg/vector3.hpp>            // Añadir dependencia de la interfaz

// Para el Ejemplo
#include <vector>
#include <chrono>


class Clase_Servicio_Accion : public rclcpp::Node
{
    public:
        using VarAction = paquete_cpp::action::VarAction;
        using GoalHandleVarAction = rclcpp_action::ServerGoalHandle<VarAction>;

        Clase_Servicio_Accion() : rclcpp::Node("nombre_servicio_accion_cpp")
        {
            // Añadimos al objeto del servidor de la acción el tipo de interfaz a utilizar, el nombre de la acción el cual
            // el cliente de la acción debe llamar para acceder a él, y el nombre de las función callback (explicadas después).
            objeto_servicio_accion = rclcpp_action::create_server<VarAction>(this, "Nombre_Accion",
                std::bind(&Clase_Servicio_Accion::handle_goal, this, std::placeholders::_1, std::placeholders::_2),
                std::bind(&Clase_Servicio_Accion::handle_cancel, this, std::placeholders::_1),
                std::bind(&Clase_Servicio_Accion::handle_accepted, this, std::placeholders::_1));

        }
    private:

        // Se llama cuando el cliente de la acción realiza la petición
        rclcpp_action::GoalResponse handle_goal(const rclcpp_action::GoalUUID &, std::shared_ptr<const VarAction::Goal> goal)
        {
            (void)goal;
            RCLCPP_INFO(this->get_logger(), "Goal recibido: a=%d, b=%d", goal->a, goal->b);

            // Si devolvemos (ACCEPT_AND_EXECUTE) se llama a la función "handle_accepted" (y se interrumpe la acción anterior)
            // Si devolvemos (ACCEPT_AND_DEFER) se espera a que termine la acción anterior y se llama a "handle_accepted"
            // Si devolvemos (REJECT) rechazamos el goal y no se llama a "handle_accepted"
            return rclcpp_action::GoalResponse::ACCEPT_AND_EXECUTE;
        }

        // Se llama cuando el cliente cancela la acción (por ejemplo: goal_handle.cancel_goal_async()).
        rclcpp_action::CancelResponse handle_cancel(const std::shared_ptr<GoalHandleVarAction> /*goal_handle*/)
        {
            RCLCPP_INFO(this->get_logger(), "Petición de cancelación recibida");

            // Si devolvemos (ACCEPT), la acción se cancela.
            // Si devolvemos (REJECT), la acción sigue.
            return rclcpp_action::CancelResponse::ACCEPT;
        }

        // Se llama cuando se acepta la petición en "handle_goal"
        void handle_accepted(const std::shared_ptr<GoalHandleVarAction> goal_handle)
        {
            // Llama a la función "execute" como hilo (en segundo plano) con el fin de no bloquear la acción ante otras posibles llamadas
            std::thread(&Clase_Servicio_Accion::execute, this, goal_handle).detach();
        }


        void execute(const std::shared_ptr<GoalHandleVarAction> goal_handle)
        {
            auto feedback_msg = std::make_shared<VarAction::Feedback>();     // Creamos el objeto de nuestra interfaz que utilizaremos como feedback de la acción
            
            auto result = std::make_shared<VarAction::Result>();    // Creamos el objeto de nuestra interfaz que devolveremos al cliente al final del callback.
            result->valores.clear();                                // Hacemos de tipo "array" la variable "valores" de nuestra interfaz

            // Obtenemos los valores del cliente de la acción para utilizarlos en el bucle
            auto goal = goal_handle->get_goal();

            double x = static_cast<double>(goal->a);
            const double b = static_cast<double>(goal->b);

            rclcpp::Rate rate(2.0);     // Delay para verlo más claro en el tópico feedback (junto a rate.sleep())

            while (rclcpp::ok() && x <= b) 
            {
                feedback_msg->entre.x = x - 0.2;
                feedback_msg->entre.y = x - 0.1;
                feedback_msg->entre.z = x;

                goal_handle->publish_feedback(feedback_msg);    // Envía periódicamente los valores al tópico /feedback

                result->valores.push_back(x);

                x += 0.1;

                rate.sleep();
            }

            goal_handle->succeed(result);   // "result" se devuelve al cliente cuando el callback finaliza
        }

        rclcpp_action::Server<VarAction>::SharedPtr objeto_servicio_accion;     // Creamos el objeto del servicio de la acción

};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto objeto_nodo = std::make_shared<Clase_Servicio_Accion>();
    rclcpp::spin(objeto_nodo); 

    rclcpp::shutdown(); 
    return 0;
}