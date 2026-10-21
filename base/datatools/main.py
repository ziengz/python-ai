# 从datatools中导入processer,reader,writer
from datatools import processer,reader,writer

def main():
    # 写入文件
    writer_lens = writer.writer_file("example.txt","hello world")
    if not writer_lens:
        print("写入失败")
        return

    # 读取文件
    read_data = reader.reader_file("example.txt")
    if not read_data:
        print("读取失败")
        return
    print(read_data)

if __name__ == '__main__':
    main()