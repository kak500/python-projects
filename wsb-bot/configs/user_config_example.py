username = "pzx97506"
password = "99040806819"

course = "https://moodle2.e-wsb.pl/course/view.php?id=44712"

learn_vocabulary = {
    'Unit 1': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293302',
    'Unit 2': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293337',
    'Unit 3': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293355',
    'Unit 4': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293379',
    'Unit 5': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293420',
    'Unit 6': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293442',
    'Unit 7': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293466'
}

test_vocabulary = {
    'Unit 1': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293303',
    'Unit 2': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293338',
    'Unit 3': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293356',
    'Unit 4': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293380',
    'Unit 5': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293421',
    'Unit 6': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293443',
    'Unit 7': 'https://moodle2.e-wsb.pl/mod/quiz/view.php?id=2293467'
}

# if "/html/body/div[8]/div[2]/div/div[2]/div/div[2]/input[1]" in "/html/body/div[8]/div[2]/div/div[2]/div/div[2]/input[1]":
#     print("git")

# text = "The correct answer is: advanced"
# text = text[23::]

# print(text)

# try:



#     f = open("test.txt",'r')
#     file_content = f.readlines()
    
#     print(file_content)

#     temp_list = ['gienek\n','jasiu\n']

#     mergedlist = list(set(file_content + temp_list))

#     print(mergedlist)
# except IOError:
#     print("File not accessible")
# finally:
#     f.close()

file1 = open("temp/temp.txt",'r')
file_content1 = file1.readlines()

file2 = open("temp/temp - bank.txt",'r')
file_content2 = file2.readlines()

print(len(file_content1))
print(len(file_content2))

# if file_content1 not in file_content2:
#     print("git")

def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

file1.close()
file2.close()
print(list_duplicates(file_content1))