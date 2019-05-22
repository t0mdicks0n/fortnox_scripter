# coding: utf8
import argparse
from jobs import create_invoices
from jobs import delete_invoices
from jobs import get_invoices

if __name__ == '__main__' :
	parser = argparse.ArgumentParser(
		description='Fortnox Scripter',
		formatter_class=argparse.RawDescriptionHelpFormatter,
		epilog="""
	 ___            _                   ___            _        _      
	| __>___  _ _ _| |_ ._ _  ___ __   / __> ___  _ _ <_> ___ _| |_ ___
	| _>/ . \| '_> | |  | ' |/ . \\ \/ \__ \/ | '| '_>| || . \ | | <_-<
	|_| \___/|_|   |_|  |_|_|\___//\_\ <___/\_|_.|_|  |_||  _/ |_| /__/
	                                                     |_|           
	""")
	# Define the arguments
	parser.add_argument(
		'-ci',
		'--create_invoices',
		action='store_true',
		help="""Iterate over all passed invoices and create invoices
				    programmatically. Requires a path to be executed."""
	)
	parser.add_argument(
		'-on',
		'--order_number',
		type=str,
		help="""A optional value that gets passed in when posting a 
						invoice under the YourOrderNumber-filed in their API.
						Finance usually put in the period of the invoice in a 
						string under this field."""
	)
	parser.add_argument(
		'-p',
		'--path',
		type=str,
		help="""Input path."""
	)
	parser.add_argument(
		'-sb',
		'--sandbox',
		action='store_true',
		help="""If this flag get's passed the program will look for
				 		a sandbox fortnox key."""
	)
	parser.add_argument(
		'-di',
		'--delete_invocies',
		type=str,
		help="""Iterate over the passed in list of Fortnox Invoice
						ID's and delete them. Do it in this format:
						"2,3,4" """
	)
	parser.add_argument(
		'-gi',
		'--get_invoices',
		action='store_true',
		help="""Get all outstanding invoices in Fortnox. Useful for removing a
		bunch you created by mistake."""
	)
	args = parser.parse_args()
	if args.create_invoices :
		if args.path is None :
			raise ValueError('Input path -p most be specified!')
		else :
			create_invoices(args.path, args.sandbox, args.order_number)
	if args.delete_invocies :
		args_as_list = [int(item) for item in args.delete_invocies.split(',')]
		delete_invoices(args_as_list, args.sandbox)
	if args.get_invoices :
		get_invoices(args.sandbox)
