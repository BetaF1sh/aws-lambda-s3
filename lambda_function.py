from datetime import datetime
import boto3
import yaml
from jejunuMeals import JejunuMeals

noalias = yaml.dumper.SafeDumper
noalias.ignore_aliases = lambda self, data: True

Bucket = boto3.resource('s3').Bucket('jejunu.muhun.dev')


def lambda_handler(event, context):
    Dump = yaml.dump(JejunuMeals().menus(), default_flow_style=False,
                     allow_unicode=True, Dumper=noalias)
    Bucket.put_object(
        Key='meals/index.yaml', Body=Dump)
    Bucket.put_object(
        Key=f'meals/logs/{datetime.now():%m-%d}.yaml', Body=Dump)
