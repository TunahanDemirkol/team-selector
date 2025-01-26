from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

TEAMS = {
    "Turkey": [
        "Galatasaray", "Fenerbahçe", "Beşiktaş", "Trabzonspor",
        "Adana Demirspor", "Antalyaspor", "Kasımpaşa", "Kayserispor",
        "Alanyaspor", "Başakşehir", "Konyaspor", "Gaziantep FK",
        "Sivasspor", "Hatayspor", "Pendikspor", "Ankaragücü",
        "İstanbulspor", "Samsunspor", "Rizespor", "Karagümrük"
    ],
    "England": [
        "Manchester City", "Arsenal", "Manchester United", "Liverpool",
        "Chelsea", "Tottenham", "Newcastle", "Brighton",
        "Aston Villa", "Brentford", "Crystal Palace", "Fulham",
        "West Ham", "Nottingham Forest", "Everton", "Luton Town",
        "Burnley", "Sheffield United", "Bournemouth", "Wolves"
    ],
    "France": [
        "PSG", "Marseille", "Lens", "Monaco",
        "Lille", "Rennes", "Lyon", "Nice",
        "Reims", "Strasbourg", "Toulouse", "Montpellier",
        "Clermont", "Nantes", "Metz", "Le Havre",
        "Lorient", "Brest", "PSG", "Reims"
    ],
    "Germany": [
        "Bayern Munich", "Borussia Dortmund", "RB Leipzig", "Union Berlin",
        "Freiburg", "Bayer Leverkusen", "Eintracht Frankfurt", "Wolfsburg",
        "Mainz 05", "Borussia Mönchengladbach", "Werder Bremen", "Augsburg",
        "Hoffenheim", "VfL Bochum", "FC Köln", "Heidenheim",
        "Stuttgart", "Darmstadt", "VfL Bochum", "RB Leipzig"
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_teams')
def get_teams():
    selected_leagues = random.sample(list(TEAMS.keys()), 2)
    team1 = random.choice(TEAMS[selected_leagues[0]])
    team2 = random.choice(TEAMS[selected_leagues[1]])
    
    return jsonify({
        'team1': {'name': team1, 'league': selected_leagues[0]},
        'team2': {'name': team2, 'league': selected_leagues[1]}
    })

if __name__ == '__main__':
    app.run(debug=True) 