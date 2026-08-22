from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    a = LaunchConfiguration('a')
    x = LaunchConfiguration('x')
    y = LaunchConfiguration('y')

    declare = [
        DeclareLaunchArgument('a', default_value='0'),
        DeclareLaunchArgument('x', default_value='0.0'),
        DeclareLaunchArgument('y', default_value='0.0'),
    ]
    
    params_file = PathJoinSubstitution  ([
                                            FindPackageShare('paquete_cpp'), 'config', 'params.yaml'
                                        ])
    
    Node_cpp = Node (
                        package='paquete_cpp',
                        executable='cpp_node',
                        name='nombre_nodo_cpp',
                        output='screen'
                    )
    Publisher_cpp = Node(
                            package='paquete_cpp',
                            executable='cpp_publisher',
                            name='nombre_publisher_cpp',
                            output='screen'
                        )
    Subscriber_cpp = Node   (
                                package='paquete_cpp',
                                executable='cpp_subscriber',
                                name='nombre_subscriber_cpp',
                                output='screen'
                            )
    Cliente_cpp = Node  (
                            package='paquete_cpp',
                            executable='cpp_cliente',
                            name='nombre_cliente_cpp',
                            output='screen',
                            arguments=[a, x, y],
                        )
    Servicio_cpp = Node (
                            package='paquete_cpp',
                            executable='cpp_servicio',
                            name='nombre_servicio_cpp',
                            output='screen'
                        )
    Serv_Act_cpp = Node (
                            package='paquete_cpp',
                            executable='cpp_serv_accion',
                            name='nombre_servicio_accion_cpp',
                            output='screen'
                        )
    Cli_Act_cpp = Node  (
                            package='paquete_cpp',
                            executable='cpp_cli_accion',
                            name='nombre_cliente_accion_cpp',
                            output='screen',
                            arguments=[1, 2],
                        )
    Parametros_cpp = Node   (
                                package='paquete_cpp',
                                executable='cpp_parametros',
                                name='nombre_parametros_cpp',
                                output='screen',
                                parameters= [{
                                                'nombre_parametro': "OLA PEPSICOLA",
                                            }]
                            )
    Node_py = Node  (
                        package='paquete_cpp',
                        executable='nodo.py',
                        name='nombre_nodo_python_c',
                        output='screen'
                    )
    Publisher_py = Node (
                            package='paquete_cpp',
                            executable='publisher.py',
                            name='nombre_publisher_python_c',
                            output='screen'
                        )
    Subscriber_py = Node    (
                                package='paquete_cpp',
                                executable='subscriber.py',
                                name='nombre_subscriber_python_c',
                                output='screen'
                            )
    Servicio_py = Node  (
                            package='paquete_cpp',
                            executable='servicio.py',
                            name='nombre_servicio_python_c',
                            output='screen'
                        )
    Cliente_py = Node   (
                            package='paquete_cpp',
                            executable='cliente.py',
                            name='nombre_cliente_python_c',
                            output='screen',
                            arguments=[a, x, y],
                        )
    Serv_Act_py = Node  (
                            package='paquete_cpp',
                            executable='serv_accion.py',
                            name='nombre_servicio_accion_python_c',
                            output='screen'
                        )
    Cli_Act_py = Node   (
                            package='paquete_cpp',
                            executable='cli_accion.py',
                            name='nombre_cliente_accion_python_c',
                            output='screen',
                            arguments=[1, 2],
                        )
    Parametros_py = Node    (
                                package='paquete_cpp',
                                executable='parametros.py',
                                name='nombre_parametros_python_c',
                                output='screen',
                                parameters= [params_file]
                            )

    
    
    return LaunchDescription([
                                Node_cpp,
                                Publisher_cpp,
                                Subscriber_cpp,
                                declare + [Cliente_cpp],
                                Servicio_cpp,
                                Serv_Act_cpp,
                                Cli_Act_cpp,
                                Parametros_cpp,
                                Node_py,
                                Publisher_py,
                                Subscriber_py,
                                declare + [Cliente_py],
                                Servicio_py,
                                Serv_Act_py,
                                Cli_Act_py,
                                Parametros_py,
                            ])


    