#2. Conocer el nombre y la cantidad de goles del goleador o goleadora.
def best_goal_scorer(players_stats):
    player_max_goals = max(players_stats, key = lambda player: player[1])
    return player_max_goals

#3. Conocer el nombre del jugador o jugadora más influyente, esto se consigue
#sumando goles a favor, goles evitados y cantidad de asistencias. La particularidad
#es que los goles a favor, evitados y las asistencias NO valen lo mismo (es un
#promedio ponderado):

values = {"goals" : 1.5,
          "goals avoided": 1.25,
          "assists": 1}

def most_influential(players_stats):
    values = {"goals" : 1.5,
          "goals avoided": 1.25,
          "assists": 1}
    name_max_points = ""
    max_points = 0
    for name in players_stats:
        total_points = (name[1] * values["goals"])+(name[2] * values["goals avoided"])+(name[3] * values["assists"])
        if total_points > max_points:
            max_points = total_points
            name_max_points = name[0]
    return name_max_points
#4. Conocer el promedio de goles por partido del equipo en general. Dato: Se jugaron 25 partidos en la temporada.

def average_goals(players_stats):
    games_playeds = 25
    summatori =0
    for name in players_stats:
        summatori = summatori + name[1]
    return summatori / games_playeds

#5. Conocer el promedio de goles por partido del goleador o goleadora. Dato: Se jugaron 25 partidos en la temporada.

def average_goal_scorer(player_stats):
    games_played = 25
    average_goals_per_game = lambda total_goals, games_played: total_goals / games_played
    total_goals_scored = player_stats[1]
    average_goals = average_goals_per_game(total_goals_scored, games_played)
    return average_goals