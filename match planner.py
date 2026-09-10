import random

# --- CONFIGURATION: PUT YOUR PLAYER NAMES HERE ---
# Exactly 3 members per group
groups = {
    "Group A": ["Croxs_killer1", "Mino_jr9", "ghost_rider21o"],
    "Group B": ["jumasalimu592@gmail.com, "B2", "B3"],
    "Group C": ["C1", "C2", "C3"],
    "Group D": ["D1", "D2", "D3"],
    "Group E": ["E1", "E2", "E3"],
    "Group F": ["F1", "F2", "F3"]
}

def generate_cross_group_fixtures(group_dict):
    group_names = list(group_dict.keys())
    
    # Shuffle the groups so the group matchups change every time you run the script
    random.shuffle(group_names)
    
    # Pair the 6 groups into 3 distinct group matchups 
    # (e.g., Group C vs Group A, Group F vs Group B, Group E vs Group D)
    group_pairs = [(group_names[i], group_names[i+1]) for i in range(0, len(group_names), 2)]
    
    # Shuffle individual player lists for maximum randomness
    for g_name in group_dict:
        random.shuffle(group_dict[g_name])
        
    # Since there are 3 players per group, it takes exactly 3 matchdays 
    # for everyone to play one cross-group match.
    for matchday in range(1, 4):
        print(f"\n=========================================")
        print(f"               MATCHDAY {matchday}        ")
        print(f"=========================================")
        
        for g1_name, g2_name in group_pairs:
            g1_players = group_dict[g1_name]
            g2_players = group_dict[g2_name]
            
            print(f"\n🔹 {g1_name} vs {g2_name}")
            print(f"-----------------------------------------")
            
            # The matrix shift logic (i + matchday) ensures that on:
            # Matchday 1: Player 1 vs Player 1, P2 vs P2, P3 vs P3
            # Matchday 2: Player 1 vs Player 2, P2 vs P3, P3 vs Player 1
            # Matchday 3: Player 1 vs Player 3, P2 vs Player 1, P3 vs P2
            for i in range(3):
                p1 = g1_players[i]
                p2 = g2_players[(i + matchday) % 3] 
                print(f"  ⚽ {p1:<12} vs   {p2}")
                
        print()

# Run the fixture generator
generate_cross_group_fixtures(groups)