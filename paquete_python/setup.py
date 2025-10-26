from setuptools import find_packages, setup

package_name = 'paquete_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chenfu',
    maintainer_email='chenfu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "python_node = paquete_python.nodo:main",
            "python_publisher = paquete_python.publisher:main",
            "python_subscriber = paquete_python.subscriber:main",
            "python_service = paquete_python.servicio:main",
            "python_cliente = paquete_python.cliente:main"
        ],
    },
)
