# https://www.udemy.com/course/100-days-of-code/learn/lecture/21489864#overview

# Day 37
# Advanced authentification / POST - PUT - DELETE requests

# Habit tracker project

import requests
import datetime

TOKEN = "token"
USERNAME = "username"

# using https://pixe.la/

# creating an account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# creating a graph
graphId = "graph1"
graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_config = {
    "id": graphId,
    "name": "Test graph",
    "unit": "test",
    "type": "int",
    "color": "sora",
    "timezone": "Europe/Paris"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# posting a pixel update
current_date = datetime.datetime.now()
# def formatDate(datetime):
#     year = datetime.year
#     month = datetime.month
#     day = datetime.day
#     if month < 10:
#         month = "0" + str(month)
#     if day < 10:
#         day = "0" + str(day)
    
#     formatted_date = str(year) + str(month) + str(day)

#     return formatted_date

# formatted_date = formatDate(current_date)
formatted_date = current_date.strftime("%Y%m%d")
print(formatted_date)

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graphId}"
pixel_params = {
    "date": formatted_date,
    "quantity": "1",
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# updating created pixel
update_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graphId}/20220616"
update_params = {
    "quantity": "10"
}
# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

# delete a pixel
delete_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graphId}/20220616"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)