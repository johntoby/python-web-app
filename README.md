# Soccer Player Comparison App ⚽

A Flask web application that compares soccer players by position and identifies the best player in each position based on ratings.

## Features

- Search for players by name
- View player position and rating
- Compare players within the same position
- Identify the best player in each position
- Display all players in an organized table

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone or navigate to the project directory:
```bash
cd python-web-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your browser and visit:
```
http://127.0.0.1:5000
```

3. Enter a player name (e.g., "Mbappe", "De Bruyne", "Van Dijk") and click "Compare"

## Available Players

**Goalkeepers:**
- Alisson (89)
- Courtois (90)
- Ederson (88)

**Defenders:**
- Van Dijk (90)
- Ramos (88)
- Dias (87)

**Midfielders:**
- De Bruyne (91)
- Modric (88)
- Kante (89)

**Forwards:**
- Mbappe (91)
- Haaland (91)
- Benzema (89)

## Project Structure

```
python-web-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Web interface
└── README.md          # Documentation
```

## How It Works

1. User enters a player name in the search form
2. Application searches through all positions to find the player
3. Compares the player's rating with others in the same position
4. Displays results showing if the player is the best in their position
5. Shows a complete table of all players for reference

## Technologies Used

- **Flask 3.0.0** - Python web framework
- **HTML/CSS** - Frontend interface
- **Jinja2** - Template engine (included with Flask)

## License

MIT
