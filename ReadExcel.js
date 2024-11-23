const XLSX = require('xlsx');

// 读取 Excel 文件
const workbook = XLSX.readFile('processed_svn_log.xlsx');
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];

// 获取 D 列的所有文件名
const filenames = XLSX.utils.sheet_to_json(worksheet, { header: 1 })
    .map(row => row[3]) // D 列的索引是 3
    .filter(name => name); // 过滤掉空值

// 定义处理函数
function processFilename(filename) {
    // 使用正则表达式匹配 _16位字符.
    const regex = /_([a-fA-F0-9]{16})\./;
    const match = filename.match(regex);

    if (match) {
        // 提取匹配到的字符串
        const matchedString = match[0];
        // 去掉匹配到的字符串及其前面的 _
        return filename.replace(matchedString, '.');
    }

    // 如果没有找到符合条件的字符串，保持原样
    return filename;
}

// 处理文件名数组
const processedFilenames = filenames.map(processFilename);

// 更新工作表中的文件名
processedFilenames.forEach((newName, index) => {
    const cellAddress = XLSX.utils.encode_cell({ r: index + 1, c: 3 }); // D 列的索引是 3
    if (!worksheet[cellAddress]) {
        worksheet[cellAddress] = {}; // 如果单元格不存在，创建它
    }
    worksheet[cellAddress].v = newName;
});

// 写回新的 Excel 文件
XLSX.writeFile(workbook, 'output.xlsx');