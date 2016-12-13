#Universidade Federal do Rio de Janeiro
#Data: 12/12/2016
#Alunos: Eryck Pedro, Hugo Faria, Lucas Murakami
#Inteligencia Artificial - Othello/Reversi - Jogador Biorr

class Biorr:
	NIVEL_MAXIMO = 4
	def __init__(self, color):
		self.color = color

	def avalia(self, cor, board):
		score = board.score()
		if (cor == board.WHITE):
			return score[0]-score[1]
		else:
			return score[1]-score[0]

		
	def minimax(self, board, corOponente, nivel):
		from itertools import izip
		moves = board.valid_moves(self.color)
		notas = [None]*len(moves) #notas dada pela funcao de avaliacao para cada movimento (notas[i] para moves[i])
		
		#no folha
		if len(moves) == 0:
			return self.avalia(self.color, board)
		
		if(nivel == self.NIVEL_MAXIMO):
			for move, i in izip(moves,range(len(moves))): #percorre moves e lista de indices ao msm tempo
				tempBoard = board.get_clone()
				if(nivel%2 == 0):
					tempBoard.play(move, self.color)
				else:
					tempBoard.play(move, corOponente)
				notas[i] = self.avalia(self.color, tempBoard) #coloca as notas
			
			
		else:
			for move, i in izip(moves,range(len(moves))):
				tempBoard = board.get_clone()
				if(nivel%2 == 0):
					tempBoard.play(move, self.color)
				else:
					tempBoard.play(move, corOponente)
				notas[i] = self.minimax(tempBoard, corOponente, nivel+1)
		
		if(nivel%2 == 0):
			melhor = max(notas)
		else:
			melhor = min(notas)
		return notas.index(melhor) #indice da melhor jogada achada
		
			
			

	def play(self, board):
		corOponente = board._opponent(self.color)
		
		indice = self.minimax(board, corOponente, 0)
		
		moves = board.valid_moves(self.color)
		
		return moves[indice]
