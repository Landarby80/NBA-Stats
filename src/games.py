import datetime
import json
import requests
import streamlit as st

url = "https://api-nba-v1.p.rapidapi.com/games"

headers = {
	"X-RapidAPI-Key": "566613b78fmsh13902d43bd1824fp1879e0jsna570c6257dac",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

        
#function to get the games status                
def get_games():

    option = st.selectbox(
    'Select Games',
    ('Live', 'By Date')
    )

    if option == 'Live':
        querystring= {"live":"all"}

    else:
        date = st.date_input("choose a date", datetime.date(2024, 1, 1))
        st.write('date is:', date)
        querystring = {"date":date
                        
        }

    response = requests.get(url,
                            headers=headers, 
                            params=querystring)

    data = response.text
    parse_json = json.loads(data)

    st.write(parse_json)
    