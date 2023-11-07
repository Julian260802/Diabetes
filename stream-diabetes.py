import pickle 
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judulweb
st.title('Data Mining Prediksi Diabetes')

pregnancies = st.text_input ('input nilai pregnancies')

glucose = st.text_input ('input nilai glucose')

bloodpressure = st.text_input ('input nilai blood pressure')

skinthickness = st.text_input ('input nilai skinthickness')

insulin = st.text_input ('input nilai insulin')
bmi = st.text_input ('input nilai bmi')
Diabetespedigreefunction = st.text_input ('input nilai diabetes pedigree function' )
Age = st.text_input('input nilai Age')
# code untuk prediksi
diab_diagnosis = ''
# membuat tombol prediksi
if st.button('test prediksi diabetes'):
    diab_prediction = diabetes_model.predict([[pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, Diabetespedigreefunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'pasien terkena diabetes'
    else :
         diab_diagnosis = ' pasien tidak terkena diabetes'
    st.success(diab_diagnosis)
