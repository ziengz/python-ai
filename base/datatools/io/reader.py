def reader_file(filename):
    '''
    读取文件
    :param filename:文件名
    :return: 返回读取后的数据
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print("读取发生异常：Exception is ",e)
        return None