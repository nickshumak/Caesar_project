*** Settings ***
Library           Selenium2Library
Library           Collections

*** Variables ***
${user}           qwerty
${password}       1234
${site_url}       http://localhost:3000/
${new student}    Semmi Vladyslava Pre-intermediate 111 5 Not approved
@{warnind`s list}    You can use only letters, space and "-"    You can use only letters, space and "-"    You can use only letters, space and "-"    You can use only letters, space and "-"    You can use only letters, space and "-"    You can use only letters, space and "-"
${url_for_start_test}    http://localhost:3000/Students/Dnipro/DP-093-JS/list
${cv_path}        ${CURDIR}\\cv.docx
${photo_path}     ${CURDIR}\\photo.jpg
&{data first student}    first_name=Vladyslava    last_name=Semmi    incoming_mark=111    entry_mark=5    english_level_first_new_student=Pre-intermediate
&{data second student}    first_name=Sherlock    last_name=Holmes    incoming_mark=333    entry_mark=3    english_level=Pre-intermediate strong
&{data third student}    first_name=Merlin    last_name=Monro    incoming_mark=123    entry_mark=3    english_level_third_new_student=Elementary
&{data editing first student by admin}    first_name=Garry    last_name=Potter    incoming_mark=222    entry_mark=2    english_level=Upper-intermediate
&{data editing first student by coordinator}    first_name=Robin    last_name=Good    incoming_mark=444    entry_mark=4    english_level=Advanced
&{data editing first student by teacher}    first_name=Clark    last_name=Kent    incoming_mark=321    entry_mark=3    english_level=Upper-intermediate low
${new_student_by_admin}    Semmi Vladyslava Pre-intermediate 111 5 Not approved
${new_student_by_coordinator}    Holmes Sherlock Pre-intermediate strong 333 3 Not approved
${new_student_by_teacher}    Monro Merlin Elementary 123 3 Not approved
${editing_student_by_admin}    Potter Garry Upper-intermediate 222 2 Not approved
${editing_student_by_coordinator}    Good Robin Advanced 444 4 Not approved
${editing_student_by_teacher}    Kent Clark Upper-intermediate low 321 3 Not approved
&{users}          first_admin=qwerty    coordinator=dmytro    teacher=sasha

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

Click Editing First Student
    Wait Until Element Is Enabled    css=#modal-window > section > section > section > table > tbody > tr:nth-child(1) > td:nth-child(5) > i    5
    Click Element    css=#modal-window > section > section > section > table > tbody > tr:nth-child(1) > td:nth-child(5) > i

Click Exit Students List Editor
    Wait Until Element Is Enabled    css=.exit    5
    Click Button    css=.exit

Click Groups Button
    Click Element    css=div.itemMenu:nth-child(3)

Click Save Data Changes Button
    Click Element    xpath=//*[@id="modal-window"]//div[6]/button[1]

Click Sort List By Name
    Click Element    css=#main-section > div > div > table > thead > tr > th.fullName

Click Students Button
    Wait Until Element Is Enabled    xpath=.//*[@id="main-section"]/div/header/div[2]/button[2]
    Click Button    xpath=.//*[@id="main-section"]/div/header/div[2]/button[2]

Deleting First Student
    Click Element    css=#modal-window > section > section > section > table > tbody > tr:nth-child(2) > td:nth-child(6) > i
    Click Element    css=#modal-window > div > div > div > div > button.btn.btn-delete > i

Edit Student Data With Administrator
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

Edit Student Data With Coordinator
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    ${second_student_first_name}=    Get From Dictionary    ${data editing first student by coordinator}    first_name
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${second_student_first_name}
    ${second_student_last_name}=    Get From Dictionary    ${data editing first student by coordinator}    last_name
    Clear Element Text    css=.lastName
    Input Text    css=.lastName    ${second_student_last_name}
    ${english level student}=    Get From Dictionary    ${data editing first student by coordinator}    english_level
    Select From List By Value    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level student}
    ${incoming_mark}    Get From Dictionary    ${data editing first student by coordinator}    incoming_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    ${entry_mark}    Get From Dictionary    ${data editing first student by coordinator}    entry_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}

Edit Student Data With Teacher
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    ${third_student_first_name}=    Get From Dictionary    ${data editing first student by teacher}    first_name
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${third_student_first_name}
    ${third_student_last_name}=    Get From Dictionary    ${data editing first student by teacher}    last_name
    Clear Element Text    css=.lastName
    Input Text    css=.lastName    ${third_student_last_name}
    ${english level third new student}=    Get From Dictionary    ${data editing first student by teacher}    english_level
    Select From List By Value    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level third new student}
    ${incoming_mark}    Get From Dictionary    ${data editing first student by teacher}    incoming_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    ${entry_mark}    Get From Dictionary    ${data editing first student by teacher}    entry_mark
    Clear Element Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}

Enter Student Data With Administrator
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

Enter Student Data With Teacher
    Wait Until Element Is Enabled    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    5
    ${second_student_first_name}=    Get From Dictionary    ${data third student}    first_name
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[1]/input    ${second_student_first_name}
    ${second_student_last_name}=    Get From Dictionary    ${data third student}    last_name
    Input Text    css=.lastName    ${second_student_last_name}
    ${english level student}=    Get From Dictionary    ${data third student}    english_level_third_new_student
    Select From List By Value    css=#modal-window > div > section > section > div:nth-child(4) > div:nth-child(1) > select    ${english level student}
    ${incoming_mark}    Get From Dictionary    ${data third student}    incoming_mark
    Input Text    xpath=//*[@id="modal-window"]//div[1]/div[2]/input    ${incoming_mark}
    ${entry_mark}    Get From Dictionary    ${data third student}    entry_mark
    Input Text    xpath=//*[@id="modal-window"]//div[2]/div[2]/input    ${entry_mark}

Expected List
    [Arguments]    ${arg1}
    @{Warnings}    Get WebElements    class:hint
    ${Warning}    Get WebElement    class:hint
    : FOR    ${Warning}    IN    @{Warnings}
    \    Create List    Get Text    ${Warning}

LogIn by Administrator
    ${admin}    Get From Dictionary    ${users}    first_admin
    Input Text    name=login    ${admin}
    Input Password    name=password    ${password}
    Click Button    xpath=//div[2]/div/div/div/button
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    30    Element user image not found.

LogIn by Coordinator
    ${admin}    Get From Dictionary    ${users}    coordinator
    Input Text    name=login    ${admin}
    Input Password    name=password    ${password}
    Click Button    xpath=//div[2]/div/div/div/button
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    30    Element user image not found.

LogIn by Teacher
    ${admin}    Get From Dictionary    ${users}    teacher
    Input Text    name=login    ${admin}
    Input Password    name=password    ${password}
    Click Button    xpath=//div[2]/div/div/div/button
    Wait Until Element Is Visible    xpath=//*[@id="icon"]/div/img    30    Element user image not found.

Open Top Menu
    Click Element At Coordinates    id=top-menu    200    20
    Wait Until Element Is Enabled    css=div.itemMenu:nth-child(3)    5

Open site
    Open Browser    ${site_url}    chrome
    Maximize Browser Window

Prepare for Tests by Administrator
    Open site
    LogIn by Administrator
    Open Top Menu
    Click Groups Button
    Select Group

Prepare for Tests by Coordanator
    Open site
    LogIn by Coordinator
    Open Top Menu
    Click Groups Button
    Select Group

Prepare for Tests by Teacher
    Open site
    LogIn by Teacher
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
