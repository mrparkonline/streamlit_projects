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

# Streamlit Page Config
st.set_page_config(
    page_title="Sprints",
    page_icon=":alarm_clock:",
    layout="wide"
)

# Title
st.title("ICS4U Sprints")
# END OF TITLE

# Links
link1, link2, link3, link4 = st.columns(4, border=True)

with link1:
    st.write("Unit 1: Python Programming")
    st.write("[Textbook Link](https://mrparkonline.gitbook.io/guide-to-high-school-computer-science/python-programming)")

with link2:
    st.write("Unit 2: Algorithmic Thinking")
    st.write("[Textbook Link](https://mrparkonline.gitbook.io/guide-to-high-school-computer-science/python-programming/introduction-to-algorithmic-thinking)")

with link3:
    st.write("Unit 3: Object Oriented Programming")
    st.write("[Textbook Link](https://mrparkonline.gitbook.io/guide-to-high-school-computer-science/python-programming/object-oriented-programming)")

with link4:
    st.write("Unit 4: Databases")
    st.write("[Textbook Link](https://mrparkonline.gitbook.io/guide-to-high-school-computer-science/python-and-databases)")
# End of Links

# Sorting Mode
sort_mode = st.radio(
    label="Sort Sprints By:",
    options=["Creation Date", "Priority", "Due Date"],
    index=0,
)

if sort_mode == "Priority":
    records = sorted(records, key=lambda x:x["Priority"], reverse=True)
elif sort_mode == "Due Date":
    records = sorted(records, key=lambda x: datetime.strptime(x["DueDate"].split(" ")[0], "%m/%d/%Y"))
# END OF SORTING MODE

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