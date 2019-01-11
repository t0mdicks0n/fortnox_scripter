import csv
import pprint
import json
from helpers import post_invoice

def parse_csv(inv_spec_dir) :
	try :
		with open(inv_spec_dir) as csv_file :
			# Create a list of dicts of the input csv file
			output = [{k: int(v) for k, v in row.items()}
								for row in csv.DictReader(csv_file, delimiter=',', skipinitialspace=True)]
	except Exception as e :
		print "There was an error with opening CSV-file: ", str(e)
	finally :
		return output

def format_invoices(raw_invoice_data) :
	customer_dict = {}
	# Group the invoice rows on CustomerNumber
	for row in raw_invoice_data :
		if row['CustomerNumber'] in customer_dict :
			customer_dict[row['CustomerNumber']] = customer_dict[row['CustomerNumber']] + [{
				"ArticleNumber": row['ArticleNumber'],
				"DeliveredQuantity": float(int(row['DeliveredQuantity']))
			}]
		else :
			customer_dict[row['CustomerNumber']] = [{
				"ArticleNumber": row['ArticleNumber'],
				"DeliveredQuantity": float(int(row['DeliveredQuantity']))
			}]
	return customer_dict

def iterate_over_invoices(invoices, fortnox_key, order_number_reference) :
	fortnox_invoice_id = []
	for CustomerNumber in invoices :
		# Post a invoice to Fortnox API and get the id Fortnox returns
		fortnox_id = post_invoice(
			CustomerNumber,
			invoices[CustomerNumber],
			fortnox_key['Access-Token'],
			fortnox_key['Client-Secret'],
			order_number_reference
		)
		# Cache the id
		fortnox_invoice_id.append(fortnox_id.split('/')[-1])
	return fortnox_invoice_id

def main(inv_spec_dir, sandbox=False, order_number_reference=False) :
	# Parse the passed in CSV to get the raw invoice data
	raw_invoice_data = parse_csv(inv_spec_dir)
	# Format the raw data in accordance with Fortnox wanted input
	invoices = format_invoices(raw_invoice_data)
	# Get the API key for Fortnox API
	if sandbox :
		fortnox_key = json.load(open('application/config/fortnox_key_sandbox.json'))
	else :
		fortnox_key = json.load(open('application/config/fortnox_key.json'))
	# Post the invoices and get their respective ids
	invoice_ids = iterate_over_invoices(invoices, fortnox_key, order_number_reference)
	print("Created invoices with the following Fortnox ID's:")
	print(invoice_ids)
