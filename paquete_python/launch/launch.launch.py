from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    a = LaunchConfiguration('a')
    x = LaunchConfiguration('x')
    y = LaunchConfiguration('y')

    declare = [
        DeclareLaunchArgument('a', default_value='0'),
        DeclareLaunchArgument('x', default_value='0.0'),
        DeclareLaunchArgument('y', default_value='0.0'),
    ]

    Node_py = Node  (
                        package='paquete_python',
                        executable='python_node',
                        name='nombre_nodo_py',
                        output='screen'
                    )
    Publisher_py = Node (
                            package='paquete_python',
                            executable='python_publisher',
                            name='nombre_publisher_py',
                            output='screen'
                        )
    Subscriber_py = Node    (
                                package='paquete_python',
                                executable='python_subscriber',
                                name='nombre_subscriber_py',
                                output='screen'
                            )
    Servicio_py = Node  (
                            package='paquete_python',
                            executable='python_service',
                            name='nombre_servicio_py',
                            output='screen'
                        )
    Cliente_py = Node   (
                            package='paquete_python',
                            executable='python_cliente',
                            name='nombre_cliente_py',
                            output='screen',
                            arguments=[a, x, y],
                        )
    Serv_Act_py = Node  (
                            package='paquete_python',
                            executable='python_serv_action',
                            name='nombre_servicio_accion_py',
                            output='screen'
                        )
    Cli_Act_py = Node   (
                            package='paquete_python',
                            executable='python_cli_action',
                            name='nombre_cliente_accion_py',
                            output='screen',
                            arguments=[1, 2],
                        )
    Parametros_py = Node    (
                                package='paquete_python',
                                executable='python_parametros',
                                name='nombre_parametros_py',
                                output='screen',
                                parameters= [{
                                                'nombre_parametro': "OLA PEPSICOLA",
                                            }]
                            )

    
    
    return LaunchDescription([
                                Node_py,
                                Publisher_py,
                                Subscriber_py,
                                declare + [Cliente_py],
                                Servicio_py,
                                Serv_Act_py,
                                Cli_Act_py,
                                Parametros_py,
                            ])
