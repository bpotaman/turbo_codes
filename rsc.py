from collections import deque
import numpy as np

class EC1:

    def __init__(self):
        self.registers = deque([0, 0])

    def iter(self, input_bit):
        bit_1 = input_bit ^ self.registers[0] 
        bit_2 = input_bit
        self.registers.rotate(1)
        self.registers[0] = input_bit ^ self.registers[0] ^ self.registers[1]
        return bit_1, bit_2
    


class EC2:
    def __init__(self):
        self.registers = deque([0, 0])
    
    def iter(self, input_bit):
        bit_1 = input_bit ^ self.registers[0] 
        self.registers.rotate(1)
        self.registers[0] = input_bit ^ self.registers[0] ^ self.registers[1]
        return bit_1
