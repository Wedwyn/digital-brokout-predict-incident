import pandas as pd
import numpy as np
import os

data_dir = os.path.dirname(os.path.realpath(__file__))
data_file = os.path.join(data_dir, 'FINAL_DATASET_643.csv')

df = pd.read_csv(data_file)

fullAreas = [
  { 'name': 'Краснокамский городской округ', 'meteo': 'Пермь' , 'predict': [] },
  { 'name': 'Пермский муниципальный округ', 'meteo': 'Пермь', 'predict': [] },
  { 'name': 'Пермский городской округ', 'meteo': 'Пермь', 'predict': [] },
  { 'name': 'Соликамский городской округ', 'meteo': 'Березники', 'predict': [] },
  { 'name': 'Кунгурский муниципальный округ', 'meteo': 'Кунгур', 'predict': [] },
  { 'name': 'городской округ Березники', 'meteo': 'Березники', 'predict': [] },
  { 'name': 'Суксунский городской округ', 'meteo': 'Кунгур', 'predict': [] },
  { 'name': 'Чайковский городской округ', 'meteo': 'Чайковский', 'predict': [] },
  { 'name': 'Чусовской городской округ', 'meteo': 'Лысьва', 'predict': [] },
  { 'name': 'Лысьвенский городской округ', 'meteo': 'Лысьва', 'predict': [] },
  { 'name': 'Добрянский городской округ', 'meteo': 'Добрянка', 'predict':[] },
  { 'name': 'Кудымкарский муниципальный округ', 'meteo': 'Кудымкар', 'predict':[] },
  { 'name': 'Нытвенский городской округ', 'meteo': 'Верещагино', 'predict':[] },
  { 'name': 'Губахинский муниципальный округ', 'meteo': 'Губаха', 'predict':[] },
  { 'name': 'Чернушинский городской округ', 'meteo': 'Чернушка', 'predict':[] },
  { 'name': 'Верещагинский городской округ', 'meteo': 'Верещагино', 'predict':[] },
  { 'name': 'Октябрьский городской округ', 'meteo': 'Октябрьский', 'predict':[] },
  { 'name': 'Горнозаводский городской округ', 'meteo': 'Бисер', 'predict':[] },
  { 'name': 'Куединский муниципальный округ', 'meteo': 'Чернушка', 'predict':[] },
  { 'name': 'Осинский городской округ', 'meteo': 'Оса', 'predict':[] },
  { 'name': 'городской округ Кизел', 'meteo': 'Губаха', 'predict':[] },
  { 'name': 'Красновишерский городской округ', 'meteo': 'Вая', 'predict':[] },
  { 'name': 'Бардымский муниципальный округ', 'meteo': 'Оса', 'predict':[] },
  { 'name': 'Карагайский муниципальный округ', 'meteo': 'Верещагино', 'predict':[] },
  { 'name': 'Ильинский городской округ', 'meteo': 'Чермоз', 'predict':[] },
  { 'name': 'Берёзовский муниципальный округ', 'meteo': 'Кунгур', 'predict':[] },
  { 'name': 'Юсьвинский муниципальный округ', 'meteo': 'Кудымкар', 'predict':[] },
  { 'name': 'Чердынский городской округ', 'meteo': 'Вая', 'predict':[] },
  { 'name': 'Частинский муниципальный округ', 'meteo': 'Ножовка', 'predict':[] }, 
  { 'name': 'Кишертский муниципальный округ', 'meteo': 'Кунгур', 'predict':[] },
  { 'name': 'Гайнский муниципальный округ', 'meteo': 'Коса', 'predict':[] },
  { 'name': 'Большесосновский муниципальный округ', 'meteo': 'Оханск', 'predict':[] },
  { 'name': 'Оханский городской округ', 'meteo': 'Оханск', 'predict':[] },
  { 'name': 'Кочёвский муниципальный округ', 'meteo': 'Кочево', 'predict':[] },
  { 'name': 'Ординский муниципальный округ', 'meteo': 'Кунгур', 'predict':[] },
  { 'name': 'Очёрский городской округ', 'meteo': 'Верещагино', 'predict':[] },
  { 'name': 'Еловский муниципальный округ', 'meteo': 'Ножовка', 'predict':[] },
  { 'name': 'Сивинский муниципальный округ', 'meteo': 'Верещагино', 'predict':[] },
  { 'name': 'Юрлинский муниципальный округ', 'meteo': 'Кочево', 'predict':[] },
  { 'name': 'Уинский муниципальный округ', 'meteo': 'Чернушка', 'predict':[] },
  { 'name': 'Косинский муниципальный округ', 'meteo': 'Коса', 'predict':[] },
  { 'name': 'Александровский муниципальный округ', 'meteo': 'Березники', 'predict':[] }
]

def getPredictParams(meteo):
  # df[df['Район'] == meteo].sort_values('Дата').tail(10)
  X = df[df['Район'] == meteo].sort_values('Дата').tail(10)
  X = X.drop(['Проиcшествие','Дата','Район'], axis=1)
  X = X.to_numpy()
  return X.tolist()

def getDoneAreas():
  for i in range(len(fullAreas)):
    fullAreas[i]['predictParams'] = getPredictParams(fullAreas[i]['meteo'])
  return fullAreas

areasForWork = getDoneAreas()
