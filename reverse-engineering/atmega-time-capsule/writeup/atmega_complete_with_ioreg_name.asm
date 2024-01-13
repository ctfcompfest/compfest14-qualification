
.include "m8515def.inc"
.def temp = r16
.def EW = r23 
.def PB = r24 
.def A  = r25
.def count = r21

MAIN:
	ldi temp, low(RAMEND)
	ldi temp, high(RAMEND)
	out SPH, temp

rjmp INIT1

EXIT:
	rjmp EXIT

DATA1:
	ldi ZH,high(2*key)
	ldi ZL,low(2*key)
	ret

DATA2:
	ldi ZH,high(2*MAIN)
	ldi ZL,low(2*MAIN)
	ret

INIT1:
	ser temp
	out DDRA,temp
	out DDRB,temp
	cbi PORTA,1
	ldi PB,0x38 
	out PORTB,PB
	sbi PORTA,0 
	cbi PORTA,0 
	cbi PORTA,1 
	ldi PB,$0E 
	out PORTB,PB
	sbi PORTA,0 
	cbi PORTA,0 
	cbi PORTA,1 
	ldi PB,$01 
	out PORTB,PB
	sbi PORTA,0 
	cbi PORTA,0 
	cbi PORTA,1 
	ldi PB,$06 
	out PORTB,PB
	sbi PORTA,0 
	cbi PORTA,0 

LOAD1: 
	cpi count, 16 
	breq PAUSE 
	rcall DATA1
	add ZL, count
	lpm 
	mov A, r0 
	rcall DATA2
	add ZL, count
	lpm 
	add A, r0
	sbi PORTA,1 
	out PORTB, A
	sbi PORTA,0 
	cbi PORTA,0 
	inc count
	rjmp LOAD1

PAUSE:
	cbi PORTA,1 
	ldi PB, $C0 
	out PORTB,PB
	sbi PORTA,0 
	cbi PORTA,0 

LOAD2: 
	cpi count, 32
	breq EXIT
	rcall DATA1
	add ZL, count
	lpm 
	mov A, r0 
	rcall DATA2
	add ZL, count
	lpm 
	add A, r0
	sbi PORTA,1 
	out PORTB, A
	sbi PORTA,0 
	cbi PORTA,0 
	inc count
	rjmp LOAD2

key:
.db 52, -150, 75, -144, 56, -122, 76, -108, -206, -155, -117, -127, -154, -133, 57, -37, -157, -107, -116, -123, 87, -50, 40, -187, 38, -135, 49, -85, -161, -95, -35, -102
