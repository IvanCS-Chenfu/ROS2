cmake_minimum_required(VERSION 3.8)
project(paquete_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(interfaces_paquete_python REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/VarServicio.srv"

  DEPENDENCIES geometry_msgs
)

ament_python_install_package(${PROJECT_NAME}_py PACKAGE_DIR ${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

add_executable(cpp_node src/nodo.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(cpp_publisher src/publisher.cpp)
ament_target_dependencies(cpp_publisher rclcpp geometry_msgs)

add_executable(cpp_subscriber src/subscriber.cpp)
ament_target_dependencies(cpp_subscriber rclcpp geometry_msgs)

add_executable(cpp_cliente src/cliente.cpp)
ament_target_dependencies(cpp_cliente rclcpp geometry_msgs interfaces_paquete_python)
rosidl_get_typesupport_target(cpp_typesupport_target ${PROJECT_NAME} "rosidl_typesupport_cpp")
target_link_libraries(cpp_cliente "${cpp_typesupport_target}")

add_executable(cpp_servicio src/servicio.cpp)
ament_target_dependencies(cpp_servicio rclcpp geometry_msgs interfaces_paquete_python)
rosidl_get_typesupport_target(cpp_typesupport_target ${PROJECT_NAME} "rosidl_typesupport_cpp")
target_link_libraries(cpp_servicio "${cpp_typesupport_target}")


install(TARGETS
  cpp_node 
  cpp_publisher
  cpp_subscriber
  cpp_cliente
  cpp_servicio
  DESTINATION lib/${PROJECT_NAME})

install(PROGRAMS
  paquete_cpp/nodo.py
  paquete_cpp/publisher.py
  paquete_cpp/subscriber.py
  paquete_cpp/servicio.py
  paquete_cpp/cliente.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()