import pickle
import streamlit as st

model = pickle.load(open("C:/Users/DELL/Desktop/index/Decision_Tree.pkl",'rb'))

def main():
    st.title("Liver Disease Prediction")

    # input Variables
Age = st.text_input("Entre your age   ") # 2
Gender = st.text_input("Entre your Sex (male = 1 and female = 2)")  # 1
 
Total_Bilirubin = st.text_input("Entre your Total_Bilirubin >  ") # 3
# Direct_Bilirubin = st.text_input("Entre your Direct_Bilirubin >  ")# 4
Alkaline_Phosphotase = st.text_input("Entre your Alkaline_Phosphotase >  ") # 5
Alamine_Aminotransferase = st.text_input("Entre your Alamine_Aminotransferase >  ") # 6
Aspartate_Aminotransferase = st.text_input("Entre your Aspartate_Aminotransferase >  ") # 7
Total_Protiens = st.text_input("Entre your Total_Protiens >  ")# 8
# Albumin = st.text_input("Entre your Albumin >  ") # 9
Albumin_and_Globulin_Rati = st.text_input("Entre your Albumin_and_Globulin_Ratio >  ") # 10 

# prediction code
if st.button("Predict"):
    makeprediction = model.predict([[Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase
                      ,Total_Protiens,Albumin_and_Globulin_Rati]])
    
    output = round(makeprediction[0],2)
    st.success("yes you have liver diases {}".format(output))

if __name__=="__main__":
    main()
