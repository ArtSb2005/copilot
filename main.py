import time
import requests
from s import main

r1 = requests.get('http://127.0.0.1:8000/api/v1/docs/copilot').json()
check_id = r1[-1]['id']

while True:
    try:
        r1 = requests.get(f'http://127.0.0.1:8000/api/v1/docs/copilot/{check_id}/').json()

        id = r1['id']
        textarea_old = r1['textarea_old']
        if check_id == int(id):
            main(textarea_old, id)
            check_id += 1
    except:
        pass

    time.sleep(3)
