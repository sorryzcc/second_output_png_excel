import pandas as pd

def process_svn_log(input_file, output_file):
    # 读取Excel文件
    df = pd.read_excel(input_file)
    
    # 获取所有Action为D的Path
    paths_to_remove = df[df['Action'] == 'D']['Path'].tolist()
    
    # 删除所有Path在paths_to_remove中的行
    df = df[~df['Path'].isin(paths_to_remove)]
    
    # 对Path列进行去重，保留第一次出现的记录
    df = df.drop_duplicates(subset=['Path'], keep='first')
    
    # 保存为新的Excel文件
    df.to_excel(output_file, index=False)

# 主函数
if __name__ == "__main__":
    input_file = 'svn_log.xlsx'
    output_file = 'processed_svn_log.xlsx'
    
    # 处理SVN日志并保存
    process_svn_log(input_file, output_file)
    
    print(f"文件已成功处理并保存到 {output_file}")