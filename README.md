
# NBA Stats App

## Introduction
This is a Streamlit-based web application that provides NBA standings and information on live games. The application is structured into multiple Python files for better organization and readability. Below is an overview of the key components and functionalities:

## Files

### `main.py`
The main entry point of the application. It configures the Streamlit app, sets the page title and icon, and calls the `welcome_page()` function from the `src.pages` module.

### `src/pages.py`
Contains functions to render different pages within the app. 

- `howto_page()`: Displays information on how to navigate and use the app.
- `standings_page()`: Renders the standings page, allowing users to select a conference and season to view team standings.
- `games_page()`: Displays live NBA games using the `get_games()` function from the `src/games` module.
- `welcome_page()`: Serves as the home page and allows users to navigate to other sections.

### `src/games.py`
Handles the retrieval and display of live NBA games.

- `get_games()`: Utilizes the RapidAPI to fetch live game data based on user input (either by date or all live games). The games are then displayed using Streamlit's `metric` component.

### `src/standings.py`
Manages the retrieval and presentation of NBA standings.

- `get_standings(seasons, conference)`: Retrieves standings data from the RapidAPI based on the selected season and conference. The data is processed into a Pandas DataFrame and displayed using Streamlit's `dataframe` component.

### `style.css`
Contains custom styles for the Streamlit app, enhancing its visual appearance. The styles are applied to the app using Streamlit's `markdown` component.

## How to Use
1. **Navigation:** Use the sidebar menu to switch between different sections - Standings and Games.
2. **Standings Page:**
    - Select a conference and season from the sidebar to view team standings.
3. **Games Page:**
    - Choose either 'Live' to view all live games or 'By Date' to select a specific date.
    - Live games are displayed with team names, scores, and status.

Feel free to explore and enjoy the NBA Stats App (https://nba-stat.streamlit.app/)! 🏀📊
