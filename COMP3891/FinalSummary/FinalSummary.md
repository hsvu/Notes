role of a os  is to be an abstract machine, mediate resurces seperat eitself form applications to it can enforce allocation and prevent applications from interfering with each other. 

some embedded OS's have no privileged component, this is easier to program and doesn't require hardware or seperate memory but if a application goes down so does the os. THe os is more of a abstraction then a enforcer of policies. 

The Monolithic Operating System Structure is not spaghetti but nota onion. 

process state has 3 parts, code, data(heap/stack) and context (PC, registers etc.)

4 main things system calls allow for
	1. process management (fork)
	2. file I/O
	3. Directory management
	4. other

r31 return address, 
v0 -> syscall number
a3 -> 0 if success else 1
v0 -> -1 if err and v0 moved to errno

c0_cause – Cause of the recent exception
there are many such as interrupt or syscall etc.
c0_status – Current status of the CPU
c0_epc – Address of the instruction that caused the exception (pc)

3 states a process can be in?
1. running
2. ready
3. blocked

PCB -> process control block. 
holds file stuff, process id, PC, process registers. etc.
each thread then has PC, stack, registers. pending alarms are handled by the process though. 

global variabels are global between threads because they arn't on the stack. huh.

memory is shared between threads and threads can access each others memory. 

finate state is just async all the way. 

why threads?
1. more threads is less costly then more processes.
2. threads can share memory easily.
3. slow I/O doesn't stop the process in it's tracks just a thread.
4.  threads can take advantage of multi core systems. 

A good solutioon to concurrency has 3 parts. mutual exclusion, doesn't make assumptions on cpu type, number, or speed, allows progress by ensuring only 1 process can hold a lock at one time and is bounded, i.e it's not possible for a process to wait forever because some asshole won't give up the lock. 

strict alternation uses busy loops to basically move a token around all the processes that need it. only 1 process cna have the token at a time and all others will wait their turn. This is as fast as the slowest member as they have to pass the token along. 

why don't we turn off interrupts?
we can only do this in the kernel, it blocks everything else including something like a network card that will drop pakcets if not allowed to run and doesn't work on multiprocessors as you have to cordinate turning off interrupts on all CPU's

issues with spinlocks using TSL 
livelock: when a low priority process has a lock but because the cpu always picks the higher priority program to run it never runs the lower one so it can release it and the higher one just waits for the lower one to release it. 
Busy loop
Starvation is possible as when 1 lock released and there are multiple waiting there is no queue built in. One process may by change never get the lock. 

P() test V() increment  -> semaphores

what are the 4 conditions of a dead lock?

Mutual exclusion condition
	each resource assigned to 1 process or is available
Hold and wait condition
	process holding resources can request additional ones without giving up what it currently holds
No preemption condition
	no one can take the lock from you without your consent
Circular wait condition
	it's possible for two process to rely on locks that the other hold.


4 ways to deal with deadlock?

1. Just ignore the problem altogether
2. prevention
	negating one of the four necessary conditions
	- mutual exclusion is needed
	- hold and wait could be taken down by making processes state what they need before running it grabs everything before running. prone to live locks as we release some resources to get more then we try to get those but release the previous ones etc. 
	- we need premption
	- ciruclar wait can be combatted if we addign a numerical order to every resource so the printer must always be held before the scanner etc.
	If B has resource 2 it's not allowed for it to get resoucre 1 it has to get 1 first. As a result id B has resource 1 all other processes must not need 1 AND be already holding a lock. otherwise they would have requested it first. 
3. detection and recovery
	matrix. once detected we can remove a resource from other processes to free them up. it's hard to tell what NOT to take the lock from. 
	we can also rollback to a checkpoint and try again hoping that by chance it doesn't deadlock again. 
	We can also just kill the process to break the deadlock and restart it. 
4. dynamic avoidance
	careful resource allocation -> needs info on max resources needed
	resource trajectories
	nobody every really knows the max resources lmao

user-level threads?
good cause it's simple and fast, switching between threads is lightning. you can have it on a os that doesn't support it and customise it as you need. you can also use virtual memory to incease max thread count! in the kernel this is harder and usually there is just a set physical table of threads and the such. 

bad cause kernel has no idea so if one blocks on a I/O it'll block them all. also no timer interrupts to make thread give up control, you can use the kernel timer interrupt but it's too coarse grain , you can only do it to the nearest second which is too slow for any real thread switching. 

overview of context switch?

1. hardware stacks program counter and where the current thread is up to
2. hardware loads new program counter form inurrupt vector (move in kernel)
3. assembly saves registers
4. assembly sets up new stack
5. C interrupt service runs
6. scheduler decides which process to run
7. C process returns to assembly
8. assembly starts up new process.  

3 types of files

1. byte sequence
2. record sequence (set size blocks)
3. key based tree structured. (key specifes file which can have children)

most os uses 1. at the hardware/code level but builds up levels of abstraction so user's think it's 2 or 3. 

2 types of file access

secquential -> awesome for magnetic tape
random access -> essential for data base systems. 

why may you want append not write. write lets you trash the file whereas append only leets you add, useful for log files. 

ELF file structure

The Header is fixed and describes the file and properties. The program header table holds offsets and sizes of parts of the program that you can load into main memory. Lets you segment the file.

The section header table does largely the same but for each section of the file. program headers splits into sections which the section header table helps us understand and use.

things to consider with file organisation
rapid access: needed if we only want to access 1 record but not if we are reading start to end
ease of udpate: important but not if we are writing to a CD ROM (burn the data on no editing)
Economy of storage: should be minimum redundancy in the data. 

why so many file systems?
Ext3 is optimised for magnetic disks ISO9660 is best of CDROMS, i.e this doesn't have to worry about being writer/edited JFFS2 is optimised for flash which can be edited etc.
Furthermore storage capacities cause new file systems to be built such as Fat 32 which could support drives above 2GB. FAT32 can not do anything larger then 32GB though.
Furthermore there are issues with CPU and memory requirements, FAT16 is not suitable for modern PCs but it is a good fit for many embedded devices.

conting allocation -> external fragmentation, fast reading/writing, simple, need max file size. 

LL allocation -> great for sequential files, small amount of meta data. sucks for random access and you have to seek a lot.

FAT file system -> file allocation table system -> table of blocks each entry contains the index of the next block, much faster to search. 
Needs entry for every block -> lots of meta data in memory + ram when being used. also still seeking through large tables. note 2 copies because it's critical. 

inode -> bitmaps are easier to find contigious spaces (look for string of 0s)

ext2 -> file checker after random crash is very slow, only stores the start and end of a file, not empty blocks inbetween, size is max index, block count included meta deta. 

s5fs -> System 5 Disk layout has boot block to bootstrap Os and super block which contains info on the file system itself. Then the inode arrray then the data . slow cause inode is at the start of disk and data block are near the end so lots of seeking. single point of failure with super block. free list ends up linking fragemented blocks which is seek heavy. 

FFS/EXT2FS -> partitions disk into groups + boot block. all blocks are equal size. each block has super block info (many copies), has data blocks a innnode table and descriptor fields. the super block keeps track of shitty shut downs and autmatically calls the file system checker if needed.

all seeking is done withing a block which is vry fast. optimises so releated memory blocks are in the same FS block. i.e 1 thread keeps writing to the same place. furthermore every write also "reserves" 8 blocks after it. So if someone wrote 1 block then 7 more they would be guarenteed to be contigious. 

directories takes names -> inode numbers (indexes) [inode no, rec legnth, name length, name] rec legnth is number of ytes to skip to get to next one. 

we can only hardlink files we own so soemoen else doesn't and blocks u from deleting shit. 

ext3 fs -> journaling

Disk arm -> FIFO, Shortest Seek Time First (may starve), Elevator (SCAN) (not sequential on back read)

There are three basic schemes with VM page tables

Use a structure that adapts to sparsity -> Teo level
Use a structure which only represents resident pages that are used -> inverted page table. 
Use VM techniques for pages tables (covered in EOS)

process vm -> hardware interfaces with OS which supports a VM
system vm -> hardware interfaces with Vm to support a OS. 

os -> security bugs means vm is useable

the VMM had to handle the CMS ""system calls"" and make sure the CMS thinks the system calls is going straight to hardware. it emulated the calls but really managed the hardware so one os didn't do shifty stuff in privilege.

the performance is near bare hardware though. the idea is lots of math isn't that bad, is quick, but if you do i/o and have to take a extra trap to pass through the VM it hits harder.

compute bound is fine but IO bound gets slower.

type 1 -> native Hyperwiser, system VM, runs in privileged mode, guest OS runs in non-privileged mode. the hypervisotr may implement the virtual kernel and user mode for the guest os or the cpu may have 3 modes (hypervisor, gues os mode, application mode)

type 2 -> hosted hypervisor. process VM, runs as user-mode. relies on the OS and passes request through. If os crashes so does the VM. 

LFS -> great + fast for small files + fails cause of cleaning overhead. 






















