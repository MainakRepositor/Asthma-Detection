"""This modules contains data about prediction page"""
import pandas as pd
# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest and XGBoost</b> for the Asthma Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    AGE = st.slider("Age", int(df["AGE"].min()), int(df["AGE"].max()))
    PackHistory = st.slider("Pack History", int(df["PackHistory"].min()), int(df["PackHistory"].max()))
    O2_dilution = st.slider("O2 Dilution", int(df["O2_dilution"].min()), int(df["O2_dilution"].max()))
    MWT1 = st.slider("MWT1", float(df["MWT1"].min()), float(df["MWT1"].max()))
    MWT2 = st.slider("MWT2", float(df["MWT2"].min()), float(df["MWT2"].max()))
    MWT1Best = st.slider("MWT1Best", int(df["MWT1Best"].min()), int(df["MWT1Best"].max()))
    FEV1 = st.slider("FEV1", int(df["FEV1"].min()), int(df["FEV1"].max()))
    FEV1PRED = st.slider("FEV1PRED", int(df["FEV1PRED"].min()), int(df["FEV1PRED"].max()))
    FVC = st.slider("FVC", int(df["FVC"].min()), int(df["FVC"].max()))
    FVCPRED = st.slider("FVCPRED", int(df["FVCPRED"].min()), int(df["FVCPRED"].max()))
    CAT = st.slider("CAT", int(df["CAT"].min()), int(df["CAT"].max()))
    HAD = st.slider("HAD", int(df["HAD"].min()), int(df["HAD"].max()))
    SGRQ = st.slider("SGRQ", int(df["SGRQ"].min()), int(df["SGRQ"].max()))
    AGEquartiles = st.slider("AGEquartiles", int(df["AGEquartiles"].min()), int(df["AGEquartiles"].max()))
    copd = st.slider("copd", int(df["copd"].min()), int(df["copd"].max()))
    severity = st.slider("severity", int(df["severity"].min()), int(df["severity"].max()))
    smoking = st.slider("smoking", int(df["smoking"].min()), int(df["smoking"].max()))
    Diabetes = st.slider("Diabetes", int(df["Diabetes"].min()), int(df["Diabetes"].max()))
    muscular = st.slider("muscular", int(df["muscular"].min()), int(df["muscular"].max()))
    hypertension = st.slider("hypertension", int(df["hypertension"].min()), int(df["hypertension"].max()))
    AtrialFib = st.slider("AtrialFib", int(df["AtrialFib"].min()), int(df["AtrialFib"].max()))

    # Create a list to store all the features
    features = [AGE,PackHistory,O2_dilution,MWT1,MWT2,MWT1Best,FEV1,FEV1PRED,FVC,FVCPRED,CAT,HAD,SGRQ,AGEquartiles,copd,severity,smoking,Diabetes,muscular,hypertension,AtrialFib]

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["AGE","PackHistory","O2_dilution","MWT1","MWT2","MWT1Best","FEV1","FEV1PRED","FVC","FVCPRED","CAT","HAD","SGRQ","AGEquartiles","copd","severity","smoking","Diabetes","muscular","hypertension","AtrialFib"]
    st.dataframe(df3)

    
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        st.info("Predicted Sucessfully...")

        

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The person is safe from lung diseases but pollution can affect health")
        elif(prediction == 2):
            st.error("The person has mild breathing problems and might be Asthma")

        elif(prediction == 3):
            st.error("The person is prone to breathing problems like Ashtma")            
        else:
            st.error("The person is having chronic Asthma")

        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", round((score*100),2),"%")
