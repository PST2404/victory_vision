import streamlit as st
import pickle
import pandas as pd


teams = ['Sunrisers Hyderabad',
'Mumbai Indians',
'Royal Challengers Bangalore',
'Kolkata Knight Riders',
'Kings XI Punjab',
'Chennai Super Kings',
'Rajasthan Royals',
'Delhi Capitals',
'Gujrat Titans',
'Lucknow Supergiants']


cities = ['Hyderabad', 'Pune', 'Rajkot', 'Indore', 'Bangalore', 'Mumbai',
      'Kolkata', 'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai',
      'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
      'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
      'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Kochi',
      'Visakhapatnam', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah',
      'Mohali', 'Bengaluru']


pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL The Victory Vision')


col1, col2 = st.columns(2)


with col1:
   batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
   bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target', min_value=1, step=1)

col3,col4,col5 = st.columns(3)


with col3:
   score = st.number_input('Score', min_value=0, step=1)
with col4:
   overs = st.number_input('Overs completed', min_value=0.0, max_value=20.0,step=0.1, format="%0.1f")
with col5:
   wickets = st.number_input('Wickets out', min_value=0, max_value=10, format="%d")


if st.button('Predict Probability'):
   if (score == target) and wickets == 10 :
      st.header("Wrong Combinations")
   elif (score > target+6):
      st.header("Wrong Combinations")
   elif score >= target and batting_team != bowling_team:
      st.header(batting_team + "-100%")
      st.header(bowling_team + "-0%")
   else :
      runs_left = target - score
      balls_left = 120 - int(overs) * 6 - (overs - int(overs)) * 10
      wickets = 10 - wickets
      if overs != 0:
         crr = score/(int(overs) * 6 + (overs - int(overs)) * 10)
      else:
         crr = 0  
      if balls_left > 0:
         rrr = (runs_left*6)/balls_left
      else :
         rrr = 0

      if batting_team != bowling_team:
         
         input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets_left':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})


         result = pipe.predict_proba(input_df)
         loss = result[0][0]
         win = result[0][1]
         st.header(batting_team + "- " + str(round(win*100)) + "%")
         st.header(bowling_team + "- " + str(round(loss*100)) + "%")
      else :
         st.header("Please ensure that you do not select the same team for both batting and bowling.")