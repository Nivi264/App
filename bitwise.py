Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=100
x**=2
x
10000
x,y=1,2
x
1
y
2
x>y
False
x<y
True
x!=y
True
x==y
False
x<=y && x>y
SyntaxError: invalid syntax
x<=y and x>y
False
x<=y or x>y
True
int(True)
1
x<=y not x<y
SyntaxError: invalid syntax
x<=y not x<y
SyntaxError: invalid syntax
x=True
not x
False
x=not
SyntaxError: incomplete input
x=not x
x
False

bin(25)
'0b11001'
oct(25)
'0o31'
hex(25)
'0x19'
 0x19
 
SyntaxError: unexpected indent
0xf
15
15
15

x,y=y,x
x
2
y
False
a=5
b=6
a,b=b,a
a
6
>>> b
5
>>> print(a b)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(a,b)
6 5
>>> x =xor x
SyntaxError: incomplete input
>>> a>>b
0
>>> a<<b
192
>>> ~12
-13
>>> ~14
-15
>>> -15
-15
>>> ~36
-37
>>> 12 & 13
12
>>> 12|13
13
>>> 13
13
>>> 25|30
31
>>> 25&30
24
>>> 12^13
1
>>> 25^30
7
>>> 25<<30
26843545600
>>> 12<<3
96
>>> 10>>2
2
>>> 12>>3
1
>>> 10<<3
80
>>> 10>>3
1
