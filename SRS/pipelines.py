# -*- coding: utf-8 -*-

import pymysql


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SrsPipeline(object):
    def __init__(self):

        self.db_conn = pymysql.connect(host='localhost', port=3306, db='pycharm',
                                       user='root', passwd='123456', charset='utf8')
        self.db_cur = self.db_conn.cursor()

    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    def insert_db(self, item):
        values = (
            item['name'],
            item['confirmeder'],
            item['curer'],
            item['dier'],
        )

        sql = 'INSERT INTO SRS VALUES(%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)
