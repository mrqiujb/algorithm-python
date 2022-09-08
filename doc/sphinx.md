1.使用conda在conda环境安装，没有直接安装

2.如果使用conda，需要现在终端activate虚拟环境，然后再使用命令

3.新建一个doc目录，此目录用于存放文档

4.运行sphinx-quickstart命令，按照conf.py配置

5.sphinx-apidoc -o outputpath inputpath 使用此命令，构建文档

6.在doc目录下，使用make clean先清除上次结构，再make html输出网页

7.输出文件在./doc/source/build/html里面