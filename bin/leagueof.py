import time
from riotwatcher import RiotWatcher, EUROPE_WEST, LoLException, error_404, error_429

class Lol:

	def __init__(self, key, default_region=EUROPE_WEST):
		self.lol_watcher = RiotWatcher(key, default_region=default_region)
		self.wait()
		self.champion_list = self.lol_watcher.static_get_champion_list()['data']


	def wait(self):
		while not self.lol_watcher.can_make_request():
			time.sleep(1)

	def test_map(self, _id):
		if _id == 1:
			return "Summoner's Rift"
		elif _id == 2:
			return "Summoner's Rift"
		elif _id == 3:
			return "The Proving Grounds (tuto)"
		elif _id == 4:
			return "Twisted Treeline"
		elif _id == 8:
			return "The Crystal Scar"
		elif _id == 10:
			return "Twisted Treeline"
		elif _id == 11:
			return "Summoner's Rift"
		elif _id == 12:
			return "Howling Abyss"
		elif _id == 14:
			return "Butcher's Bridge"

	def test_queue(self, _id):
		if _id == 0:
			return "Custom"
		elif _id == 2:
			return "Normal 5v5 blind"
		elif _id == 4:
			return "Ranked Solo 5v5"
		elif _id == 6:
			return "Ranked Premade 5v5"
		elif _id == 7:
			return "Coop vs ia 5v5"
		elif _id == 8:
			return "Normal 3v3"
		elif _id == 9:
			return "Ranked flex"
		elif _id == 14:
			return "Normal Draft 5v5"
		elif _id == 16:
			return "Odin 5v5 Blind"
		elif _id == 17:
			return "Odin 5v5 Draft"
		elif _id == 25:
			return "Coop vs ia 5v5"
		elif _id == 31:
			return "Coop vs ia (intro)"
		elif _id == 32:
			return "Coop vs ia (beginner)"
		elif _id == 33:
			return "Coop vs ia (Intermediate)"
		elif _id == 41:
			return "Ranked Team 3v3"
		elif _id == 52:
			return "Ranked Team 5v5"
		elif _id == 61:
			return "GROUP_FINDER_5v5"
		elif _id == 65:
			return "Aram"
		elif _id == 70:
			return "One For All"
		elif _id == 72:
			return "FIRSTBLOOD_1v1"
		elif _id == 73:
			return "FIRSTBLOOD_2v2"
		elif _id == 75:
			return "Hexakill"
		elif _id == 76:
			return "URF"
		elif _id == 78:
			return "One For All"
		elif _id == 83:
			return "Bot URF"
		elif _id == 91:
			return "DOOM Bot (rank 1)"
		elif _id == 92:
			return "DOOM Bot (rank 2)"
		elif _id == 93:
			return "DOOM Bot (rank 5)"
		elif _id == 96:
			return "Ascension"
		elif _id == 98:
			return "Hexakill"
		elif _id == 100:
			return "BILGEWATER_ARAM_5v5"
		elif _id == 300:
			return "Poro King"
		elif _id == 310:
			return "COUNTER_PICK"
		elif _id == 313:
			return "BILGEWATER_5v5"
		elif _id == 315:
			return "Siege"
		elif _id == 317:
			return "Definitly Not Dominion"
		elif _id == 318:
			return "Aram URF"
		elif _id == 400:
			return "Normal Draft"
		elif _id == 410:
			return "Ranked"
		elif _id == 420:
			return "Ranked Solo/Duo"
		elif _id == 440:
			return "Ranked Flex"

	def test_champ(self, _id):
		temp = []
		for k in self.champion_list:
			temp.append(self.champion_list[k])
		temp = [nb for nb in temp if nb['id'] == _id]
		return temp[0]['name']

	def test_ranked_stats(self, stats, key):

		stats = stats['champions']
		stats = [nb for nb in stats if nb['id'] == 0]
		stats = stats[0]['stats']
		return stats[key]

	def test_team(self, _id):
		if _id == 100:
			return ":large_blue_circle:"
		else:
			return ":red_circle:"

	def check_lol(self, player, region):
		try:
			self.wait()
			return self.lol_watcher.get_summoner(name=player, region=region)
		except LoLException as e:
			if e == error_429:
				return ":x: Resseye dans {} secondes.".format(e.headers['Retry-After'])
			elif e == error_404:
				return ":x: Summoner inconnu : {}".format(player)

	def message_lol(self, summoner):
		message = ":information_source: {} :video_game:\n\n".format(summoner['name'])
		message += " :information_source: Général Stats\n"
		message += " **ID**: {}\n".format(summoner['id'])
		message += " **Level**: {}\n".format(summoner['summonerLevel'])
		self.wait()
		temp = self.lol_watcher.get_league(summoner_ids=[summoner['id']])
		rank = []
		for i in temp[str(summoner['id'])]:
			rank.append(i['queue'] + " " + i['tier'])
		message += " **Rank**: {}\n".format(rank)
		#message += " **Mastery Levels**: {}\n".format()
		#message += " **Mastery Points**: {}\n".format()
		#message += " **Mastery Tokens**: {}\n".format()
		self.wait()
		player_stats = self.lol_watcher.get_stat_summary(summoner['id'])['playerStatSummaries']
		player_stats = [nb for nb in player_stats if nb['playerStatSummaryType'] == 'Unranked']
		player_stats = player_stats[0]
		message += " **Wins**: {}\n".format(player_stats['wins'])
		message += " **Kills**: {}\n".format(player_stats['aggregatedStats']['totalChampionKills'])
		message += " **Assistances**: {}\n".format(player_stats['aggregatedStats']['totalAssists'])
		message += " **Creeps tués**: {}\n".format(player_stats['aggregatedStats']['totalMinionKills'])
		message += " **Tourelles détruite**: {}\n\n".format(player_stats['aggregatedStats']['totalTurretsKilled'])
		#message += " **Dernière connexion**: {}\n\n".format()
		message += ":information_source: Ranked Stats :\n"
		try:
			self.wait()
			ranked_stats = self.lol_watcher.get_ranked_stats(summoner['id'])
			message += " **Win:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalSessionsWon'))
			message += " **Loose:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalSessionsLost'))
			message += " **Kill:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalChampionKills'))
			message += " **Assistance:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalAssists'))
			message += " **Damages infligés:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalDamageDealt'))
			message += " **Damages Reçus:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalDamageTaken'))
			message += " **Argent gagné:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalGoldEarned'))
			message += " **Creeps tués:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalMinionKills'))
			message += " **Tourelles détruites:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalTurretsKilled'))
			message += " **Double kills:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalDoubleKills'))
			message += " **Triple kills:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalTripleKills'))
			message += " **Quadra kills:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalQuadraKills'))
			message += " **Penta kills:** {}\n".format(self.test_ranked_stats(ranked_stats, 'totalPentaKills'))
			message += " **Total Killing Spree:** {}\n\n".format(self.test_ranked_stats(ranked_stats, 'killingSpree'))

		except:
			message += "**Aucune Stats de Ranked n'a été trouvée !**\n\n"

		message += ":information_source: Game en cours :\n"

		try:
			self.wait()
			temp = self.lol_watcher.get_current_game(summoner['id'])
			message += " **ID Partie:** {}\n".format(temp['gameId'])
			message += " **GameMode:** {}\n".format(temp['gameMode'])
			message += " **GameType:** {}\n".format(temp['gameType'])
			message += " **ID Queue:** {}\n".format(self.test_queue(temp['gameQueueConfigId']))
			message += " **ID Platform:** {}\n".format(temp['platformId'])
			message += " **ID Map:** {}\n".format(self.test_map(temp['mapId']))

			for i in temp['participants']:
				message += "  " + i['summonerName'] + " (" + self.test_champ(i['championId']) + ") Team: " + self.test_team(i['teamId']) + "\n"

		except:
			message += "**Aucune game en cours...**"
		
		return message

def main(key):
	leagueof = Lol(key, default_region=EUROPE_WEST)
	print(leagueof.message_lol(leagueof.check_lol('ST Leeroyjenkins', EUROPE_WEST)))




if __name__ == "__main__":
	main('RGAPI-d5620781-f00e-4cc1-80cd-4a6e9289bb67')