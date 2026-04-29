import yagmail

sender = '3507497566@qq.com'
password = 'wogpxjgizscycjhh'
receiver = '3507497566@qq.com'

yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com')

header = '安杰-树莓派-家安全'
contents = [
    '这个邮件来自安杰树莓派',
    '你可以点击下方链接访问我们服务器：',
    '<a href="https://www.baidu.com">安杰网站</a>',
    r"img300.jpg"
]

yag.send(receiver, header, contents)
print('邮箱发送成功')
