# 2121 Final Exam Sample Questions

## Exam Notes
* call trees

* What serial IO is

Input output protocol where each bit of information is sent one after another. 

* When should you use Serial vs Parallel? 

Parallel needs more wires and shit. Parallel is more suss to noise and shit.

* don’t need the shift register 

* UART structure 
* understand the data format
* full and half duplex

Full duplex - **F**ull **F** is the start of the number **FOUR**, so there are **FOUR** wires 

Half Duplex - Half of full

* shift registers

are not needed

* no voltage

* know what AVR offers in this

* how Receiving and transmitting work, (how its turning voltage on a pin to a byte of data)
* what parity is for

to ensure that the sent data is has not been corrupted. Parity does not include the parity bit.

* what frame errors are

When reading in data, there is no end or start bit.

* know the errors (framing, data overrun, parity)

	* Data Overrun - When the recieving buffer fills up but is not emptied before more data is read in. Invalid baud rates are usually the issue.
 	* Parity - Amount of 1's in the data. Is set to 1 if odd, 0 if even. 
	* Framing - covered already.

* Error Recovery

A bit is split into 16 parts and the middle 3 are read. The majority is taken as the correct value.

* what interrupts UART can generate
	* Transmission Done
	* Recieve Done
	* Transmission Buffer Empty


* no initialisation sequence
* basic UART theory

* no wiring

## ADC & DAC

### DAC
|Methods|Pros|Cons|
|---|---|---|
|Binary Weighted|None its shit as|Lots of resistors hence expensive, high heat generation, impractical to scale|
|R-2R|A wide range of resistances, cheaper, less heat, easy to scale|Uses twice as many resistors|

### ADC
|Methods|Pros|Cons|
|---|---|---|
|Successive Approximation|Cheap and easy like Zain|Really slow|
|Paralell|Very quick|takes 2^n - 1 comparitors|
|Two stage Paralell | still quick but uses way less comparitors | expensive





## Short Answer 
**( I have it on pretty shitty authority that this was last sem's q's )**

##### What is a stack? How do we implement a stack in AVR? Why does the stack grow from higher memory addresses?

A stack is a data structure that has the FIFO property. The only operations we can preform on a stack is pushing data on, and popping it off. In AVR, the stack is implemented as a block of consecutive bytes in SRAM, and a stack pointer that keeps track of the 'top' of the stack. 

The stack beings at RAMEND and grows upwards, allowing the top of SRAM to be used for registers and other general data as the stack grows upwards. Furthermore the commands used to access the stack's data manually (LDD) can only adjust the pointer they are given positively. Thus reading from the top of the stack downwards works fine as the stack pointer is dsiplaced to higher addresses. 
If the stack grew towards higher addresses then going from the top of the stack down would require the stack pointer to be subtracted which LDD does not support directly.  

To implement this in AVR simply set up the stack pointer as such

```
ldi r16, low(RAMEND)
out SPL, r16
ldi r16, high(RAMEND)
out SPH, r16
```
and then use the commands push and pop which will automatically add the data to the top of the stack from a register
and adjust the stack pointer as needed. 

##### How do we choose the right frequency for analog-digital conversion?

The frequency should always be twice the frequency of the analog signal being read in to prevent aliasing. Aliasing is when our freqency is too great, and we read in data points from different parts of different peaks of wave, and create a wave that has a period that is far larger than usual.

##### Why do we take 3 samples for USART in AVR?

##### In AVR, we use polling and interrupts. Compare the two and list when we would use one or the other.

Polling is the action of checking a certain condition at regular intervals until the condition triggers a certain piece of code. This requires the code to manually check the condition every so often and often requires a busy loop where the processor is not able to do any other work. This is also not as responsive as depending on the polling interval it may take some time for the processor to pick up on the condition being changed. This is still used though as it is easy to implement and requires no additional hardware or support. 

Interrupts are usually built into a processor and allow a external pin or internal condition to automatically trigger a response. Usually once the interrupts are activated the processor stops it's current task and after finishing the last command it was on will handle the interrupt code. Once done it returns and resumes. This is more responsive and allows the code to do other work while waiting for a interrupt but can interrupt code in the middle of a calculation or process possibly causing issues and lag. 

Polling is great for non-time critical applications to produce cheap response acitivty where only one task is needed to be done, such as checking for a button to be pressed to activate some other peice of hardware. 

Interrupts are better for time critical applications to produce quick responses where the processor has other work to be doing. An example is a alarm system which must be detecting input from sensors, calculating, responding to keypads and driving alarms. 
 
##### Find the errors in the code (theres 10 altogether)
	* Apparently the given code is a bubble sort
	* a constant is too negative (i.e rolled over to positive)
	* wrong instruction
	* wrong branch condition


##### You're given a fictitious microprocessor, and its instruction set. You're asked to write a program that multiplies two 8-bit numbers together (or two 16 bit, most likely 8 bit). You are then asked to encode it in binary.



## Unofficial Sample Programming Questions

##### Write a program that calculates the n'th Fibonnaci number. Assume `n` is read in from register 16. Store the output in register 17.

```
.include "m2560def"

.def first=r18
.def second=r19
.def count=r20
.def next=r17
.def temp=r21

fib:
	ldi first, 0
	ldi second, 1
	
	
	StartLoop:
	cp count, r16
	breq halt
	
		cpi count, 2
		brgt NORMAL
		mov next, count
		inc count
		jump StartLoop
	
		NORMAL:
		
		ld temp, first
		add temp, second
		
		mov output, temp
		mov first, second
		mov second, next
		
		inc count
	
		jump StartLoop
		
halt:
	jmp halt

```

# Official Sample Exam

##### Write an AVR assembly program to find the max value in an array. Each element is stored as a two-byte integer, and the array length is 10
```
.include "m2560def"

.def currentMax=r16
.def count=r17
.def tempH=r18
.def tempL=r19
.def maxL=r20
.def maxH=r21

.cseg
rjmp start
array: .dw 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

start:
	ldi ZH, high(array<<1)
	ldi ZL, low(array<<1)
	ldi count, 0
	lpm tempL, Z+
	lpm tempH, Z+
	inc count
	mov maxH, tempH
	mov maxL, tempL
loop:
	cpi count, 10
	breq halt
	lpm tempL, Z+
	lpm tempH, Z+
	inc count
	cp tempL, maxL
	cpc tempH, maxH
	brge updateMax
	rjmp loop
	
updateMax:
	mov maxH, tempH
	mov maxL, tempL
	rjmp loop

halt:
	rjmp halt
	
```

### Store the string 12345678 into program memory using .db and .dw and then store them into data memory in the reverse order. 

```
.include "m2560def.inc"

.def temp = r16
.def temp2 = r17

.dseg
array2: .byte 10
.cseg 
rjmp start
array: .db "123456789",'\0'

start:
	ldi r16, low(RAMEND)
	out SPL, r16
	ldi r16, high(RAMEND)
	out SPH, r16
	
	ldi ZL, low(array << 1)
	ldi ZH, high(array << 1)
	
	ldi YL, low(array2)
	ldi YH, high(array2)
	
	ldi temp, 0
	push temp

loadstack:
	lpm temp, Z+
	cpi temp, '\0'
	breq reverse
	
	push temp
	rjmp loadstack

reverse:
	pop temp
	cpi temp, 0
	
	breq finish
	
	st Y+, temp
	rjmp reverse
	
finish:
	rjmp finish

```

### Multiply a 8 bit and 16 bit value

```
.include "m2650.inc"

.def AH=r16 ; shifted
.def AL=r17
.def B=r18
ldi temp, 0
mul AH, B
mov XH, r1
mov XL, r0
mul AL, B
mov YH, r1
mov YL, r0
add XL, YL
adc XH, YH
mov temp, SREG
andi temp, 0b01000000
cpi temp, 0
breq noCarry
ldi carry, 1
noCarry:


```









