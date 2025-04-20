from Qlearning import QLearningAgent
import numpy as np

if __name__=="__main__":
    
    startState=np.array([
        [2,6,5],
        [0,8,7],
        [4,3,1]
    ])
    
    agent=QLearningAgent(alpha=0.1,gamma=0.9,epsilon=0.1,startState=startState)
    
    print("Huan luyen mo hinh...")
    agent.train(episodes=5000)
    
    print("\nGiai 8-puzzle:")
    agent.solve()