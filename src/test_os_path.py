import os
print("abspath: repository absolute path")
print(os.path.abspath('./lib/calc_class'))

print("realpath: file absolute path")
print(os.path.realpath(__file__))

print("isdir: directory or not")
print(os.path.isdir(os.path.abspath('.')))
print(os.path.isdir(os.path.realpath(__file__)))

print("isfile: file or not")
print(os.path.isfile(os.path.realpath(__file__)))

print("exists: check for existence of path")
print(os.path.exists(os.path.abspath('.')))

print("join: combine paths and files")
print(os.path.join(os.path.abspath('.'),'web'))

print("dirname: directory name")
print(os.path.dirname(os.path.realpath(__file__)))
