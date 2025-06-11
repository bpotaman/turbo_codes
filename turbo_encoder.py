import numpy as np
from rsc import EC1, EC2
from interleaver import Interleaver

class TurboEncoder:

    def __init__(self):
        self.ec1 = EC1()
        self.ec2 = EC2()
        self.interleaver = Interleaver()

    def encode(self, message: np.ndarray):
        encoded_message = np.zeros(3 * message.size, dtype=int)
        interleaved_message = self.interleaver.interleave(message)
        a = []
        """
        Array of size x has the last index equal to x-1, array of size 3x, has the last index 3x - 1.
        In the for loop, for i = x -1, we have 3(x - 1) + 2 = 3x - 1, which is the last index of this bigger array, so we don't go out of bounds
        """
        for i in range(message.size):
            input_bit_ec1 = message[i]
            input_bit_ec2 = interleaved_message[i]
            encoded_message[3 * i], encoded_message[3 * i + 1] = self.ec1.iter(input_bit_ec1)
            encoded_message[3 * i + 2] = self.ec2.iter(input_bit_ec2)
            a.append(encoded_message[3*i])
            
        
        return encoded_message
            


