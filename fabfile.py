from fabric.api import *
from fabric.contrib.files import exists


@task
def java():
    sudo('apt-get update')
    sudo('apt-get install openjdk-7-jdk --assume-yes')

@task
def es_install():
    if not exists('/vagrant/tmp/elasticsearch-0.90.2.deb'):
        sudo('wget -P /vagrant/tmp/ https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.2.deb')

    sudo('dpkg -i /vagrant/tmp/elasticsearch-0.90.2.deb')

    es_addplugins()
    sudo('service elasticsearch restart')

@task
def es_addplugins():
    sudo('/usr/share/elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic')
    sudo('/usr/share/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-transport-thrift/1.5.0')
    sudo('/usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head')

