import streamlit as st
import pandas as pd
import joblib


df=pd.read_csv('ml_model_web_app/filtered_data.csv')

st.title("Job Category Prediction")

#Domain
Domain1 = df['Domain'].value_counts().index.tolist()
Domain=st.selectbox('Job Role',Domain1)
domain=[]
domain.append(Domain)

#Expericence Level
Experience=st.radio('Experience Level',['Entry Level','Associate Level','Mid-Senior Level'])
experience=[]
experience.append(Experience)

#Industry
Industry1=df['Industry'].value_counts().index.to_list()
Industry=st.selectbox('Industry',Industry1)
industry=[]
industry.append(Industry)

#Location
Location1=df['Location'].value_counts().index.to_list()
Location=st.selectbox('Location',Location1)
location=[]
location.append(Location)

#job description

job_description=st.text_area('Description',placeholder='Paste job description or enter anything about your job role like skills, tools, etc. Note: min 500 words ', max_chars=10000)
Job_Description=[]
Job_Description.append(job_description)

#Explanation

st.write('AI Adoption role - Jobs that currently require AI skills like AI Creation, Management or Advanced Use.')
st.write('Automation role - Jobs that AI can automate in Future like repetitive, rules-based tasks.')
st.write('Low AI Impact role - Jobs that are resistant to AI and Automation.')

done=st.button('Done')

if done:

    new_cat_data = {
    'Location': location,
    'Experience Level': experience,
    'Industry': industry,
    'Domain': domain,
    'Job Description' : Job_Description
    }

    # 3. Convert categorical data to a DataFrame
    new_job_data = pd.DataFrame(new_cat_data)

    full_pipeline = joblib.load('ml_model_web_app/full_pipeline')
    prediction_array = full_pipeline.predict(new_job_data)

    

    label_mapping = {0: 'AI adoption role', 1: 'automation role', 2: 'low ai impact role'} # Adjust this based on your actual labels
    predicted_label = label_mapping[prediction_array[0]]

    st.success(f"The model predicts the job role is a {predicted_label}")
