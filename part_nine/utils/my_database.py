"""
pip install DBUtils

"""

import pymysql
from DBUtils.PooledDB import PooledDB
from part_nine.config.mysql_config import set_mysql_config


def create_pool():
    db_config = set_mysql_config("dev")
    return PooledDB(pymysql,
                    5,
                    host=db_config["host"],
                    user=db_config["user"],
                    passwd=db_config["passwd"],
                    db=db_config["db"],
                    port=db_config["port"],
                    charset=db_config["charset"]).connection()



