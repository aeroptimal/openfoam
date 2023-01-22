from decouple import config
from pathlib import Path
import boto3

BASE_DIR = Path(__file__).resolve().parent.parent.as_posix()

HOST = config('HOST', cast=str)
AWS_ID = config('AWS_ID', cast=str)
AWS_ACCESS_KEY = config('AWS_ACCESS_KEY', cast=str)
OPENFOAM_QUEUE_URL = config('OPENFOAM_QUEUE_URL', cast=str)

AWS_CLIENT = boto3.client('sqs', region_name='us-east-1',
                    aws_access_key_id=AWS_ID, 
                    aws_secret_access_key=AWS_ACCESS_KEY)