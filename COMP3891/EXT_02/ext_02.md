# Extended Lecture 2

try atom, visual studio, etc.

 a context switch can refer to a switch betwen threads or processes. invovles saving and restroing of state. 
 
 when doing it with processes you need to switch the threads and the extra info associated with process, i.e memory maps. (this is called a full context switch)
 
 os161 only has threads, no processes. at least atm lmao we have to put that in 
 
spl stands for set priority level, allows us to meddle with interrupts. in the old days setting the priority too high means no interrupt could meet it and this interrupts are disabled. 

splhigh() disabled interrupts and returns the old interrupt level so it can be set. 

splx, sets the interrupt level. 

this is better then enable and disable because if yoi nest functions that play with it, each one will restore it back to what it was. 

don't use this in the assignments. 

if a critical section takes hours to run the interrupt blocking method will just cause a system wide pause.

spinlock aquire is a function that sets up a spin lock, i.e poll the lock until it's open instead of sleeping. 

HANGMAN_WAIT is a way to detect deadlock via a timeout

spinlock_aquire and release is just interrupt enable and disable for uniprocessor system. 

assert!!! do it!

lock_do_i_hold is better then lock_who_holds because by the time you know who owns the lock that info has changed. 

wchan is wait channel not w-chan lmao

each lock has a wait channel. 

the zombie state is just a stack which you cant destory within a thread. 

