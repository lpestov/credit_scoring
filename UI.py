import joblib
import streamlit as st
import numpy as np
import sklearn

from input_processing import preprocess


# Функция для предсказания на основе входных данных
def predict(features):
    model = joblib.load("best_credit_risk_model.joblib")
    return model.predict(preprocess(features))

#Заголовок для приложения
st.title("Кредитный скоринг")

# Ввод параметров от пользователя
translation = {"Мужской":'male', "Женский":'female',
               'В собственности': 'own', 'Нет': 'free', 'Аренда': 'rent',
               'Нет информации': 'nan', 'Малый': 'little' , 'Достаточно большой': 'quite rich', 'Большой':  'rich' , 'Умеренный': 'moderate',
               'Радио/Телевидение':'radio/TV', 'Образование':'education', 'Мебель/Оборудование':'furniture/equipment', 'Автомобиль':'car', 'Бизнес':'business',
'Бытовая Техника':'domestic appliances', 'Ремонт':'repairs', 'Отпуск/Другое':'vacation/others'
}


Age = st.number_input("Возраст", min_value=19, max_value=75, value=19)
Sex = translation[st.selectbox(
    "Пол",
    ("Мужской", "Женский") # male, female
)]
Job = st.number_input("Работа", min_value=0, max_value=3, value=1)
Housing = translation[st.selectbox("Недвижимость", ('В собственности', 'Нет', 'Аренда'))]
Saving_accounts = translation[st.selectbox("Совокупный размер сберегательных счетов", ('Нет информации', 'Малый', 'Достаточно большой', 'Большой', 'Умеренный'))] 
Checking_account = translation[st.selectbox("Размер текущего счёта", ('Нет информации', 'Малый', 'Умеренный', 'Большой'))] 
Duration = st.number_input("Длительность", min_value=4, max_value=72, value=4)
Purpose = translation[st.selectbox("Цель", ('Радио/Телевидение', 'Образование', 'Мебель/Оборудование', 'Автомобиль', 'Бизнес', 'Бытовая Техника', 'Ремонт', 'Отпуск/Другое')
)] 
if not (19 <= Age <= 75):
    st.error("Возраст должен быть в диапазоне от 19 до 75 лет")

if not (0 <= Job <= 3):
    st.error("Кол-во работ должно быть неотрицательным и не более 3-х")

if not (4 <= Duration <= 72):
        st.error("Длительность должна быть между 4 и 72")


# Сбор всех параметров в один массив
features = np.array([Age, Sex, Job, Housing, Saving_accounts,
       Checking_account, Duration, Purpose])

# Кнопка для выполнения предсказания
if st.button("Проверить кредитоспособность"):
    result = predict(features)
    if result == 1: 
        st.success("Кредит одобрен!")
    else:
        st.error("Кредит не одобрен")
