import requests

KEY = "sLjkkM1fasVUtkHXOh662ECP09Vxic8m"
API = "https://api.exchangeratesapi.io/v1/latest?access_key=" + KEY


def all_currency_names_rate_lower_10_real_data():
	"""
	prod section
	"""
	print(API)  # check the path
	response = requests.get(API)  # get request
	data = response.json()  # formatting to json
	print(data)  # print data
	data = filter(data.rates < 10, data)  # filter the data
	print(data)
	return data
all_currency_names_rate_lower_10_real_data()

def all_currency_names_rate_lower_10_mock_data():
	# just mocking data of arbitrary currency name
	return {
		"AAA", "BBB", "CCC"
	}
