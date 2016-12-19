#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'apple'
__mtime__ = '2016/12/8'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

# the fastest way to set up the inventory

# hosts list
import json

import ansible
from ansible import inventory
from ansible import runner

hosts = ["192.168.0.132"]
# set up the inventory, if no group is defined then 'all' group is used by default

example_inventory = ansible.inventory.Inventory(host_list=hosts)

try:

	pm = ansible.runner.Runner(
		module_name='setup',
		module_args='',
		timeout=5,
		inventory=example_inventory,
		remote_user='liukai423',
		remote_pass='Roomy@2016',
		remote_port=22,
		#subset='all'  # name of the hosts group
	)


	out = pm.run()

	data = json.dumps(out,indent=4)
	print data
except Exception,e:
	print e

# print json.dumps(out, sort_keys=True, indent=4, separators=(',', ': '))