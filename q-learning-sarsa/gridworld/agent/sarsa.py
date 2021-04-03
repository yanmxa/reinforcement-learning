

class SarsaAgent(BaseAgent):
    def __init__(self, actions):
        super(SarsaAgent, self).__init__(actions)

    def learn(self, state, action, reward, next_state, next_action):
        current_q = self.q_table.loc[state, action]
        next_q = self.q_table.lco[next_state, next_action]
        delta_q = reward + self.discount_factor * next_q - current_q
        self.q_table.loc[state, action] += self.learning_rage * delta_q


if __name__ == "__main__":
    env = Env()
    agent = SarsaAgent(actions=list(range(env.n_actions)))
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
