from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver_option = webdriver.ChromeOptions()
driver_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(driver_option)
driver.implicitly_wait(2)
driver.get("https://orteil.dashnet.org/cookieclicker/")

select_lang = driver.find_element(By.ID, "langSelect-EN")
select_lang.click()

# -------Running the game for 5 mins-------------
total_cookies = ""
game_time = time.time() + 60 * 5

while time.time() < game_time:

    t_end = time.time() + 5
    cookie = driver.find_element(By.ID, "bigCookie")
    while time.time() < t_end:
        cookie.click()
    time.sleep(1)
    cookie_number = driver.find_element(By.ID, "cookies")
    score = cookie_number.text.split(" ")[0]

    find_upgrades = driver.find_elements(By.CLASS_NAME, "price")
    max_upgrade = 0
    upgrade_id = ""
    for x in find_upgrades:
        if "," in x.text:
            value = x.text.replace(",", "")
        else:
            value = x.text
        if value != "" and int(score) >= int(value) > max_upgrade:
            max_upgrade = int(value)
            upgrade_id = x.get_attribute(name="id")

    upgrade = upgrade_id.replace("Price", "")

    # ----- get upgrade by first scrolling down-----------------
    get_upgrades = driver.find_element(By.ID, upgrade)
    driver.execute_script("arguments[0].scrollIntoView(true);", get_upgrades)
    get_upgrades.click()
    time.sleep(1)
    total_cookies = driver.find_element(By.ID, "cookies").text.split(" ")[3]
print(f"{total_cookies}/Seconds")
driver.quit()
