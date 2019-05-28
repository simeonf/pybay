"""
Autogenerated a Swagger Client and saw 50K LOC!

Let's try something minimal supporting only the methods I need...
"""

import functools
import logging
import requests
import sys


def endpoint(path):
  def decorator(f):
    @functools.wraps(f)
    def wrapper(self, **kwargs):
      url = self._server + path.format(**kwargs)
      logging.debug(url)
      headers = self._headers()
      logging.debug(headers)
      r = requests.get(url, headers=headers)
      if r.status_code == 200:
        return f(self, r, **kwargs)
      else:
        msg = "Error accessing {}. Status code {}. {}".format(url, r.status_code, r.text)
        raise self.ApiException(msg)
    return wrapper
  return decorator

class HubbClient:

  class ApiException(Exception): pass

  def __init__(self, client_id, client_secret, scope):
    self._client_id = client_id
    self._client_secret = client_secret
    self._scope = scope
    self._server = "https://ngapi.hubb.me"
    self._access_token = None
    self._authorize()

  def _authorization_params(self):
    return dict(client_id=self._client_id, client_secret=self._client_secret, scope=self._scope)

  def _authorize(self):
    endpoint = "/auth/token"
    headers = {'Content-Type': 'application/x-www-form-urlencode'}
    body = ("client_id={client_id}&client_secret={client_secret}"
            "&scope={scope}&grant_type=client_credentials")
    body = body.format(**self._authorization_params())
    r = requests.post(self._server + endpoint, headers=headers, data=body)
    json = r.json()
    self._access_token = json['access_token']

  def _headers(self):
    return {'Authorization': "bearer {}".format(self._access_token),
            'Content-Type': 'application/json'}

  @endpoint('/api/v1/{event_id}/Sessions')
  def sessions(self, r, event_id=None):
    return r.json()

  @endpoint('/api/v1/{event_id}/SessionTypes')
  def sessiontypes(self, r, event_id=None):
    return r.json()


  @endpoint('/api/v1/{event_id}/Users')
  def users(self, r, event_id=None):
    return r.json()



  @endpoint('/api/v1/Events')
  def events(self, r):
    return r.json()




hc = HubbClient(client_id="secret",
                client_secret="secret",
                scope="secret"
                )

root = logging.getLogger()
root.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)

#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#handler.setFormatter(formatter)
root.addHandler(handler)


print(hc.sessions(event_id=2717))

#print(hc.users(event_id=2717))