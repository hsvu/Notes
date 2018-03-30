# Extended Lecture 3 (THIS CAN BE TESTED)

This is a lazy lecture, the slide numbers are given and any additional comments added. 

`25`

Every sensitive instruction should cause a trap into the hypervisor.
 
`27`
trap the sensitive or privileged instruction and emulate it's activity. 

i.e  disabling the interrupts just means that the internal timer interrupts are turned off in the hypervisor. 

One way the VMM/Hypervisor can handle this by having a set of variables per os which represent stuff like coprocessor 0 status registers

Then the VMM can force the system to never jump to the general interrupt vector so it looks like to the machine there are 0 interrupts. 

`28-29` it's sorta privileged not entirely. The EFLAGS register is available from user and kernel. What it did was not raise an exception but silently ignore any change made to sensitive registers. Which meant that it was impossible to tell as no exception was raised. This was not virtualisable. 
VMWare actually did fix this with binary rewriting. Every time it loaded a kernel page it replaced every pop stack setting the IF FLAG in the register with a actual call to the hypervisor. amazing. 

## Scheduler Activation
---

`8`

It is incredibly quick to do user level threads, like so quick, order of magnitude quicker the kernel threads. oh god and making a new process for every thread my fucken god so slow. 

`9`

here the Scheduler acts as the bridge, it assigns one of its 3 internal threads onto 2 of the available kernel threads. 

n on m threading (used in windows fibres)

here we create the kernel threads first so we don't have to recreate that, it's a bit slower at start time but then literally nothing because after they are created the internal code the kernel thread runs is swapped out by the user Scheduler. 

There is a issue though because if both the kernel threads block the 3rd internal user thread is blocked as well. Moves the problem back a bit but it's still there. You have to tune the number of n to m to make it work 

`11`

the idea is having the user and kernel schedule communicate. 
this is self tuning. 

`12`

a normal system is a downcall, the user calls to the os, transitions, runs code then returns. 

a upcall is when the OS wants to give the control to the application it actually just returns exeuction at a well known SET entry point and before going there gives the application some info on where it was before i,e registers stack pointer etc. 

the application then figures out what it wanted to do, the entry point is usually the sceduler.
The application can restore or switch. 

`15`

basically instead of assuming the thread can't do anything until the system call finished the os goes "hey user, i'm gonna be a while, you can do some other stuff while you wait"

when the os is done it goes "hey bro the guy who was previously blocked is fine, you should prob deal with the fact that your hypothetical thread that was running before finished"

note that the kernel thread is what gets blocked it just lets the user level handle that. 

`16`

virtual CPU = kernel thread

preempted is "user yo, i'm fucking with you and taking a kernel thread, deal with it"

`17-27`
the system PROVIDES for another kernel thread to the process if one blocks. 












 
