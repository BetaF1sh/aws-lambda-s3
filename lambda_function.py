from datetime import datetime
import boto3
import json
from jejunuMeals import JejunuMeals

Bucket = boto3.resource('s3').Bucket('jejunu.muhun.dev')


def lambda_handler(event, context):
    Dump = json.dumps(JejunuMeals().menus(), ensure_ascii=False)
    Bucket.put_object(
        Key='meals/index.json', Body=Dump)
    Bucket.put_object(
       Key=f'meals/logs/{datetime.now():%m-%d}.json', Body=Dump)

# TODO: '없음' 들어있는 속성 없애기
# def lambda_handler():
#     meals = JejunuMeals().menus()
#     meals_copy = copy.deepcopy(meals)
#     for w in meals.keys():
#         for tim in meals[w].keys():
#             for typ, val in meals[w][tim].items():
#                 if val[0] == '없음' or val[0].find(' ') != -1:
#                     del meals_copy[w][tim][typ]
#     return meals_copy
