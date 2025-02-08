import joblib
import numpy as np
import pandas as pd


def preprocess(features):
    # Загружаем имена колонок
    column_names = pd.read_csv('german_credit_data.csv', nrows=0).columns

    # Удаляем таргет и дубликат индекса
    column_names = column_names.drop(['Credit amount', 'Unnamed: 0'])
    input_series = pd.DataFrame([pd.Series(features, index=column_names)])


    input_series = input_series.replace('nan', 'unknown')

    categorical_columns = ['Sex', 'Housing', 'Checking account', 'Purpose']

    # Загрузим OneHotEncoder
    ohe = joblib.load('one_hot_encoder.joblib')

    # Загрузим OrdinalEncoder
    oe = joblib.load('ordinal_encoder.joblib')

    # Применяем кодирование
    input_series['Saving accounts'] = oe.transform(input_series[['Saving accounts']])

    encoded_data = ohe.transform(input_series[categorical_columns]).toarray()

    encoded_input_series = pd.DataFrame(encoded_data, columns=ohe.get_feature_names_out(categorical_columns))

    # Добавляем к фрейму кодирование и выбрасываем старые колонки
    input_series = pd.concat([input_series, encoded_input_series], axis=1).drop(categorical_columns, axis=1)


    input_series = input_series.replace([np.inf, -np.inf], np.nan)

    # Скалирование
    scaler = joblib.load('scaler.joblib')
    input_series = scaler.transform(input_series)

    return input_series
