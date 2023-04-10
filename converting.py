#Iaas        caas         serverless
#ec2         EKS
#lightsail   ECS 
#            Fargate             

#lambda:- is a serverless technology(is mostly supported for event based triggers(s3uploads,ec2startstop,cloud watch)(max 15min code run)(no maintance,pay as you go,high avalability,scalability)
#Runtime:it gives us   customer Runtime:we create our own runtime 
#python and node.js we can edit lambda code
#in lambda we can apply our code by 1)writting on console,2)uploading by zip file and 3)uploading by s3 url <10mb to run the code
#
#
#
#
#
#main lambda code format:-
import json

def lambda_handler(event, context):
    # TODO implement                                        #{                    
    return {                                                #   "statusCode": 200
        'statusCode': 200,                                  #  "body": "\"Hello from Lambda!\""
        'body': json.dumps('Hello from Lambda!')            #}
    }

{                                                         #{
  "statusCode": 200,                                         #status 
  "body": "\"Hello from Lambda!\""                           #body
}                                                          #}

#with sm changes to the basic code in lambda
import json

def lambda_handler(event, context):
    # TODO implement
    print("sagar muthyala")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello sagar muthyala!')
    }                                                                    #Hello sagar muthyala

#2)By using lambda and s3 we are converting csv file to json file
import csv
import json
import boto3

 

def lambda_handler(event, context):

    targetbucket = 'convert890'
    csvkey = 'groceries.csv'
    jsonkey = 'groceries.json'

    s3 = boto3.resource('s3')
    csv_object = s3.Object(targetbucket, csvkey)
    csv_content = csv_object.get()['Body'].read().splitlines()
    s3_client = boto3.client('s3')
    l = []

    for line in csv_content:
        x = json.dumps(line.decode('utf-8')).split(',')
        Username = str(x[0])
        Company = str(x[1])
        Title = str(x[2])
        y = '{ "Username": ' + Username + '"' + ','  \
            + ' "Company": ' + '"' + Company + '"' + ',' \
            + ' "Title": ' + '"' +  Title + '"' + '}'
        l.append(y)

 

    s3_client.put_object(
        Bucket=targetbucket,
        Body= str(l).replace("'",""),
        Key=jsonkey,
        ServerSideEncryption='AES256'
    )


"""
import json
import datetime
import random
import boto3

session=boto3.Session(aws_access_key_id=AKIAWRFJHTO6D6YI6NK5,
                      aws_secret_access_key=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, region_name=us-east-1)

client = session.client('kinesis')

kinesis_stream="{converttesting}"


def getData(iotName, lowVal, highVal):
   data = {}
   data["iotName"] = iotName
   data["iotValue"] = random.randint(lowVal, highVal) 
   return data

temp=0;

while temp<100:
   rnd = random.random()
   if (rnd < 0.01):
      data = json.dumps(getData("DemoSensor", 100, 120))  
      client.put_record(StreamName=kinesis_stream, Data=data, PartitionKey="1")
      print('*************************** anomaly *********************** ' + data)
   else:
      data = json.dumps(getData("DemoSensor", 10, 20))  
      client.put_record(StreamName=kinesis_stream, Data=data, PartitionKey="1")
      print(data)
   temp=temp+1
"""

#checking the accountno by using lambda layers concept
#dic = {'accountno' : '1234567890'}
def AccValidation(event):
    if len(event['accountno']) == 10 :         #first create a new folder,creat a file,and zip the folder and upload in lambda layer
        return True                            #this code is used layer to create a validate code by 
    else :
        return False

#this is palced in lambda code(to get account number)
import json
import accvali

def lambda_handler(event,context):
    #TODO implement
    if accvali.AccValidation(event):
        Create_Account()                                               #this is main code in lambda 
        print("Account Number is : ",event.get('accountno'))
    else:
        print("Invalid Account Number..!")
def Create_Account():
    print("New Account is Created...!")


#after that edit the test place with:
#{
 #"accountno" : "1234567890"                                            #this is changed in key value place in lambda test
#}
#
#then we get null values the code will be get run 

#listing buckets in aws by lambda:-
#import json
#import boto3
#
#s3 - boto3.resource('s3')
#
#def lambda_handler(event,context):
#    bucket4list - []
#    for bucket in s3.bucket.all():
#        bucketlist.append(bucket.name)
#    print(json.dumps(bucketlist))
#    return {
#        "statuscode": 200,
#        "body": bucketlist
#    }                                                 #this will list the bucket list
              
#                  
#listing buckets in aws by lambda with python pytz time:-
#import json
#import boto3
#from pytz import timezone
#import pytz 
#from help import print_name
#from datetime import datetime
#
#s3 - boto3.resource('s3')
#
#def handler(event,context):
#    tz - timezone("Asia/Calcutta")
#    print(datetime.now(tz))
#    bucketlist - []
#    print_name("hello")
#    for bucket in s3.bucket.name):
#        bucketlist.append(bucket.name):
#    return {
#        "statuscode": 200,
#        "buckets": bucketlist                          #this will show the bucketlist and time in the descrepition
#    }




#from one bucket to anther bucket data transfered
#from __future__ import print_function
#import boto3
#import time, urllib
#import json
#"""Code snippet for copying the objects from AWS source S3 bucket to target S3 bucket as soon as objects uploaded on source S3 bucket
#@author: Prabhakar G
#"""
#print ("*"*80)
#print ("Initializing..")
#print ("*"*80)
#
#s3 = boto3.client('s3')
#
#def lambda_handler(event, context):
# TODO implement
#source_bucket = event['Records'][0]['s3']['bucket']['name']
#object_key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
#target_bucket = 'my-target-bucket'
#copy_source = {'Bucket': source_bucket, 'Key': object_key}
#print ("Source bucket : ", source_bucket)
#print ("Target bucket : ", target_bucket)
#print ("Log Stream name: ", context.log_stream_name)
#print ("Log Group name: ", context.log_group_name)
#print ("Request ID: ", context.aws_request_id)
#print ("Mem. limits(MB): ", context.memory_limit_in_mb)
#try:
#print ("Using waiter to waiting for object to persist through s3 service")
#waiter = s3.get_waiter('object_exists')
#waiter.wait(Bucket=source_bucket, Key=object_key)
#s3.copy_object(Bucket=target_bucket, Key=object_key, CopySource=copy_source)
#return response['ContentType']
#except Exception as err:
#print ("Error -"+str(err))
#return e 


#S3 objects list code
## aws s3api get-object --bucket arn:aws:s3-object-lambda:us-east-1:xxxxx:accesspoint/just-purchases --key orders.json transformed_data.json

#import boto3
#import urllib3
#import json

#http = urllib3.PoolManager()

#def lambda_handler(event, context):
#print(event)

#1 & 2 Extract relevant metadata including S3URL out of input event
#object_get_context = event["getObjectContext"]
#request_route = object_get_context["outputRoute"]
#request_token = object_get_context["outputToken"]
#s3_url = object_get_context["inputS3Url"]

# 3 - Download S3 File
#response = http.request('GET', s3_url)

#original_object = response.data.decode('utf-8')
#as_list = json.loads(original_object)
#result_list = []

# 4 - Transform object
#for record in as_list:
#if record['orderType'] == "PURCHASE":
#result_list.append(record)

# 5 - Write object back to S3 Object Lambda
#s3 = boto3.client('s3')
#s3.write_get_object_response(
#Body=json.dumps(result_list),
#RequestRoute=request_route,
#RequestToken=request_token)

#return {'status_code': 200}
#
#
#creat bucket through lambda
#import json
#import boto3
#
#def lambda_handler(event, context):
#    client = boto3.client('s3')
#
#    response = client.create_bucket(
#    Bucket='hergiyhguiselhtgiy',
#    CreateBucketConfiguration={
#        'LocationConstraint': 'ap-south-1'
#    },
#)
#
#
#copy to  different folders
#import urllib.request, urllib.parse, urllib.error
#import json
#import os.path
#import boto3
#print('function start (Cloudwatch)')
#
#s3 = boto3.client('s3')
#
#def lambda_handler(event, context):
#    source_bucket = event['Records'][0]['s3']['bucket']['name']
#    key = urllib.prase.unquote_plus(event['Records'][0]['s3']['object']['key'])
#    copy_source = {'bucket': source_bucket, 'Key':key}
#
#    #cloudwatch info
#    print("Log stream name:", context.log_stream_name)
#    print("Log group name:", context.log_group_name)
#    print("Request ID:", context.aws_request_id)
#
#    #Logic
#    try:
#        waiter = s3.get_waiter('object_exist')
#        waiter.wait(Bucket=source_bucket, Key=key)
#
#        #get the file extension
#        extension = os.path.splitext(key)[1]
#
#        #copy from s3 to s3
#        if extension==",jpg"
#
#
##copy from s3 to s3
#        if extension==".jpg":
#            s3.copy_object(Bucket="lambdatestingtothebucket", Key=key, Copy_source=copy_source)
#        if extension==".pdf":
#            s3.copy_object(Bucket="lambdatestingtothebucket2", Key=key, Copy_source=copy_source)
#        if extension==".txt":
#            s3.copy_object(Bucket="lambdatestingtothebucket3", Key=key, Copy_source=copy_source)
#
#    except Extension as e:
#        print(e)
#        print('Error while trying to copy the file, Does not exist' .format(key, source_bucket))
#        raise e
#
#
#copy to another folder bucket
#import boto3
#def lambda_handler(event, context):
#    file_name = event['Records'][0]['s3']['object']['key']
#    source_bucket_name='tarun-in'
#    service_name='s3'
#    region_name='ap-south-1'
#    aws_access_key_id='AKIAU66KP2H4RKL4XIRW'
#    aws_secret_access_key='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'
#    s3 = boto3.resource(
#        service_name=service_name,
#        region_name=region_name,
#        aws_access_key_id=aws_access_key_id,
#        aws_secret_access_key=aws_secret_access_key
#        )
#    copy_source = {
#        'Bucket':source_bucket_name,
#        'Key': 'vamsy.pem'
#    }
#    s3.meta.client.copy(copy_source, 'tarun-out', 'sainath/vamsy.pem')
#
#
#to create instance
#import json
#import boto3
#ec2 = boto3.resource('ec2')
#
#instances = ec2.create_instances(
#        ImageId="ami-090fa75af13c156b4",
#        MinCount=1,
#        MaxCount=1,
#        InstanceType="t2.micro",
#        KeyName="mine.222dlt"
#   )
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#





























