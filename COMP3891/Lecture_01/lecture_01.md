
# Course Information

## Interesting Facts
---

C is the dominent language for OS and embedded systems

In code such as 

```c
int *a, *b;
```

Will just set up two pointers but not initialise them and thus a and b point to random places because they hold junk data. **wow**

## Assignments
---

We use OS/161 which was develoepd by the Systems Group at Harvard and contains roughly 20,000 lines of code and comments. 

A lot easier then unix, there are missing parts that we get to code up!

80% is understanding and 20% programming, less coding, more understanding. write code that you are somewhat sure works. build it up slowly. 

There is a warmup excersize that is due monday week 4 8am.
the main goal of this is to set up a build enviornment and code navigation system because there are 300 files and you need to hop between easily. 

vim emacs, sublime -> nail one down and have it set up so you can hop to a function defintion with one click and not look for the file. 

## Textbook
---

Andrew Tanenbaum Modern Operating Sytems 3rd and 4th addition prentice hall -> a good read apparently

# Introduction to Operating Systems

## Role 1 of the OS
---

> The operating system is an abstract machine

An os provides high level abstractions and extends basic hardware with added functionality. It allows a common core for all applications and allows the details fo the hardware to be hidden away. Makes application code portable, code can be cross computer because the os handles the direct interfacing with cards. 

## Role 2 of the OS
---

> The operating system is responsible for allocating and mediating resources between competing users and processes. It helps prevents world war `0011`

It must ensure no starvation of resources, progress (doesn't halt) and that allocation is according to some desired policy, first come first server or maybe weighted fair share it depends on the context. 

Overall the os must make sure the system is efficiently used. 

## Role 3 of the OS
---

> The os must enforce the "extended" machine, seperating itself from applications so it can enforce resoure allocation policies and prevent applications from interfeting with each other. 

The operating system is the nucleus or supervisor of the system because it is a privilaged (not user) system.

Applications should not be able to interfere or bypass the os. 


## Computer Structure
---
#### Basic

The operating system Kernel is the portion of the operating system that is running in privileged mode, it resides in main memory and contains fundamental functionality that other applications are built on. As such it must handle security as any application should not be able to break through the os to manipulate hardware. 

This means usually a computer system is split into user and kernal mode. user mode is what applications run in but a kernal mode is what the os runs in. 

When you call malloc or printf you are calling system libaries that interact with the os which is the only thing that can access devices and perriphals.
in some cases some applications do get access to devices exactly for example in frame buffers where going through the os would take too long for a time critical application. 

> The OS is the big dog

The os interacts with load and store instructions to all memory, cpu and devices registers and interrupts. any sort of hardware interaction goes through it
Note that this os code is not special, it's normal C code but the code just runs in privilged mode which makes it different. 

#### System Libraries

Now Applications interact with themselfes and system libraries but system libraries make `system calls` to the os in the kernal. 

Sometimes the system libraries don't need to interact with the os like mem copy, which you could code yourself, the os isn't need to move memory from one place to another. 

But some functions need to get the os involved. printf for example uses the write system call so the os can output something to a file or to the terminal. 
The system call does return something, either a success or error message or data if you are having a read system call. So the system libraries just act as a wrapper to help faciliate these system calls easier. 

system calls functions are in the library for convience if you want to use them directly

```bash
man syscalls
```

#### Privilege-less OS
Some Embedded OSs have no privileged component – e.g. PalmOS, Mac OS 9, RTEMS

These work the same as usual but without seperating, the os can not enforce any rules but only implement the abstractions as suggesting. 
Because all the code runs in a single memory space is a application goes down and crahses or is buggy, it all goes down, the od can't enforce each application to be seperate and isolated. 

> If i go down i'm taking you all with me

lmao i guess that means in some instances privilege is good

#### Operating System Software

The os is simple normal code, but it has to relinquishes control of the processor to execute other programs. This is done with the pretense/assumptions that the os will reestablish control after some system call from the application or through a interrupt (the os must come in to do something every 50 seconds and will shove aside application code or if someone plugs in a usb)

Do note that even though it is simple C you do not have the standard libraries because you are in the os. you can't use malloc in the os if malloc asks the os for memory. 

<img src="simpsons_1.jpg">

#### Structure
If you see a outline of os where it's just a simple onion like layered system, run. That is outdated and not right. If you see that in a book and keep reading it's all ogre from there. `I HAD TO I'M SORRY`

IN practice layering is only a guide, Operating systems have many interdepencies. the scheduling will rely on virtual memory and the vm will rely on I/o and rely on files but files rely on Vm etc etc.

It's not exactly a spaghetti nest but rather closer to a reasonable stucture of dependecy. This can be called `The Monolithic Operating System Structure`

## Major OS Concepts Overview
---

#### Processes
A program in execution. In essence a unit of resource ownership. A process id just tags something as having some amount of resource at the moment. 

A process does not have to be a program or have to be executing something. 
A process is loaded with code, it's seperate.

Note that for the os/161 only has 4k big stack, so avoid recurrsion in your os code. You will blow out the stack lmao

#### Process State
Consists of three components

- The program code
- The data needed by the program
	- Data
	- Stack 
- The execution context of the program
	- registers
	- program counter 
	- stack pointer 
	- internal os variables 
		- files that are open
		- etc. 

#### Memory Management

All about isolating processes so they can't access each others memory and also automatic alocation and amnagement of memory so users don't have to deal with data structures and physical memory. 

On top of this the os also has to handle protection and access control so every process can't just go wherever. 

and there is of course virtual memory and file systems

#### Virtual Memory

This allows programers to address memory from a logical point of view, it lets you use memory as if it makes sense. It's simple from `0x00000000` to `0x10000000`. 
This is not how physical memory works, this is a lie. an illusion. 

THE os gives logical addresses independent of other process and lets the user have the illsuion of have a lot of ram eventhough physically there isn't. 

It also allows processes to feel like they are in memory but really the os just is switching between giving both access quickly.

Because of all of this stuff the os has to handle, most microprocessors has a memory management unit that transltes program memory addresses into main memory addresses. It does this in real time at incredible speed. 

#### File Systems
Implements long term storage and helps organise data into objects called files. 
This lets us have meaningful names and structures to represent our data. 


#### Scheduling and Resource Management

This is to do with allocating processing cpu time and you want this to be fair to all processes but of course sometimes you want to have `differential responsiveness` to prioritise jobs and of course we always want to maximise efficiency. Maximising throughput and minimize response time and accomodate as many users as possible. 













