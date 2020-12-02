import aios
import time
import threading
import numpy as np
import json

Server_IP_list = []


def main():

    Server_IP_list = aios.broadcast_func()
    if Server_IP_list:

        # for j in range(200):
        #     for i in range(len(Server_IP_list)):
        #         aios.getIOState(Server_IP_list[i])
        #     print('\n')
        #     time.sleep(0.1)

        for j in range(500):
            start = time.time()
            dict = {
                'PWM0_CH' : 1024,
                'PWM1_CH' : 2048,
                'SERVO0' : 90,
                'SERVO1' : 120
            }
            for i in range(len(Server_IP_list)):
                aios.setIOState(dict, True, Server_IP_list[i])
            latency = time.time() - start
            print(latency);
            print('\n')
            time.sleep(0.1)

            dict = {
                'PWM0_CH' : 32768,
                'PWM1_CH' : 60000,
                'SERVO0' : 30,
                'SERVO1' : 180
            }
            for i in range(len(Server_IP_list)):
                aios.setIOState(dict, True, Server_IP_list[i])
            print('\n')
            time.sleep(0.1)



if __name__ == '__main__':
    main()
