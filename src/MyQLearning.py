from QLearning import QLearning

class MyQLearning(QLearning):
    def update_q(self, state, action, r, state_next, possible_actions, alfa, gamma):
        # Get the current Q value for the state-action pair
        curr_q = self.get_q(state, action)

        # Find the Q value for the next possible actions
        possible_q_values = [self.get_q(state_next, a) for a in possible_actions]


        max_q = max(possible_q_values)

        
        # Use the update rule
        new_q = curr_q + alfa * (r + gamma * max_q - curr_q)

        # if(new_q != 0):
        #     print(str(new_q))
        # Set the updated Q value for state-action pair
        self.set_q(state, action, new_q)
        return
