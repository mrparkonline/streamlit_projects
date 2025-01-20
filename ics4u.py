import streamlit as st
import gspread

# Internal Import
from datetime import datetime

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
# -- Sprint Keys
# """
# Sprint Keys
# - "Timestamp" : when it was created
# - "Name" : name of the Sprint
# - "InstructionLink" : link with the instructions
# - "Priority" : priority value (integer) from 1 to 5
# - "DueDate" : DD/MM/YEAR 24H:00M
# """

sort_mode = st.radio(
    label="Sort Sprints By:",
    options=["Creation Date", "Priority", "Due Date"],
    index=0,
)

if sort_mode == "Priority":
    records = sorted(records, key=lambda x:x["Priority"], reverse=True)
elif sort_mode == "Due Date":
    records = sorted(records, key=lambda x: datetime.strptime(x["DueDate"].split(" ")[0], "%m/%d/%Y"))

for i, sprint in enumerate(records):
    with st.container(border=True, key=f"row_{i}"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(f"**[{sprint["Name"]}]({sprint["InstructionLink"]})**")
        
        with col2:
            st.write(f"**Priority:** {sprint["Priority"]}")
        
        with col3:
            st.write(f"**Due Date:** {sprint["DueDate"]}")

# END OF CONTENT