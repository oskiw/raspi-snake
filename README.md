# RaspiSnake

<h4>Snake game for Raspberry Pi with Sense Hat</h4>

![Demo 1](demo/demo1.gif "Demo 1")
![Demo 2](demo/demo2.gif "Demo 2")

<h5> Game description</h5>

A simple snake game displayed on SenseHat LED matrix and controlled by SenseHat joystick.

Try to eat as many treats as possible without eating yourself.
Treats with different colors have different effects.
They can increase the speed, change your joystick's keys or be poisonous to your snake and kill you immediately.
New treat is created when a treat is eaten or expires.

You can pause/unpause the game any time by pressing return key on SenseHat joystick.

<h5>Requirements</h5>

Hardware:
- Raspberry Pi with connected:
    - SenseHat
    - monitor (required for pygame display)

Python libraries:
- pygame
- SenseHat

<h5>Run</h5>

To start the game just run raspisnake.py on your Raspberry Pi.
