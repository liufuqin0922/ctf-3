# ctf

This is where I store CTF writeups I've made. 

## Pwn

#### ROP Chain
+ x64: bkp16/pwn/simple-calc Basic ROP Chain, syscall to execve("/bin/sh", NULL, NULL), Weird method of writing data to memeory
#### Return 2 System
+ x86: TUCTF/guestbook  Infoleak, PIE, strcpy
#### Faking Inputs
+ x64: bkp16/pwn/complex-calc pass false pointer to free and not crash, pointer is to bss

## Reverse Engineering (RE)

#### Dynamic Analysis
+ x64: bkp16/re/jit Use gdb to reverse obfuscated program, read breakpoints on input
