# chanlit is a chat app
# it is a web app jismy hm kisi bhi trha ka chat bna skty hen

# chat session
# it represent a chat session between two users
# Event
# ye hota jesy hm kisi chiz ko step by step krna wo sary steps event khlaty hen ke phly user aya chat pr sms kiya ye kiya ans aya 
# hooks
# hooks are special functions that hook into thiese events like loading  auser information by user information by runing custom code when specific session ACCURE

# DECORATORS
    #  these are special markers that enhance the functionality of a function
    
#STATELESS CONVERSATION
# JB DATA KHI STORE NHI HOTA OR REALOD HONY PR DATA GAIB HO JATA HE TOI TO STATELESS HOTA HAI

# STATEFUL CONVERSATION 
# JB DATA KHI STORE HO RHA HITA HE H OR REALOD HONY PR DATA GAIB  NHI HOTA   TO TO STATEFUL HOTA HAI

# run chainlit hello

import chainlit as cl

@cl.on_message
# ye decorater ak new sms leta he user sy chat strat krta he
async def main(message: cl.Message):
    response=f"You said: {message.content}"
    # content me jakr user ka sms seva hota he
    await cl.Message(content=response).send()
    # send ka method hi ye text ko chat pr send karta he
    
    