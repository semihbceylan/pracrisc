LESSONS = [
    {
        "title": "Introduction to RISC",
        "content": """
RISC (Reduced Instruction Set Computer) is a type of microprocessor architecture
that uses a small, highly optimized set of instructions. Key features of RISC include:
- Simple instructions that execute in one clock cycle.
- A large number of registers.
- Load/store architecture (only load and store instructions access memory).
        """
    },
    {
        "title": "Registers and Memory",
        "content": """
The RISC simulator has:
- **32 General-Purpose Registers**: R0 to R31.
- **Memory**: A dictionary that maps addresses to values.

Example:
- Registers: R0 = 10, R1 = 20, R2 = 30
- Memory: {100: 10, 104: 20, 108: 30}
        """
    },
    {
        "title": "Arithmetic Instructions",
        "content": """
Arithmetic instructions perform mathematical operations on registers.
Examples:
- **ADD**: Add two registers (e.g., ADD R1, R2, R3 → R1 = R2 + R3).
- **SUB**: Subtract one register from another (e.g., SUB R1, R2, R3 → R1 = R2 - R3).
- **MUL**: Multiply two registers (e.g., MUL R1, R2, R3 → R1 = R2 * R3).
- **DIV**: Divide one register by another (e.g., DIV R1, R2, R3 → R1 = R2 / R3).
        """
    },
    {
        "title": "Logical Instructions",
        "content": """
Logical instructions perform bitwise operations on registers.
Examples:
- **AND**: Bitwise AND (e.g., AND R1, R2, R3 → R1 = R2 & R3).
- **OR**: Bitwise OR (e.g., OR R1, R2, R3 → R1 = R2 | R3).
- **XOR**: Bitwise XOR (e.g., XOR R1, R2, R3 → R1 = R2 ^ R3).
- **NOT**: Bitwise NOT (e.g., NOT R1, R2 → R1 = ~R2).
        """
    },
    {
        "title": "Data Transfer Instructions",
        "content": """
Data transfer instructions move data between registers and memory.
Examples:
- **LOAD**: Load data from memory into a register (e.g., LOAD R1, 100 → R1 = Memory[100]).
- **STORE**: Store data from a register into memory (e.g., STORE R1, 100 → Memory[100] = R1).
        """
    },
    {
        "title": "Control Instructions",
        "content": """
Control instructions change the flow of execution.
Examples:
- **JUMP**: Jump to a specific instruction (e.g., JUMP 8 → Set PC to 8).
- **BEQ**: Branch if two registers are equal (e.g., BEQ R1, R2, 10 → If R1 == R2, jump to instruction 10).
- **BNE**: Branch if two registers are not equal (e.g., BNE R1, R2, 10 → If R1 != R2, jump to instruction 10).
- **HALT**: Stop execution.
        """
    },
    {
        "title": "Shift Instructions",
        "content": """
Shift instructions perform bitwise shifts on register values.
Examples:
- **SLL**: Shift left logical (e.g., SLL R1, R2, 5 → R1 = R2 << 5).
- **SRL**: Shift right logical (e.g., SRL R1, R2, 5 → R1 = R2 >> 5).
        """
    }
]