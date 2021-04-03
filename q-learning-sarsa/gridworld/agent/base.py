import numpy as np
import pandas as pd


class BaseAgent(object):
    def __init__(self, actions, learning_rate=0.01, discount_factor=0.9,=0.1):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def learn(self, state, action, reward, next_state, next_action):
        raise NotImplementedError

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            init_state_series = pd.Series(
                [0] * len(self.actions), index=self.q_table.columns, name=state)
            self.q_table = self.q_table.append(init_state_series)

    def get_action(self, state):
        self.check_state_exist(state)
        if np.random.rand() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            # take action according to the q function table
            state_action = self.q_table.loc[state, :]
            action = np.random.choice(
                state_action[state_action == np.max(state_action)].index)
        return action
