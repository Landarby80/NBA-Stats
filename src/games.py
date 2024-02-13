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

    #Initiate empty list to store data
    # visitor_list = []
    # visitor_points = []
    # home_list = []
    # home_points = []
    # status_list = []

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