# Extended Lecture 11, More Ass 3 Tips

address space functions are called for each for the sections of code, we have to keep track of what is assigned so we our vm_fault knows what's going on. 

There are sections for code, data, the user stack etc. 

walk through EFL loader is a good thing to read...

as_preapre_load() should make READONLY regions READWRITE for loading purposed and when as_complete_load() turn it back all. 

We remove a page from the page tables in as_destory. 

we don't care about freeing memory for the os shutting down. 
we only really want to free memroy that we can reuse usefully. 

the slides go through all of the address space functions .

rip the code for as_activate from dumb_vm

you can have as_deactivate call activate. 

there is a good flowchart of how VM Fault works. 

don't use kprintf() in the vm_fault(), kprintf() blocks the current process while printing, this calls a context switch which empties your table that you just filled lmao. 

use trace161 !!

note as_copy is where we do shared paged, you don't copy it for read only segements and also all the time, just copy it when one tries to use it. 

 there does need to be a reference count in the frame table then because of this. 

 ADVANCED COMPONENTS HAS TESTS!!! 

 

