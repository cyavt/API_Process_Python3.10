# Author: Nguyen Van Truc
# Date: 2024/01/20

# Import libraries auch as selenium, time, PIL, pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Import libraries for image processing
from PIL import Image
import pytesseract
# Import libraries for remove background
from rembg import remove

# Process image to text
# custom_config = r'--oem 3 --psm 6 -l vie'
pytesseract.pytesseract.tesseract_cmd = r'/app/.apt/usr/bin/tesseract'
def run_img_to_text(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, config=custom_config)
    return text
def run_remove_bg(image_path):
    input = Image.open(image_path)
    output = remove(input)
    output.save(image_path, 'PNG')

# Process autoclick program
def run_autoclick(user, ps):
    global result
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r"executable_path=E:\\3.LAPTRINH\\PYTHON\\chromedriver-win64\\chromedriver.exe")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://daotao.ute.udn.vn/viewsmsg.asp")
    driver.implicitly_wait(10)

    username = driver.find_element(By.NAME, "maSV")
    username.send_keys(user)

    password = driver.find_element(By.NAME, "pw")
    password.send_keys(ps)

    btn = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Đăng nhập']")
    btn.click()
    time.sleep(3)

    val = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[2]/table/tbody/tr[2]/td")
    # print(val.text)
    valText = val.text
    start_index = valText.find("Xin chào sinh viên ") + len("Xin chào sinh viên ")
    end_index = valText.find("\n", start_index)
    student_name = valText[start_index:end_index]

    # Print the extracted name
    # print(student_name)

    driver.close()
    driver.quit()
    return student_name


if __name__ == "__main__":
    run_remove_bg()
