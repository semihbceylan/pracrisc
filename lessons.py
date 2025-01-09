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
    },
    {
        "title": "Von Neumann Architecture",
        "content": """
Von Neumann architecture is the foundation of modern computers. It consists of:
- **Control Unit (CU)**: Manages instruction execution.
- **Arithmetic Logic Unit (ALU)**: Performs arithmetic and logical operations.
- **Memory**: Stores data and instructions.
- **Input/Output Devices**: Allow interaction with external systems.

Key features:
- Uses a single bus for data and instructions.
- Executes instructions sequentially.
        """
    },
    {
        "title": "Memory Hierarchy",
        "content": """
Memory hierarchy organizes storage in a computer system based on speed and cost:
1. **Registers**: Fastest and smallest, located inside the CPU.
2. **Cache Memory**: Faster than main memory, divided into L1, L2, and L3 caches.
3. **Main Memory (RAM)**: Volatile memory used for active processes.
4. **Secondary Storage (HDD/SSD)**: Non-volatile memory for long-term storage.

The hierarchy ensures faster access to frequently used data.
        """
    },
    {
        "title": "Pipelining",
        "content": """
Pipelining is a technique to improve CPU performance by overlapping instruction execution stages:
- **Stages**: Fetch, Decode, Execute, Memory Access, Write Back.
- **Advantages**: Increases throughput and efficiency.
- **Challenges**: Pipeline hazards (e.g., data hazards, control hazards).

Example: A 5-stage pipeline can process multiple instructions simultaneously.
        """
    },
    {
        "title": "Instruction Set Architecture (ISA)",
        "content": """
ISA defines the set of instructions a CPU can execute. Key components:
- **Instruction Formats**: Fixed-length or variable-length.
- **Addressing Modes**: How operands are specified (e.g., immediate, register, memory).
- **Instruction Types**: Arithmetic, logical, control, and data transfer.

Examples of ISA:
- RISC (Reduced Instruction Set Computer): Simple, fixed-length instructions.
- CISC (Complex Instruction Set Computer): Complex, variable-length instructions.
        """
    },
    {
        "title": "Parallel Processing",
        "content": """
Parallel processing involves executing multiple tasks simultaneously. Types include:
- **SIMD (Single Instruction Multiple Data)**: One instruction operates on multiple data points.
- **MIMD (Multiple Instruction Multiple Data)**: Multiple processors execute different instructions on different data.

Applications: Graphics processing, scientific computing, and machine learning.
        """
    },
    {
        "title": "Cache Memory",
        "content": """
Cache memory is a small, fast memory layer between the CPU and main memory. Types:
- **L1 Cache**: Fastest and smallest, located inside the CPU.
- **L2 Cache**: Larger and slower than L1, often shared between cores.
- **L3 Cache**: Largest and slowest, shared across all cores.

Purpose: Reduces memory access time and improves performance.
        """
    },
    {
        "title": "Virtual Memory",
        "content": """
Virtual memory extends the apparent size of physical memory using disk space. Key concepts:
- **Paging**: Divides memory into fixed-size blocks (pages).
- **Page Table**: Maps virtual addresses to physical addresses.
- **Page Fault**: Occurs when a required page is not in RAM.

Benefits: Allows running larger programs and improves memory management.
        """
    },
    {
        "title": "Harvard Architecture",
        "content": """
Harvard architecture uses separate memory spaces for data and instructions. Features:
- **Separate Buses**: Data and instructions are accessed via different buses.
- **Advantages**: Allows simultaneous access to data and instructions, improving performance.
- **Disadvantages**: More complex design compared to Von Neumann architecture.

Commonly used in embedded systems and DSPs (Digital Signal Processors).
        """
    },
    {
        "title": "Control Unit (CU)",
        "content": """
The Control Unit (CU) is a component of the CPU that manages instruction execution. Functions:
- **Instruction Fetch**: Retrieves instructions from memory.
- **Instruction Decode**: Interprets the instruction.
- **Execution Control**: Coordinates data movement and ALU operations.

The CU ensures instructions are executed in the correct sequence.
        """
    },
    {
        "title": "Arithmetic Logic Unit (ALU)",
        "content": """
The ALU performs arithmetic and logical operations. Key operations:
- **Arithmetic**: Addition, subtraction, multiplication, division.
- **Logical**: AND, OR, NOT, XOR.
- **Shift Operations**: Left shift, right shift.

The ALU is a critical component of the CPU, enabling computation and decision-making.
        """
    },
    {
        "title": "Program Counter (PC)",
        "content": """
The Program Counter (PC) is a register that holds the address of the next instruction to execute. Functions:
- **Increment**: Automatically increments after each instruction fetch.
- **Jump**: Updated during control instructions (e.g., JUMP, BEQ).

The PC ensures the CPU executes instructions in the correct order.
        """
    },
    {
        "title": "Memory Address Register (MAR)",
        "content": """
The Memory Address Register (MAR) holds the address of the memory location being accessed. Functions:
- **Read Operations**: Specifies the address to read from.
- **Write Operations**: Specifies the address to write to.

The MAR is essential for memory access operations.
        """
    },
    {
        "title": "Secondary Storage",
        "content": """
Secondary storage devices provide non-volatile, long-term data storage. Examples:
- **Hard Disk Drives (HDD)**: Magnetic storage with high capacity.
- **Solid-State Drives (SSD)**: Faster and more reliable than HDDs.
- **Flash Memory**: Used in USB drives and memory cards.

Secondary storage is slower than primary memory but essential for data persistence.
        """
    },
    {
        "title": "CISC vs. RISC",
        "content": """
CISC (Complex Instruction Set Computer) and RISC (Reduced Instruction Set Computer) are two CPU design philosophies:
- **CISC**: Emphasizes complex instructions that perform multiple operations. Examples: x86 architecture.
- **RISC**: Focuses on simple, fixed-length instructions executed quickly. Examples: ARM, MIPS.

Comparison:
- CISC: Higher code density, more complex hardware.
- RISC: Simpler hardware, better performance for specific tasks.
        """
    }
]