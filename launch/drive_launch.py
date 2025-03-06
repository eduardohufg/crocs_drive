from launch import LaunchDescription
from launch_ros.actions import Node
import launch_ros.actions
import launch


def generate_launch_description():
    joy_dev = launch.substitutions.LaunchConfiguration('joy_dev')

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument('joy_dev', default_value='/dev/input/js0'),
        Node(
            package='crocs_drive',
            executable='crocs_drive',
            name='crocs_drive'
        ),

        launch_ros.actions.Node(
            package='joy', 
            executable='joy_node',
            name='joy_node',
            parameters=[{
                'dev': joy_dev,
                'deadzone': 0.1,
                'autorepeat_rate': 20.0,
            }]),

        Node(
            package='crocs_drive',
            executable='proc_velocity',
            name='proc_velocity'
        ),



        
    ])