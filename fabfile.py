#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
fabric deploy file
fab build
fab deploy -H 172.16.211.129 -u wangwa
"""

from fabric.api import *

# env.user = 'wangwa'
# env.hosts = ['172.16.211.129']
env.use_ssh_config = True

_NAME = 'flower_ex'
_TAR_FILE = local('python setup.py --fullname', capture=True).strip() + '.tar.gz'
_REMOTE_TMP = '/srv/flower_ex.tar.gz'


def build():
    """
    本地打包
    """
    local('python3 setup.py sdist --formats=gztar', capture=False)


def deploy():
    """
    发布到远端
    """
    # 将代码归档上传到服务器当中的临时文件夹内
    put('dist/%s' % _TAR_FILE, _REMOTE_TMP, use_sudo=True)
