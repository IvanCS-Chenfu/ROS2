#include "rclcpp/rclcpp.hpp"
#include <rclcpp_action/rclcpp_action.hpp>
#include "paquete_cpp/action/var_action.hpp"

#include <chrono>                       // Necesario para poner 1s
using namespace std::chrono_literals;   // <-- habilita 500ms, 1s, etc.

using VarAction = paquete_cpp::action::VarAction;
using GoalHandleVarAction = rclcpp_action::ClientGoalHandle<VarAction>;

class Clase_Cliente_Accion : public rclcpp::Node 
{
    public:
        Clase_Cliente_Accion() : rclcpp::Node("nombre_cliente_accion_cpp")
        {
            // Añadimos al objeto del cliente de la acción el tipo de interfaz a utilizar y el nombre de la acción al que llamar.
            objeto_cliente_accion = rclcpp_action::create_client<VarAction>(this, "Nombre_Accion");

            // Bucle del que no sale hasta que el cliente encuentre la acción querida. Se repite cada 1 segundo.
            while (!objeto_cliente_accion->wait_for_action_server(1s)) 
            {
                RCLCPP_INFO(get_logger(), "Servicio no disponible");
            }
        }

        void enviar_datos(int a, int b) 
        {
            RCLCPP_INFO(get_logger(), "Datos Obtenidos");

            VarAction::Goal goal;   // Creamos el objeto de la datos a enviar.
            goal.a = a;
            goal.b = b;

            // Creamos los callbacks
            rclcpp_action::Client<VarAction>::SendGoalOptions opts;

            opts.goal_response_callback = std::bind(&Clase_Cliente_Accion::on_goal_response, this, std::placeholders::_1);

            opts.feedback_callback = std::bind(&Clase_Cliente_Accion::on_feedback, this, std::placeholders::_1, std::placeholders::_2);

            opts.result_callback = std::bind(&Clase_Cliente_Accion::on_result, this, std::placeholders::_1);

            objeto_cliente_accion->async_send_goal(goal, opts);   // Se envía el goal al servidor de la acción
        }

    private:
        
        // Callback que se llama cuando el servidor acepta o rechaza el goal.
        void on_goal_response(std::shared_ptr<GoalHandleVarAction> goal_handle) 
        {
            if (!goal_handle) 
            {
                RCLCPP_WARN(get_logger(), "Goal rechazado");
                return;
            }
            RCLCPP_INFO(get_logger(), "Goal aceptado, esperando resultado…");
        }

        // Callback que se llama cuando el servidor publica en el feedback
        void on_feedback(std::shared_ptr<GoalHandleVarAction>, const std::shared_ptr<const VarAction::Feedback> feedback) 
        {
            const auto & e = feedback->entre;
            RCLCPP_INFO(get_logger(), "Feedback: [%.3f, %.3f, %.3f]", e.x, e.y, e.z);
        }

        // Callback que se llama al terminar el feedback (con exito, con cancelación o al abortar)
        void on_result(const GoalHandleVarAction::WrappedResult & future) 
        {
            const auto & vals = future.result->valores;
            std::string s = "[";

            for (size_t i = 0; i < vals.size(); ++i) 
            {
                s += std::to_string(vals[i]);
                if (i + 1 < vals.size()) s += ", ";
            }

            s += "]";

            RCLCPP_INFO(get_logger(), "Resultado: %s", s.c_str());
        }
        rclcpp_action::Client<VarAction>::SharedPtr objeto_cliente_accion;  // Creamos el objeto del cliente de la acción 
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    auto objeto_nodo = std::make_shared<Clase_Cliente_Accion>(); 

    objeto_nodo->enviar_datos(std::stoi(argv[1]), std::stoi(argv[2]));

    rclcpp::spin(objeto_nodo); 

    rclcpp::shutdown();
    return 0;
}