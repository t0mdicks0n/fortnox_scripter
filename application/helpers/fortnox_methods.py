import requests
import json

def post_invoice(customer_number, invoice_rows, access_token, client_secret) :
	try :
		r = requests.post(
			url="https://api.fortnox.se/3/invoices",
			headers = {
				"Access-Token": access_token,
				"Client-Secret": client_secret,
				"Content-Type":"application/json",
				"Accept":"application/json",
			},
			data = json.dumps({
				"Invoice": {
						"InvoiceRows": invoice_rows,
						"CustomerNumber": customer_number
				}
			})
		)
		print('Response HTTP Status Code : {status_code}'.format(status_code=r.status_code))
		print('Response HTTP Response Body : {content}'.format(content=r.content))
	except requests.exceptions.RequestException as e :
		print('HTTP Request failed')
	finally :
		json_data = json.loads(r.content)
		return json_data['Invoice']['@url']