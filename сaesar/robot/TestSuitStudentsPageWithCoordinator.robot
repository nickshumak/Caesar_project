*** Settings ***
Documentation     Tests check the adding, removal and editing of student data, adding cv_files and photo in the list of students with role coordinator.
Suite Setup       Prepare for Tests by Coordanator
Suite Teardown    Close Browser
Test Teardown     Url for start next test    ${url_for_start_test}
Library           Selenium2Library
Library           Collections
Resource          Resource/students_page_resource.robot

*** Test Cases ***
test01_new_student
    [Documentation]    Check adding new student by coordinator.
    [Tags]    add student
    Click Edit Students List Button
    Click Add New Student Button
    Enter Student Data With Coordinator
    Click Save Data Changes Button
    Click Exit Students List Editor
    @{Students list}=    Students list
    List Should Contain Value    ${Students list}    ${new_student_by_coordinator}    New student is not added.

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
    Edit Student Data With Administrator
    Click Save Data Changes Button
    Click Exit Students List Editor
    @{Students list}=    Students list
    List Should Contain Value    ${Students list}    ${editing_student_by_admin}    Student is not edited.

*** Keywords ***
Enter Student Data With Coordinator
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    ${first_student_first_name}=    Get From Dictionary    ${data second student}    first_name
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${first_student_first_name}
    ${first_student_last_name}=    Get From Dictionary    ${data second student}    last_name
    Input Text    css=.lastName    ${first_student_last_name}
    ${english level first new student}=    Get From Dictionary    ${data second student}    english_level
    Select From List By Value    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level first new student}
    ${incoming_mark}    Get From Dictionary    ${data second student}    incoming_mark
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    ${entry_mark}    Get From Dictionary    ${data second student}    entry_mark
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}
    Comment    Select From List By Label

Edit Student Data With Coordinator
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    ${second_student_first_name}=    Get From Dictionary    ${data editing first student by coordinator}    first_name
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${second_student_first_name}
    ${second_student_last_name}=    Get From Dictionary    ${data editing first student by coordinator}    last_name
    Clear Element Text    css=.lastName
    Input Text    css=.lastName    ${second_student_last_name}
    ${english level second new student}=    Get From Dictionary    ${data editing first student by coordinator}    english_level
    Select From List By Value    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level first new student}
    ${incoming_mark}    Get From Dictionary    ${data editing first student by coordinator}    incoming_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    ${entry_mark}    Get From Dictionary    ${data editing first student by coordinator}    entry_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}
