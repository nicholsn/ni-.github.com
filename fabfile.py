import os

from fabric.api import local

def clean():
    if os.path.isdir('output'):
        local('rm -rf output')
        local('mkdir output')

def build():
    local('pelican content -o output -s pelicanconf.py')

def rebuild():
    clean()
    build()

def regenerate():
    local('pelican -r -s pelicanconf.py')

def serve():
    local('cd output && python -m SimpleHTTPServer')

def reserve():
    build()
    serve()

def publish():
    local('pelican content -o output -s publishconf.py')
    local('ghp-import output')
    local('git push origin gh-pages:master')

