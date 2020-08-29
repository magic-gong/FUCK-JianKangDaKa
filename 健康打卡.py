from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.select import Select

def JudgeTime(chrome_driver,UserName,PassWord):
    while(1):
        while(time.localtime().tm_hour!=8):#八点开始打卡
            time.sleep(1800)
        HealtyReport(chrome_driver,UserName,PassWord)#打卡以后休眠20h
        time.sleep(72000)

def HealtyReport(chrome_driver,UserName,PassWord):

    options = Options()#取消下面三行注释掉，就是无头模式
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument('lang=zh_CN.UTF-8')

    driver=Chrome(executable_path=chrome_driver,options=options)
    driver.get('https://healthreport.zju.edu.cn/ncov/wap/default/index')

    SearchUserName = driver.find_element_by_id('username')
    SearchPassWord = driver.find_element_by_id('password')
    SearchLoingIn = driver.find_element_by_id('dl')
    SearchUserName.send_keys(UserName)
    SearchPassWord.send_keys(PassWord)
    SearchLoingIn.click()
    time.sleep(2)
    sfzx = driver.find_element_by_xpath("//*[@name='sfzx']/div/div[1]/span[1]")#div1是在校，2是不在
    sfzx.click()
    sfzgn = driver.find_element_by_xpath("//*[@name='sfzgn']/div/div[1]/span[1]")#div1是境内，2是不在
    sfzgn.click()
    Location = driver.find_element_by_xpath("//*[@placeholder='点击获取地理位置 Click to get geographic location']")#获取位置
    Location.click()
    time.sleep(3)
    ShiBai = driver.find_element_by_class_name('wapat-btn.wapat-btn-ok')
    ShiBai.click()
    Select(driver.find_element_by_xpath("//*[@class='hcqbtn hcqbtn-danger']")).select_by_value('浙江省')
    Select(driver.find_element_by_xpath("//*[@class='hcqbtn hcqbtn-warning']")).select_by_value('杭州市')
    Select(driver.find_element_by_xpath("//*[@class='hcqbtn hcqbtn-primary']")).select_by_value('西湖区')
    jrdqtlqk = driver.find_element_by_xpath("//*[@name='jrdqtlqk']/div/div[3]/span[1]")#div3是好
    jrdqtlqk.click()
    sfymqjczrj = driver.find_element_by_xpath("//*[@name='sfymqjczrj']/div/div[2]/span[1]")#div2是好
    sfymqjczrj.click()
    sfqrxxss = driver.find_element_by_xpath("//*[@name='sfqrxxss']/div[1]/div[1]/span[1]")#div1是好
    sfqrxxss.click()
    Tijiao = driver.find_element_by_class_name('wapcf-btn-qx')
    Tijiao.click()
    print('ok')
    time.sleep(3)
    driver.quit()

if __name__=='__main__':
    UserName = '在这里输入用户名'
    PassWord = '在这里输入密码'
    chrome_driver = r"在这里输入chromedriver的位置"
    JudgeTime(chrome_driver,UserName,PassWord)