import os
import flask
import requests

app = flask.Flask(__name__)

hoover_url = os.environ['HOOVER_URL']
authproxy_session = os.environ['AUTHPROXY_SESSION']


@app.before_request
def dispatch():
    url = f"{hoover_url}{flask.request.full_path}"
    headers = {'Cookie': f'authproxy.session={authproxy_session}'}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if 200 <= resp.status_code < 300:
        rv = flask.Response(
            status=resp.status_code,
            headers=resp.headers.items(),
        )
        rv.data = resp.content
        return rv

    else:
        return "Received redirect from upstream. Auth probably failed.", 500
