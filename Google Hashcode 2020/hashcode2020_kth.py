fh = open('f_libraries_of_the_world.txt')
contents = fh.readlines()
(total_books, total_libs, total_days) = contents[0][:-1].split(' ')
(total_books, total_libs, total_days) = (int(total_books), int(total_libs), int(total_days))
book_scores = []
for elem in contents[1][:-1].split(' '):
    book_scores.append(int(elem))
books_array = []
capacity_array = []
signupdays_array = []
bookno_array = []
contents = contents[2:]
for i in range(total_libs):
    book_numbers = []
    (books, signup_days, capacity) = contents[2*i][:-1].split(' ')
    (books, signup_days, capacity) = (int(books), int(signup_days), int(capacity))
    books_array.append(books)
    capacity_array.append(capacity)
    signupdays_array.append(signup_days)
    for elem in contents[2*i+1][:-1].split(' '):
        book_numbers.append(int(elem))
    bookno_array.append(book_numbers)

lib_scores = []
for l in range(total_libs):
    days_action = total_days - signupdays_array[l]
    days_capacity = capacity_array[l]*days_action
    days_books = []
    for elem in bookno_array[l]:
        days_books.append((elem,book_scores[elem]))
        days_books.sort(key=lambda x: x[1], reverse=True)
    books_to_choose = min(days_capacity,len(days_books))
    score = 0
    for k in range(books_to_choose-1):
        score += days_books[k][1]
    lib_scores.append((l,score,books_to_choose,score/signupdays_array[l]))

lib_scores.sort(key=lambda x: x[3],reverse=True)

lib_choices = []
pointer = 0
days_left = total_days
for i in range(len(lib_scores)):
    days_to_signup = signupdays_array[i]
    if days_left - days_to_signup <=0:
        continue
    if days_left <= 0:
        break
    days_left -= days_to_signup
    lib_choices.append((lib_scores[i][0],lib_scores[i][2]))

fw = open('f_answer6.txt','w')
fw.writelines(str(len(lib_choices))+'\n')
global_books = []
for m in range(len(lib_choices)):
    days_books = []
    books_selected = []
    for elem in bookno_array[lib_choices[m][0]]:
        days_books.append((elem, book_scores[elem]))
        days_books.sort(key=lambda x: x[1], reverse=True)
    books_selected = [i[0] for i in days_books]
    res = [i for i in books_selected if i not in global_books]
    books_to_choose = min(lib_choices[m][1], len(res))
    books_selected = res[0:books_to_choose]
    global_books = global_books + books_selected
    books_str = ' '.join(str(v) for v in books_selected)
    fw.writelines(str(lib_choices[m][0]) + ' ' + str(len(books_selected)) + ' ' + '\n')
    fw.writelines(books_str + '\n')







