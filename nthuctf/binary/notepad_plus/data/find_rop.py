from pwn import *

bin = ELF("../notepad_plus")
rop = ROP(bin)
print(rop.gadgets)

# for i in rop.gadgets:
#     print(i)

rop.find_gadget(["pop rdi", "ret"])