import datetime
import json
import requests
import streamlit as st

from dotenv import dotenv_values

secrets = dotenv_values(".env")

url = secrets["GAMES_URL"]

headers = {
	"X-RapidAPI-Key": secrets["X-RapidAPI-Key"],
	"X-RapidAPI-Host": secrets["X-RapidAPI-Host"],
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

   
    #variable to get the number of games
    num_games = parse_json['results']

    if num_games == 0:
        st.error("No games")
    else:
        for num in range(num_games):
            
            visitor_list = parse_json['response'][num]['teams']['visitors']['nickname']
            visitor_points= parse_json['response'][num]['scores']['visitors']['points']
            
            home_list = parse_json['response'][num]['teams']['home']['nickname']
            home_points = parse_json['response'][num]['scores']['home']['points']
            
            status = parse_json['response'][num]['status']['long']
    
            col1, col2, col3 = st.columns(3)
            col1.metric(visitor_list, visitor_points)
            col2.metric(home_list, home_points)
            col3.metric("Status", status)