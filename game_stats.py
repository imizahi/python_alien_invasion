class GameStats:
	"""game stats"""
	def __init__(self,ai_game):
		"""initialize statistick"""
		with open('score.txt') as file_object:
			self.high_score = int(file_object.read())
		self.settings = ai_game.settings
		self.reset_stats()
		self.game_active = False
		#self.high_score = 0
		self.level = 1

	def reset_stats(self):
		"""initialize statistick that can change"""
		self.ships_left = self.settings.ship_limit
		self.score = 0

