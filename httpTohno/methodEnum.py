#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'apple'
__mtime__ = '2016/11/19'
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

class methodEnum(object):
	# 文件创建
	file_create = '/file?action=create'
	# 文件更新
	file_update = '/file?action=update'
	# 文件删除
	file_delete = '/file?action=delete'
	# 文件获取
	file_get = '/file?action=get'
	# 文件重命名
	file_rename = '/file?action=rename'
	# 备份文件内容获取
	file_backupget = '/file?action=backupget'
	# 目录创建
	dir_create = '/dir?action=create'
	# 目录删除
	dir_delete = '/dir?action=delete'
	# 目录重命名
	dir_rename = '/dir?action=rename'
	# 目录浏览
	dir_scan = '/dir?action=scan'
	# serverInfoList
	server_infos = '/syncinfo?action=get'
	# server_url_infos  - shiva
	server_url_infos = '/getServerUrlInfos'
	# server_uru_info - shiva
	server_url_info_get = '/getServerUrlInfo'

	# templateFile - shiva
	templateFile = '/templateFile'
	#templateFileList - shiva
	templateFileList = '/templateFileList'
	#hostlist - shiva
	hostlist = '/hostlist'
	#host
	host = '/host'