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
    
    s = get_standings(seasons, conference)
    print(s)

    st.dataframe(s,height=560, width=900)
    
if __name__ == "__main__":
    main()