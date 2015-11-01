.globl start
start:
        movl $0x2F,  %r8d
        movl $0x34,  %r9d
        add  %r8d, %r9d
        movl %r9d, %edi
        movl $0x2000001, %eax
        syscall
