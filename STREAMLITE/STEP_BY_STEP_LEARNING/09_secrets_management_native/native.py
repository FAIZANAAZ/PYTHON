import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
    # environ me bhi wahi save  hota he jo hmny diya he secrets me or st.secrets bhi wahi fetch krta he to ye dekh rha he le same he ya nhi 
)