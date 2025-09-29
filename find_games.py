import pandas as pd

MATCHES_PATH = "Data/Data/matches/matches_England.json"


def list_match_ids_for_team(team_id):
    df = pd.read_json(MATCHES_PATH)

    match_ids = []

    for _, row in df.iterrows():
        teams = row.get("teamsData", {})

        if not isinstance(teams, dict):
            continue

        for k, v in teams.items():
            try:
                tid = int(k)
            except:
                tid = v.get("teamId") if isinstance(v, dict) else None

            if tid == team_id:
                match_ids.append(row["wyId"])
                break

    return sorted(set(match_ids))

TEAM_ID = 1625 
result = list_match_ids_for_team(TEAM_ID)

print(f"Jogos encontrados para teamId {TEAM_ID}: {len(result)}")
print(result)