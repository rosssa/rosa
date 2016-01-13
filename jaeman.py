Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # 재만
>>> #1. set
>>> {1,2,3} == {3,2,1}
True
>>> #왜냐하면 set에는 순서가 없기 때문에
>>> 
>>> #2. List, Set
>>> a=[1,1,1,1,2,3,3,2,5,6,3,1]
>>> set(a)
{1, 2, 3, 5, 6}
>>> 
>>> 
>>> #3. b="this    is     test"
>>> #3. list 사용하기
>>> b= "this     is     test"
>>> re.split(r"\s+",a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    re.split(r"\s+",a)
NameError: name 're' is not defined
>>> 
