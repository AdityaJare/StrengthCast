import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="StrengthCast", page_icon="🧱")

model=joblib.load("concrete_strength_model.pkl")


st.markdown("<h1 style='text-align: center; color: orange;'>StrengthCast</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Enter the concrete mix components and get the predicted strength</h4>", unsafe_allow_html=True)

col1, col2=st.columns(2)
with col1:
    cement = st.number_input("Cement (kg/m³)", min_value=100, max_value=600, value=300)
    blast_furnace_slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0, max_value=400, value=0)
    fly_ash = st.number_input("Fly Ash (kg/m³)", min_value=0, max_value=200, value=0)
    water = st.number_input("Water (kg/m³)", min_value=100, max_value=400, value=200)
with col2:
    superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0, max_value=35, value=0)
    coarse_aggregate = st.number_input("Coarse Aggregate (kg/m³)", min_value=500, max_value=1200, value=800)
    fine_aggregate = st.number_input("Fine Aggregate (kg/m³)", min_value=500, max_value=1200, value=800)
    age = st.number_input("Age (days)", min_value=1, max_value=365, value=28)

input_values=pd.DataFrame([[cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]],
columns=["cement","blast_furnace_slag","fly_ash","water","superplasticizer","coarse_aggregate","fine_aggregate ", "age"]
)

if st.button("Predict Concrete Strength"):

    prediction=model.predict(input_values)
    pred_int = int(prediction[0])

    if pred_int <= 20:
        st.error(f"The predicted concrete strength is {pred_int} MPa (WEAk concrete)")
    elif pred_int > 20 and pred_int <= 60:
        st.warning(f"The predicted concrete strength is {pred_int} MPa (normal concrete)")
    else:
        st.success(f"The predicted concrete strength is {pred_int} MPa (High strength concrete)")
 