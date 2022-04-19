# TFL Disruption Tracker

## TL;DR
Application pulls data from the public TFL api, and sends a text message (SMS) to the recipient. Recipient receives information about the current disruptions to the TFL network, split by network line, where disruptions for each line are sent in a seperate text message (no message is sent for lines where no disruptions are present.

Application is written Python and run using AWS Lambda and AWS SNS.

## Prerequisites & Steps to run this application
### Prerequisites
- AWS Account

### Steps
- Create Lambda Function in AWS
- Create an IAM role that enables Lambda to use Amazon SNS
- Use code provided within this repository to create a lambda function, usind Python runtime
- Attach Lambda layer to enable the function to use Python libraries (Requests and Pandas)
- Adjust Function Timeout to >10 seconds to ensure the function doesn't time out
- Optional: Add trigger to Lambda function to run function automatically
