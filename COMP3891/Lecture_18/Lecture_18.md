# Virtual Memory 2

## MIPS VM related exceptions
---

#### TLB Refill

TLB refill is handled by software via an exception handler in the mips. TLB refill expections accessing useg are expected to be frequent so the CPU is optiised for handling kuseg TLB refills by hacing a special exception handler just for this.

#### The Special Exception vector

At physical address `0x00000000` is for kuseg TLB miss's only. all other exceptions have the normal vector of `0x00000080`

Because of this the exception doesn't need to check what caused the exception, t's obvious. Furthermore we only need to use two regsiters `k0,k1` that are always to be used only her and thus we don't need to save any register state. small, fast. 
note it does not check if PTE exists it Assumes virtual linear array –
see extended OS notes. 

#### Others

Others still need to be handled but go through general exception handling

**TLB Mod** Is the TLB modify exception, attempt to write a read only page
**TLB Load** Attempted load from a page with a invalid translation
**TLB Store** Attempt to store to a page with an invalid translation.

Note that we have a register `c0_badvaddr` is the 
Note: these can be slower as they are mostly either caused by an error, or non-resident page. Page-loads from disk dominate the fault resolution cost so really not worth setting up special vectors and as a general rule:

> We never optimise for errors, it's never worth it

#### Amdahl's Law

States that overall performance improvement is limited by the fraction of time an enhancement can be used. 

If we only run a code 5% of the time but double it's speed it isn't that great. 

\\(Speedp={ExecutionTimeWithoutEnhancement\over ExecutionTimeWithEnhancement}\\)

#### The TLB and EntryHi,EntryLo

Each TLB entry contains EntryHi to match Page# and ASID and EntryLo which contains frame# and protection. 

we can use the c0 registers `c0_EntryHi, c0EntryLo, c0_Index` to interact with the TLB. the index being the table line. 

#### Special TLB management Instructions

- TLBR
    - TLB Read, EntryHi and EntryLo are set from index register
- TLBP
    - TLB probe
    - index is loaded with the value of a line that matches the current EntryHi
- TLBWR
    - Write EntryHi and EntryLo to a psudorandom location
- TLBWI
    - Write EntryHi and EntryLo to the location in the TLB pointed to by the Index register

usually we just use random, working out where to replace and why is too much work and just replacing a random one usually works out being way faster and fine for most cases

#### Coproc 0 registers on a refil exception

Instr | value
--- | ---
c0.EPC | PC
c0.cause.ExcCode | TLBL ; if read fault
c0.cause.ExcCode | TLBS ; if write fault
c0.BadVaddr | faulting address
c0.EntryHi.VPN | page number of faulting address
c0.status | kernel mode, interrupts disabled.
c0.PC | 0x8000 0000   

#### TLB miss handling

What software does is look up the PTE (in main memory) corresponding to the faulting address, if it's found we load c0_EntryLo with translation and use TLBWR. If not found page fault. 
We could create the EntryLo 32 bits but why do that when we can load up the PTE with the preformatted ready to go EntryLo. This is what we do. 

Now in OS161 there is none of this. 

After switch to kernel stack, it simply calls the common exception handler
– Stacks all registers
– Can (and does) call ‘C’ code
– Unoptimised
– Goal is ease of kernel programming, not efficiency

It does not have a page table, It uses the 64 TLB entries and then panics it runs out. Only supports 256K user level address space. 

## Demand Paging/Segmentation
---

With VM, only parts of the program image need to be resident in memory for execution, we can transfer presently unused pages/segments to disk and reloaded them when needed, i.e on demand.

Of course doing this we may need to free some programs in memory before swapping one from disk in. This is where we have some page replacement policies where we choose which page (the victim) is gonna go. 

Note we call a victim clean if it's unmodified since the last time we brought it in from disk, i,e we don't have to write it into disk, it's already there on disk we just replace it. Hence why we have the ""dirty"" bit. 

#### Why does this work?

The program executes at full speed only when accessing the resident set, TLB misses introduce delays of several microseconds as so page/segment faults. 

So why do it? It means we need less physical memory required per process.  Improved chance of finding a runnable one and we can pack more process into memory. 

Furthermore the prinicple of locality holds. This principle states that a program spends 90% of times in 10% of it's code. Keep that 10% in memory and we are good. 

We can reasonably predict what instructiosn and data a program wil use in the near future based on the past. So we can make this work well. 

#### Locality

There are two types of locality

1. Temporal locality, if i accessed something in the last second i will access it again
2. Spatial locality, things close together can accessed together

Research shows that both of these hold somewhat well for paging. 

#### Working Set

The pages/segments required by an application in a time window (∆) is called its memory working set.

Working set is an approximation of a programs’ locality

- if ∆ too small will not encompass entire locality.
- if ∆ too large will encompass several localities.
- if ∆ = ∞ it will encompass entire program.
- – ∆’s size is an application specific tradeoff

System should keep resident at least a process’s
working set cause the process executes while it remains in its working set

Working set tends to change gradually as it gets only a few page/segment faults during a time window. It's possible (but hard) to make intelligent guesses about which pieces will be needed in the future and use this to be able to pre-fetch page/segments
















