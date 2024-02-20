#设定初始镜像mysql版本
FROM mysql:8.0.32
#设定工作目录，用于处理初始化mysql的sql文件
WORKDIR /docker-entrypoint-initdb.d
#默认mysql无法输入中文，修改编码使其支持中文
ENV LANG=C.UTF-8
#加入需要初始化的sql文件
ADD initdata.sql .
