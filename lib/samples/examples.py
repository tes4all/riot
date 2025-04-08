from riot.connection import connect
from riot.constants import regions
from riot.lol import league as lol_league, summoner, spectator
from riot.tft import league as tft_league


connect('<API_KEY>', region=regions.EUW1)
summoner_id = '<SUMMONER_ID>' # => summoner.id
summoner_name = '<SUMMONER_NAME>'

curr_summoner = summoner.summoner_by_name(summoner_name)
print(curr_summoner.successful, curr_summoner.data)

games = lol_league.entries_by_summoner_id(summoner_id)
print(games.successful, games.data)

games = tft_league.entries_by_summoner_id(summoner_id)
print(games.successful, games.data)

active_game = spectator.active_game_by_summoner_id(summoner_id)
print(active_game.successful, active_game.data)
