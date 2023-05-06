import pyautogui as pt
import time
import random

movie_list = ['monkey','dog', 'leopard', 'frog', 'pig']
# secure random generator
secure_random = random.SystemRandom()

limit = input("Enter limit:")
i = 0
time.sleep(5)

while i < int(limit):
    pt.typewrite(secure_random.choice(movie_list))
    # the message is written where -
    # the cursor belongs      

    pt.press("enter")

    i+=1
