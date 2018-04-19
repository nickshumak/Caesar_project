*** Settings ***
Library           Selenium2Library
Library           Collections

*** Variables ***
${user}           qwerty
${password}       1234
${site_url}       http://localhost:3000/
${new student}    Semmi Vladyslava Pre-intermediate 111 5 Not approved
@{warnind`s list}     You can use only letters, space and "-"      You can use only letters, space and "-"      You can use only letters, space and "-"      You can use only letters, space and "-"      You can use only letters, space and "-"      You can use only letters, space and "-"
${url_for_start_test}    http://localhost:3000/Students/Dnipro/DP-093-JS/list
${cv_path}        ${CURDIR}\\cv.docx
${photo_path}     ${CURDIR}\\photo.jpg
&{data first student}    first_name=Vladyslava    last_name=Semmi    incoming_mark=111    entry_mark=5    english_level_first_new_student=Pre-intermediate
&{data editing first student by admin}    first_name=Garry    last_name=Potter    incoming_mark=222    entry_mark=2    english_level=Upper-intermediate
${new_student_by_admin}    Semmi Vladyslava Pre-intermediate 111 5 Not approved
${editing_student_by_admin}    Potter Garry Upper-intermediate 222 2 Not approved

*** Keywords ***
Actual Warnings
    Wait Until Element Is Visible    css=.hint
    @{Actual warnings}=    Create List
    @{Warnings}    Get WebElements    css=.hint
    ${Warning}    Get WebElement    css=.hint
    : FOR    ${Warning}    IN    @{Warnings}
    \    ${Warning Data}    Get Text    ${Warning}
    \    Collections.Append To List    ${Actual warnings}    ${Warning Data}
    Return From Keyword    ${Actual warnings}

Add CV File
    Wait Until Element Is Enabled    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(1) > input    5
    Choose File    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(1) > input    ${cv_path}

Add Photo File
    Wait Until Element Is Enabled    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(2) > input    5
    Choose File    css=#modal-window > div > section > section > div:nth-child(5) > div:nth-child(2) > input    ${photo_path}

Check Is New Student Added
    Wait Until Element Is Visible    xpath=//*[@id="main-section"]/div/header/div[1]/button    5
    @{Students list}=    Create List
    @{Students}    Get WebElements    css=.tableBodyStudents
    ${Student}    Get WebElement    css=.tableBodyStudents
    : FOR    ${Student}    IN    @{Students}
    \    ${Student Data}=    Get Text    ${Student}
    \    Collections.Append To List    ${Students list}    ${Student Data}
    Return From Keyword    @{Students list}

Click Add New Student Button
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]/section//button[1]    5
    Click Element    xpath=//*[@id="modal-window"]/section//button[1]

Click Edit Students List Button
    Wait Until Element Is Enabled    xpath=//*[@id="main-section"]/div/header/div[1]/button    5
    Click Button    xpath=//*[@id="main-section"]/div/header/div[1]/button

Click Exit Students List Editor
    Wait Until Element Is Enabled    css=.exit    5
    Click Button    css=.exit

Click Groups Button
    Click Element    css=div.itemMenu:nth-child(3)

Click Save Data Changes Button
    Click Element    xpath=//*[@id="modal-window"]//div[6]/button[1]

Click Sort List By Name
    Click Element    css=#main-section > div > div > table > thead > tr > th.fullName

Deleting First Student
    Click Element    css=#modal-window > section > section > section > table > tbody > tr:nth-child(2) > td:nth-child(6) > i
    Click Element    css=#modal-window > div > div > div > div > button.btn.btn-delete > i

Enter Student data
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    ${first_student_first_name}=    Get From Dictionary    ${data first student}    first_name
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${first_student_first_name}
    ${first_student_last_name}=    Get From Dictionary    ${data first student}    last_name
    Input Text    css=.lastName    ${first_student_last_name}
    ${english level first new student}=    Get From Dictionary    ${data first student}    english_level_first_new_student
    Select From List By Value    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level first new student}
    ${incoming_mark}    Get From Dictionary    ${data first student}    incoming_mark
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    ${entry_mark}    Get From Dictionary    ${data first student}    entry_mark
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}
    Comment    Select From List By Label

Expected List
    [Arguments]    ${arg1}
    @{Warnings}    Get WebElements    class:hint
    ${Warning}    Get WebElement    class:hint
    : FOR    ${Warning}    IN    @{Warnings}
    \    Create List    Get Text    ${Warning}

LogIn
    Input Text    name=login    ${user}
    Input Password    name=password    ${password}
    Click Button    xpath=//div[2]/div/div/div/button
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    30    Element user image not found.

Open Top Menu
    Click Element At Coordinates    id=top-menu    200    20
    Wait Until Element Is Enabled    css=div.itemMenu:nth-child(3)    5

Open site
    Open Browser    ${site_url}    chrome
    Maximize Browser Window

Prepare for Tests
    Open site
    LogIn
    Open Top Menu
    Click Groups Button
    Select Group

Select Group
    Wait Until Element Is Visible    css=.small-group-view    10
    @{Groups}    Get WebElements    css=.small-group-view
    Log Many    @{Groups}
    ${Group}    Get WebElement    css=.small-group-view
    : FOR    ${Group}    IN    @{Groups}
    \    ${GroupName}    Get Text    ${Group}
    \    Run Keyword If    '${GroupName}'=='DP-093-JS'    Click Element    ${Group}

Students list
    Wait Until Element Is Visible    css=#main-section > div > div > table > thead > tr > th.fullName    5
    @{Students list1}=    Create List
    @{Students}    Get WebElements    css=.tableBodyStudents
    ${Student}    Get WebElement    css=.tableBodyStudents
    : FOR    ${Student}    IN    @{Students}
    \    ${Student Data}    Get Text    ${Student}
    \    Collections.Append To List    ${Students list1}    ${Student Data}
    Return From Keyword    @{Students list1}

Url for start next test
    [Arguments]    ${arg1}
    Go To    ${url_for_start_test}

Click Editing First Student
    Wait Until Element Is Enabled    css=#modal-window > section > section > section > table > tbody > tr:nth-child(1) > td:nth-child(5) > i    5
    Click Element    css=#modal-window > section > section > section > table > tbody > tr:nth-child(1) > td:nth-child(5) > i

Edit Student Data
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    ${first_student_first_name}=    Get From Dictionary    ${data editing first student by admin}    first_name
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${first_student_first_name}
    ${first_student_last_name}=    Get From Dictionary    ${data editing first student by admin}    last_name
    Clear Element Text    css=.lastName
    Input Text    css=.lastName    ${first_student_last_name}
    ${english level first new student}=    Get From Dictionary    ${data editing first student by admin}    english_level
    Select From List By Value    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level first new student}
    ${incoming_mark}    Get From Dictionary    ${data editing first student by admin}    incoming_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    ${entry_mark}    Get From Dictionary    ${data editing first student by admin}    entry_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}
