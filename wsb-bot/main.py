from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import shutil
from configs import user_config

learn_vocabulary = user_config.learn_vocabulary
test_vocabulary = user_config.test_vocabulary
course = user_config.course

class WsbBot:
    def __init__(self):

        # options = Options()
        # options.add_argument('window-size=1920x1080')
        
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920, 1080)
        self.driver.get("https://login.wsb.pl/login?service=https%3A%2F%2Fportal.wsb.pl%2Fc%2Fportal%2Flogin%3Fredirect%3D%252F%26refererPlid%3D3593%26p_l_id%3D60068")
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(user_config.username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(user_config.password)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Moodle')]").click()
        sleep(3)

    def go_to_course(self, url):
        self.driver.get(url)
        sleep(3)

    # Script goes to given URL of quiz attempts page
    def go_to_quiz(self,quiz_url):
        self.driver.get(quiz_url)

        highest_score = self.driver.find_element_by_xpath("//h3[contains(text(), 'Highest grade:')]").text
        highest_score = highest_score.lstrip('Highest grade: ').rstrip('.').split(' / ')[0]

        scores = self.driver.find_elements_by_xpath("//td[@class='cell c2']")
        review_buttons = self.driver.find_elements_by_xpath("//a[contains(text(), 'Review')]")
        for index, score in enumerate(scores):
            if score.text == highest_score:
                review_buttons[index].click()
                break
                print(score.text)
       
        
    def scan_quiz(self,filename):
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(text(), 'Show all questions on one page')]").click()

        pl_words_elements = self.driver.find_elements_by_class_name("qtext")
        sleep(0.5)
        answer_objects = self.driver.find_elements_by_xpath("//input[contains(@name, '_answer')]")
        words_dictonary = {}
        incorrect_dictonary = {}
        file = open(f'word_lists/{filename}.txt','w')
        incorrect_words = open(f'word_lists/incorrect/{filename}_incorrect.txt','w')
        for pl,en in zip(pl_words_elements,answer_objects):
            if "incorrect" not in en.get_attribute("class"):
                words_dictonary[pl.text] = en.get_attribute("value")
                file.write(f'{pl.text} - {en.get_attribute("value")}\n')
            else:
                incorrect_dictonary[pl.text] = en.get_attribute("value")
                incorrect_words.write(f'{pl.text} - {en.get_attribute("value")}\n')
        print(incorrect_dictonary)
        sleep(4)
        file.close()
        incorrect_words.close()

    # Goes to quiz and solves on 0 %
    def solve_test(self, test_url):
        self.driver.get(test_url)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//a[@class='endtestlink']").click()
        sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(),'Submit all and finish')]").click() # correct works

        sleep(8)

    # Method that gathers list of words
    def gather_quiz(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'Show all questions on one page')]").click()
        pl_words_elements = self.driver.find_elements_by_class_name("qtext")
        answer_objects = self.driver.find_elements_by_class_name("rightanswer")

        solid_file = open("temp/temp.txt","r")
        solid_file_content = solid_file.readlines()
        temp_file = open("temp/temp.txt","w")

        temp_list = []
        for pl,en in zip(pl_words_elements,answer_objects):
            en = en.text[23::]
            temp_list.append(f'{pl.text} - {en}\n')

        print(f'solid_file length: {len(solid_file_content)}')
        print(f'temp list length: {len(temp_list)}') 
        mergedlist = list(set(solid_file_content + temp_list))  # Merge two files
        print(len(mergedlist))

        for element in mergedlist:
            temp_file.write(element)
        temp_file.close()
        solid_file.close()
        print("Temp file created")
        self.driver.find_element_by_xpath("//a[contains(text(), 'Finish review')]").click()


    def clear_temp(self):
        open('temp/temp.txt', 'w').close()
        print("Temp file cleared")


    def copy_temp(self, name):
        shutil.copy2('temp/temp.txt', f'word_lists/processed temp/{name}.txt')
        print("File copied")


    def job_done(self):
        self.driver.execute_script("alert('Script done')")

       
used_unit = 'Unit 3'
wsb_bot = WsbBot()
wsb_bot.go_to_course(course)
wsb_bot.solve_test(test_vocabulary.get(used_unit))

# for i in range(1,8):
#     wsb_bot.go_to_quiz(learn_vocabulary.get(f'Unit {i}'))
#     wsb_bot.scan_quiz(f'Unit {i}')

wsb_bot.job_done()
sleep(5)
