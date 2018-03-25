#!/usr/bin/env python
# -*- coding:utf-8 -*-


import xlrd
import datetime as dt
import os
import glob
import markdown

# def create_md():
#     DT = dt.date.today().strftime('%Y-%m-%d')
#     file_name = "/Users/admin/Documents/work/日报-周报/运维日报(" + DT + "-贾文龙).xlsx"
#     md_file = "/Users/admin/Documents/work/shells/rb.md"
#
#     rb = open(md_file, 'w')
#     book = xlrd.open_workbook(file_name)
#     sh = book.sheet_by_index(0)
#
#     for hang in range(0, sh.nrows):
#         if hang == 0 or hang == 1:
#             continue
#         for lie in range(0, sh.ncols):
#             if sh.cell_value(rowx=hang, colx=lie):
#                 value = sh.cell_value(hang, lie)
#             if lie == 5:
#                 rb.write("|" + '\n')
#                 if hang == 2 and lie == 5: rb.write("|--|--|--|--|--|" + '\n')
#             else:
#                 rb.write("|")
#                 rb.write(value.encode("utf-8"))
#
#
#
# def markdown2html():
#     SOURCE_FILES_PATH = os.path.join("/Users/admin/Documents/work/shells/", "rb.md")
#     SOURCE_FILES = glob.glob(SOURCE_FILES_PATH)
#
#     for pos in range(0, len(SOURCE_FILES)):
#         file_base_name = os.path.basename(SOURCE_FILES[pos])
#         file_name = file_base_name.replace(".md", "")
#         output_files_path = os.path.join("/Users/admin/Documents/work/shells/", file_name + ".html")
#
#         markdown.markdownFromFile(
#             input=SOURCE_FILES[pos],
#             output=output_files_path,
#             encoding="utf-8",
#             extensions=[
#                 'markdown.extensions.fenced_code',
#                 'markdown.extensions.tables'
#             ],
#             output_format="html5"
#         )


excel_path = "/Users/admin/Documents/work/日报-周报/"
MD_PATH="/Users/admin/Documents/work/shells/"
md_name = "rb.md"
css = """
<style type="text/css">
table,th,td { border:1px solid blue; }
th { background-color:#98bf21; color:white; }
#td { background-color:#98bf21; color:white; }
</style>"""

def create_md():
    DT = dt.date.today().strftime('%Y-%m-%d')
    file_name = excel_path + "运维日报(" + DT + "-贾文龙).xlsx"
    md_file = MD_PATH + md_name
    if not os.path.isfile(file_name):
        print "没有 " + file_name + " 这个文件！!\n请检查！！！"
        exit()
    rb = open(md_file, 'w')
    book = xlrd.open_workbook(file_name)
    sh = book.sheet_by_index(0)
    rb.write(css)
    for hang in range(0, sh.nrows):
        if hang == 0 or hang == 1:
            continue
        for lie in range(0, sh.ncols):
            if sh.cell_value(rowx=hang, colx=lie):
                value = sh.cell_value(hang, lie)
            else:
                value = "-"
            if lie == 5:
                rb.write("|" + '\n')
                if hang == 2 and lie == 5: rb.write("|--|--|--|--|--|" + '\n')
            else:
                rb.write("|")
                rb.write(value.encode("utf-8"))
    rb.closed


def markdown2html():
    SOURCE_FILES_PATH = os.path.join(MD_PATH, "*.md")
    SOURCE_FILES = glob.glob(SOURCE_FILES_PATH)
    for pos in range(0, len(SOURCE_FILES)):
        file_base_name = os.path.basename(SOURCE_FILES[pos])
        file_name = file_base_name.replace(".md", "")
        output_files_path = os.path.join(MD_PATH, file_name + ".html")
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

if __name__ == "__main__":
    create_md()
    markdown2html()
