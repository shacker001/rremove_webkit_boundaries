def remove_webkit_boundaries(input_string):
    # Remove the boundary markers and line breaks
    output_string = input_string.replace("----WebKitFormBoundary\r\n", "").replace("\r\n", "").replace("\n", "")
    return output_string

input_string = """Z\r\n----WebKitFormBoundary\r\n
m\r\n----WebKitFormBoundary\r\n
x\r\n----WebKitFormBoundary\r\n
h\r\n----WebKitFormBoundary\r\n
Z\r\n----WebKitFormBoundary\r\n
3\r\n----WebKitFormBoundary\r\n
t\r\n----WebKitFormBoundary\r\n
t\r\n----WebKitFormBoundary\r\n
d\r\n----WebKitFormBoundary\r\n
W\r\n----WebKitFormBoundary\r\n
x\r\n----WebKitFormBoundary\r\n
0\r\n----WebKitFormBoundary\r\n
M\r\n----WebKitFormBoundary\r\n
X\r\n----WebKitFormBoundary\r\n
B\r\n----WebKitFormBoundary\r\n
s\r\n----WebKitFormBoundary\r\n
M\r\n----WebKitFormBoundary\r\n
3\r\n----WebKitFormBoundary\r\n
A\r\n----WebKitFormBoundary\r\n
0\r\n----WebKitFormBoundary\r\n
c\r\n----WebKitFormBoundary\r\n
n\r\n----WebKitFormBoundary\r\n
R\r\n----WebKitFormBoundary\r\n
z\r\n----WebKitFormBoundary\r\n
Y\r\n----WebKitFormBoundary\r\n
z\r\n----WebKitFormBoundary\r\n
B\r\n----WebKitFormBoundary\r\n
u\r\n----WebKitFormBoundary\r\n
Z\r\n----WebKitFormBoundary\r\n
n\r\n----WebKitFormBoundary\r\n
V\r\n----WebKitFormBoundary\r\n
z\r\n----WebKitFormBoundary\r\n
M\r\n----WebKitFormBoundary\r\n
3\r\n----WebKitFormBoundary\r\n
N\r\n----WebKitFormBoundary\r\n
9\r\n----WebKitFormBoundary\r\n"""

output_string = remove_webkit_boundaries(input_string)
print(output_string)

