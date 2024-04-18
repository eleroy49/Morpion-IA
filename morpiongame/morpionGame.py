# creation of the empty board
emptyBoard=[
    ["_","_","_"],
    ["_","_","_"],
    ["_","_","_"],
    ]




class morpion:
    
    # initialise the board game with an empty board
    def __init__(self,board=emptyBoard):
        self.board=board
        
    # textual representation of the board     
    def __str__(self):
        s=self.board[0][0]+"|"+self.board[0][1]+"|"+self.board[0][2]+"\n"
        s=s+self.board[1][0]+"|"+self.board[1][1]+"|"+self.board[1][2]+"\n"
        s=s+self.board[2][0]+"|"+self.board[2][1]+"|"+self.board[2][2]+"\n"
        return s
    # return the list of the actions that are possible
    def actions(self):
        listeAction=[]
        for ligne in range(len(self.board)):
            for colonne in range(len(self.board)):
                if self.board[ligne][colonne]=="_":
                    listeAction.append((ligne,colonne))    
                    
        return listeAction
    
    
    
    def result(self,a,player):#retourne l'état après avoir effectué l'action a sur s par le joueur player ("X" ou "O")
        boardCopy=[]
        for ligne in self.board:
            add=[]
            for el in ligne:
                add.append(el)
            boardCopy.append(add)
        

        ligne=a[0]
        colonne=a[1]
        
        boardCopy[ligne][colonne]=player
        
        return morpion(boardCopy)
                
    
    
    def terminalTest(self):
        # on regarde si une des lignes/colonnes n'est remplie que de la même chose
        
        
        
        for k in range(len(self.board)):
            
            if self.board[k][0]==self.board[k][1]  and self.board[k][1]==self.board[k][2] and (self.board[k][2]=="X" or self.board[k][2]=="O"): #gagnant selon ligne
                return True
            
            if self.board[0][k]==self.board[1][k]  and self.board[1][k]==self.board[2][k] and( self.board[2][k]=="X" or self.board[2][k]=="O") : #gagnant selon colonne
                return True
            
        if self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2] and ( self.board[2][2]=="X" or self.board[2][2]=="O"):#diagonale descendante
            return True
        
        if self.board[2][0]==self.board[1][1] and self.board[1][1]==self.board[0][2] and ( self.board[2][0]=="X" or self.board[2][0]=="O"):#diagonale montante
            return True
    
        #Il n'y a pas de ligne/colonne/ diag gagnante donc on regarde si c'est rempli
        
        for ligne in self.board:   
            if "_" in ligne:
                return False
        return True
       
    def utility(self):#considering s is on terminal state
       
        
        for k in range(len(self.board)):
            
            if self.board[k][0]==self.board[k][1]  and self.board[k][1]==self.board[k][2]: #gagnant selon ligne
                return 1 if self.board[k][0]=="X" else -1
            
            if self.board[0][k]==self.board[1][k]  and self.board[1][k]==self.board[2][k]: #gagnant selon lcolonne
                return 1 if self.board[0][k]=="X" else -1
            
        if self.board[0][0]==self.board[1][1] and self.board[1][1]==self.board[2][2]:#diagonal descendante
            return 1 if self.board[0][0]=="X" else -1
        
        if self.board[2][0]==self.board[1][1] and self.board[1][1]==self.board[0][2]:#diagonal montante
            return 1 if self.board[2][0]=="X" else -1
        return 0# dans le cas sans gagnant    