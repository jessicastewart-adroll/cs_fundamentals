.segment __DATA,__bss
  sum resb 1

.segment __TEXT,__text
.globl start
start:
        movl $0x2F,  %r8d
        movl $0x34,  %r9d
        add  %r8d, %r9d
        movl %r9d, %edi

        movl [sum], eax
        movl ebx, 1
        movl eax, 4
        syscall

        movl ecx, sum
        movl $1, %edx
        movl $1, %ebx
        mov eax, 4
        syscall

        movl $0x2000001, %eax
        syscall
