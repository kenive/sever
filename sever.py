from flask import Flask, render_template

from database import create_server_connection


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
    # connection = create_server_connection("127.0.0.1", "", '')

# import requests module
# import requests
 
# # Making a get request
# response = requests.get('https://xuannguyen.pythonanywhere.com/api/test')
 
# # print response
# print(response)
 
# # print json content
# print(response.json())