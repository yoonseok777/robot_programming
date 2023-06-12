from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                namespace='dice_and_point_pub',
                package='beagle_first_package',
                executable='beagle_first_pub',
                output='screen'
            ),
            Node(
                namespace='dice_and_point_sub',
                package='beagle_first_package',
                executable='beagle_first_sub',
                output='screen'
            ),
            Node(
                namespace="beagle_position_service",
                package='beagle_first_package',
                executable='beagle_service_server',
                output='screen'
            ),
        ]
    )

# game making 애들용, 
# following, finding, recognize
# 2 ~ 4 팀까지 하나의 주제로  승산없음

# 게임
'''
1. 주사위 굴러가고 나서 " 몇초간 " 딜레이를  "어디에" 걸것이냐

2. current ==> service의 역할을 정하지못함, action ==> 화살표 인식, 기믹, 라이다, 종료조건
   future ==> service --> 게임시작순서를 결정, srv로 현재로봇의 위치가 어디인지 
               action --> (화살표인식)==> (주사위인식으로 보냄pub), 
                        라이다 --> 내가 이겼을때 노래, 내가 졌을때 노래 
                        종료조건 --> 뭐로? lidar + (내부 code ==> srv 에서 로봇의 현재위치를 알수 있으니까)
             

                        
    DETAIL

    1. 변수에대한 값이 이리저리 잘 움직여야함 --> 전역변수로 하건, msg 타입으로 넘겨서 확인을 하건
                                          rosparam 이걸로해서 뭐 값을 어케하든가

    2. 가위바위보를해서, 이긴사람이 1로봇   -->   주사위를 던짐      -->     기믹을 밟건 안밟건 일단 앞으로감 -->       따라잡음 -->  종료조건
          (사람의 영역)                 (publish, subscribe)          (기믹은service)                        (action, lidar)
    param, 실행인자

    cpp  --> logging,?
    그럼 ... 칸번호는 어케매겨요 ? 어떤 변수에 따라 더해지면서, 로봇이 움직인곳이 바로 그칸 번호다, 

    0 ~ 15 ==>이거 배열 try exeception 박아?
    map_checker[16] = [0, 1, 2,34,5,6,6,7,]
'''