file_content = """Stacy, 0.267
Alyssa, 0.300
Jenny, 0.350
Simon, 0.280
Marcy, 0.330
Kyle, 0.220
Alex, 0.290
Jordan, 0.360
Taylor, 0.270
Morgan, 0.320"""
with open("players_scores.txt", "w") as file:
    file.write(file_content)

Player_names = {"Stacy": 0.267, "Alyssa": 0.300, 
        "Jenny": 0.350, "Simon": 0.280, "Marcy": 0.330,
        "Kyle": 0.220, "Alex": 0.290, "Jordan": 0.360,
        "Taylor": 0.270, "Morgan": 0.320}
print ("Player Names\tAverage Score:")
for name, score in Player_names.items():
    print(name, "\t\t", score)
