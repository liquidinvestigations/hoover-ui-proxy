# Liquid proxy for Hoover UI development

A proxy that forwards [Hoover Search][] API requests to an upstream [Liquid
Investigations][] server. Useful when working on [Hoover UI][].

[Hoover Search]: https://github.com/hoover/search/
[Liquid Investigations]: https://github.com/liquidinvestigations/
[Hoover UI]: https://github.com/hoover/ui/


## HowTo

Clone the repo and install dependencies:

```shell
git clone https://github.com/liquidinvestigations/hoover-ui-proxy
cd hoover-ui-proxy
pipenv install
```

Open the hoover app of a Liquid Investigations bundle of your choice and, using
the web inspector, steal its `authproxy.session` cookie. It looks something
like this:

```
eyJhY2Nlc3NfdG9rZW4iOiJCS1h4MFZ1bEhiYmptWnBCaUphbHpib1NUaTZhcVEiLCJuZXh0IjoiaHR0cHM6Ly9ob292ZXIubGlxdWlkZGVtby5vcmcvIn0.XaIRiA.dvGeqEP5oLVDe9p-dcUC4vAcxaw
```

Configure environment variables by creating a `.env` file with content like so:

```shell
HOOVER_URL=https://hoover.liquiddemo.org
AUTHPROXY_SESSION=eyJhY2Nlc3NfdG9rZW4iOiJCS1h4MFZ1bEhiYmptWnBCaUphbHpib1NUaTZhcVEiLCJuZXh0IjoiaHR0cHM6Ly9ob292ZXIubGlxdWlkZGVtby5vcmcvIn0.XaIRiA.dvGeqEP5oLVDe9p-dcUC4vAcxaw
```

Run the server:

```shell
pipenv run env FLASK_APP=hoover_ui_proxy.py flask run
```

Then, when developing `hoover-ui`, run the dev server like so:

```shell
HOOVER_REMOTE_SEARCH_URL=http://localhost:5000 npm run dev
```
