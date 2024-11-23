import xml.etree.ElementTree as ET
import pandas as pd
from datetime import datetime
import pytz

def parse_svn_log(xml_file):
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # 存储日志条目的列表
    log_entries = []
    
    # 遍历每个logentry元素
    for logentry in root.findall('logentry'):
        revision = logentry.get('revision')
        author = logentry.find('author').text
        date_utc = logentry.find('date').text
        message = logentry.find('msg').text
        
        # 将UTC时间转换为北京时间
        date_utc = datetime.strptime(date_utc, '%Y-%m-%dT%H:%M:%S.%fZ')
        date_cst = date_utc.replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Shanghai'))
        date_cst_str = date_cst.strftime('%Y-%m-%d %H:%M:%S')
        
        # 提取路径信息，只保留路径名字以 .png 结尾的路径
        paths = logentry.findall('paths/path')
        for path in paths:
            if path.text.endswith('.png'):
                log_entries.append({
                    'Revision': revision,
                    'Author': author,
                    'Date': date_cst_str,
                    'Message': message,
                    'Path': path.text,
                    'Action': path.get('action')
                })
    
    return log_entries

def save_to_excel(log_entries, excel_file):
    # 将日志条目列表转换为DataFrame
    df = pd.DataFrame(log_entries)
    
    # 保存为Excel文件
    df.to_excel(excel_file, index=False)

# 主函数
if __name__ == "__main__":
    xml_file = 'log.xml'
    excel_file = 'svn_log.xlsx'
    
    # 解析XML文件
    log_entries = parse_svn_log(xml_file)
    
    # 保存为Excel文件
    save_to_excel(log_entries, excel_file)
    
    print(f"日志已成功保存到 {excel_file}")