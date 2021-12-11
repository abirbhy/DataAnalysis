
import requests
import time
from pprint import pprint

redash_url = 'http://51.178.128.212:8080'

class Redash(object):
    def __init__(self, redash_url, api_key):
        self.redash_url = redash_url
        self.api_key = api_key

    def poll_job(self, s, job):
        while job['status'] not in (3,4):
            response = s.get('{}/api/jobs/{}'.format(redash_url, job['id']))
            job = response.json()['job']
            time.sleep(1)
        return job['status'] == 3

    def get_fresh_query_result(self, query_id, api_key):

        s = requests.Session()
        s.headers.update({'Authorization': 'Key {}'.format(api_key)})
        response = s.post('{}/api/queries/{}/refresh'.format(redash_url, query_id))
        if response.status_code != 200:
            raise Exception('Refresh failed.')
        self.poll_job(s, response.json()['job'])
        response = s.get('{}/api/queries/{}/results.json'.format(redash_url, query_id))
        if response.status_code != 200:
            raise Exception('Failed getting results.')
        return response.json()['query_result']['data']['rows']


if __name__ == '__main__':
    redash_url = 'http://51.178.128.212:8080'
    api_key = 'DLO2Fz3i8ETRpvrG4GnTx6t6Z5RrsXEhY9PD7Pl2'
    redash = Redash(redash_url, api_key)

    # Need to use a *user API key* here (and not a query API key).
    for i in range(303, 309):
        pprint(redash.get_fresh_query_result(i, api_key))
