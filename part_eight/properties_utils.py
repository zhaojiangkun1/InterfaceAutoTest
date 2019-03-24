


class Properties():

    def __init__(self, file_name):
        self.properties_file_name = file_name
        self.properties = {}

    def get_properties(self) -> dict:
        with open(self.properties_file_name, 'r', encoding='UTF-8') as pro_file:
            for line in pro_file.readlines():
                # 去掉两端的空格和\n
                line = line.strip().replace("\n", "")
                # 如果发现# ，就代表着这一行或者是他的后边是注释内容
                if line.find("#") != -1:
                    line = line[0:line.find("#")]

                # 如果包含等号，我们就要进行字典类型的转换处理
                if line.find("=") > 0:
                    # 我们就用等号进行切分，形成了新的字典类型的list
                    strs = line.split("=")
                    # 获取字典
                    self.__get_dict(strs[0].strip(), self.properties, strs[1].strip())

        return self.properties

    def __get_dict(self, key_name, result_dict, value):
        # 检查key中是否包含. 包含的话我们就切分，不包含就直接设置值
        if key_name.find(".") > 0:
            k = key_name.split(".")[0]  #用.切分，我拿第一个www作为一个key
            result_dict.setdefault(k,{})  # 把结果字典设置成{www.{imooc: {com:value}}}
            return self.__get_dict(key_name[len(k) + 1:], result_dict[k], value)

        else:
            result_dict[key_name] = value