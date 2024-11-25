const XLSX = require('xlsx');

// 读取Excel文件
const workbook = XLSX.readFile('picture.xlsx');
const sheetName = workbook.SheetNames[0]; // 获取第一个工作表的名称
const worksheet = workbook.Sheets[sheetName];

// 将工作表转换为JSON数组
const data = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

// 定义正则表达式
const regex = /_[0-9a-fA-F]{16}/;

// 处理数据，删除匹配的行
const filteredData = data.filter(row => {
  if (row[6] && regex.test(row[6])) { // G列的索引是6
    return false; // 删除该行
  }
  return true;
});

// 将过滤后的数据转换回工作表
const newWorksheet = XLSX.utils.aoa_to_sheet(filteredData);

// 更新工作簿
workbook.Sheets[sheetName] = newWorksheet;

// 写回Excel文件
XLSX.writeFile(workbook, 'filtered_picture.xlsx');