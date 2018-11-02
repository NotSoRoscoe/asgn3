# asgn3
## rock paper scissors chooser and score keeper

5 weapons
=========
1. rock
2. paper
3. scissors
4. spock
5. lizard

Instructions
============
+ Shake micro:bit to have it choose a weapon
+ press button a to tally a win
+ press b to tally a loss
+ press a and b at the same time to show scorecard

Problem
=======
Pressing a and b to show score card works if its pressed shortly after
a sleep command in the button instructions, but if pressed after waiting 
a second or so it's likely to trigger as pressing one or the other buttons
and not both. 

May try to find a better way for the inputs to be closer to human reaction
time or to trigger on release. 
