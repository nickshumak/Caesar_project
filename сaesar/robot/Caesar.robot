*** Settings ***
Documentation     Tests check the adding, removal and editing of student data, adding cv_files and photo in the list of students with \ role administrator also check the opportunity of adding new student with empty data and sorting student's list by name.
Suite Setup       Prepare for Tests
Suite Teardown    Close Browser
Test Teardown     Url for start next test    ${url_for_start_test}
Library           Selenium2Library

*** Variables ***
${user}           qwerty
${password}       1234
${site_url}       http://localhost:3000/
${first_name}     Vladyslava
${last_name}      Semmi
${incoming_mark}    111
${entry_mark}     5
${new student}    Semmi Vladyslava
${english level first new student}    Pre-intermediate
@{warnind`s list}    ['You can use only letters, space and "-"',    'You can use only letters, space and "-"', 'You can use only letters, space and "-"', 'You can use only letters, space and "-"', 'You can use only letters, space and "-"', 'You can use only letters, space and "-"']
${cv_path}        C:\\Python27\\cv.docx
${url_for_start_test}    http://localhost:3000/Students/Dnipro/DP-093-JS/list
${photo_path}     C:\\Python27\\photo.jpg

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
    Deleting First Student

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
    Should Be Equal    Expected List    @{warnind`s list}

test05_add_photo
    [Documentation]    Check is photo file added to the student's data \ by administrator.
    Click Edit Students List Button
    Click Add New Student Button
    Add Photo File
    Page Should Contain    photo.jpg    Photo is not download.

*** Keywords ***
LogIn
    Input Text    name=login    ${user}
    Input Password    name=password    ${password}
    Click Button    xpath=//div[2]/div/div/div/button
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    30    Element user image not found.

Select Group
    @{Groups}    Get WebElements    class:small-group-view
    Log Many    @{Groups}
    ${Group}    Get WebElement    class:small-group-view
    : FOR    ${Group}    IN    @{Groups}
    \    ${GroupName}    Get Text    ${Group}
    \    Log    ${GroupName}
    \    Run Keyword If    '${GroupName}'=='DP-093-JS'    Click Element    ${Group}

Open Top Menu
    Click Element At Coordinates    id=top-menu    200    20
    Wait Until Element Is Enabled    css=div.itemMenu:nth-child(3)     5

Open site
    Open Browser    ${site_url}    chrome
    Maximize Browser Window

Click Groups Button
    Click Element    css=div.itemMenu:nth-child(3)

Click Edit Students List Button
    Click Element    xpath://*[@id="main-section"]/div/header/div[1]/button

Click Add New Student Button
    Click Element    xpath://*[@id="modal-window"]/section//button[1]

Enter Student data
    Input Text    xpath://*[@id="modal-window"]//div[2]/div[1]/input    ${first_name}
    Input Text    xpath://*[@id="modal-window"]//div[3]/div[1]/input    ${last_name}
    Select From List By Label    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level first new student}
    Input Text    xpath://*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    Input Text    xpath://*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}

Click Save Data Changes Button
    Click Element    xpath://*[@id="modal-window"]//div[6]/button[1]

Click Exit Students List Editor
    Click Element    class:exit

Check Is New Student Added
    Page Should Contain    ${new student}    New student is not added

Deleting First Student
    Click Element    xpath://*[@id="modal-window"]//td[6]/i
    Confirm Action

Add CV File
    Choose File    xpath://*[@id="modal-window"]/div/section/section/div[5]/div[1]/input    ${cv_path}

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
    Choose File    xpath://*[@id="modal-window"]/div/section/section/div[5]/div[2]/input    ${photo_path}
