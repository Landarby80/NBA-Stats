import streamlit as st

from src.standings import get_standings




def main() -> None:

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
    
if __name__ == "__main__":
    main()