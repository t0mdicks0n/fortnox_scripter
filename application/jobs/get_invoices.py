import csv
import pprint
import json
from helpers import get_all_invoices

def iterate_and_filter_invoices(invoices) :
	filtered_invoices = []
	for invoice in invoices :
		if invoice["Sent"] is False :
			# TODO: Make this filter dynamic, did it quick and dirty 
			# now to fix an emergancy.
			if invoice["InvoiceDate"] == "2019-05-22" :
				filtered_invoices.append(invoice["@url"].split('/')[-1])
				print json.dumps(invoice, indent=2)
	return filtered_invoices

def main(sandbox=False) :
	# Get the API key for Fortnox API
	if sandbox :
		fortnox_key = json.load(open('application/config/fortnox_key_sandbox.json'))
	else :
		fortnox_key = json.load(open('application/config/fortnox_key.json'))
	invoices = get_all_invoices(fortnox_key['Access-Token'], fortnox_key['Client-Secret'])
	filtered_invoices = iterate_and_filter_invoices(invoices)
	print(json.dumps(filtered_invoices, indent=2))