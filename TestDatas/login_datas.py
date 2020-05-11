
#正常场景的数据
success_data={"user":"18684720553","passwd":"python"}

# 异常用例手机号格式不正确(大于11位 小于11位 为空  不在这个号码段)
phone_data=[
{"user":"186847205534","passwd":"python","check":"请输入正确的手机号"},
{"user":"186847205","passwd":"python","check":"请输入正确的手机号"},
{"user":"","passwd":"python","check":"请输入手机号"},
{"user":"1163563232","passwd":"python","check":"请输入正确的手机号"}
]


