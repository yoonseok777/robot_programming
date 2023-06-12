from roboid import *

beagle = Beagle()

end_game = 1                        # 1이면 일반 모드, 2면 멸망전; 주사위 눈 수 x2
move_point = 0                      # 현재 비글의 위치
wheel_pulse = 1440
wheel_speed = 15*end_game

print("beagle go 1")
for i in range(1*end_game) :
  move_point += 1
  beagle.move_forward_pulse(wheel_pulse, wheel_speed)
  if (move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16) :
    #beagle.stop()
    beagle.turn_right_pulse(705,30)
  if move_point > 16 :
    move_point -= 16


print("beagle go 2")
for i in range(2*end_game) :
  move_point += 1
  beagle.move_forward_pulse(wheel_pulse, wheel_speed)
  if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
    #beagle.stop()
    beagle.turn_right_pulse(705,30)
  if move_point > 16 :
    move_point -= 16


print("beagle go 3")
for i in range(3*end_game) :
  beagle.move_forward_pulse(wheel_pulse, wheel_speed)
  move_point += 1
  if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
    #beagle.stop()
    beagle.turn_right_pulse(705,30)
  if move_point > 16 :
    move_point -= 16


print("beagle go 4")
for i in range(4*end_game) :
  move_point += 1
  beagle.move_forward_pulse(wheel_pulse, wheel_speed)
  if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
    #beagle.stop()
    beagle.turn_right_pulse(705,30)
  if move_point > 16 :
    move_point -= 16


print("beagle go 5")
for i in range(5*end_game) :
  beagle.move_forward_pulse(wheel_pulse, wheel_speed)
  move_point += 1
  if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
    #eagle.stop()
    beagle.turn_right_pulse(705,30)
  if move_point > 16 :
      move_point -= 16

print("beagle go 6")
for i in range(6*end_game) :
  beagle.move_forward_pulse(wheel_pulse, wheel_speed)
  move_point += 1
  if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
    #beagle.stop()
    beagle.turn_right_pulse(705,30)
  if move_point > 16 :
    move_point -= 16



'''
from roboid import *

beagle = Beagle()

beagle.move_forward_pulse(1440,30)
beagle.turn_right_pulse(705,30)

dispose()
'''



'''
기본 코드
from roboid import *

beagle = Beagle()


move_point = 0

print("beagle go 1")
move_point += 1

beagle.wheels(60, 60)
wait(750)
if (move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16) :
  #beagle.stop()
  beagle.wheels(30,-30)
  wait(775)
  if move_point > 16 :
      move_point -= 16


print("beagle go 2")
for i in range(2) :
    move_point += 1
    beagle.wheels(60, 60)
    wait(750)
    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
      #beagle.stop()
      beagle.wheels(30,-30)
      wait(775)
    if move_point > 16 :
      move_point -= 16


print("beagle go 3")
for i in range(3) :
    beagle.wheels(60, 60)
    wait(750)
    move_point += 1
    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
      #beagle.stop()
      beagle.wheels(30,-30)
      wait(775)
    if move_point > 16 :
      move_point -= 16


print("beagle go 4")
for i in range(4) :
    move_point += 1
    beagle.wheels(60, 60)
    wait(750)
    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
      #beagle.stop()
      beagle.wheels(30,-30)
      wait(775)
    if move_point > 16 :
      move_point -= 16


print("beagle go 5")
for i in range(5) :
    beagle.wheels(60, 60)
    wait(750)
    move_point += 1
    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
      #eagle.stop()
      beagle.wheels(30,-30)
      wait(775)
      if move_point > 16 :
        move_point -= 16

print("beagle go 6")
for i in range(6) :
    beagle.wheels(60, 60)
    wait(750)
    move_point += 1
    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
      #beagle.stop()
      beagle.wheels(30,-30)
      wait(775)
    if move_point > 16 :
      move_point -= 16
'''
