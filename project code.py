import wiotp.sdk.device
import time
import random
myConfig = { 
    "identity": {
        "orgId": "178vg8",
        "typeId": "IOTdevice",
        "deviceId":"1001"
    },
    "auth": {
        "token": "1234567890"
    }
}

def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

T=24    #Threshold temperature
while True:
    temp=random.randint(-20,125)
    fs=random.randint(0,100)
    myData={"d":{'temperature':temp, 'firesensor':fs}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    if temp > T:
        print("Switch on the AC")
    else:
        print("Switch off the AC")

    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
