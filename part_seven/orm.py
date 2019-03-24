from part_seven.field import Field
from part_seven.my_database import create_pool

#  定义元类，控制model对象的创建

class ModelMetaClass(type):
    """
    关于参数
    table_name : 类名，那么也是对应的数据库中的表名
    bases: 父类的元组
    attrs : 类的属性方法和值组成的键值对
    """

    def __new__(cls, table_name, bases, attrs):
        if table_name == "Model":
            return super(ModelMetaClass, cls).__new__(cls, table_name, bases, attrs)

        mappings = dict()
        for k, v in attrs.items():
            # 保存类属性和列的映射关系到mappings字典中
            if isinstance(v, Field):
                mappings[k] = v # 这个mappings就存放了 属性名称：字段名，列名

        for k in mappings.keys():
            # 将类的属性移除。 使得定义的类字段不污染User的类属性
            # 也就是说只有在实例中才可以访问这些key。 就是类名.属性名称不可以调用
            attrs.pop(k)

        # 把表名转换为小写，也就是那个类名要变成小写
        # 并且要添加一个__table__属性，来表示属性中存储的表名
        attrs['__table__'] = table_name.lower()

        # 保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        return super(ModelMetaClass, cls).__new__(cls, table_name, bases, attrs)

# 编写一个model子类（基类），这个类用于被具体的model对象继承
# 来实现具体的增删改查方法
# 基于面向对象中三大特性的继承规则，那么以后每一个model类的实现都有了这些方法


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)
# insert into table_name (字段名称) values (值)
    def insert(self, column_list, param_list):
        print("执行了insert方法")
        fields = []
        for k, v in self.__mappings__.items():
            fields.append(k)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("这个字段没有发现 field not found")

        # 检查参数的合法性   "val"ue"
        args = self.__check_params(param_list)

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(column_list), ','.join(args))
        res = self.__do_execute(sql)
        print(res)

    def __check_params(self,param_list):
        args = []
        for param in param_list:
            # 如果参数中包含双引号，全部换成字符串双引号，防止sql注入
            if "\"" in param:
                param = param.replace("\"", "\\\"")

            # 自己在参数的两边加上双引号
            param = "\"" + param + "\""
            args.append(param)

        return args

    def __do_execute(self, sql):
        conn = create_pool()
        cur = conn.cursor()
        print(sql)
        if "select" in sql:
            cur.execute(sql)
            rs = cur.fetchall()
        else:
            rs = cur.execute(sql)

        conn.commit()
        cur.close()
        return rs

    def select(self, column_list, where_list):
        print("调用select方法")
        args = []
        fields = []
        for k, v in self.__mappings__.items():
            fields.append(k)
        for key in where_list:
            args.append(key)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("field not found")
        sql = 'select %s from %s where %s' % (','.join(column_list), self.__table__, ' and '.join(args))

        res = self.__do_execute(sql)
        return res

    def update(self, set_column_list, where_list):
        print("调用update方法")
        args=[]
        fields = []

        for key in set_column_list:
            fields.append(key)

        for key in where_list:
            args.append(key)

        for key in set_column_list:
            if key not in fields:
                raise RuntimeError("field not found")
        sql = 'update %s set %s where %s' % (self.__table__, ','.join(set_column_list), ' and '.join(args))
        res = self.__do_execute(sql)
        return res

    def delete(self, where_list):
        print("调用删除方法")
        args = []
        for key in where_list:
            args.append(key)

        sql = 'delete from %s where %s' % (self.__table__, ' and '.join(args))

        res = self.__do_execute(sql)
        return res
