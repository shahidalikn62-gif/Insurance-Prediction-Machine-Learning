import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import steamlit as st
#steamlit is for webapplication project



st.title("Health Insurance Prediction")
img_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRs4KhTbDjzCufZXz-J8NTKzcxA9YjnnF85qVN5UOHS0A&s=10"
st.image(img_url)


#load data and ml model part
#step2: load insurance data
url="https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df=pd.read_csv(url)



#step3: EDA
#to get the top 5 rows
df.drop("Customer_ID", axis=1, inplace=True)
df['Previous_Insurance']=df['Previous_Insurance'].map({'No':0, "Yes":1})
df['Insurance_Bought']=df['Insurance_Bought'].map({'No':0, "Yes":1})

#step4: 
X=df.iloc[:,:-1]
y=df.iloc[:, -1]

#step 5:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=42, test_size=0.3)


#step 6: train model
model= LogisticRegression()
model.fit(X_train, y_train)

#show dtaa sample
st.write(df.head())

#create side bar for user input
st.sidebar.title("fill customer details")
st.sidebar.image(img_url)


#to get user input
all_ans=[]
for index, col_name in enumerate(X.columns):
  min_v= X[col_name].min()
  max_v= X[col_name].max()
  if col_name != "Previous_Insurance":
    value = st.sidebar.slider(f"select value for {col_name}",
                              min_value = min_v,
                              max_value = max_v)
  else:
    value = st.sidebar.number_input(f"select value for {col_name} (0:No, 1:Yes): ")
    all_ans.append(value)
ud={j:all_ans[i] for i,j in enumerate(X.columns)}
user_df  = pd.DataFrame(ud, index=[1])
sr.write(user_df)

#======================prediction=======================


if st.button("click ton predict: "):
  with st.spinner("predicting..."):
    import time
    time.sleep(2)
  final_ans= model.predict([all_ans])[0]
  if final_ans==0:
    st.info("customer will not buy the insurance")
  else:
    st.info("customer will buy the  insurancve")
  










