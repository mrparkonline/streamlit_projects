import streamlit as st
import gspread

# Initialize gspread
GC_API = st.secrets["google_cloud"]
gc = gspread.api_key(GC_API)
gc_file = gc.open_by_key("1m6eH5rgyZY4mqEB7pEgFpW5SaCRobE3Oo7IBNInjOjc")
sheet = gc_file.sheet1

records = sheet.get_all_records() # List of Dictionaries
# END OF GSPREAD

# Title
st.title("ICS4U Sprints")
# END OF TITLE

# Content
for sprint in records:
    st.write(sprint)

# END OF CONTENT