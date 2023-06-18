import random
class MyEGreedy:
    def __init__(self):
        return 

    def get_random_action(self, agent, maze):
        valid_actions = maze.get_valid_actions(agent)
        assert len(valid_actions) > 0, "No available actions (from random_action method)"
        random_index = random.randint(0, len(valid_actions)-1)
        return valid_actions[random_index]

    def get_best_action(self, agent, maze, q_learning):
        valid_actions = maze.get_valid_actions(agent)
        assert len(valid_actions) > 0, "No available actions (from best_action method)"
        rewards = q_learning.get_action_values(agent.get_state(maze), valid_actions)
        if all(reward == rewards[0] for reward in rewards):
            return self.get_random_action(agent, maze)
        else:
            max_index = rewards.index(max(rewards))
            return valid_actions[max_index]

    def get_egreedy_action(self, agent, maze, q_learning, epsilon):
        # TODO to select between random or best action selection based on epsilon.
        if random.random() <= epsilon:
            return self.get_random_action(agent, maze)
        else:
            return self.get_best_action(agent, maze, q_learning)
