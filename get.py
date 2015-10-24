from datetime import datetime, timedelta
import time
import requests

class FullContactAdaptiveClient(object):
    REQUEST_LATENCY=0.2

    def __init__(self):
        self.next_req_time = datetime.fromtimestamp(0)

    def call_fullcontact(self, email):
        self._wait_for_rate_limit()
        r = requests.get('https://api.fullcontact.com/v2/person.json',
                         params={'email': email, 'apiKey': 'YOUR API KEY'})
        self._update_rate_limit(r.headers)
        return r.json()

    def _wait_for_rate_limit(self):
        now = datetime.now()
        if self.next_req_time > now:
            t = self.next_req_time - now
            time.sleep(t.total_seconds())

    def _update_rate_limit(self, hdr):
        remaining = float(hdr['X-Rate-Limit-Remaining'])
        reset = float(hdr['X-Rate-Limit-Reset'])
        spacing = reset / (1.0 + remaining)
        delay = spacing - self.REQUEST_LATENCY
        self.next_req_time = datetime.now() + timedelta(seconds=delay)
