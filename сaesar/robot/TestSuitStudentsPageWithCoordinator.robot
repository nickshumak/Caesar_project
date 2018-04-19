*** Settings ***
Documentation     Tests check the adding, removal and editing of student data, adding cv_files and photo in the list of students with role coordinator.
Suite Setup       Prepare for Tests
Suite Teardown    Close Browser
Test Teardown     Url for start next test    ${url_for_start_test}
Library           Selenium2Library
Library           Collections
Resource          Resource/students_page_resource.robot

*** Test Cases ***
test01_new_student
    [Documentation]    Check adding new student by administrator.
    [Tags]    add student
    Click Edit Students List Button
    Click Add New Student Button
    Enter Student data
    Click Save Data Changes Button
    Click Exit Students List Editor
    @{Students list}=    Students list
    List Should Contain Value    ${Students list}    ${new_student_by_admin}    New student is not added.
    [Teardown]

test02_del_student
    [Documentation]    Check deleting first student from the student's list by administrator.
    [Tags]    del student
    Click Edit Students List Button
    ${First Student}    Get Text    css=#main-section > div > div > table > tbody:nth-child(2) > tr
    Deleting First Student
    Click Exit Students List Editor
    Page Should Not Contain    ${First Student}    First Student is not deleted.

test03_adding_cv
    [Documentation]    Check is cv file added to the student's data \ by administrator.
    [Tags]    CV
    Click Edit Students List Button
    Click Add New Student Button
    Add CV File
    Page Should Contain    cv.docx    CV is not download.

test04_add_photo
    [Documentation]    Check is photo file added to the student's data \ by administrator.
    Click Edit Students List Button
    Click Add New Student Button
    Add Photo File
    Page Should Contain    photo.jpg    Photo is not download.

test05_editing_first_student
    [Documentation]    Check is first student editing by administrator.
    Click Edit Students List Button
    Click Editing First Student
    Edit Student Data
    Click Save Data Changes Button
    Click Exit Students List Editor
    @{Students list}=    Students list
    List Should Contain Value    ${Students list}    ${editing_student_by_admin}    Student is not edited.