import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
# ye doniya bhar ke time ko lekr ayga

time_zone=[
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("Time Zone")

selected_time=st.multiselect("Select Time Zone",time_zone,default=["UTC","Asia/Karachi"])
# AGR USER KOI VALUE NAHI SELECT KAREGA TO DEFAULT TIME ZONE HOGA

st.subheader("Selected Time Zone")

for tz in selected_time:
    current_time=datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # ZoneInfo ye ak time module he jo ke sb countryies ke current time ko lekr ayga
    
    # strftime is a python function jo ke ak time ko sahi format me lekr ayga
    st.write(F"**{tz}**:{current_time}")
    
# ***************    

st.subheader("Convert Time Zone")

current_time=st.time_input("current Time",value=datetime.now()) 
    # ye current time lega jo user input karega sb ka taky user slect kr sky ke konsa time krna he jesy 11  12 13
    
from_tz=st.selectbox("From  Time Zone",time_zone,index=0)  

# yani konsa time covert krna he

# index =0 yani default time zone hoga array ka sbsy phla element

to_tz=st.selectbox("To Time Zone",time_zone,index=1)



if st.button("Convert Time"):
    dt=datetime.combine(datetime.today().date() ,current_time,tzinfo=ZoneInfo(from_tz))
    
    # dt=datetime.combine(datetime.today().date() ,current_time,tzinfo=ZoneInfo(from_tz))
    # # Iska kaam kya hai?
    # # Yeh user ke input time ko datetime object me convert kar raha hai aur usko "from_tz" wale time zone ke sath associate kar raha hai.

    # # Breakdown:
    # datetime.today().date() → Aaj ki tareekh le raha hai.
    # current_time → Jo user ne time select kiya hai, wo le raha hai.
    # datetime.combine(datetime.today().date(), current_time, tzinfo=ZoneInfo(from_tz))
    # Yeh date + time ko mila kar ek proper datetime object bana raha hai.
    # Isme tzinfo=ZoneInfo(from_tz) se yeh ensure ho raha hai ke input time from_tz wale time zone me hai.

  
    convert_time=dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    
    #  convert_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    # Iska kaam kya hai?
    # .astimezone(ZoneInfo(to_tz)) → Yeh time ko from_tz se to_tz wale time zone me convert kar raha hai.
    # .strftime("%Y-%m-%d %I:%M:%S %p") → Yeh converted time ko readable format me convert kar raha hai:
    # %Y-%m-%d → Year-Month-Day
    # %I:%M:%S %p → Hours:Minutes:Seconds AM/PM
    
    st.success(f"Converted Time in {to_tz}: {convert_time}")