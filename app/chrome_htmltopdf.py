from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 通过selenium调起chrome的打印功能完成批量导出pdf功能。
# 注意，ChromeDriver和Chrome的版本需要一一对应，具体的chrome和ChromeDriver可从下面链接下载：
# https://googlechromelabs.github.io/chrome-for-testing/

# 配置 Chrome 浏览器选项
chrome_options = Options()
#chrome_options.add_argument('--headless=new')  # 无头模式，即不显示浏览器窗口
chrome_options.add_argument('--disable-gpu')  # 禁用 GPU 加速
chrome_options.add_argument('--kiosk-printing')  # 开启打印模式
chrome_options.add_argument('--print-to-pdf')  # 打印为 PDF

# 创建 Chrome WebDriver 对象
driver = webdriver.Chrome(options=chrome_options)

# 读取包含网页链接的文本文件
with open('../config/urls.txt', 'r') as file:
    urls = file.readlines()

# 批量转换网页为 PDF
for url in urls:
    url = url.strip()  # 去除链接前后的空格和换行符

    # 打开网页
    driver.get(url)

    # 等待页面加载完成（可根据需要调整等待时间）
    driver.implicitly_wait(10)

    # 使用 Chrome 打印功能将网页保存为 PDF
    driver.execute_script('window.print();')
    print(f'转换成pdf完成url=',url)

print('批量转换完成')

# 关闭浏览器
driver.quit()
