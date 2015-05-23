Fource
======

It contains fource cli, shinken, thruk, graphite and Apache.

How to run:

    $ git clone https://github.com/fource/fource.git
    $ cd fource
    $ sudo docker run -i -t -v "$(pwd)/dockerize/custom_configs:/etc/shinken/custom_configs" -v "$(pwd)/config:/etc/fource/config" -p 80:80 rohit01/fource

Once done, visit these urls (Default credentials - admin/admin):

* Default WebUI: <http://localhost/>
* Thruk Web Interface: <http://localhost/thruk/>

Note:

* [dockerize/custom_configs/](dockerize/custom_configs/): It contains shinken configuration.
* [config/](config/): It contains all test cases configured.
* [dockerize/custom_configs/htpasswd.users](dockerize/custom_configs/htpasswd.users): Define user login credentials here. Documentation is written as comments in this file.

Docker registry link: <https://registry.hub.docker.com/u/rohit01/fource/>
