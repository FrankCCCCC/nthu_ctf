shellcode = asm("""
xor     eax, eax;
push    eax;
push    0x68732f2f;
push    0x6e69622f;
mov     ebx, esp;
push    eax;
mov     edx, esp;
push    ebx;
mov     ecx, esp;
mov     al, 11;
int     0x80;
""")
runner = run_shellcode(shellcode)
runner.interactive()
runner.wait_for_close()
runner.poll()