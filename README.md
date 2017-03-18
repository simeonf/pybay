# pybay

The website for PyBay - the Bay Area Python Conference.

To work on this you'll need Python 3. Then:

1. Fork the repo to your own personal github.
2. Clone the repo to your local environment.
3. Create a virtualenv and activate it
4. `pip install` the requirements
5. start the management server

Try:

    $ git clone git@github.com:YOURUSERNAME/pybay
    $ cd pybay
    $ python3 -m venv ENV
    $ source ENV/bin/activate
    (ENV)$ pip install -r requirements.txt
    (ENV)$ python manage.py runserver

If you also will be adding fixes to symposion we forked you can delete
the version in your site-packages and symlink in the directory on your
disk. Eg:

    $ cd ~/workspace/pybay/ENV/lib/python3.6/site-packages/
    $ rm -rf symposion
    $ ln -s /Users/sfranklin/workspace/symposion/symposion .