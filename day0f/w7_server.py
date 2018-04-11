'''
tcp:通信
'''

from socket import  *
import time

SERVER_IP = "0.0.0.0"
SERVER_PORT = 8888

# 创建流式套接字对象
server_sd = socket(AF_INET, SOCK_STREAM)
# 将本地地址与套接字对象绑定  必须绑定,这样客户端才知道与谁链接
server_sd.bind((SERVER_IP, SERVER_PORT))
# 使得套接字处于监听状态, 参数指明最大的链接个数
server_sd.listen(10)

while True:
    # 等待接收客户端的请求
    newsd, remote_addr = server_sd.accept() # newsd用于数据交换的套接字  remote_add 对端地址
    print("recive the new connect, the addr %s:%s" % remote_addr)
    # 向客户端发送消息
    newsd.send(b'welcome connect me')
    # 接收客户端消息
    rcvdata = newsd.recv(1024)
    print("recive data is %s" % rcvdata.decode('utf-8'))
    snddata = time.ctime() + rcvdata.decode('utf-8')
    newsd.send(snddata.encode('utf-8')) # python3 str--->unicode  网络传输的数据bytes  unicode--->bytes (encode)
    #time.sleep(100)

server_sd.close()

