import streamlit as st

st.title("🎈 :rainbow[My new app]")
st.write(
    "Let's start building! For help and inspiration, head over to [google](https://www.google.com/)."
)
st.header("Hello world !",divider=True)
st.subheader("Streamlit-set-up",divider=True)

left,middle,right=st.columns(3)
if left.button("shinchan",type="primary",use_container_width=True):
    left.markdown("Hai 😜",unsafe_allow_html=False)
if middle.button("zoe",type="primary",use_container_width=True):
    middle.markdown("Hello 😁",unsafe_allow_html=False)
if right.button("Nanako",type="primary",use_container_width=True):
    right.markdown("Welcome 🤷‍♂️",unsafe_allow_html=False)

if st.button("Hit"):
    st.markdown("Pressed",unsafe_allow_html=False)
    st.balloons()
else:
    st.markdown("press the Hit !",unsafe_allow_html=False)
st.color_picker("pick a color",label_visibility="visible")
st.selectbox("Your gender :",["Male","Female"],)

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )