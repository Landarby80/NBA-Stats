import streamlit as st

from src.pages import welcome_page


def main() -> None:

    
    # Set page configuration for the welcome page
    st.set_page_config(page_title="NBA Stats App", page_icon="🏀", layout="wide")

    #adding styles
    with open('style.css') as f:
        css = f.read()

    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

    #title
    st.title('NBA :blue[Stats] :basketball:')

    welcome_page()

    
if __name__ == "__main__":
    main()