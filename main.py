# Создайте три разные функции представления:

#     функция index должна отображаться по корневому маршруту и по маршруту index со знаком слэша (/) на конце и возвращать строку "index"
#     функция contact должна отображаться по маршруту contact со знаком слэша (/) на конце и возвращать строку "contact information"
#     функция calculate должна отображаться по роуту "/calculate/7/9/" и возвращать число 7, возведенное в 9 степень, где результат преобразован к строке

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return
	
@app.route('/<myyau>/')
def speak_myau(myyau):
	return myyau



if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)
