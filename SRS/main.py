from scrapy import cmdline
from scrapy import cmdline
from pyecharts.charts import Map
# cmdline.execute('scrapy crawl SRS_spider'.split())
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
from scrapy import cmdline
import pymysql
from scrapy import cmdline

# 执行scrapy爬虫
cmdline.execute('scrapy crawl SRS_spider'.split())
# 从mysql中获取数据库
conn=pymysql.connect("localhost", "mpp", "123456", "pycharm", charset='utf8')
# 使用cursor()方法获取操作游标
cursor = conn.cursor()

# 使用execute方法执行SQL语句
cursor.execute("select site,confirmeder from srs")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchall()
# 关闭数据库连接
cursor.execute("select max(confirmeder) from srs")
maxvalue=cursor.fetchall()
conn.close()

# 用于测试的例子，部分取自 Faker ，也就是 from pyecharts.faker import Faker


# 生成数据可视化的html地图
# 连续性数据显示，不同颜色不同省份
def map_visualmap() -> Map:
    c = (
        Map()
        .add("总计确认人数", [list(z) for z in data], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全国疫情情况"),
            visualmap_opts=opts.VisualMapOpts(max_= maxvalue[0][0]),
        )
    )
    return c
if __name__ == '__main__':
    city_ = map_visualmap()
    city_.render(path="test_map_1.html")



# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get("https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1")
# print(driver.page_source)
# from selenium import webdriver

