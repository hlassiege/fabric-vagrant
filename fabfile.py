from fabric.api import *
from fabric.contrib.files import exists
from fabric.contrib.files import sed


env.roledefs = {
    'db': ['127.0.0.1:2222']
}


@task
@roles('db')
def java():
    sudo('apt-get update')
    sudo('apt-get install openjdk-7-jdk --assume-yes')

@task
@roles('db')
def es_stop():
    sudo('service elasticsearch stop')

@task
@roles('db')
def es_start():
    sudo('service elasticsearch start')

@task
@roles('db')
def es_restart():
    sudo('service elasticsearch restart')

@task
@roles('db')
def es_install():
    if not exists('/vagrant/tmp/elasticsearch-0.90.2.deb'):
        sudo('wget -P /vagrant/tmp/ https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.90.2.deb')

    sudo('dpkg -i /vagrant/tmp/elasticsearch-0.90.2.deb')

    es_addplugins()
    es_restart()


@task
@roles('db')
def es_addplugins():
    sudo('/usr/share/elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic')
    sudo('/usr/share/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-transport-thrift/1.5.0')
    sudo('/usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head')


@task
@roles('db')
def uninstall():
    sudo('aptitude purge elasticsearch --assume-yes')
