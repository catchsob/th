import Adafruit_DHT as sensor
from sys import argv
import argparse
from time import sleep
#import paho.mqtt.publish as publish

# constants
GPIO_VALID = range(0, 28) # 0 .. 27 is valid
DHT_VALID = [11, 22] # DHT model

# define arguments
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--gpio', type=int, default=2, help='GPIO number, 0 ~ 27, default 2')
parser.add_argument('-d', '--dht', type=int, default=22, help='DHT type, 11 or 22, default 22')
parser.add_argument('-m', '--mqtt_broker', type=str, help='IP address of MQTT broker')  # None means no MQTT transmission
parser.add_argument('-p', '--period', type=int, default=1, help='period of grabbing temperature and humidity in second, default 1s')
parser.add_argument('-c', '--count', type=int, default=0, help='count of grabbing grabbing temperature and humidity, default 0 for infinite')

# avoid jupyter notebook exception
if argv[0][-21:] == 'ipykernel_launcher.py':
    args = parser.parse_args(args=[])
else:
    args = parser.parse_args()

# check arguments
if args.gpio not in GPIO_VALID:
    print('invalid GPIO number!', end='\n')
    exit(1)
if args.dht not in DHT_VALID:
    print('invalid DHT model!', end='\n')
    exit(1)

# read sensor
count = args.count
c = 0
while (count<=0 or c<count):
    h, t = sensor.read(args.dht, args.gpio)
    if h is not None or t is not None:
        print(f'DHT{args.dht} 溼度:{h:.1f}%, 溫度：{t:.1f}度', end='\n')
    if (count<=0 or c<count-1):
        sleep(args.period)
    c += 1
