import csv
import requests


URL = "http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/gross_output_by_industrial_division_at_current_prices.csv&nid=135"


def get_data():
    r = requests.get(URL)
    data = r.text
    RESULTS = {'children': []}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        RESULTS['children'].append({
         'name': line['industrial_classification'],
             'sample': line['industrial_classification'],
             'sample': line['industrial_classification'],
            'price': line['value']
           
        })
    return RESULTS
