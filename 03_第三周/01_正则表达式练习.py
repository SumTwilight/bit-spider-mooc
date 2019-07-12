import re
# test1
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

# test2 匹配为空
match = re.match(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))
print(match.group(0))
'''
Traceback (most recent call last):
  File "C:\ProgramData\Anaconda3\lib\site-packages\IPython\core\interactiveshell.py", line 3296, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-12-4d972d6c40f1>", line 1, in <module>
    match.group(0)
AttributeError: 'NoneType' object has no attribute 'group'
'''
# 匹配不为空
match = re.match(r'[1-9]\d{5}', '100081 BIT')
print(match.group(0))

# test 3
ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)

# test 4
temp = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(temp)

# test 5
temp = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
print(temp)


# test 6
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
    if m:
        print(m.group(0))


# test 7
temp = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
print(temp)
