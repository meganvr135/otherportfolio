start = '''
You are at school and the school goes on lockdown. While you and your classmates are hiding, an armed murderer bursts in.
'''

attack_one = '''
You decide to charge at the armed gunman and he shoots you.
'''
window = '''
You throw a chair at the window and it shatters. You leap out and other students follow suit. Your best friend tries to jump out of the window, but gets stuck.
'''
save_friend = '''
You go back and manage to get your get your friend free, but your friend gets cut by the window shards.
'''
stop = '''
You stop to bandage your friend's wounds and the gunman shoots you in the back. You finished bandaging your friend before you die, and your friend manages to get away.
'''
keep_running = '''
You and your friend keep running, but your friend is losing too much blood. Your friend passes out and dies, but you survive the attack.
'''
leave_friend = '''
You leave your friend and manage to get away from the school. You survive the attack, but the guilt eats you up for the next ten years of your life. You eventually die from guilt.
'''
run_for_door_one = '''
You try to make a break for the door, but the gunman shoots and kills you.
'''
hide = '''
The gunman starts shooting everyone that remained hidden. The gunman succeeds in killing six of your friends. You pretend to be dead. After the gunman thinks he succeeded in killing everyone, the murderer leaves the room.
'''
run_for_door_two = '''
The gunman is just around the corner with his back to you.
'''
run_the_other_way = '''
You decide to run the opposite way in hopes of avoiding the gunman. However you are in a long, narrow hallway and the gunman hears your footsteps. He turns around the corner and shoots you.
'''
attack_two = '''
You decide to attack the gunman while he has his back to you. You manage to disarm him and escape with the gun.
'''
keep_hiding = '''
You decide to keep hiding and pretend to be dead. Your phone goes off and the gunman comes back and shoots you.
'''


print(start)
done = False
print("Type 'attack' to attack the gunman, 'break' to break the window and jump out, 'run' to make a break for the door, or 'hide' in order to continue hiding.")
while not done:
    user_input = input()
    if user_input == "attack":
        print(attack_one)
        print("You were killed during the attack. Better luck next time.")
        done = True
    elif user_input == "break":
        print(window)
        finish = False
        print("Type 'save' to try to save your friend or 'leave' to leave your friend.")
        while not finish:
            user_input_two = input()
            if user_input_two == "save":
                print(save_friend)
                end = False
                print("Type 'stop' to stop and bandage your friend or 'run' to keep running.")
                while not end:
                    user_input_three = input()
                    if user_input_three == "stop":
                        print(stop)
                        print("You were killed during the attack. Better luck next time.")
                        end = True
                        finish = True
                        done = True
                    elif user_input_three == "run":
                        print(keep_running)
                        print("You survived during the attack! Congrats.")
                        end = True
                        finish = True
                        done = True
                    else:
                        print("This is not an exceptable answer. Type 'stop' to stop and bandage your friend or 'run' to keep running.")
            elif user_input_two == "leave":
                print(leave_friend)
                print("You survived during the attack! Congrats.")
                finish = True
                done = True
            else:
                print("This is not an exceptable answer. Type 'save' to try to save your friend or 'leave' to leave your friend.")
    elif user_input == "run":
        print(run_for_door_one)
        print("You were killed during the attack. Better luck next time.")
        done = True
    elif user_input == "hide":
        print(hide)
        idk = False
        print("Type 'run' in order to run for the door or 'hide' in order to stay hidden.")
        while not idk:
            user_input_four = input()
            if user_input_four == "run":
                print(run_for_door_two)
                haha = False
                print("Type 'run' to run the other way or 'attack' to attack the gunman while his back is turned.")
                while not haha:
                    user_input_five = input()
                    if user_input_five == "run":
                        print(run_the_other_way)
                        print("You were killed during the attack. Better luck next time.")
                        haha = True
                        idk = True
                        done = True
                    elif user_input_five == "attack":
                        print(attack_two)
                        print("You survived during the attack! Congrats.")
                        haha = True
                        idk = True
                        done = True
                    else:
                        print("This is not an exceptable answer. Type 'run' to run the other way or 'attack' to attack the gunman while his back is turned.")
            elif user_input_four == "hide":
                print(keep_hiding)
                print("You were killed during the attack. Better luck next time.")
                idk = True
                done = True
            else:
                print("This is not an exceptable answer. Type 'run' in order to run for the door or 'hide' in order to stay hidden.")
    else:
        print("This is not an exceptable answer. Type 'attack' to attack the gunman, 'break' to break the window and jump out, 'run' to make a break for the door, or 'hide' in order to continue hiding.")

print("Game Over.")
