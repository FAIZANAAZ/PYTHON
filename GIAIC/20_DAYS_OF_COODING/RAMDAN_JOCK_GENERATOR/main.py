import streamlit as st
import requests as req
import random

def get_random_joke():
    """Get a random joke from the Joke API."""
    
    try :
        response=req.get("https://official-joke-api.appspot.com/random_joke")
    
        if response.status_code==200:
            joke_data=response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a random joke. Please try again later."
    except Exception as e:
      return f"An error occurred: {str(e)}"
  
  
# ****************** UI **************************  
def main():
    st.title("Random Joke Generator")
    st.write("Get a random joke from the Joke API.")
    if st.button("Generate Joke"):
        joke=get_random_joke()
        st.success(joke)
if __name__ == "__main__":
    main()
   
  
  
  
  
