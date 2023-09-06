# ImageServer
一个基于python Flask框架的简单小程序（生成自chatGPT）

## 说明

主要包含了一个上传文件夹upload，一个下载文件夹download和一个主程序main.py。

## 如何使用？

1. 使用pip安装flask框架。
2. 找到自己本地电脑的IPv4地址后，修改主程序main.py的最后一行代码`app.run(host='192.168.0.100', port=5000)`。例如我本机的IPv4地址为'192.168.23.1'，那么应该将该行代码修改为``app.run(host='192.168.23.1', port=5000)``。
3. 运行main.py.

## 如何使用？

### 欢迎界面

打开任意浏览器输入这个网址：`<你的IPv4地址>:5000`,出现以下欢迎界面：

![](https://github.com/hljmssjg/ImageServer/blob/main/readme_imgs/welcome.png)

### 上传图片

点击欢迎界面中的upload按钮，跳转到上传界面：

![](https://github.com/hljmssjg/ImageServer/blob/main/readme_imgs/upload1.png)

点击选择文件按钮选择要上传的图片再点击upload按钮，完成上传图片操作：

![](https://github.com/hljmssjg/ImageServer/blob/main/readme_imgs/upload2.png)

此时对应的本地主机里的upload文件夹中应该有了之前通过网页界面上传的照片(例如我上传了一张猫的照片):

![](https://github.com/hljmssjg/ImageServer/blob/main/readme_imgs/upload3.png)

### 下载图片

假设现在有一些图片经过处理，放置在了该项目中的download文件夹中，可以通过网页中的download页面来进行下载。比如，现在我的download文件夹中存在一张狗的图片，我在欢迎界面点击download按钮：

![](https://github.com/hljmssjg/ImageServer/blob/main/readme_imgs/download.png)

点击对应的图片，即可完成下载操作。

