*** Settings ***
Documentation     Tests check the adding, removal and editing of student data, adding cv_files and photo in the list of students with \ role administrator also check the opportunity of adding new student with empty data and sorting student's list by name.
Suite Setup       Prepare for Tests
Suite Teardown    Close Browser
Test Teardown     Url for start next test    ${url_for_start_test}
Library           Selenium2Library
Library           Collections

*** Variables ***
${user}           qwerty
${password}       1234
${site_url}       http://localhost:3000/
${first_name}     Vladyslava
${last_name}      Semmi
${incoming_mark}    111
${entry_mark}     5
${new student}    Semmi Vladyslava Pre-intermediate 111 5 Not approved
${english level first new student}    Pre-intermediate
@{warnind`s list}    'You can use only letters, space and "-"'    'You can use only letters, space and "-"'    'You can use only letters, space and "-"'    'You can use only letters, space and "-"'    'You can use only letters, space and "-"'    'You can use only letters, space and "-"'
${cv_path}        ${CURDIR}\\cv.docx
${url_for_start_test}    http://localhost:3000/Students/Dnipro/DP-093-JS/list
${photo_path}     ${CURDIR}\\photo.jpg
@{data new student}    'Semmi Vladyslava'    'Pre-intermediate'    111    5

*** Test Cases ***
test01_new_student
    [Documentation]    Check adding new student by administrator.
    [Tags]    add student
    Click Edit Students List Button
    Click Add New Student Button
    Enter Student data
    Click Save Data Changes Button
    Click Exit Students List Editor
    Check Is New Student Added
    [Teardown]

test02_del_student
    [Documentation]    Check deleting first student from the student's list by administrator.
    [Tags]    del student
    Click Edit Students List Button
    ${First Student}    Get Text    css=#main-section > div > div > table > tbody:nth-child(2) > tr
    Deleting First Student
    Click Exit Students List Editor
    Page Should Not Contain    ${First Student}

test03_adding_cv
    [Documentation]    Check is cv file added to the student's data \ by administrator.
    [Tags]    CV
    Click Edit Students List Button
    Click Add New Student Button
    Add CV File
    Page Should Contain    cv.docx    CV is not download.

test04_add_student_empty_data
    [Documentation]    Check adding new student with empty fields by administrator
    [Tags]    empty data
    Click Edit Students List Button
    Click Add New Student Button
    Click Save Data Changes Button
    Wait Until Element Is Visible    css=.hint
    @{actual warnings}    Create List    css=.hint
    Page Should Contain Element    @{actual warnings}

test05_add_photo
    [Documentation]    Check is photo file added to the student's data \ by administrator.
    Click Edit Students List Button
    Click Add New Student Button
    Add Photo File
    Page Should Contain    photo.jpg    Photo is not download.

test06_adding_equal_students
    Click Edit Students List Button
    Click Add New Student Button
    Enter Student data
    Click Save Data Changes Button
    Click Add New Student Button
    Enter Student data
    Click Save Data Changes Button
    Element Should Be Enabled    xpath=//*[@id="modal-window"]//div[6]/button[1]

*** Keywords ***
LogIn
    Input Text    name=login    ${user}
    Input Password    name=password    ${password}
    Click Button    xpath=//div[2]/div/div/div/button
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    30    Element user image not found.

Select Group
    Wait Until Element Is Visible    css=.small-group-view    10
    @{Groups}    Get WebElements    css=.small-group-view
    Log Many    @{Groups}
    ${Group}    Get WebElement    css=.small-group-view
    : FOR    ${Group}    IN    @{Groups}
    \    ${GroupName}    Get Text    ${Group}
    \    Run Keyword If    '${GroupName}'=='DP-093-JS'    Click Element    ${Group}

Open Top Menu
    Click Element At Coordinates    id=top-menu    200    20
    Wait Until Element Is Enabled    css=div.itemMenu:nth-child(3)    5

Open site
    Open Browser    ${site_url}    chrome
    Maximize Browser Window

Click Groups Button
    Click Element    css=div.itemMenu:nth-child(3)

Click Edit Students List Button
    Wait Until Element Is Enabled    xpath=//*[@id="main-section"]/div/header/div[1]/button    5
    Click Button    xpath=//*[@id="main-section"]/div/header/div[1]/button

Click Add New Student Button
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]/section//button[1]    5
    Click Element    xpath=//*[@id="modal-window"]/section//button[1]

Enter Student data
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${first_name}
    Input Text    css=.lastName    ${last_name}
    Select From List By Label    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level first new student}
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}
    Comment    Select From List By Label

Click Save Data Changes Button
    Click Element    xpath=//*[@id="modal-window"]//div[6]/button[1]

Click Exit Students List Editor
    Wait Until Element Is Enabled    css=.exit    5
    Click Button    css=.exit

Check Is New Student Added
    Wait Until Element Is Visible    xpath=//*[@id="main-section"]/div/header/div[1]/button    5
    @{Students list}=    Create List
    @{Students}    Get WebElements    css=.tableBodyStudents
    ${Student}    Get WebElement    css=.tableBodyStudents
    : FOR    ${Student}    IN    @{Students}
    \    ${Student Data}=    Get Text    ${Student}
    \    Collections.Append To List    ${Students list}    ${Student Data}
    List Should Contain Value    ${Students list}    ${Student Data}

Deleting First Student
    Click Element    css=#modal-window > section > section > section > table > tbody > tr:nth-child(2) > td:nth-child(6) > i
    Comment    Confirm Action
    Click Element    css=#modal-window > div > div > div > div > button.btn.btn-delete > i

Add CV File
    Wait Until Element Is Enabled    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(1) > input    5
    Choose File    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(1) > input    ${cv_path}

Expected List
    [Arguments]    ${arg1}
    @{Warnings}    Get WebElements    class:hint
    ${Warning}    Get WebElement    class:hint
    : FOR    ${Warning}    IN    @{Warnings}
    \    Create List    Get Text    ${Warning}

Prepare for Tests
    Open site
    LogIn
    Open Top Menu
    Click Groups Button
    Select Group

Url for start next test
    [Arguments]    ${arg1}
    Go To    ${url_for_start_test}

Add Photo File
    Wait Until Element Is Enabled    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(2) > input    5
    Choose File    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(2) > input    ${photo_path}
