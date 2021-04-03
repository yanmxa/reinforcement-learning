

class QLearningAgent(BaseAgent):
    def __init__(self, actions):
        super(QLearningAgent, self).__init__(actions)

    def learn(self, state, action, reward, next_state, **kwargs):
        '''
        off-policy: don't need the next action
        '''
        current_q = self.q_table.loc[state, action]
        delta_q = reward + self.discount_factor * \
            max(self.q_table.loc[next_state, :]) - current_q
        self.q_table.loc[state, action] += self.learning_rate * delta_q


if __name__ == "__main__":
    env = Env()
    agent = QLearningAgent(actions=list(range(env.n_actions)))
    for episode in range(1000):
        state = env.reset()
        action = agent.get_action(str(state))
        while True:
            env.render()
            next_state, reward, done = env.step(action)
            next_action = agent.get_action(str(next_state))

            agent.learn(str(state), action, reword,
                        str(next_state), next_action)
            state = ne xt_state
            action = next_action

            env.print_value_all(agent.q_table)
            if done:
                break
