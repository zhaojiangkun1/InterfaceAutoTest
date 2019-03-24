from part_seven.field import Field,StringField,TextField
from part_seven.orm import Model

class Goods(Model):
    computer_part = Field("computer_part", "varchar(200)")
    computer_info = Field("computer_info", "text")

goods = Goods()
# goods.insert(["computer_part","computer_info"], ["组\"件", "组件信息"])
# result = goods.select(["computer_part","computer_info"],["computer_part='组件'"])
# print(result)
goods.update(["computer_part='组件1'"], ["computer_part='组件'"])


# class Goods():
#     computer_part = StringField("computer_part")
#     computer_info = TextField("computer_info")
#

