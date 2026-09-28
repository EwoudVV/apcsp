# makes stuff slower
import time
while True:
    # input the stuff
    speedinput = float(input("speed 0-1. 1 is instant, 0 is slow: "))
    textinput = input("text to slow down: ")
    # convert the speed input to second delay
    speedtime = 1 - speedinput
    # break text into individual chars and print them according to speed delay
    for char in textinput:
        print(char, end="", flush=True) # end="" stops print from making a new line, flush=True makes each char print immideately instead of all at once when done
        time.sleep(speedtime)
    print()