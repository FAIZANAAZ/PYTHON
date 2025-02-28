***********************Streamlit Kya He?************************

Streamlit ek open-source Python framework hai jo data scientists aur AI/ML engineers ke liye banaya gaya hai. Iska maqsad interactive data applications ko asaani se aur kam code mein banane ka hai.

Streamlit ki khaas baatein:

(1)Asaan istemal: Streamlit ka istemal bahut aasan hai. Aap sirf Python code likhte hain aur Streamlit use web application mein badal deta hai.

(2)Tezi se development: Isse aap apne data projects ko bahut jaldi web applications mein badal sakte hain, bina kisi complex web development ki zaroorat ke.

(3)Interactive elements: Streamlit aapko sliders, buttons, aur text inputs jaise interactive elements add karne ki suvidha deta hai, jisse users aapke data ke saath interact kar sakte hain.

(4)Data visualization: Ye charts, graphs, aur maps banane mein madad karta hai, jo aapke data ko samajhne mein aasan banata hai.

(5)Machine learning models ka demonstration: Aap apne ML models ko easily deploy kar sakte hain, jisse dusre log unhe samajh aur test kar sakein.



****************Setup in colab******************
(1)!pip install streamlit
(2)!pip install pyngrok
(3) Now create an app.py file in files tab.

(4) Write your streamlit app in app.py file. (yani cooding krni he ismy)

(5) Now create an Authtoken from the following link. (yha jkr your oth token copy krna he)
# https://dashboard.ngrok.com/get-started/your-authtoken  

(6)Now save that Authtoken in Colab Secrets (jo side me key bnihoti he wha ja kr key me name likhna he koch bhi or value me token  past krna he ).

(7)Now import your keys into your code.
   esy :
       from google.colab import userdata
       pyngrok_token = userdata.get('pyngrok_authtoken')

(8)Now initiate your ngrok with your token       

(9)!ngrok authtoken 2aRzznCKBUOzIyOn6hLfU3Aharn_7haovBjVXMEHBTWAiypes  (ya tovariable ki jga direct esy rkh do token)
********for url of streamlit app********* 
(10)Now let's run our app.py
(11)from pyngrok import ngrok
(12)Run Streamlit 
    !streamlit run app.py
(13)public_url = ngrok.connect(addr=8501)
    public_url    

************for vs code****************
*********************WORKING PROCEES WITH STREAMLIGHT ******************

(1)pip install streamlit
(2)write code in app.py file
(3)push code in github


********************* for deployemnt https://share.streamlit.io/ *******************

(1)open https://share.streamlit.io/
(2)continue sign in ang continuse with google
(3)in What stage of app development are you at? => select (My app is ready to deploy.) => agr githup pr push ho chuka heto
(4)click on create app 
(5)githup ke connect krna he account ko
(6)Main file path ..me hm main file ka name dengy jismy sy code othaY GA streamlit  jesy yha walli app.py
(6)or phir repo ko conent krky deploy krdengy

<!-- terminal me run krny ke liye -->
streamlit run app.py    