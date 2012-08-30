#!/usr/bin/python
#encoding: utf8
# +-----------------------------------------------------------------------------
# | File: setup.py
# | Author: huxuan
# | E-mail: i(at)huxuan.org
# | Created: 2012-08-30
# | Last modified: 2012-08-30
# | Description:
# |     setup.py file of py2exe which will create exe file for win
# |
# | Copyrgiht (c) 2012 by huxuan. All rights reserved.
# | License GPLv3
# +-----------------------------------------------------------------------------
from distutils.core import setup
import py2exe

setup(
        name = "Lucky You",
        version = "1.0",
        options = {
            "py2exe" : {
                "compressed" : 1,
                "optimize" : 2,
                "bundle_files" : 2,
                "dll_excludes" : [ "MSVCP90.dll" ] }},
        windows = ["lucky_you.py"],
        zipfile = None,
        author = "Hu Xuan",
        author_email ="i@huxuan.org",
        url = "http://github.com/huxuan/luck_you/",
      )
