from machine import Pin, ADC
from gpio_lcd import GpioLcd
from picozero import Button
import utime
#This code was created from a base of 'hello+world.py' by Ramji Patel https://www.instructables.com/Raspberry-Pi-Pico-and-16x2-LCD/
#Configure the Gpio pin of the Raspberry pi pico
lcd = GpioLcd(rs_pin = Pin(0),
              enable_pin = Pin(1),
              d4_pin = Pin(2),
              d5_pin = Pin(3),
              d6_pin = Pin(4),
              d7_pin = Pin(5),
              num_lines = 2, num_columns = 16)
#print the string on the display
#lcd.putstr('Hello Sam')

temp_pin = ADC(Pin(26))
gas_pin = ADC(Pin(27))
press= Button(6, pull_up=True)

state=1

#temp_pin.atten(ADC.ATTN_11DB)
while True:
    gas = gas_pin.read_u16()
    CO = (gas/65536)*100
    CO = round(CO,2)
    temp = temp_pin.read_u16()
    t=(temp/4096)* 3300/10.24 -273.15 #eq from https://wiki.dfrobot.com/DFRobot_LM35_Linear_Temperature_Sensor__SKU_DFR0023_
    t=round(t,2)
    if press.is_pressed:
        if state == 4:
            state=1
        else:
            state+=1
    if state == 3:
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr("Carbon Monoxide Level")
        lcd.move_to(0,1)
        lcd.putstr(str(CO)+'% detected')
        utime.sleep(0.5)
        #lcd.putstr(str(state))
    #lcd.move_to(0,1)
    if state ==4:
        lcd.clear()
        #lcd.putstr(str(state))
        lcd.move_to(0,0)
        lcd.putstr("Pan Temperature")
        lcd.move_to(0,1)
        lcd.putstr(str(t)+'°C')
        utime.sleep(0.5)
        
    if state ==1:
        lcd.clear()
        lcd.putstr("Welcome to SMART TONGS")
        utime.sleep(0.5)
    if state ==2:
        lcd.clear()
        lcd.putstr("More features     soon!!!")
        utime.sleep(0.5)
    #lcd.move_to(0,0)
    #utime.sleep(0.25)
    












    lcd.move_to(0,1)
#     #temp=temp_pin.value()
#     temp=temp_pin.read_u16()
#     t=(temp/4096)* 3300/10.24 -273.15 #eq from https://wiki.dfrobot.com/DFRobot_LM35_Linear_Temperature_Sensor__SKU_DFR0023_
#     lcd.putstr(str(t))
#     lcd.move_to(0,0)
#     if temp > 50:
#         #lcd.clear()
#         lcd.putstr("Temp High!")
#     else:
#         lcd.putstr("No Temp concern")
# 
#     utime.sleep(1)
#create an infinite loop 
#while True:
 #   for i in range(1000):
  #      lcd.move_to(0,1)    #set the curstor location to (0,1)
   #     lcd.putstr(str(i))  #convert the i into string and print it
    #    utime.sleep(0.5)    #create a delay of 0.5 second

