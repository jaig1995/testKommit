from Tank import Tank
from Tubing import Tubing
import time

if __name__ == '__main__':

    #Tanques
    tanks = [Tank(10), Tank(25), Tank(30), Tank(53)]

    #Tuberias
    tubings = [Tubing(1, [tanks[0], tanks[1]]), Tubing(4, [tanks[0], tanks[2]]), Tubing(8, [tanks[2], tanks[3]])]

    #Tiempo
    timeFlow = 20

    while True:

        inFlowNow = 4

        for tank in tanks:
            inFlowNow = tank.fill(inFlowNow)

        for tubing in tubings:
            tubing.addFlow()

        time.sleep(1)
        timeFlow -= 1
        if timeFlow == 0:
            break

    for tank in tanks:
        print(tank.getContent())

