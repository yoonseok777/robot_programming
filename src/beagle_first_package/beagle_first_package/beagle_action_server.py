import roboidai as ai
from rclpy.action import ActionServer
from rclpy.node import Node
import rclpy as rp

# 여기서 action.msg ==> key 를가지고 입력을해서 게임을 실행

# 게임끝나는 조건
# 화살표 인식도 해서, 앞으로 한칸 감, 뒤로 한칸 감
# 라이다 거리 측정해서 예외처리로 소리 울리면서 경고음

from beagle_msgs.action import Distbeagle

class DistbeagleaServer(Node) :
    
    def __init__(self) :
        super().__init__('beagle_dist_action')
        
        self.action_server = ActionServer(
                self,
                'dist_beagle',
                self.execute_callback
        )


    def execute_callback(self, goal_handle) :
       
        goal_handle.succeed()
        result = Distbeagle.Result()
        return result

   
    


def main(args = None) :
    rp.init(args = args)
    beagle_dist_action_server = DistbeagleaServer()
    rp.spin(beagle_dist_action_server)
 

if __name__ == '__main__' :
    main()