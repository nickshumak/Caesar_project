from caesar_items.pages.students_page import Student

data = {'url_for_test_start': 'http://localhost:3000/Students/Dnipro/DP-093-JS/list',
        # expected variables
        'expected_url_group_info': 'http://localhost:3000/Groups/Dnipro/DP-093-JS/info',
        'expected_url': 'http://localhost:3000/Students/Dnipro/DP-093-JS/list',
        'expected_name_file_cv': 'cv.docx',
        'expected_name_file_photo': 'photo.jpg',
        'group_name': 'DP-093-JS',
        'expected_warnings': ['You can use only letters, space and "-"',
                              'You can use only letters, space and "-"',
                              'You can use only letters, space and "-"',
                              'You can use only letters, space and "-"',
                              'You can use only letters, space and "-"',
                              'You can use only letters, space and "-"'],
        # data for adding new student
        'first_new_student': Student(first_name='Vladyslava',
                                     last_name='Semmi', incoming_mark='111',
                                     entry_mark='5', english_level='Pre-intermediate',
                                     approved_by='Not approved'),
        'second_new_student': Student('Sherlock', 'Holmes', '333', '3',
                                      'Pre-intermediate strong', 'N. Varenko'),
        'third_new_student': Student('Merlin', 'Monro', '123', '3', 'Elementary',
                                     'Custom', 'Casper'),
        # data for editing student
        'first_new_data_student': Student('Garry', 'Potter', '222', '2',
                                          'Upper-intermediate', 'Not approved'),
        'second_new_data_student': Student('Robin', 'Good', '444', '4',
                                           'Advanced', 'N. Varenko'),
        'third_new_data_student': Student('Clark', 'Kent', '321', '3',
                                          'Upper-intermediate low',
                                          'Custom', 'Casper'),
        # file's path
        'path_file_cv': "..\\resource\cv.docx",
        'path_file_photo': "..\\resource\photo.jpg"
        }
