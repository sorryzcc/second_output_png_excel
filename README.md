# second_output_png_excel
要在 Excel 中实现从 o列到 D 列的优先级赋值给 M 列，可以使用嵌套的 IF 函数。给我具体的步骤和公式：


1双击bat
2运行python convert_svn_log_to_excel.py 输出svn_log.xlsx'
3运行process_svn_log.py输出processed_svn_log.xlsx.xlsx
4手动分列path列...处理表格  
=IF(T2<>"", T2, IF(S2<>"", S2, IF(R2<>"", R2, IF(Q2<>"", Q2, IF(P2<>"", P2, IF(O2<>"", O2, IF(N2<>"", N2, IF(M2<>"", M2, IF(L2<>"", L2, "")))))))))

5.运行js文件输出output.xlsx
6手动删除重复项目
7运行update_paths.py
8运行Source_file_not_found.py