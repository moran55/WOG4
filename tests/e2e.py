import time
from selenium import webdriver
from selenium.webdriver.common.by import By

app_url = 'http://0.0.0.0:5000/'


def test_scores_service(url):
    driver = webdriver.Chrome(executable_path="/home/moran/PycharmProjects/WOG/Moran_WOG/chromedriver")
    driver.get(url)
    time.sleep(2)
    try:
        score = driver.find_element(by=By.ID, value='score')
        if 1 <= int(score.text) <= 1000:
            return True
        else:
            return False
    except BaseException as e:
        pass
    finally:
        driver.close()


def main():
    res = test_scores_service(app_url)
    if res:
        return 0
    else:
        return -1


if __name__ == '__main__':
    main()
