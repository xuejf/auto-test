#创建文件夹：
import os
import shutil
import codecs
import xlrd

def buildfile(echkeyfile):
    if os.path.exists(echkeyfile):
        #创建前先判断是否存在文件夹，if存在则删除
        shutil.rmtree(echkeyfile)
        os.makedirs(echkeyfile)
    else:
        os.makedirs(echkeyfile)#else则创建语句
    return echkeyfile#返回创建路径

#传入的参数是需要创建文件夹的路径，比如我想在D盘下创建一个名字为newfile的文件夹，则传入参数为r’ D:\newfile’。同样，返回的参数也是r’ D:\newfile’


##写入文本1：

def write_txt(txt, path):
    f = codecs.open(path, 'a', 'utf8')
    f.write(str(txt))
    f.close()
# 传入参数为txt，path；txt为需要写入的内容，数据类型为字符串，path为写入的内容，数据类型为字符串。
# 传入的path需如下定义：path= r’ D:\text.txt’
# f = codecs.open(path, 'a', 'utf8')中，codecs为包，需要用impor引入，’a’表示追加写入txt，可以换成’w’，表示覆盖写入。'utf8'表述写入的编码，可以换成'utf16'等。

##写入文本2（等同于写入文本1，但是这个比较常用）：
import codecs
def writetxt(path, content, code='utf8'):
    with codecs.open(path, 'w', encoding=code)as f:
        f.write(content)
    return path+' is ok!'


##读取txt：
def read_txt_a(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
    return lines
## 表示按行读取txt文件,utf8表示读取编码为utf8的文件，可以根据需求改成utf16，或者GBK等。
## 返回的为数组，每一个数组的元素代表一行，若想返回字符串格式，可以将改写成return ‘\n’.join(lines)
def read_txt(path):
    with open(path, 'r', encoding='utf8') as f:
        lines = f.readlines()
        return '\n'.join(lines)

###读取Excel文件：

def read_xls(path):
    xl = xlrd.open_workbook(path)
    sheet = xl.sheets()[0] # 0表示读取第一个工作表sheet
    data = []
    for i in range(0, sheet.ncols): # ncols表示按列读取
        data.append(list(sheet.col_values(i)))
    return data
# xlrd为第三方包，可以通过用pip下载，具体操作：打开运行，输入cmd→在cmd中输入pip install xlrd，enter →等待安装完成即可。在后续若存在需要使用的第三方包，都可以通过这种方式下载和安装。
# 传入参数为path，path为excel所在路径。
# 传入的path需如下定义：path= r’ D:\excel.xlsx’或path= r’ D:\excel.xls’
# col_values(i)表示按照一列中的所有单元格遍历读取
# 可以根据需求，把col替换成row，则表示按行读取
# return data ：返回的data是一个二维数组，根据col和row，传回的数据呈现形式也不同，即row是col的转置。

##遍历文件夹：
def file_walker(path):
    fileArray = []
    for root, dirs, files in os.walk(path):
        for fn in files:
            eachpath = str(root+'\\'+fn)
            fileArray.append(eachpath)
    return fileArray
# 传入参数为path，path为需要遍历的文件夹路径。
# return fileArray 返回的是当前文件下所有文件的绝对路径

# 测试
if __name__ == "__main__":
    #str=read_txt("..\in_data\en_data_login.txt")
    content='byVGhRVtD4Qa1Ohd0O26CcsBOvx0DL0jZLF4KBbQ3GX10xPtL0UdyVhE5oTRJS0Mcf3b6ngRMyVbYqZiQsijE2kGfWLUaC9ARJt8atOmwIwH1jzAReHkoD7uHWEOuLbxSa9G2Qok36HazJGg8dPl4BFHsq/SS7Ec4qn1Jwsnv7jOs1F1YELlp3woIgsFQJ0OAmgG0xhmV1ilUS2TAzHkLidKHLSCe9P3Qs4ZHHdL2akRYI1LYaOk6rROfoUF5c91c46WpAsIIU/UdOeDQAXbhrgfoSizwWjENdeHnGv7yF0eATyJwgMoTD49dOIrozcrj8TZaqmodCsAUX+R9aOczFUPFFhZ1bHnBV16dEuuXSIRNcteUPdwgwyr7ZmB3eIpipuaKqlqFS/5oMhSAPVXdTgcbJlxGDxPIwOjBCGFmqIJEXCZH9hAo6oO8M8A1zaqHZm2VRksT28iPlXR4RkW0o3uf7H9bqzV42r2kYBYGgUjVu34+9e+OQGkrrbohgPhBQACCJe0sLsJnWn7X0x+I1g3SR+N64c1zialJtPdU3DhNVNkJXDIP71L/G6QizuFIO5SrqbOlTKZTnvXLRNvHXc0+xPCb6LejwlcjmeK4ndfyMM6eCM4f8fK7CmWTo0hVdWumO/hxGibHdVcKyNsP6y+5/hpfsgchoGIVDYMabttq1aVxrZZ7vh9AUFBbeH9cEe9nMckbOE7zH6qTXi3rKASss7B0zHpsXGtPgL0fAsHxheb9r/iVqejfF3Ub3z12lmMsbzyPOUhkVrrwU1ha6K7H95x12CXeBGXLSlKTbFXDRiKLl8TYAUGXKLHuwwTQiEin00sWBtw+oFHpaVbXJ2mFZaZisx+C0GttcCISLc='
    writetxt("..\\out_data\\r_data_login.txt",content)
    print (str)