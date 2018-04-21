*** Settings ***
Documentation     Tests check the adding, removal and editing of student data, adding cv_files and photo in the list of students with \ role administrator also check the opportunity of adding new student with empty data and sorting student's list by name.
Suite Setup       Prepare for Tests by Administrator
Suite Teardown    Close Browser
Test Teardown     Url for start next test    ${url_for_start_test}
Library           Selenium2Library
Library           Collections
Resource          Resource/students_page_resource.robot

*** Test Cases ***
test01_sort_students_list
    [Documentation]    Check with role administrator is student's list sorting by name.
    @{Students list}=    Students list
    Remove Values From List    ${Students list}    ${None}
    Sort List    ${Students list}
    Click Sort List By Name
    @{Students list sorted by button}=    Students list
    Lists Should Be Equal    ${Students list}    ${Students list sorted by button}    Lists are not equal.

test02_new_student
    [Documentation]    Check adding new student by administrator.
    [Tags]    add student
    Click Edit Students List Button
    Click Add New Student Button
    Enter Student Data With Administrator
    Click Save Data Changes Button
    Click Exit Students List Editor
    @{Students list}=    Students list
    List Should Contain Value    ${Students list}    ${new_student_by_admin}    New student is not added.
    [Teardown]

test03_del_student
    [Documentation]    Check deleting first student from the student's list by administrator.
    [Tags]    del student
    Click Edit Students List Button
    ${First Student}    Get Text    css=#main-section > div > div > table > tbody:nth-child(2) > tr
    Deleting First Student
    Click Exit Students List Editor
    Page Should Not Contain    ${First Student}    First Student is not deleted.

test04_adding_cv
    [Documentation]    Check is cv file added to the student's data \ by administrator.
    [Tags]    CV
    Click Edit Students List Button
    Click Add New Student Button
    Add CV File
    Page Should Contain    cv.docx    CV is not download.

test05_add_photo
    [Documentation]    Check is photo file added to the student's data \ by administrator.
    Click Edit Students List Button
    Click Add New Student Button
    Add Photo File
    Page Should Contain    photo.jpg    Photo is not download.

test06_add_student_empty_data
    [Documentation]    Check adding new student with empty fields by administrator
    [Tags]    empty data
    Click Edit Students List Button
    Click Add New Student Button
    Click Save Data Changes Button
    @{actual warnings}=    Actual Warnings
    Lists Should Be Equal    ${warnind`s list}    ${actual warnings}    Warnings are not visible.

test07_adding_equal_students
    [Documentation]    Check opportunity of adding two equal students by administrator.
    Click Edit Students List Button
    Click Add New Student Button
    Enter Student Data With Administrator
    Click Save Data Changes Button
    Click Add New Student Button
    Enter Student Data With Administrator
    Click Save Data Changes Button
    Element Should Be Enabled    xpath=//*[@id="modal-window"]//div[6]/button[1]

test08_editing_first_student
    [Documentation]    Check is first student editing by administrator.
    Click Edit Students List Button
    Click Editing First Student
    Edit Student Data With Administrator
    Click Save Data Changes Button
    Click Exit Students List Editor
    @{Students list}=    Students list
    List Should Contain Value    ${Students list}    ${editing_student_by_admin}    Student is not edited.
