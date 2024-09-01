from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description(): 

    publisher = Node(
        package = 'pubsub',
        executable = 'publisher',
    )
    
    subscriber = Node(
        package = 'pubsub',
        executable = 'subscriber',
    )

    return LaunchDescription(
        [
            publisher,
            subscriber,
        ]   
    )