import numpy as np

class eightPuzzle:
    def __init__(self, distanceType='manhattan',startState=None):
        self.goalState=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,0]
        ])
        if startState is not None:
            self.state=np.array(startState)
            if not self.isValidState(self.state):
                raise ValueError("Trang thai bat dau khong hop le: Phai chua cac so tu 0 den 8, moi so xuat hien dung 1 lan")
            if not self.isSolvable(self.state):
                raise ValueError("Trang Thai bat dau khong the giai duoc: so nghich the khong cung chan le voi trang thai muc tieu.")                
        else:
            self.state=self.scrambleState()
        self.distanceType=distanceType
    
    def scrambleState(self):
        state=self.goalState.flatten()
        np.random.shuffle(state)
        state= state.reshape(3,3)
        while not self.isSolvable(state):
            np.random.shuffle(state)
            state=state.reshape(3,3)
        return state
        
    def isValidState(self,state:np.ndarray):
        stateFlatten=state.flatten()
        return len(stateFlatten) == 9 and sorted(stateFlatten) == list(range(9))
        
    def countInversions(self,state:np.ndarray):
        stateFlatten=state.flatten()
        tiles=[x for x in stateFlatten if x!=0]
        inversions=0
        
        for i in range(len(tiles)):
            for j in range(i+1,len(tiles)):
                if tiles[i]>tiles[j]:
                    inversions+=1
        return inversions
    
    def isSolvable(self,state):
        goalInversions=self.countInversions(self.goalState)
        stateInversions=self.countInversions(state)
        return (goalInversions%2)==(stateInversions%2)
    
    def stateToTuple(self,state):
        return tuple(map(tuple,state))
    
    def getBlankPosition(self,state):
        pos=np.argwhere(state==0)
        if pos.size==0:
            raise ValueError("Khong tim thay so 0")
        return pos[0][0],pos[0][1]
    
    def manhattan(self,state,end):
        return sum(abs(r1-r2)+abs(c1-c2)
                   for num in range(1,9)
                   for r1,c1 in [np.argwhere(state==num)[0]]
                   for r2,c2 in [np.argwhere(end==num)[0]])
        
    def calculateDistance(self,state):
        return self.manhattan(state,self.goalState)
    
    def getReward(self,state):
        distance=self.calculateDistance(state)
        if self.isGoal(state):
            return 100
        return -distance
    
    def isGoal(self,state):
        return np.array_equal(state,self.goalState)
    
    def action(self, state):
        row,col=np.argwhere(state==0)[0]
        moves=[
            (-1,0),
            (0,-1),
            (1,0),
            (0,1)
        ]
        for dr,dc in moves:
            newRow,newCol=dr+row,dc+col
            if(0<=newRow<3) and (0<=newCol<3):
                newState=np.copy(state)
                newState[row,col],newState[newRow,newCol]=newState[newRow,newCol],newState[row,col]
                yield newState
                
    def getPossibleStates(self,state):
        return list(self.action(state))
    
    def takeAction(self,state,nextStateIndex):
        possibleStates=self.getPossibleStates(state)
        if not possibleStates or nextStateIndex>=len(possibleStates):
            return state, -10
        
        newState=possibleStates[nextStateIndex]
        reward=self.getReward(newState)
        return newState,reward
    
    def getState(self):
        return self.state
    
    def setState(self,state):
        self.state=state