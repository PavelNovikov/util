#!/usr/bin/env python

import pandas as pd
import json
from google.oauth2 import service_account

def main():
    credentials = service_account.Credentials.from_service_account_file(
        './files/apikey.json')
    task = json.load(open('./files/task.json','r'))
    project_id = task['project_id']
    query = task['query']
    df = pd.read_gbq(query, project_id=project_id, credentials=credentials,dialect='legacy')
    df.to_csv('./files/result.csv')

if __name__ == '__main__':
    main()
