# Writeup
You are given a file `atmega.asm` and `key.txt`, find what the .asm file does.

## Solution
First, identify some information about what kind of assembly this is. From the problem title `ATMEGA` we know this is an avr assembly. The problem description also stated that the file was created on 8-5-15. This is, in fact, a hint to what chip this program use. It is `ATMEGA8515`. Add `.include "m8515def.inc"` so the program is runnable.   

Now time to find out how to use the `key.txt`. Check these line.
```
DATA1:
	ldi ZH,high(2*key)
	ldi ZL,low(2*key)
	ret
```
We know from these line that there's supposed to be some data under the `key` label inside the program, of course from the label itself, it's obvious that we should put the `key.txt` content under this label like this.
```
key:
.db 52, -150, 75, -144, 56, -122, 76, -108, -206, -155, -117, -127, -154, -133, 57, -37, -157, -107, -116, -123, 87, -50, 40, -187, 38, -135, 49, -85, -161, -95, -35, -102
``` 

Now, if you actually try to run the program in avr studio, it will run. But it doesn't give any direct output. If we analyze the program further, we found out that there's a lot of output to IO registers (from `out <io> <reg>` instruction). Check the name of io register from the include file and take a note of all IO registers the program use. Check `atmega_complete_with_ioreg_name.asm`.   

We can identify what kind of device this program use from how the program interact with the IO register. This program give calculation output to Port B and always set the clear the bit of Port A. This pattern is what we use to interact with lcd. We can use a simulator `hapsim` to simulate lcd and hook it with avr studio. Configure the lcd settings so every lcd input are attached to correct port and run the program once again while hapsim is running and we got the flag printed on the lcd screen.  

![Hapsim Configuration](https://cdn.discordapp.com/attachments/889143849396604928/990842042043224064/unknown.png)   

![Flag Printed on LCD Screen](https://cdn.discordapp.com/attachments/889143849396604928/993369061914316901/unknown.png)

> COMPFEST14{aTcApSule_c74048f89e}
