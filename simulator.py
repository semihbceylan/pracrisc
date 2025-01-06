class RISC_Simulator:
    def __init__(self):
        self.registers = {f'R{i}': 0 for i in range(32)}  # 32 general-purpose registers
        self.memory = {100: 10, 104: 20}  # Initialize memory with some values
        self.pc = 0  # Program counter
        self.halted = False  # Halt flag

    def run(self, code):
        """Run the given RISC assembly code."""
        self.halted = False
        instructions = code.split('\n')
        while not self.halted and self.pc < len(instructions):
            line = instructions[self.pc].strip()
            if not line:
                self.pc += 1
                continue
            self.run_instruction(line)
            if not self.halted:
                self.pc += 1  # Move to the next instruction unless halted or jumped

    def run_instruction(self, line):
        """Run a single RISC instruction."""
        parts = line.replace(',', '').split()
        parts = [part.upper() for part in parts]
        if not parts:
            return  # Skip empty lines

        instruction = parts[0]
        try:
            if instruction == 'ADD':
                self.registers[parts[1]] = self.registers[parts[2]] + self.registers[parts[3]]
            elif instruction == 'SUB':
                self.registers[parts[1]] = self.registers[parts[2]] - self.registers[parts[3]]
            elif instruction == 'MUL':
                self.registers[parts[1]] = self.registers[parts[2]] * self.registers[parts[3]]
            elif instruction == 'DIV':
                if self.registers[parts[3]] == 0:
                    raise ValueError("Division by zero")
                self.registers[parts[1]] = self.registers[parts[2]] // self.registers[parts[3]]
            elif instruction == 'AND':
                self.registers[parts[1]] = self.registers[parts[2]] & self.registers[parts[3]]
            elif instruction == 'OR':
                self.registers[parts[1]] = self.registers[parts[2]] | self.registers[parts[3]]
            elif instruction == 'XOR':
                self.registers[parts[1]] = self.registers[parts[2]] ^ self.registers[parts[3]]
            elif instruction == 'NOT':
                self.registers[parts[1]] = ~self.registers[parts[2]]
            elif instruction == 'LOAD':
                address = int(parts[2])
                self.registers[parts[1]] = self.memory.get(address, 0)
            elif instruction == 'STORE':
                address = int(parts[2])
                self.memory[address] = self.registers[parts[1]]
            elif instruction == 'JUMP':
                self.pc = int(parts[1]) - 1  # Subtract 1 because pc increments after
            elif instruction == 'BEQ':
                if self.registers[parts[1]] == self.registers[parts[2]]:
                    self.pc = int(parts[3]) - 1  # Subtract 1 because pc increments after
            elif instruction == 'BNE':
                if self.registers[parts[1]] != self.registers[parts[2]]:
                    self.pc = int(parts[3]) - 1  # Subtract 1 because pc increments after
            elif instruction == 'SLL':
                self.registers[parts[1]] = self.registers[parts[2]] << int(parts[3])
            elif instruction == 'SRL':
                self.registers[parts[1]] = self.registers[parts[2]] >> int(parts[3])
            elif instruction == 'HALT':
                self.halted = True
            else:
                print(f"Unknown instruction: {instruction}")
        except (IndexError, KeyError, ValueError) as e:
            print(f"Error executing instruction: {line}")
            print(f"Details: {e}")