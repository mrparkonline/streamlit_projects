import streamlit as st

# Title
st.title("ICS4U Landing Page")
st.write("Grade 12 Computer Science Content.")
# END OF TITLE

# Content
# Navigation:
tab1, tab2, tab3, tab4 = st.tabs(["U1: Python Programming", "U2: Algorithmic Thinking", "U3: Object Oriented Programming", "U4: Databases"])

with tab1:
    st.write("Python Programming")

with tab2:
    st.write("Algorithmic Thinking")

with tab3:
    st.write("Object Oriented Programming")

with tab4:
    st.write("Databases")

# END OF CONTENT