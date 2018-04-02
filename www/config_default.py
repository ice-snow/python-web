#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Default configuration
'''
__author__ = 'Leo'


configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'blog',
        'password': 'blog123',
        'db': 'webblog'
    },
    'session': {
        'secret': 'webblog'
    }
}


