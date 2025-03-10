import streamlit as st
import pandas as pd # for data manipulation and data manupulation 
import csv 
# ismy bhut sy kisam ka data store hota he jesy pdf
import datetime

import  os #for file operation
# ye agli file koo cheq krta he ke wo mojood he bhi ya nhi 

# **************************

# agr hm capital me likhty hen variable ka name to wo ontant hota he yani hm osko change nhi krengy
MOOD_FILE="mood_log.csv"

# hmny ismy ak file ko store krwaya he jo hmny bnai he

# ye data lekr ayga read kryga ****************
def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        # hek kry ga ke file he ya nhi he
        # c
        return pd.DataFrame(columns=["Date","Mood"])
        #ye file ko ak dataframe me convert krta he yani data ko table me convert krta he ak fram me dal deta he
       
    return pd.read_csv(MOOD_FILE)
#    ye tb retrun hoga jb file hogi 


# ye data ko save krwaya he****************

def save_mood_data(date,mood):
    with open(MOOD_FILE,"a") as file:
        # a he append add krna r yani read 
         writer=csv.writer(file)
        #  ye file ke write mood me open kryga
         writer.writerow([date,mood])
        #  ye data ko write krenga

st.title("Mood Tracker")
today=datetime.date.today()
# hmny date ko store krwaya he present

st.subheader(f" How are your feeling today ?")

mood =st.selectbox("Mood",["Happy","Neutral","Sad","Angry"])
# ye mood ko select krwaya he

if st.button("Save Mood"):
    save_mood_data(today,mood)
    # FUNCTION CALL KRKY DATE DEDI AJ KI OR USER KA SLECT KIYA GYA MOOD
    
    st.success("Mood Saved Successfully")
    # yani file me dosri wali data save ho gyi
    
    
#  **************************   # 
 #HM NY FILE KO SAVE KRWAYA HE SHEET KE FORMATE ME
 
data=load_mood_data()
# hmny file ko load krwaya he 

if not data.empty:
    # ye condition he ki file me data he ya nhi he
    st.subheader("Mood Trends Over Time")
    data["Date"] = pd.to_datetime(data["Date"])
    # isko hm object ke shakal me save kry hen 
    # to_datetime ye ak object me dalra he file
    
    mood_counts = data.groupby("Mood").count()["Date"]
    
    # yani group kryga ke kis kis date ko user ka mood kesa rha OR AK JESY MOOD KO AK JHA RAKHLYGA taky bta sky ke konsa zada tha mood konsa kam
    
    st.bar_chart(mood_counts)
    # chart ki soat me display krengy data
    st.write("Build with ❤️ by [FAIZA NAAZ]")