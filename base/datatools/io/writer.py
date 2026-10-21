def writer_file(filename,data):
    '''
    写文件
    :param filename:文件名
    :return: 返回写入后的数据
    '''
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            return f.write(data)
    except Exception as e:
        print("写入发生异常：Exception is ",e)
        return None