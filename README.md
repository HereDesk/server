# 关于Here Desk Server

> Here Desk 接口是基于python3、Django开发而成

#### 

#### 安装

环境检查，如检查版本非`python3`以上，请安装`python3`，不支持`python2`

```shell
$ python --version
```

所需的库在`requirements.txt文`件中

```shell
$ pip install -r requirements.txt
```

#### 配置文件

系统的配置文件为：`settings.py`

开发环境配置文件为：`settings_dev.py`

#### 数据库

```shell
$ python manage.py makemigrations 
$ python manage.py migrate
```

or 开发环境

```shell
$ python manage_dev.py makemigrations 
$ python manage_dev.py migrate
```

#### 导入数据

Sql文件：`full_database.sql`

将此sql文件导入已创建的数据库中即可。

#### 创建用户

Script脚本：`initialize_user.py`

```

```

