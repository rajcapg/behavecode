from behave import *
import requests 

@given(u'Given url is {URL} and status code {200} ')
def def step_impl(context, url,status):
url_test=url
status_test=status

#url
'''
https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=hour 
 https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=day
  https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=week
  https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=month
'''
response = requests.get(url)
status_code=response.status_code

if status_code == 200: 
    logging.log("test case pass")
    assert Pass
else:
   logging.log("test case fail")    

@given(u'Given url is  {URL} and status code is {200} ,return the json {'messsage'}')
def def step_impl(context, url,status,json):
url_test=url
status_test=status
json_message=json

#https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=10-10-30&unit=day

response=requests.get(url)
status_code=response.status_code

if status_code == 200: 
    logging.log("test case pass")
    assert Pass
else:
   logging.log("test case fail")  
   
 message=response.text()

if message.equals( json_message):
    loggging.info ("message is same Test case pass")
    asset pass
 elif:
    loggging.info ("message is not same Test case fail")
    assert fail
    
    
@given(u'Given change url is  {URL} and status code is {200} ,missing unit in url return the json {'messsage'}')
def def step_impl(context, url,status,json):
url_test=url
status_test=status
json_message=json

#https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30

response=requests.get(url)
status_code=response.status_code

if status_code == 200: 
    logging.log("test case pass")
    assert Pass
else:
   logging.log("test case fail")  
   
 message=response.text()

if message.equals( json_message):
    loggging.info ("message is same Test case pass")
    asset pass
 elif:
    loggging.info ("message is not same Test case fail")
    assert fail
    
    
#Bug
@given( url is  {URL} and status code is {200} ,return "the correct the hour"}

def step_impl(context, url,status,hour):
url_test=url
status_test=status
hour=hour

#https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=2023-08-13

response=requests.get(url)
status_code=response.status_code

if status_code == 200: 
    logging.log("test case pass")
    assert Pass
else:
   logging.log("test case fail")  
   
   message=response.text()
   
   if any(re.findall(r'24', message, re.IGNORECASE):
        print 'test case failed it is not returning correct hour'
        assert Fail
        
    else
       print 'test case pass it is  returning correct hour'
        assert pass
    
    
 @given(url is  {URL} and status code is {200} ,return "the 0 week should return")
 def step_impl(context, url,status,hour):
url_test=url
status_test=status
hour=hour

#https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=2023-08-13

response=requests.get(url)
status_code=response.status_code

if status_code == 200: 
    logging.log("test case pass")
    assert Pass
else:
   logging.log("test case fail")  
   
   message=response.text()
   
   if any(re.findall(r'0', message, re.IGNORECASE):
        print 'test case pass it is  returning correct 'week
        assert pass
        
    else
       print 'test case fail it is not returning correct week'
        assert fail
 
 
  @given(url is  {URL} and status code is {200} ,return "the 1 day should return")
  
  def step_impl(context, url,status,hour):
url_test=url
status_test=status
hour=hour

#https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=2023-08-13

response=requests.get(url)
status_code=response.status_code

if status_code == 200: 
    logging.log("test case pass")
    assert Pass
else:
   logging.log("test case fail")  
   
   message=response.text()
   
   if any(re.findall(r'1', message, re.IGNORECASE):
        print 'test case pass it is  returning  1 day'
        assert pass
        
    else
       print 'test case  not pass it is  returning not day hour'
        assert fail