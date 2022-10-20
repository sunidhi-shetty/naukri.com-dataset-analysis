import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
from pickle import load
from sklearn.preprocessing import LabelEncoder,StandardScaler
import matplotlib.image as mp


st.set_page_config(layout='wide')
st.title("***JOB MARKET TRENDS BASED ON NAUKRI.COM***")

image = mp.imread("job_market.png")
st.image(image)



option = st.sidebar.selectbox('SELECT',['Job Title','Job Salary(in Lacs)','Location','Experience(in Yrs)','Key Skills','Find Jobs'])

df = pd.read_csv("cleaned_dataset(range).csv")
df = df.drop(["Unnamed: 0"],axis =1)



# Job Title

top_title=df['Job_Title'].value_counts().nlargest(n=5)
fig1, ax1 = plt.subplots()
ax1.pie(top_title,labels=top_title.index,autopct='%.2f%%')


# Job Salary(in Lacs) 
top_salary=df['Job_Salary'].value_counts().nlargest(n=5)
#fig5, ax5 = plt.subplots()
#ax5.pie(top_salary,labels=top_salary.index,autopct='%.2f%%')

# Location
top_location=df['Location1'].value_counts().nlargest(n=5)
fig3, ax3 = plt.subplots()
ax3.pie(top_location,labels=top_location.index,autopct='%.2f%%')

# Experience(in Yrs)
experience_required=pd.DataFrame(df['Job_Experience'].value_counts()).head(5)

# Key Skills

top_skills=df['Key_Skills'].value_counts().nlargest(n=15)
#fig5, ax2 = plt.subplots()
#ax5.pie(top_skills,labels=top_skills.index,autopct='%.2f%%')


if option == "Job Title" :
        st.pyplot(fig1)
if option == "Job Salary(in Lacs)" :
	st.bar_chart(top_salary)
if option == "Location" :
	st.pyplot(fig3)
if option == "Experience(in Yrs)" :
        st.bar_chart(experience_required)
if option == "Key Skills":
	st.bar_chart(top_skills)



if option == "Find Jobs":
    genre = st.sidebar.radio("select", ["None", "By Designation", "By Experience(in Yrs)", "By Location(in Lacs)", "By All"])
    if genre =="By Designation":
        st.subheader("By Designation")   
        #job input("Enter your designation")
        #top-level filters
        job = st.selectbox("select the Job", sorted(pd.unique(df["Job_Title"])))
        #job = st.text_input("Designation", "")                              
        #job = str.title(job)
        if st.button("search", key="Search"):
           st.table(df[df['Job_Title']==job])
                                      
    if genre == "By Experience(in Yrs)":
        st.subheader("By Experience(in Yrs)")
        #exp = st.number_input('Experience')
        exp = st.selectbox("select the Experience(in Yrs)", pd.unique(df["Job_Experience"]))
        if st.button("Search", key="Search"):
            st.table(df[df ["Job_Experience"]== exp])                                  
                                    
    if genre == "By Location(in Lacs)":
        st.subheader("By Location(in Lacs)")
        #job = input("Enter your designation")
        #loc = st.text_input('Location')
        #loc= str.title(loc)
        loc = st.selectbox("Select the Location", sorted(pd.unique (df["Location1"])))
        if st.button("Search", key="search"):
            st.table(df[df['Location1']== loc])    
                                                                                                      
                                      
    if genre=='By All':
        st.subheader("By All")
        #job1 = st.text_input('Designation', '')
        #job1 = str.title(job1)
        #loc1 = st.text_input('Location', '')
        #loc1 = str.title(loc1)
        #exp1 = st.number_input('Experience')
        job1 = st.selectbox("Select the Job", pd.unique (df["Job_Title"]))
        #exp1 = st.selectbox("Select the Experience (in Yrs)", sorted(pd.unique (df["Min. Exp."])))
        exp1= st.selectbox("select the Experience(in Yrs)", df.loc[df['Job_Title'] == job1, 'Job_Experience'])
        loc1 = st.selectbox("Select the Location", df.loc[df[ 'Job_Title'] == job1, 'Location1'])
                                      
        if st.button("Search", key="Search"):
           st.table(df[(df['Job_Title']==job1) & (df['Job_Experience']== exp1) & (df['Location1']==loc1)])       
                                      
                                      
                                      
                                      