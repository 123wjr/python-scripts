def process_directory_structure(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    processed_lines = []
    stack = []  # 存储各层级的目录
    
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:  # 跳过空行
            continue

        indent_level = len(line) - len(stripped_line)  # 计算缩进层级
        
        # 根据缩进层级调整stack
        while len(stack) > (indent_level // 4):  # 每4个空格为一级
            stack.pop()
        
        stack.append(stripped_line)  # 将当前目录加入栈

        # 生成完整路径并保存
        full_path = "::".join(stack)
        processed_lines.append(full_path)
    
    # 将补全路径的内容写入新文件
    with open("processed_directory_structure.txt", 'w', encoding='utf-8') as f:
        for line in processed_lines:
            f.write(line + '\n')

    print("目录结构已补全并保存至 'processed_directory_structure.txt' 文件中。")

# 使用方法
file_path = 'E:/2025届一轮复习/化学配套精练/FreePic2Pdf_bkmk.txt'
process_directory_structure(file_path)
