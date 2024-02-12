import streamlit as st

from src.standings import get_standings
from src.games import get_games



#function to create the standing page
def standings_page():

    st.title("Standings")

    conference = st.sidebar.selectbox('Conference',
                                 ("East", "West"), 
                                 index=None, 
                                 placeholder="Select a conference...",
                                 )

    seasons = st.sidebar.selectbox  ('Season',
                                 ("2021","2022","2023"), 
                                 index=None, 
                                 placeholder="Select a season...",
                                 )



    st.write( conference, "in ", seasons)
    
    standings = get_standings(seasons, conference)

    st.dataframe(standings,
                 column_config={
                    "Logo": st.column_config.ImageColumn(
                        label="Logo",width="medium",help=None
                    ) 
                 },
                 height=560, width=970)

    

# Function to create the other page
def howto_page():
    st.markdown(
        """
            ## How to Use:

            **Navigation:** Use our sidebar menu to navigate between different sections - Standings.
        """
    )

def games_page():
      st.title("Live Games")

      get_games()


def welcome_page ():
    st.markdown(
    """
    Welcome to the NBA Stats Hub, your ultimate destination for comprehensive NBA statistics and analytics. Whether you're a die-hard fan, fantasy basketball enthusiast, or a data-driven analyst, our website offers a treasure trove of up-to-date information to satisfy your basketball cravings.

    ## Features:

    ### 1. Standings
    Stay on top of the NBA standings with our regularly updated tables. Monitor your team's position in the conference and division standings.

    """
)
    page = st.sidebar.selectbox(
                'Select Page', ('default', 
                                'Standings',
                                'Live Games'
                                )
                )


    if page == 'default':
                howto_page()
    elif page == 'Standings':
                standings_page()
    elif page == 'Live Games':
                games_page()    

def main() -> None:

    
    # Set page configuration for the welcome page
    st.set_page_config(page_title="NBA Stats App", page_icon="🏀", layout="wide")

    st.title('NBA :blue[Stats] :basketball:')

    welcome_page()

    
if __name__ == "__main__":
    main()