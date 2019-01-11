# Scripting Program on Fortnox API
```

	 ___            _                   ___            _        _      
	| __>___  _ _ _| |_ ._ _  ___ __   / __> ___  _ _ <_> ___ _| |_ ___
	| _>/ . \| '_> | |  | ' |/ . \ \/ \__ \/ | '| '_>| || . \ | | <_-<
	|_| \___/|_|   |_|  |_|_|\___//\_\ <___/\_|_.|_|  |_||  _/ |_| /__/
	                                                     |_|           


```
To automate administration.
## How to run
### Commands
By running `python application/main.py -h` you get the help text that of all flags that at the time of writing this readme looked like this:

```
Fortnox Scripter

optional arguments:
  -h, --help            show this help message and exit
  -ci, --create_invoices
                        Iterate over all passed invoices and create invoices
                        programmatically. Requires a path to be executed.
  -on ORDER_NUMBER, --order_number ORDER_NUMBER
                        A optional value that gets passed in when posting a
                        invoice under the YourOrderNumber-filed in their API.
                        Finance usually put in the period of the invoice in a
                        string under this field.
  -p PATH, --path PATH  Input path.
  -sb, --sandbox        If this flag get's passed the program will look for a
                        sandbox fortnox key.
  -di DELETE_INVOCIES, --delete_invocies DELETE_INVOCIES
                        Iterate over the passed in list of Fortnox Invoice
                        ID's and delete them. Do it in this format: "2,3,4"

	 ___            _                   ___            _        _      
	| __>___  _ _ _| |_ ._ _  ___ __   / __> ___  _ _ <_> ___ _| |_ ___
	| _>/ . \| '_> | |  | ' |/ . \ \/ \__ \/ | '| '_>| || . \ | | <_-<
	|_| \___/|_|   |_|  |_|_|\___//\_\ <___/\_|_.|_|  |_||  _/ |_| /__/
	                                                     |_|           

```

### Creating Invoices in Fortnox from a file
The use case for this is to create invoices from a input file. The program expect the input CSV file to have the following format:
```csv
CustomerNumber,ArticleNumber,DeliveredQuantity
260,41,100
261,41,120
262,41,150
260,41,160
```
For this to work the `CustomerNumber` and `ArticleNumber` needs to be inputted to Fortnox before running this program.

Notice in the example above that the last entry in the CSV-file has the same `CustomerNumber` as the first entry. The program supports this and will group the two together to create one invoice with two rows in this instance.

One example of how to run the program to create invoices:
```bash
python application/main.py \
	-ci \
	-sb \
	-on "October - December" \
	-p ./examples/example_invoices.csv
```
What we are doing here is:

1. Define that you want to create invoices
2. Pass in -sb for Sandbox, default is prod
3. We pass in a string field for --order_number so that the receiver of this invoice nows which period the invoice is refering
4. Define the path for where the input file is

When the program has run we get the following ouput:
```
Created invoices with the following Fortnox ID's:
['37', '38', '39']
```
We can then use this list of ID's to delete ("makulera") invoices in Fortnox.

### Deleting ("makulera") invoices in Fortnox
For development we want to delete ("makulera") invoices. We can do this by passing in specific Fortnox invoice id's that we want to delete like this:

```bash
python application/main.py \
	-di "37,38,39"
```
## How to create Fortnox API Keys

1. Create a developer account with Fortnox [here](https://developer.fortnox.se/). A human will get in touch and supply the fields needed to authenticate. After this you yourself as a developer account will have a Fortnox instance. This can then be used as a Sandbox environment for testing this program.
2. After that you can make the one time request described here: [here](https://developer.fortnox.se/getting-started/).
3. When you have received the Access-Token you can then create the file `application/config/fortnox_key_sandbox.json` in the following format:
```json
{
	"Access-Token": "A very secret Token",
	"Client-Secret": "A very secret secret"
}
```
4. Then what you probably want to do is to use this developer account (or "integration" as Fortnox calls it) to interact with your companies Fortnox-account. What you then need to do is to go to the user management page inside the target Fortnox accounts web UI. You can then click `+ Lägg till integration` and search for your specific integration by inputting your developer accounts `Client-Secret`. After this you will get an email with a authentication code similar to when you created your developer account. Just as before you can then request the specific Access-Token for this new integration. Finally input this in the file `application/config/fortnox_key.json` in the same format as the sandbox key.

## Future improvements

1. Add API functionality to for example post a invoice receiver triggered by a network request.
2. Implement Docker.
3. Add support for creating customers in Fortnox.
