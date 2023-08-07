class SQLQuery:
    insert_team_query: str = "INSERT INTO team (teamId, name, eventId, gameId) VALUES (%s, %s, %s, %s)"

    insert_player_query: str = "INSERT INTO player (playerId, playerName) VALUES (%s, %s)"

    insert_team_player_query: str = "INSERT INTO team_player (id, playerId, teamId) VALUES (%s, %s, %s)"

    get_team_details_query: str = "SELECT * FROM team"

    get_player_details_query: str = "SELECT * FROM player"

    get_teams_detail_query: str = "SELECT * FROM team JOIN team_player JOIN player on team.teamId = team_player.teamId AND team_player.playerId = player.playerId;"

    get_last_inserted_team_id: str = "SELECT teamId FROM `team` ORDER BY teamId DESC LIMIT 1"

    insert_fixture_query: str = "INSERT into matches (matchId,date,firstTeamId,secondTeamId,duration) VALUES (%s, %s, %s, %s, %s)"

    get_last_inserted_fixture_id: str = "SELECT matchId FROM `matches` ORDER BY matchId DESC LIMIT 1"

    get_last_inserted_player_id: str = "SELECT playerId FROM `player` ORDER BY playerId DESC LIMIT 1"

    get_last_inserted_team_player_id: str = "SELECT id FROM `team_player` ORDER BY id DESC LIMIT 1"
