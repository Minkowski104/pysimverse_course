from pysimverse import Drone

import time
drone = Drone()
drone.connect()

drone.take_off()
time.sleep(5)

drone.land()
time.sleep(5)
