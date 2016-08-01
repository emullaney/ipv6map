ipv6map
==============

Below you will find basic setup and deployment instructions for the rapidpro_community_portal
project. To begin you should have the following applications installed on your
local development system::

- Python >= 3.5
- `pip <http://www.pip-installer.org/>`_ >= 1.5
- `virtualenv <http://www.virtualenv.org/>`_ >= 1.10
- `virtualenvwrapper <http://pypi.python.org/pypi/virtualenvwrapper>`_ >= 3.0
- Postgres >= 9.1
- git >= 1.7

Getting Started
------------------------

First clone the repository from Github and switch to the new directory::

    git clone git@github.com:emullaney/ipv6map.git
    cd ipv6map
    
To setup your local environment you should create a virtualenv running Python 3.5 and install the
necessary requirements. You probably don't need to run the `workon` command, but this is just to ensure that you are connected to your new virtual environment.::

    mkvirtualenv heatmap -p /usr/bin/python3.5
    workon heatmap
    $VIRTUAL_ENV/bin/pip install requirements.txt
    
Create the database and run the initial syncdb, which will also execute any required migrations. This step may take a while because it will read in all 355,000+ rows of data from the IPv6 CSV file.::

    createdb -E UTF-8 heatmap
    python manage.py syncdb
    
Run the small suite of tests with::

    python manage.py test

You should now be able to run the development server::

    python manage.py runserver
