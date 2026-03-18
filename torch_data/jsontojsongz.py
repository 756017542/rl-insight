import os
import json
import gzip
from pathlib import Path

def convert_json_to_gz(directory_path):
    """
    将指定目录下所有 .json 文件转换为 .json.gz 格式。
    
    参数:
        directory_path (str or Path): 目录路径
    """
    dir_path = Path(directory_path)
    
    if not dir_path.exists():
        print(f"目录不存在: {directory_path}")
        return
    
    if not dir_path.is_dir():
        print(f"路径不是目录: {directory_path}")
        return

    # 遍历目录中所有 .json 文件
    json_files = dir_path.glob("*/*.json")
    
    for json_file in json_files:
        gz_file = json_file.with_suffix(".json.gz")
        
        try:
            # 读取原始 JSON 文件
            with open(json_file, 'r', encoding='utf-8') as f_in:
                data = json.load(f_in)
            
            # 写入压缩的 .json.gz 文件
            with gzip.open(gz_file, 'wt', encoding='utf-8') as f_out:
                json.dump(data, f_out, ensure_ascii=False, indent=2)
            
            print(f"coverting: {json_file.name} -> {gz_file.name}")
            
        except Exception as e:
            print(f"fail: {json_file.name} | 错误: {e}")

# 使用示例
if __name__ == "__main__":
    target_directory = "./profile_meta"  # 修改为你的目标目录
    convert_json_to_gz(target_directory)
