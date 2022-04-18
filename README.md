# TFL Disruption Tracker

### TL;DR
Application pulls data from the public TFL api, and sends a text message (SMS) to the recipient. Recipient receives information about the current disruptions to the TFL network, split by network line, where disruptions for each line are sent in a seperate text message (no message is sent for lines where no disruptions are present.

Application is written Python and run using AWS Lambda and AWS SNS. Architecture Diagram below:
