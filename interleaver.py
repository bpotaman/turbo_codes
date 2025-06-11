import numpy as np

class Interleaver:

    def interleave(self, message):
        M = np.array(message).reshape(int(message.size/2), 2)
        interleaved_message = np.zeros(shape=(message.size), dtype=int)
        k = 0
        for j in range(len(M[0])):
            for i in range(len(M)):
                interleaved_message[k] = M[i][j]
                k += 1
        
        return interleaved_message
    
    def deinterleave(self, interleaved_message):
        M = np.array(interleaved_message).reshape(2, int(interleaved_message.size/2))
        deinterleaved_message = np.zeros(shape=(interleaved_message.size), dtype=int)
        k = 0
        for j in range(len(M[0])):
            for i in range(len(M)):
                deinterleaved_message[k] = M[i][j]
                k += 1
        return deinterleaved_message
