import numpy as np
from interleaver import Interleaver
from trellis import Trellis

class TurboDecoder:

    def __init__(self):
        self.trellis = Trellis()
        self.interleaver = Interleaver()

    def decode(self, encoded_message: np.ndarray):
        parity_systematic_part = np.array([encoded_message[i] for i in range(encoded_message.size) if i % 3 != 2], dtype=int)  # pick systematic and parity bits from the encoded message 
        interleaved_part = np.array([encoded_message[i] for i in range(encoded_message.size) if i % 3 == 2], dtype=int)  # interleaved parity bits


        decoded_1 = self.trellis.viterbi(parity_systematic_part)  # this will now serve as systematic bits to the interleaved encoded part
        encoded_interleaved_message = np.zeros(parity_systematic_part.size, dtype=int)

        # don't forget to interleave it as well!
        decoded_1 = self.interleaver.interleave(decoded_1)
        for i in range(decoded_1.size):
            encoded_interleaved_message[2*i] = interleaved_part[i]
            encoded_interleaved_message[2*i + 1] = decoded_1[i]

        decoded_message = self.trellis.viterbi(encoded_interleaved_message)


        decoded_message = self.interleaver.deinterleave(decoded_message)
        
        return decoded_message
    

