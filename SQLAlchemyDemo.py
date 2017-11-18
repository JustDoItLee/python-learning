#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


class City(Base):
    # 表的名字:
    __tablename__ = 'city'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    province_id = Column(Integer)
    city_name = Column(String(25))
    description = Column(String(25))

    def __str__(self):
        return ("%d,cityName:%s,description:%s" % (self.id, self.city_name, self.description))


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:lizhi@localhost:3306/springbootdb')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# # 创建session对象:
# session = DBSession()
# # 创建新User对象:
# new_city = City(province_id=4, city_name='北京', description='帝都')
# # 添加到session:
# session.add(new_city)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()




try:
    # 创建Session:
    session = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    city = session.query(City).filter(City.city_name == "北京" and City.id == 5).all()
    # 打印类型和对象的name属性:
    print('type:', type(city))
    print('name:', city)
    for c in city:
        print(c)
except Exception as e:
    print(e)
finally:
    # 关闭Session:
    session.close()
