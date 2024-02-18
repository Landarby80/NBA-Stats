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

            **Navigation:** Use our sidebar menu to navigate between different sections - Standings and Games.
        """
    )

def games_page():
      st.title("Live Games")

      get_games()


def welcome_page ():
 
    page = st.sidebar.selectbox(
                'Select Page', ('Home', 
                                'Standings',
                                'Games'
                                )
                )


    if page == 'Home':
                howto_page()
    elif page == 'Standings':
                standings_page()
    elif page == 'Games':
                games_page()