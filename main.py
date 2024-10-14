import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Edge()
wait = WebDriverWait(browser, 10)
# browser.get("https://jsj.top/f/MCv737")  # 问卷网址
browser.get("https://jsj.top/f/NAAZPa")  # 问卷网址
# https://jsj.top/f/MCv737

    # # 选项框，这里“8XEm”代表“是”
    # car = wait.until(EC.presence_of_element_located((By.XPATH,'//[@value="8XEm"]')))
    # car.clear()
    # car.click()

    # 文本框
name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="TextInputfield_1"]')))
print(type(name_input))
name_input.clear()
name_input.send_keys('输入名字')

    # 地理位置
    # location = wait.until(EC.presence_of_element_located((By.XPATH,'拿到对应元素')))
    # location.click()
    # search = wait.until(EC.presence_of_element_located((By.XPATH, '/拿到对应元素')
    # ))
    # search.send_keys('这里输入地址')
    # time.sleep(1)
    # 将页面滑到底，防止按钮被遮挡
button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="ant-btn ant-btn-primary ant-btn-two-chinese-chars form-theme--submit-button  published-form__submit  FooterButton_button__vJkWw"]')))
browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
button.click()
time.sleep(1)
    # 提交
submit = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="ant-btn ant-btn-primary ant-btn-two-chinese-chars form-theme--submit-button  published-form__submit  FooterButton_button__vJkWw"]')))
submit.click()
# time.sleep(50)
# browser.close()