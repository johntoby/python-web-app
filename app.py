from flask import Flask, render_template, request

app = Flask(__name__)

players_data = {
    'Goalkeeper': [
        {'name': 'Alisson', 'rating': 89},
        {'name': 'Courtois', 'rating': 90},
        {'name': 'Ederson', 'rating': 88}
    ],
    'Defender': [
        {'name': 'Van Dijk', 'rating': 90},
        {'name': 'Ramos', 'rating': 88},
        {'name': 'Dias', 'rating': 87}
    ],
    'Midfielder': [
        {'name': 'De Bruyne', 'rating': 91},
        {'name': 'Modric', 'rating': 88},
        {'name': 'Kante', 'rating': 89}
    ],
    'Forward': [
        {'name': 'Mbappe', 'rating': 91},
        {'name': 'Haaland', 'rating': 91},
        {'name': 'Benzema', 'rating': 89}
    ]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        player_name = request.form.get('player_name', '').strip()
        result = find_player_position(player_name)
    return render_template('index.html', result=result, positions=players_data)

def find_player_position(player_name):
    for position, players in players_data.items():
        for player in players:
            if player['name'].lower() == player_name.lower():
                best_player = max(players, key=lambda x: x['rating'])
                return {
                    'player': player_name,
                    'position': position,
                    'rating': player['rating'],
                    'best_player': best_player['name'],
                    'best_rating': best_player['rating'],
                    'is_best': player['name'] == best_player['name']
                }
    return {'error': 'Player not found'}

if __name__ == '__main__':
    app.run(debug=True)
