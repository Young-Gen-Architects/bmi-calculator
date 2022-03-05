import streamlit as st

st.title("Our BMI calculator is here!")
weight = st.number_input("Enter your weight in kgs")
status= st.radio("Select your height format:",('cms', 'meters', 'feet'))

if(status == 'cms'):
    height = st.number_input('centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter your height")
         
elif(status == 'meters'):
    height = st.number_input('meters')
     
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter your height")
         
else:
    height = st.number_input('feet')
     
    # 1 meter = 3.28
    try:
        bmi = weight / ((height/3.28)**2)
    except:
        st.text("Enter your height")
if(st.button('Calculate your BMI')):

    st.text("Your BMI index is {}".format(bmi))
    if(bmi < 16):
        st.error("Extremely underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")       
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely overweight")

