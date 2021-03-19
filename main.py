import selenium.webdriver
import requests
import time

quizId = input("Quiz ID: ")
quiz = requests.get("https://play.kahoot.it/rest/kahoots/" + quizId).json()
if "uuid" not in quiz:
    print("Quiz ID not valid!")
    exit()

driver = selenium.webdriver.Firefox()

driver.get("https://kahoot.it")
question = 0
while True:
    try:
        driver.find_element_by_xpath("//button[@data-functional-selector='answer-0']")
    except:
        time.sleep(0.1)
        continue

    for i, choice in enumerate(quiz["questions"][question]["choices"]):
        if choice["correct"]:
            driver.find_element_by_xpath(f"//button[@data-functional-selector='answer-{i}']").click()
            break

    question += 1