#!/usr/bin/python
##===============================================================================
# CERN (BE-CO-HT)
# Script to get started on documentation
#===============================================================================
# author: Theodor Stana (t.stana@cern.ch)
#
# date of creation: 2014-08-05
#
# version: 1.0
#
# description:
#       Asks user for name of document and title and performs necessary changes
#       across the files
#
#===============================================================================
# GNU LESSER GENERAL PUBLIC LICENSE
#===============================================================================
# This source file is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation; either version 2.1 of the License, or (at your
# option) any later version. This source is distributed in the hope that it
# will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details. You should have
# received a copy of the GNU Lesser General Public License along with this
# source; if not, download it from http://www.gnu.org/licenses/lgpl-2.1.html
#===============================================================================
# last changes:
#    2014-08-05    Theodor Stana     File created
#===============================================================================
#  TODO: -
#===============================================================================

import glob
import os
import os.path

fname = raw_input("Document file names : ")
title = raw_input("Document title      : ");

# Add name in Makefile
with open("Makefile", 'r+') as f:
    buf = f.read()
    buf = buf.replace("FILE=doc", "FILE=" + fname)
    f.seek(0)
    f.write(buf)

# Change file names
for f in glob.glob("doc.*"):
    if (os.path.basename(f)[-1] == '~'):
        continue
    new = fname + os.path.basename(f)[-4:]
    os.rename(f, new)

# Change "\bibliography{doc}" to "\bibliography{<fname>}"
with open(fname + ".tex", "r+") as f:
    buf = f.read()
    buf = buf.replace("\\bibliography{doc}", "\\bibliography{" + fname + "}")
    f.seek(0)
    f.write(buf)

# Change the title in title.tex
with open("title.tex", "r+") as f:
    buf = f.read()
    buf = buf.replace("Title", title)
    f.seek(0)
    f.write(buf)

