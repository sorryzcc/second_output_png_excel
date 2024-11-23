import os
import shutil
import pandas as pd

def copy_png_files(input_file, target_dir):
    # 读取Excel文件
    df = pd.read_excel(input_file)
    
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 初始化计数器
    copied_files = 0
    skipped_files = 0
    skipped_files_log = []

    # 遍历所有路径
    for _, row in df.iterrows():
        source_path = row['Path']
        
        # 检查文件是否存在
        if os.path.exists(source_path):
            # 构建目标路径
            target_path = os.path.join(target_dir, os.path.basename(source_path))
            
            # 检查目标路径是否存在，如果存在则重命名
            if os.path.exists(target_path):
                base_name, ext = os.path.splitext(os.path.basename(source_path))
                new_base_name = f"{base_name}_copy{ext}"
                target_path = os.path.join(target_dir, new_base_name)
            
            # 拷贝文件
            shutil.copy2(source_path, target_path)
            print(f"Copied {source_path} to {target_path}")
            copied_files += 1
        else:
            print(f"Source file not found: {source_path}")
            skipped_files += 1
            skipped_files_log.append((source_path, "Source file not found"))
    
    # 打印总结信息
    print(f"Total files processed: {len(df)}")
    print(f"Files copied: {copied_files}")
    print(f"Files skipped: {skipped_files}")
    
    # 打印被跳过的文件及其原因
    if skipped_files > 0:
        print("\nSkipped files and reasons:")
        for file_path, reason in skipped_files_log:
            print(f"{file_path}: {reason}")

# 主函数
if __name__ == "__main__":
    input_file = 'updated_processed_svn_log.xlsx'
    target_dir = os.path.expanduser('~/Desktop/PNG_Files2')
    
    # 拷贝PNG文件
    copy_png_files(input_file, target_dir)
    
    print(f"PNG文件已成功拷贝到 {target_dir}")