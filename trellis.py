import numpy as np

class Trellis:
    
    def __init__(self):

        self.states = ["s1", "s2", "s3", "s4"]  # states
        self.prev_states = {"s1": ["s1", "s2"], # each state has two predecessing states it can be reached from
                            "s2": ["s3", "s4"],
                            "s3": ["s1", "s2"],
                            "s4": ["s3", "s4"]
                            }
        

        # transitions, where s1 is 00, s2 01, s3 10, s4 11
        # {state: {state_it_can_reach: output_bits}}
        self.transitions = {"s1": {"s1": [0, 0], "s3": [1, 1]}, 
                            "s2": {"s1": [1, 1], "s3": [0, 0]}, 
                            "s3": {"s2": [0, 1], "s4": [1, 0]}, 
                            "s4": {"s2": [1, 0], "s4": [0, 1]}}
        

    def viterbi(self, encoded_message: np.ndarray):
        encoded_message = encoded_message.reshape(int(encoded_message.size/2), 2)  # split it for convinience
        decoded_message_length = int(encoded_message.size/2)
        # V stores states and their best hamming distances and their predecessing state for every timestep  
        V = [{}]
        for current_state in self.states:
            V[0][current_state] = {"cost": 0, "prev": None}
        for time_step in range(1, decoded_message_length + 1):  # encoded_message is always divisible by 2 (I said so)
            V.append({})  # each timestep will have a separate dictionary of the form {"state": {"cost": <int>, "prev": <prev_state>}} for all four states
            for current_state in self.states:
                V[time_step][current_state] = {}
                path_cost = min(V[time_step - 1][prev_state]["cost"] + 
                                    self.hamming_distance(encoded_message[time_step - 1], 
                                                          self.transitions[prev_state][current_state]) for prev_state in self.prev_states[current_state])  # find the smallest path cost
                V[time_step][current_state]["cost"] = path_cost
                for prev_state in self.prev_states[current_state]:
                    if path_cost == V[time_step - 1][prev_state]["cost"] + self.hamming_distance(encoded_message[time_step - 1], self.transitions[prev_state][current_state]):
                        V[time_step][current_state]["prev"] = prev_state

        # Now we have to recover the best path based on V
        lowest_cost = min(V[decoded_message_length][state]["cost"] for state in self.states)
        
        end_state = None
        # optimal states, but their names, so s1, s2 etc. There will be one more of them (draw a trellis and think about it)
        optimal_path_state_names = np.zeros(decoded_message_length + 1, dtype=np.dtypes.StringDType())  
        optimal_path_bits = np.zeros(decoded_message_length, dtype=int)
        for state in self.states:
            if V[decoded_message_length][state]["cost"] == lowest_cost:
                end_state = state
                # print(end_state)
        # print(V)
        if end_state is None:
            raise TypeError 
        else:
            optimal_path_state_names[decoded_message_length] = end_state
            optimal_path_state_name = end_state
            for time_step in range(decoded_message_length):
                optimal_path_state_name = V[decoded_message_length - time_step][optimal_path_state_name]["prev"]
                optimal_path_state_names[decoded_message_length - time_step - 1] = optimal_path_state_name
        
        # convert state names to corresponding transition output bits :)
        for i in range(optimal_path_state_names.size - 1):
            state_now = optimal_path_state_names[i]
            state_next = optimal_path_state_names[i+1]
            if state_now == "s1":
                if state_next == "s1":
                    optimal_path_bits[i] = 0
                elif state_next == "s3":
                    optimal_path_bits[i] = 1
            if state_now == "s2":
                if state_next == "s1":
                    optimal_path_bits[i] = 1
                elif state_next == "s3":
                    optimal_path_bits[i] = 0
            if state_now == "s3":
                if state_next == "s2":
                    optimal_path_bits[i] = 1
                elif state_next == "s4":
                    optimal_path_bits[i] = 0
            if state_now == "s4":
                if state_next == "s2":
                    optimal_path_bits[i] = 0
                elif state_next == "s4":
                    optimal_path_bits[i] = 1

        # print(optimal_path_state_names)
        optimal_path_bits = np.array(optimal_path_bits, dtype=int)
        return optimal_path_bits
        
                
    
    def hamming_distance(self, message_part, trellis_output_part):
        result = (message_part[0] ^ trellis_output_part[0]) + (message_part[1] ^ trellis_output_part[1])
        return result

