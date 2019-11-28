# Mock 范例

这份代码，python3.7.2 的环境

重点想做的范例是如何精确 mock 掉单独一个文件中的web请求，分为两种 mock 方式，一种是自定 req 进行mock 一种是直接对 request 进行 mock

核心是通过制定文件，实现对指定文件的共用函数的mock
