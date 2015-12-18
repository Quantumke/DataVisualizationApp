import csv
import requests


URL = "https://www.opendata.go.ke/api/views/kwqv-7djf/rows.csv?accessType=DOWNLOAD"


def get_data():
    r = requests.get(URL)
    data = r.text
    RESULTS = {'children': []}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        RESULTS['children'].append({
            'timeperiod': line['Year'],
            'class': line['Classification of accident victim'],
            'stats': line['Numbers']
        })
    return RESULTS