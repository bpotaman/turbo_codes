from turbo_encoder import TurboEncoder
from turbo_decoder import TurboDecoder
import numpy as np
import random
import matplotlib.pyplot as plt

def bit_flip(encoded_message: np.ndarray, prob):
    message_copy = encoded_message.copy()  # must make a copy, so that you don't alter the actual message

    for i in range(encoded_message.size):
        if random.uniform(0, 1) > prob:
            message_copy[i] = encoded_message[i] ^ 1
    return message_copy

def get_ber(p):
    ber_list = []
    message = np.zeros(1024, dtype=int)
    message[:512] = 1

    for _ in range(2500):
        np.random.shuffle(message)

        encoded_message = TurboEncoder().encode(message)

        altered_message = bit_flip(encoded_message, p)
        decoded_messsage = TurboDecoder().decode(altered_message)

        number_of_bit_errors = sum(message ^ decoded_messsage)
        ber_list.append(number_of_bit_errors/message.size)

    ber = sum(ber_list)/len(ber_list)
    return ber

def plot_ber():
    ber_list = []
    p_list = []
    p = 0.01
    for _ in range(40):
        p += 0.01
        p_list.append(p)
        ber = get_ber(p)
        ber_list.append(ber)
    ber_list = np.array(ber_list)
    p_list = np.array(p_list)
    plt.plot(p_list, ber_list)
    plt.show()

plot_ber()

