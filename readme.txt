# Random Football Teams Selector

## Overview
This Python application selects two random football teams from specified leagues (Turkey, England, France, and Germany) and displays them on the screen after pressing the 'Start' button. The team data is fetched from the internet.

---

## Features
- Fetch team data from online sources for Turkey, England, France, and Germany leagues.
- Randomly select two teams from different leagues.
- Display the selected teams after a 2-second delay.
- Simple Python-based implementation.

---

## Prerequisites

Before running the application, ensure you have the following:

- **Python 3.8+**
- **pip (Python package manager)**
- Internet connection to fetch team data
- The `requests` and `time` libraries (installable via pip)

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/football-teams-selector.git
   cd football-teams-selector
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Run the Application**
   ```bash
   python main.py
   ```

2. **How It Works**
   - Press the `Start` button to trigger the selection process.
   - The program will fetch team data from online sources.
   - Two random teams from different leagues will be displayed on the screen after a 2-second delay.

---

## Example Code
Below is the simplified Python code for this application:

```python
import requests
import random
import time

def fetch_teams():
    leagues = {
        "Turkey": "https://api.example.com/turkey",
        "England": "https://api.example.com/england",
        "France": "https://api.example.com/france",
        "Germany": "https://api.example.com/germany",
    }

    teams = {}
    for league, url in leagues.items():
        response = requests.get(url)
        if response.status_code == 200:
            teams[league] = response.json().get("teams", [])
        else:
            print(f"Failed to fetch data for {league}")
    return teams

def select_teams(teams):
    league1, league2 = random.sample(list(teams.keys()), 2)
    team1 = random.choice(teams[league1])
    team2 = random.choice(teams[league2])
    return team1, team2

def main():
    print("Fetching team data...")
    teams = fetch_teams()

    print("Press 'Start' to select teams.")
    input("Start > ")

    print("Selecting teams...")
    time.sleep(2)

    team1, team2 = select_teams(teams)
    print(f"Selected Teams:\n1. {team1} (from {list(teams.keys())[0]})\n2. {team2} (from {list(teams.keys())[1]})")

if __name__ == "__main__":
    main()
```

---

## Troubleshooting

- **Issue**: Failed to fetch team data.
  - **Solution**: Check your internet connection and ensure the API URLs are correct.

- **Issue**: No teams displayed.
  - **Solution**: Verify that the fetched data includes valid team names.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For further assistance, reach out to:
- **Email**: support@footballteamsselector.com
- **GitHub Issues**: [https://github.com/your-repo/football-teams-selector/issues](https://github.com/your-repo/football-teams-selector/issues)

