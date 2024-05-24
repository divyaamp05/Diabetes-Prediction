import numpy as np
import pickle
import streamlit as st



loaded_model = pickle.load(open("D:/Harshu/Machine Learning/Projects/Diabetes Prediction/trained_model.sav", "rb"))

def diabetes_prediction(input_data):
     input_data=np.array(input_data)
     print(input_data)
     input_data=input_data.reshape(1,-1)
     prediction=loaded_model.predict(input_data)
     print(prediction)
     if(prediction=="array([0])"):
          print("Person does not Diabetics")
     else:
          print("Person have Diabetics")

def main():
    st.title("Diabetes Prediction Web")


    Pregnancies= st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose level")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the person")

    diagnosis=''

    if st.button("Diabetes Test Result"):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])


        st.success(diagnosis)

if __name__ == '__main__':
    main()


