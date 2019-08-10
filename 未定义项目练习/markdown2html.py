#!/usr/bin/env python
#-*- coding:utf-8 -*-

import glob
import os
import markdown


SOURCE_FILES_PATH = os.path.join("/Users/admin/Documents/work/shells/", "test.md")
SOURCE_FILES = glob.glob(SOURCE_FILES_PATH)

for pos in range(0, len(SOURCE_FILES)):
    file_base_name = os.path.basename(SOURCE_FILES[pos])
    file_name = file_base_name.replace(".md", "")
    output_files_path = os.path.join("/Users/admin/Documents/work/shells/", file_name + ".html")

    markdown.markdownFromFile(
        input=SOURCE_FILES[pos],
        output=output_files_path,
        encoding="utf-8",
        extensions=[
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables'
        ],
        output_format="html5"
    )


