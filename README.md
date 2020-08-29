# 自动健康打卡
______
## Tips：
程序更新到2020.8.29，之后可能会出现增加选项等情况。
## 原理：
selenium进行页面模拟，通过统一身份认证登录
## 依赖条件：
1、安装selenium库  
2、chromedriver.exe    
## 使用：
1、修改UserNmae、PassWord分别为用户名和密码（统一身份认证的密码）；  
2、修改chrome_driver为chromedriver的位置；  
3、运行。程序会在每天早点8点的某一个时间进行打卡，之后休眠20h；  
## 无头模式：
取消options = Options()下面三行注释。

