from setuptools import find_packages
from setuptools import setup
import os

# 打印当前工作目录
print(f"Current working directory: {os.getcwd()}")
# 检查文件是否存在
# file_path = '/home/wzq/GIDS/gids_module/build/BAM_Feature_Store/BAM_Feature_Store.so'
# if not os.path.exists(file_path):
#     raise FileNotFoundError(f"File not found: {file_path}")
# else :
#     print(f"File found: {file_path}")
setup(
        name = "GIDS",
        version     = '0.1.2',
        packages=find_packages(),
        package_data={
            '':['/root/BAM_Tensor/BAM_DataLoader/module/build/BAM_Feature_Store/BAM_Feature_Store.so'] }
)

