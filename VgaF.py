#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess

proc = subprocess.Popen(['lspci', '-k', '|', 'grep', '-EA3',  'VGA|3D|Display'],stdout=subprocess.PIPE)

line = proc.stdout.readline()

print line
