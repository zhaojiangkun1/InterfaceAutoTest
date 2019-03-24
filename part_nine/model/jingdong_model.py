
from part_nine.orm.orm import Model
from part_nine.orm.field import Field

class Goods(Model):
    computer_part = Field("computer_part", "varchar(200)")
    computer_info = Field("computer_info", "text")

