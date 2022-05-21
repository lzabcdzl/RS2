"""邮箱基本设置"""
# 邮件服务器地址
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server = 'smtp.QQ.com'
# 邮件服务器端口号
port = 25
# 发件人地址
sender = '2091719742@qq.com'
# 授权码
code = 'irxuxtbqychdeiee'
# 收件人
receivers = '2091719742@qq.com;2444252210@qq.com'

"""写邮件"""
# 创建邮件对象
mail = MIMEMultipart()
# 设置发件人
mail['from'] = sender
# 设置收件人
mail['to'] = receivers
# 主题
mail['subject'] = 'RS2自动化测试报告第一版'

"""添加附件"""
# 读取文件
path = r'../report/report_2022-05-09_14-54-48.html'
with open(path, 'rb') as file:
    report = file.read()
# 对附件进行编码
attachment = MIMEText(report, 'base64', 'utf-8')
# 设置附件的类型
attachment['Content-Type'] = 'application/octet-stream'
# 设置附件的处理方式
attachment['Content-Disposition'] = 'attachment;filename=%s'%path.split('/')[-1]
# 添加附件
mail.attach(attachment)

"""添加正文"""
# #编辑正文
# content = '''
# <p>邮件内容如下：</p>
# <br>
# <p>&nbsp;&nbsp;&nbsp;&nbsp;RS2自动化第一版测试已经完成，附件中是初步的测试报告，请查收！</p>
# <br>
# <p>此致，</p>
#
# <p>&nbsp;&nbsp;&nbsp;&nbsp;敬礼！</p>
#
# <p>吝昭</p>
# <p>2022.5.6</p>
# '''

# 对正文进行编码
body = MIMEText(report, _subtype='html', _charset='utf-8')
# 添加正文
mail.attach(body)


"""发送邮件"""
# 创建smtp对象
smtp = smtplib.SMTP()
# 连接邮件服务器
smtp.connect(server, port)
# 登陆邮件服务器
smtp.login(sender, code)
# 发送邮件
smtp.sendmail(sender, receivers.split(';'), mail.as_string())
# 关闭邮件服务器
smtp.close()
print('邮件发送完毕')
