# https://fastapi.tiangolo.com/
# api stand for Application Programming Interface
# it is a way to connect/communicate with the different services in the internat

# run in terminal (uv add fastapi[standard])


from fastapi import FastAPI 
# ye ak module he fastapi ke ander ka
import random

app = FastAPI()
# ye fastapi ki class ko hmny call kiya isy ye hoga ke isky ander jitni chizen hen sb app me store ho jaygy

# or iska name hmy app hi rkhna  hota he


side_hustles = [
                 "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
                ]
# ye sb bs ak skil ka array he


money_quotes = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don’t happen. You create them. – Chris Grosser",
    "Don’t stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It’s not about having lots of money. It’s about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]

# ye sb bs ak kam he jo famouse logon ne kiye thy oska array he

@app.get("/side_hustles")
# ye ak decorator he fastapi ke ander ka
# ye simple get method he jo api ke liye use hota he api ko read ke liye
def get_side_hustles(apiKey:str):
    """"This function returns random side hustle ideas"""
    # ye simple comment ki trha he doc string
    if apiKey == "secret":
        return {"side_hustle": random.choice(side_hustles)}
    else:
        return {"error": "Invalid API Key"}

   # ye simple choice krky random vaue lekr ayga 

# *************

@app.get("/money_quotes")

def get_money_quotes(apiKey:str):
    if apiKey == "secret":
        return {"money_quote": random.choice(money_quotes)}
    else:
        return {"error": "Unauthorized"}


# ye dono as a endpoint kam krengy   

# ****************

# run in terminal (fastapi dev api.py) dev yani development mode   

# terminal me is url pr click krengy (http://127.0.0.1:8000/docs)

# phir jo ui open hogi ismy jakr try it out pr click krky api key dalengy =>execute

# phir is trha end point lga kr hm browser me cheq krengy

# http://127.0.0.1:8000/side_hustles
# http://127.0.0.1:8000/money_quotes