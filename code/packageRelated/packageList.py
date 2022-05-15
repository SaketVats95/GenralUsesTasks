import pkg_resources as pkg

list = [i for i in pkg.working_set]
type(list[1])
# print(list[3])
for i in range(len(list)):
    reqlist = list[i].requires()
    if len(reqlist) > 0:
        print(reqlist, '\n',list[i])
    # print(list[i].requires())


help('IPython')
dir('IPython')


import sys
sys.path

__name__





