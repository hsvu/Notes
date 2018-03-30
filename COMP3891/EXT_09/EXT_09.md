# Virtual Linear Array Page Table

It's like a 2 level page table but all in virtual table. Means we can do it in 1 lookup as we can index in the array. 

It's in the virtual address space so even if the array is 500 GB but if frames are empty then physical frames arn't allocated there. 

The root Page table is kept in physical memory.

the context register simply loads the Page table entry by indexing off the page table entry start point. 

ccasionally will get a double fault. User faults to os saying memory doesn't exist, Kernel tries to look up the page and faults because that page entry doesn't exist which then goes down to the physical 4k level one table, it assigns a page table entry which then maps to physical memory. 

C0 Context register contains the Base of the PTE and the VPN. 

C0_Context = PTEBase + 4*PAgeNUmber (32 bit page table entries)

whenever we fault this is loaded up already with what to look up. 

Tapeworm lets u take a stream of tlb misses and have a virtual tlb simulated. 

OSF1/Mach 3.0 have 3 levels of table but have the 2 deeoer ones in virtual memory. 

Ultrix and OSF/1 used virtual memory for various data structures. Mach 3.0 was exerminting pushing file system and nerworking and scheduling not in the kernel, this was called a micro kernel. 

Itanium Page Table. Takes a bet. 