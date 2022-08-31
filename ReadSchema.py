import sys, keyword
import re, string, os


pattern_node = re.compile(r"^[0-9]+\s.+;\s.+;\s([0-1])\s([0-9]+)\s([0-1])", re.I)
pattern_variable_node = re.compile(r"^[0-9]+\s.+;\s.+;\s([0-1])\s([0-9]+)\s1", re.I)
pattern_nonvariable_node = re.compile(r"^[0-9]+\s.+;\s.+;\s([0-1])\s([0-9]+)\s0", re.I)

pattern_field = re.compile(r"^.+;\s[a-z];\s([0-1])\s[0-9]+\s([0-9]+)")


def FindAllFile(base):
    for root, ds, fs in os.walk(base, topdown=False):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


if __name__ == '__main__':
    filelist = FindAllFile("C:/Users/13190/Documents/brep_control/ps_schema")
    for file in filelist:
        state = True

        with open(file) as file_obj:
            line = file_obj.readline()

            while line:
                matchobj_node = pattern_variable_node.match(line)
                # 如果是可变的
                if matchobj_node:
                    # 如果需要输出
                    if 1:#matchobj_node.group(1) == '1':
                        #num 记录可变且输出的node底下有几个可变的field
                        num = 0
                        # 逐行读取field
                        for i in range(int(matchobj_node.group(2))):
                            line = file_obj.readline()
                            matchobj_field = pattern_field.match(line)
                            #如果field需要输出,但存在node显示可变但可变变量不输出的情况
                            if (matchobj_field) :#and (matchobj_field.group(1) == '1'):
                                #如果为可变field
                                if matchobj_field.group(2) == '1':
                                    num = num + 1
                        if num != 1:
                            state = False
                            break

                line = file_obj.readline()

        if state == True:
            print("{} is true".format(file))
        else:
            print("{} is false".format(file))