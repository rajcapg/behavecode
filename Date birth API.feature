
Feature: Date birth API 


@regression
Scenario Outline: check the API url should working and status code is 200 
Given url is  <URL> and status code <200>


Examples:
  | URL | Status code |
  |https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=hour       | 200    |
  | https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=day  | 200         |
  | https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=week | 200        |
  |https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30&unit=month|200|

@regression
Scenario Outline: change the API URL MM-YYYY-DD 
Given url is  <URL> and status code is <200> ,return the json <'{"message"}'>

Examples:
| url | 200 | json |
|  https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=30-10-1990&unit=hour    | 200 | '{"message": "Please specify dateofbirth in ISO format YYYY-MM-DD"}' |

@regression
Scenario Outline: change the API URL without unit
Given change url is  <URL> and status code is <200> ,missing unit in url return the json <'messsage'>
Examples:
| url | 200 | json |
| https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=1990-10-30     | 200 | 'Please pass the correct format' |


#Bug  hour is not correct
@regression
Scenario Outline: change the API URL and pass next day
Given url is  <URL> and status code is <200> ,return "the correct the hour"
| url | 200 | result |
 |https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=2023-08-14&unit=hour  |200| 24   |

@regression
Scenario Outline: change the API URL and pass next day
Given url is  <URL> and status code is <200> ,return "the 0 week should return"
| url | 200 | result |
 |https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=2023-08-14&unit=week  |200| 0   |


@regression
Scenario Outline: change the API URL and pass next day
Given url is  <URL> and status code is <200> ,return "the 0 month should return"
| url | 200 | result |
 |https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=2023-08-14&unit=month  |200| 0   |


@regression
Scenario Outline: change the API URL and pass next day
Given url is  <URL> and status code is <200> ,return "the 1 day should return"
| url | 200 | result |
 |https://lx8ssktxx9.execute-api.eu-west-1.amazonaws.com/Prod/next-birthday?dateofbirth=2023-08-14&unit=day  |200| 0   |

