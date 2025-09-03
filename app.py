import streamlit as st
from circle_utils import area_of_circle

st.title("Circle Area Calculator")

radius = st.number_input("Enter the radius of the circle:", min_value=0.0, format="%.2f")

if st.button("Calculate Area"):
    try:
        area = area_of_circle(radius)
        st.success(f"The area of the circle is: {area:.2f} square units")
    except ValueError as e:
        st.error(str(e))
