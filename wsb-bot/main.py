from selenium import webdriver
from time import sleep
from configs import user_config


class WsbBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://login.wsb.pl/login?service=https%3A%2F%2Fportal.wsb.pl%2Fc%2Fportal%2Flogin%3Fredirect%3D%252F%26refererPlid%3D3593%26p_l_id%3D60068")
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(user_config.username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(user_config.password)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Moodle')]").click()
        sleep(3)

    def go_to_course(self):
        self.driver.get("https://moodle2.e-wsb.pl/course/view.php?id=44712")
        sleep(3)

    # Script goes to given URL of quiz attempts page
    def go_to_quiz(self,quiz_url):
        self.driver.get(quiz_url)

        highest_score = self.driver.find_element_by_xpath("//h3[contains(text(), 'Highest grade:')]").text
        print(highest_score)
        highest_score = highest_score[15:-10:]
        print(self.driver.find_elements_by_xpath("//a[@title='Review your responses to this attempt']"))
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Review')]").click()
        sleep(10)

    def scan_quiz(self,filename):
        self.driver.find_element_by_xpath("//a[contains(text(), 'Show all questions on one page')]").click()

        pl_words_elements = self.driver.find_elements_by_class_name("qtext")
        sleep(0.5)
        answer_objects = self.driver.find_elements_by_xpath("//input[contains(@name, '_answer')]")
        words_dictonary = {}
        incorrect_dictonary = {}
        file = open(f'word_lists/{filename}.txt','w')
        incorrect_words = open(f'word_lists/{filename}_incorrect.txt','w')
        for pl,en in zip(pl_words_elements,answer_objects):
            if "incorrect" not in en.get_attribute("class"):
                words_dictonary[pl.text] = en.get_attribute("value")
                file.write(f'{pl.text} - {en.get_attribute("value")}\n')
            else:
                incorrect_dictonary[pl.text] = en.get_attribute("value")
                incorrect_words.write(f'{pl.text} - {en.get_attribute("value")}\n')
        print(incorrect_dictonary)
        sleep(10)
        file.close()
        incorrect_words.close()

used_unit = 'Unit 1'
wsb_bot = WsbBot()
wsb_bot.go_to_course()
wsb_bot.go_to_quiz(user_config.quizes.get(used_unit))
# wsb_bot.scan_quiz(used_unit)