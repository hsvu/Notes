# Extended Lecture 10, Assignment 3 Intro

## Pointer Recap
---

lets assume we have 4-bit addresses, i.e we have address range from 0-15

remember that if you write a int at address 4 it actually writes into address 4 5 6 and 7 because ints are 4 bytes long. 

(a lot of this is just how c handles pointers, nothing special)

## Intro
---

Has two parts
1. Frame Table (An allocator for physical memory)
    - Test Heavily if this fucks up, everything else fucks up in placed that makes it hard to trace the problem back 
2. Page table and region support
    - virtual memory for applications

There are some tests in the wiki that are ok. 

you can edit the os161 max ram to test your program with running out of memory. 

There is a macro defined for converting physical and virtual addresses into each other which adds or subtracts the needed offset. PADDR_TO_KVADDR converts a physical address into a kernel virtual address. 

ram_getfirstfree() gives you the bump allocator, you should only use it once and from that point onwards take over allocation. 

You can assume that only 1 page at a time, i.e they don't ask for >4k. if it's more then 1 page, return NULL. 

free frame table should be a liked list. 

we can place the frame table at the top of free ram and then decrease free frame size 

YOu can also place it at the bottom and use the bump allocator, this is a little encouraged this year. 

you can have frametable be t0 begin with and we can detect this as a signal to "use the bump allocator cause the actual stuff does'nt exist yet"

load_elf is good to read. you can use -objdump to get location info of memory. 

bin true is a good starting test program, thereis also huge which allocates HEAPS. 

