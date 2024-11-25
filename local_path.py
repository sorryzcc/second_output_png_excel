import pandas as pd
import re

def update_paths(input_file, output_file, base_path):
    # 读取Excel文件
    df = pd.read_excel(input_file)
    
    # 定义正则表达式模式
    pattern = re.compile(r'/branches/PMGameDEV_CN/PM_Mainland_Trunk_20230321_r552586/PMGameClient/PMGame/(.*)')
    
    # 更新Path列
    df['Path'] = df['Path'].apply(lambda x: re.sub(pattern, lambda m: f'{base_path}/{m.group(1)}', x))
    
    # 保存为新的Excel文件
    df.to_excel(output_file, index=False)

# 主函数
if __name__ == "__main__":
    input_file = 'log.xlsx'
    output_file = 'local_path.xlsx'
    base_path = r'I:\PM_Mainland_Trunk_20230321_r552586\PMGameClient\PMGame'
    
    # 更新路径并保存
    update_paths(input_file, output_file, base_path)
    
    print(f"文件已成功处理并保存到 {output_file}")