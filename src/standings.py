import json
import requests
import pandas as pd
import streamlit as st



url = "https://api-nba-v1.p.rapidapi.com/standings"

headers = {
	"X-RapidAPI-Key": "566613b78fmsh13902d43bd1824fp1879e0jsna570c6257dac",
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}


st.title('NBA :blue[Stats] :basketball:')



def get_standings(seasons,conference)-> pd.DataFrame:
    querystring = {"league":"standard",
                   "season":seasons,
                   "conference":conference}
    
    response = requests.get(url, 
                            headers=headers, 
                            params=querystring)
    
    data = response.text
    parse_json = json.loads(data)

    

   
    # Initialize empty lists to store data
    # ids_list = []
    logo_list = []
    names_list = []
    ranks_list = []
    wins_list = []
    losses_list = []

    for ids in range(min(15, len(parse_json['response']))):
        # ids_list.append(parse_json['response'][ids]['team']['id'])
        logo_list.append(parse_json['response'][ids]['team']['logo'])
        names_list.append(parse_json['response'][ids]['team']['name'])
        ranks_list.append(parse_json['response'][ids]['conference']['rank'])
        wins_list.append(parse_json['response'][ids]['conference']['win'])
        losses_list.append(parse_json['response'][ids]['conference']['loss'])
   
  
    df = pd.DataFrame(
        {
            # "ID": ids_list,
            "Rank": ranks_list,
            "Logo": logo_list,
            "Name": names_list,
            "Win": wins_list,
            "Loss": losses_list
        }
    )

    df = df.sort_values(by='Rank')

  

    return df













