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
import json
import unittest
import ansible.inventory


class MyTestCase(unittest.TestCase):
	def test_something(self):
		self.assertEqual(True, False)

	def test_setup(self):
		# the fastest way to set up the inventory

		# hosts list
		hosts = ["192.168.0.132"]
		# set up the inventory, if no group is defined then 'all' group is used by default
		example_inventory = ansible.inventory.Inventory(hosts)

		pm = ansible.runner.Runner(
			module_name='command',
			module_args='uname -a',
			timeout=5,
			inventory=example_inventory,
			subset='all'  # name of the hosts group
		)

		out = pm.run()

		print json.dumps(out, sort_keys=True, indent=4, separators=(',', ': '))


if __name__ == '__main__':
	unittest.main()
