import json
import requests
import pandas as pd
import boto3

import warnings
warnings.filterwarnings('ignore')


client = boto3.client('sns')

def lambda_handler(event, context):
    print("Running")
    lines = ['bakerloo', 'central', 'circle', 'district', 'dlr', 'hammersmith-city', 'jubilee', 'metropolitan',
    'northern','piccadilly','victoria', 'waterloo-city']



    data = pd.DataFrame()
    for i in lines:
            request_string = "https://api.tfl.gov.uk/Line/" + i + "/Status"
            request_object = requests.get(request_string).json()
            temp_df = pd.DataFrame(request_object[0]["lineStatuses"])
            temp_df["Line"] = i
            data = data.append(temp_df)
    output_data =  data[["Line","statusSeverityDescription","reason"]]

    disruption_filtered_data = []
    for i in range(len(output_data)):
        if output_data.iloc[i][1] == "Good Service":
            pass
        else:
            disruption_filtered_data.append([output_data.iloc[i][0],str(output_data.iloc[i][2]).lower() +"\n\n"])
            
    df = pd.DataFrame(disruption_filtered_data,columns=(["line","disruption"])).set_index("line")
    unique_disruption_list = list(set(df.index.tolist()))
    
    message_list = []
    for i in range(len(unique_disruption_list)):
        message = ""
        disruption_list = []
        temp_df = df[df.index==unique_disruption_list[i]]
        disruption_list.append(temp_df["disruption"].tolist())
        
        for j in range(len(disruption_list[0])):
            message += disruption_list[0][j]
        message_list.append(message)
    
    for i in message_list:
        message = i
        response = client.publish(
            PhoneNumber="+XXXXXXXXXX",
            Message=message,
            MessageAttributes={
                'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': "status-tfl"
                }    
            }
        )
        print(message)
    return "Success"