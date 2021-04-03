

class SarsaLambda(BaseAgent):
    def __init__(self, actions):
        super(SarsaLambda, self).__init__(actions)
        self.lamda = 0.9
        self.trace = self.q_table.copy()

    def learn(self, state, action, reward, next_state, next_action):
        current_q = self.q_table.loc[state, action]
        next_q = self.q_table.lco[next_state, next_action]
        delta_q = reward + self.discount_factor * next_q - current_q

        self.trace.loc[state, action] += 1
        # 使用整个trace最为权重系数，对整个q_table进行更新
        self.q_table += self.learning_rage * delta_q * self.trace
        self.trace *= self.discount_factor * self.lamda


if __name__ == "__main__":
    env = Env()
    agent = SarsaLambda(actions=list(range(env.n_actions)))
    for episode in range(1000):
        state = env.reset()
        action = agent.get_action(str(state))
        while True:
            env.render()
            next_state, reward, done = env.step(action)
            next_action = agent.get_action(str(next_state))

            agent.learn(str(state), action, reword,
                        str(next_state), next_action)
            state = next_state
            action = next_action

            env.print_value_all(agent.q_table)
            if done:
                state = env.reset()
                action = agent.get_action(str(state))
