import streamlit as st

# SQL کنکشن بنائیں
conn = st.connection('pets_db', type='sql')

# ٹیبل بنائیں اور ڈیٹا ڈالیں
conn.execute('CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);')
conn.execute('DELETE FROM pet_owners;')

pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
for owner, pet in pet_owners.items():
    conn.execute(
        'INSERT INTO pet_owners (person, pet) VALUES (?, ?);',
        (owner, pet)
    )

# ڈیٹا کوئری کریں اور دکھائیں
pet_owners = conn.query('SELECT * FROM pet_owners', ttl=0)
st.dataframe(pet_owners)
