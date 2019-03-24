from part_eight.properties_utils import Properties

#
# pro = Properties('log.properties').get_properties()
#
# print(pro)
# print(pro["filename"])
# print(pro["www"])
# print(pro["www"]["imooc"])
# print(pro["www"]["imooc"]["com"])
import logging

def set_log_config():
    pro = Properties('log.properties').get_properties()
    log_config = {
        "filename": pro["filename"],
        "level": pro["level"]
    }
    logging.basicConfig(**log_config)

from part_eight.use_log2 import use_log2_file

if __name__=="__main__":
    set_log_config()
    logging.info("info log")
    use_log2_file()
