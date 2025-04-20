import random
import numpy as np

from Environment_QLearn import eightPuzzle

class QLearningAgent:
    def __init__(self, alpha=0.1,gamma=0.9,epsilon=0.1,startState=None):
        self.env=eightPuzzle(distanceType='manhattan',startState=startState)
        self.initialState=np.copy(self.env.getState()) if startState is not None else None
        self.qTable={}
        self.alpha=alpha
        self.gamma=gamma
        self.epsilon=epsilon
        
    def chooseAction(self,state):
        stateTuple=self.env.stateToTuple(state)
        possibleStates=self.env.getPossibleStates(state)
        numPossible=len(possibleStates)
        
        if numPossible==0:
            return -1
        
        if stateTuple not in self.qTable:
            self.qTable[stateTuple] = {i:0 for i in range(numPossible)}
            
        if random.random()<self.epsilon:
            return random.randint(0,numPossible-1)
        else:
            qValues=self.qTable[stateTuple]
            return max(qValues,key=qValues.get)
        
    def updateQTable(self,state,actionIndex,reward,nextState):
        stateTuple=self.env.stateToTuple(state)
        nextStateTuple=self.env.stateToTuple(nextState)
        
        possibleNextStates=self.env.getPossibleStates(nextState)
        if nextStateTuple not in self.qTable:
            self.qTable[nextStateTuple]={i:0 for i in range(len(possibleNextStates))}
            
        currentQ=self.qTable[stateTuple][actionIndex]
        maxFutureQ=max(self.qTable[nextStateTuple].values()) if possibleNextStates else 0
        newQ=currentQ+self.alpha*(reward+self.gamma*maxFutureQ-currentQ)
        self.qTable[stateTuple][actionIndex]=newQ
        return currentQ,newQ
        
    def train(self,episodes=5000):
        for episode in range(episodes):
            # self.env.setState(self.env.scrambleState())
            # state=self.env.getState()
            state=self.env.scrambleState()
            steps=0

            # print(f"\nEpisode {episode + 1}:")
            # print("Trạng thái ban đầu:")
            # print(state)
            while not self.env.isGoal(state) and steps<1000:
                actionIndex=self.chooseAction(state)
                if actionIndex==-1:
                    break
                
                nextState,reward=self.env.takeAction(state,actionIndex)
                
                oldQ,newQ=self.updateQTable(state,actionIndex,reward,nextState)
                
                # if episode<5:
                #     print(f"\nBuoc {steps+1}: ")
                #     print(f"Hanh dong (chi so trang trang thai tiep theo): {actionIndex} ")
                #     print(f"Phan Thuong: {reward} ")
                #     print(f"Trang Thai tiep theo:")
                #     print(nextState)
                #     print(f"Gia tri Q cu: {oldQ:.2f}, Gia tri Q moi {newQ:.2f}")
                
                state=nextState
                self.env.setState(state)
                steps+=1
            if (episode+1)%100==0:
                print(f"Hoan thanh {episode+1} episodes.")
                
    def solve(self):
        
        if self.initialState is not None:
            self.env.setState(self.initialState)
        
        state=self.env.getState()
        steps=0
        print("Trang thai ban dau: ")
        print(state)
        
        while not self.env.isGoal(state) and steps<100:
            actionIndex=self.chooseAction(state)
            if actionIndex == -1:
                print("\nKhong co hanh dong kha thi!")
                break
            nextState,reward=self.env.takeAction(state,actionIndex)
            state=nextState
            self.env.setState(state)
            print(f"\nBuoc {steps+1}: Chuyen trang thai moi")
            print(state)
            steps+=1
        if self.env.isGoal(state):
            print("\nDa gia duoc 8-puzzle")
        else:
            print("\nKhong giai duoc trong gioi han buoc")