#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author ： @jiawenlong
# Date ：2018-07-05

__author__ = '@jiawenlong'

import pymysql, xlwt
from datetime import datetime
from datetime import timedelta


def export_excel(table_name, sql):
    conn = pymysql.connect(user=user, host=host, port=port, passwd=passwd, db=db, charset='utf8')
    cur = conn.cursor()
    cur.execute(sql)
    fileds = [filed[0] for filed in cur.description]
    all_data = cur.fetchall()
    # 写excel
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')
    for col, field in enumerate(fileds):
        sheet.write(0, col, field)

    # 从第一行开始写
    row = 1
    for data in all_data:
        for col, field in enumerate(data):
            sheet.write(row, col, field)
        row += 1
    book.save('%s.xls' % table_name)


def give_time():
    today = datetime.today()
    today_date = datetime.date(today) - timedelta(days=1)
    return str(today_date)


if __name__ == "__main__":
    host = 'rm-bp1l97d3ioa1b9058.mysql.rds.aliyuncs.com'
    user = 'tom_read'
    passwd = 'System123456'
    db = 'tom_system'
    port = 3306
    sql = "select case channel when 0 then '好升益' when 1 then '母婴' when 2 then '倍全' when 3 then '阳光物业' when 4 then '酒知己' end 租户,id 店铺id,name 店铺名称,FROM_UNIXTIME(creation_time/1000, '%Y-%m-%d %H:%i:%s') 店铺创建时间 from t_store where creation_time>=(UNIX_TIMESTAMP(DATE_FORMAT(now(), '%y%m%d'))-24*60*60)*1000 and creation_time<(UNIX_TIMESTAMP(DATE_FORMAT(now(), '%y%m%d')))*1000 order by channel,creation_time;"
    Yesterday = give_time()
    execl_file = '/tmp/新开店铺信息_' + Yesterday
    export_excel(execl_file, sql)






    # # __Desc__ = 从数据库中导出数据到excel数据表中
    # import xlwt
    # import pymysql
    # from datetime import datetime
    # from datetime import timedelta
    #
    #
    # class MYSQL:
    #     def __init__(self):
    #         pass
    #
    #     def __del__(self):
    #         self._cursor.close()
    #         self._connect.close()
    #
    #     def connectDB(self):
    #         """
    #         连接数据库
    #         :return:
    #         """
    #         try:
    #             self._connect = pymysql.Connect(
    #                 host='127.0.0.1',
    #                 port=3306,
    #                 user='tom_read',
    #                 passwd='System123456',
    #                 db='tom_system',
    #                 charset='utf8'
    #             )
    #
    #             return 0
    #         except:
    #             return -1
    #
    #     def export(self, sqll, output_path):
    #         self._cursor = self._connect.cursor()
    #         count = self._cursor.execute(sqll)
    #         # print(self._cursor.lastrowid)
    #         print(count)
    #         # 重置游标的位置
    #         self._cursor.scroll(0, mode='absolute')
    #         # 搜取所有结果
    #         results = self._cursor.fetchall()
    #
    #         # 获取MYSQL里面的数据字段名称
    #         fields = self._cursor.description
    #         workbook = xlwt.Workbook()
    #
    #         # 注意: 在add_sheet时, 置参数cell_overwrite_ok=True, 可以覆盖原单元格中数据。
    #         # cell_overwrite_ok默认为False, 覆盖的话, 会抛出异常.
    #         sheet = workbook.add_sheet('tablename', cell_overwrite_ok=True)
    #
    #         # 写上字段信息
    #         for field in range(0, len(fields)):
    #             sheet.write(0, field, fields[field][0])
    #
    #         # 获取并写入数据段信息
    #         row = 1
    #         col = 0
    #         for row in range(1,len(results)+1):
    #             for col in range(0, len(fields)):
    #                 sheet.write(row, col, u'%s' % results[row-1][col])
    #
    #         # 获取当前日期，得到一个datetime对象如：(2016, 8, 9, 23, 12, 23, 424000)
    #         today = datetime.today()
    #         # 将获取到的datetime对象仅取日期如：2016-8-9 Yesteday
    #         today_date = datetime.date(today) - timedelta(days=1)
    #
    #         workbook.save(output_path + str(today_date) + '.xls')
    #
    #
    # if __name__ == '__main__':
    #     excel_path = '/Users/admin/Downloads/'
    #     sql = "select case channel when 0 then '好升益' when 1 then '母婴' when 2 then '倍全' when 3 then '阳光物业' when 4 then '酒知己' end 租户,id 店铺id,name 店铺名称,FROM_UNIXTIME(creation_time/1000, '%Y-%m-%d %H:%i:%s') 店铺创建时间 from t_store where creation_time>=(UNIX_TIMESTAMP(DATE_FORMAT(now(), '%y%m%d'))-24*60*60)*1000 and creation_time<(UNIX_TIMESTAMP(DATE_FORMAT(now(), '%y%m%d')))*1000 order by channel,creation_time;"
    #     mysql = MYSQL()
    #     flag = mysql.connectDB()
    #     if flag == -1:
    #         print('数据库连接失败')
    #     else:
    #         print('数据库连接成功')
    #         mysql.export(sql, excel_path)




    # ==================== 不同的方法


    # 以下是python2执行
    # import sys
    # import time
    # import xlwt
    # import MySQLdb
    # from datetime import datetime
    # from datetime import timedelta
    # import json
    #
    # # host = 'rm-bp1l97d3ioa1b9058.mysql.rds.aliyuncs.com'
    # host = '127.0.0.1'
    # user = 'tom_read'
    # passwd = 'System123456'
    # db = 'tom_system'
    # port = 3306
    # sql = "select case channel when 0 then '好升益' when 1 then '母婴' when 2 then '倍全' when 3 then '阳光物业' when 4 then '酒知己' end 租户,id 店铺id,name 店铺名称,FROM_UNIXTIME(creation_time/1000, '%Y-%m-%d %H:%i:%s') 店铺创建时间 from t_store where creation_time>=(UNIX_TIMESTAMP(DATE_FORMAT(now(), '%y%m%d'))-24*60*60)*1000 and creation_time<(UNIX_TIMESTAMP(DATE_FORMAT(now(), '%y%m%d')))*1000 order by channel,creation_time;"
    # # sql="select * from t_store limit 10;"
    # table_head = ['租户', '店铺id', '店铺名称', '店铺创建时间']
    # excel_path = '/Users/admin/Downloads'
    #
    # def get_data(sql):
    #     # 创建数据库连接.
    #     conn = MySQLdb.connect(host, user, passwd, db, port, charset='utf8')
    #     # 创建游标
    #     cur = conn.cursor()
    #     # 执行查询，
    #     cur.execute(sql)
    #     # 由于查询语句仅会返回受影响的记录条数并不会返回数据库中实际的值，所以此处需要fetchall()来获取所有内容。
    #     result = cur.fetchall()
    #     # 关闭游标
    #     cur.close()
    #     # 关闭数据库连接
    #     conn.close
    #     # 返给结果给函数调用者。
    #     return result
    #
    #
    # def write_data_to_excel(name, sql):
    #     # 将sql作为参数传递调用get_data并将结果赋值给result,(result为一个嵌套元组)
    #     result = get_data(sql)
    #     #    print result
    #     # 实例化一个Workbook()对象(即excel文件)
    #     wbk = xlwt.Workbook()
    #     # 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
    #     sheet = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)
    #     # 获取当前日期，得到一个datetime对象如：(2016, 8, 9, 23, 12, 23, 424000)
    #     today = datetime.today()
    #     #    print today
    #     # 将获取到的datetime对象仅取日期如：2016-8-9 Yesteday
    #     today_date = datetime.date(today) - timedelta(days=1)
    #     #    print today_date
    #     # 遍历result中的没个元素。
    #     for i in xrange(len(result)):
    #         # 对result的每个子元素作遍历，
    #         #       print i,result[i]
    #         for j in xrange(len(result[i])):
    #             # 将每一行的每个元素按行号i,列号j,写入到excel中。
    #             #           print j,result[i][j]
    #             # for i in xrange(len(['租户','店铺id','店铺名称','店铺创建时间'])):
    #             #    sheet.write(0,i,table_head[0][i])
    #             # i+=1
    #             sheet.write(i, j, result[i][j])
    #     # 以传递的name+当前日期作为excel名称保存。
    #     wbk.save(excel_path + name + str(today_date) + '.xls')
    #
    #
    # # 如果该文件不是被import,则执行下面代码。
    # if __name__ == '__main__':
    #     # 定义一个字典，key为对应的数据类型也用作excel命名，value为查询语句
    #     db_dict = {'新开店铺信息-': sql}
    #     # 遍历字典每个元素的key和value。
    #     for k, v in db_dict.items():
    #         # 用字典的每个key和value调用write_data_to_excel函数。
    #         write_data_to_excel(k, v)
