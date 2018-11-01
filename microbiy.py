from microbit import *
import random

rock = Image("00000:"
             "00000:"
             "00900:"
             "09990:"
             "09990:")

paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999:")

scissors = Image("99009:"
                 "99090:"
                 "00900:"
                 "99090:"
                 "99009:")

spock = Image("90900:"
              "90900:"
              "99909:"
              "99990:"
              "99900:")

lizard = Image("00900:"
               "99999:"
               "00900:"
               "09990:"
               "90909:")

rpssl = [rock, paper, scissors, spock, lizard]
total_wins = 0
total_losses = 0


def show_score(wins, losses):
    message = '{} Wins {} Losses'.format(wins, losses)
    return message


while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        display.show(random.choice(rpssl))

    elif button_a.is_pressed() and button_b.is_pressed():
        sleep(500)
        display.clear()
        display.scroll(show_score(total_wins, total_losses))
        sleep(500)

    elif button_a.is_pressed():
        sleep(500)
        display.clear()
        display.show(Image.HAPPY)
        total_wins += 1
        sleep(500)

    elif button_b.is_pressed():
        sleep(500)
        display.clear()
        display.show(Image.SAD)
        total_losses += 1
        sleep(500)

    else:
        continue