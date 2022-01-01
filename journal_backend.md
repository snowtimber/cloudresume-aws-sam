Hey all, here is my attempt at Forrest Brazeal's #CloudResumeChallenge:

This repo and journal is specific to my attempt to create the backend using dynamoDB, Lambda, AWS API gateways necessary for my cloud resume's visitor counter using AWS SAM.  Please see this link for the frontend code and my full experience building out this challenge -> https://github.com/MooseEagleShark/LoganTMeyerResume/

Here are the challenge requirements from his blogpost at: https://forrestbrazeal.com/2020/04/23/the-cloud-resume-challenge/

Some notes from my Journey:

Grabbed AWS lamda template with pre-traffic and pos-traffic stages from:
https://docs.aws.amazon.com/codedeploy/latest/userguide/tutorial-lambda-sam-template.html

Grabbed basic Lambda, API Gateway, Dynamo DP yml from:
https://medium.com/@gurlgilt/deploying-aws-sam-lambda-api-gateway-dynamodb-and-s3-ad11e619d322

Found sample resources from AWS samples at https://github.com/aws-samples/cookiecutter-aws-sam-dynamodb-python

A cool thing about the above definitions: You don’t actually need to separately define the API Gateway Resources, specifications for those resources will be inferred. Another note: only one resource is made with multiples methods (endpoints).

Found https://seanjziegler.com/how-to-build-a-free-static-resume-site-with-aws-s3-cloudfront-and-route-53/#5-deploy-a-dynamodb-table-with-cloudformation which covers a lot of ground but leaves out the tricky backend parts...

The page views vs visitors part is interesting and gives me an idea to capture visitors by ip and access date time.  This data can be used to count unique visitor and when they viewed my resume.

A little about me:
I am a Mech Eng. from CU Boulder, always had a passion for tech growing up, but have spent my professional life working in Oil & Gas and construction (MEP for those in the industry) and small development (ADUs) in OK and Denver, CO.

As far as my tech background, I dabbled in some early Joomla websites for friends and family while in college in the early 2010s, before wordpress took over everything.  I know a bit about website frontend but all of the cloud and backend stuff is new to me.

Here goes my attempt at Forrest Brazeal's challenge:
