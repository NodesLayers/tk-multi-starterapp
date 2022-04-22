#!/usr/bin/env python
#
# Copyright (c) 2022 Nodes&Layers Ltd.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.
#
#################################
# USAGE:                        #
#################################
# Python 3.7 - PySide2 required
# Install PySide2 to your Virtual Environment!
#

import os
import fileinput

# The path to output all built .py files to:
UI_PYTHON_PATH = "../python/app/ui"
current_dir = os.path.dirname(__file__)


# Helper functions to build UI files
def build_py(ui_name):
    print("Building {}...".format(ui_name))

    ui_path = os.path.join(current_dir, ui_name+".ui").replace("\\", "/")
    print(ui_path)
    python_path = os.path.join(os.path.dirname(current_dir), "python", "app", "ui", ui_name+".py").replace("\\", "/")
    print(python_path)

    # compile ui to python
    cmd = 'pyside-uic --from-imports "{}" -o "{}"'.format(ui_path, python_path)
    print(cmd)
    os.system(cmd)

    # replace PySide imports with tank.platform.qt and remove line containing Created by date
    # echo 'sed -i "" -e "s/from PySide import/from tank.platform.qt import/g" -e "/# Created:/d" '
    # echo $UI_PYTHON_PATH/$3.py
    replace_in_file(python_path, "from PySide import", "from tank.platform.qt import")
    replace_in_file(python_path, "Ui_Dialog(object)", "Ui_Dialog(QtGui.QWidget)")

def replace_in_file(file_path, search_text, new_text):
    for line in fileinput.input(file_path, inplace=True):
        if search_text in line:
            line = line.replace(search_text, new_text)
        print(line), # for Python 2

if __name__ == "__main__":
    build_py("dialog")