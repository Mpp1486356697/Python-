# python-scrapy爬虫-
放假期间无聊写了简单爬虫，现在整理出来
开源python提供的scrapy异步爬虫框架来搭建的
https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_1 爬取的网站 
由于是动态网页上有使用了splash来进行转换为静态网在通过XPath路径来获得数据，最后把数据保存在mysql数据库里面，最后使用python的pyecharts库来将数据可视化
scrapy-splash使用的是Splash HTTP API， 所以需要一个splash instance，一般采用docker运行splash，所以需要安装docke
SRS文件夹就是scrapy项目结构， 其中test_map.html是最后的html
