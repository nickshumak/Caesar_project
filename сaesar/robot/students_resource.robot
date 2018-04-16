*** Settings ***
Library           Selenium2Library

*** Variables ***
${user}           qwerty
${password}       1234
${site_url}       http://localhost:3000/
${first_name}     Vladyslava
${last_name}      Semmi
${incoming_mark}    111
${entry_mark}     5
${new student}     Semmi Vladyslava \
${english level first new student}    Pre-intermediate

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

Open site
    Open Browser    ${site_url}    chrome
    Maximize Browser Window

Click Groups Button
    Click Element    css:div.itemMenu:nth-child(3)

Click Edit Students List Button
    Click Element    xpath://*[@id="main-section"]/div/header/div[1]/button

Click Add New Student Button
    Click Element    xpath://*[@id="modal-window"]/section//button[1]

Enter Student data
    Input Text    xpath://*[@id="modal-window"]//div[2]/div[1]/input     ${first_name}
    Input Text    xpath://*[@id="modal-window"]//div[3]/div[1]/input     ${last_name}
    Click Element    xpath://*[@id="modal-window"]//div[4]/div[1]/select
    Select From List By Value    value:${english level first new student}    ${english level first new student}
    Input Text    xpath://*[@id="modal-window"]//div[1]/div[2]/input     ${incoming_mark}
    Input Text    xpath://*[@id="modal-window"]//div[2]/div[2]/input     ${entry_mark}

Click Save Data Changes Button
    Click Element    xpath://*[@id="modal-window"]//div[6]/button[1]

Click Exit Students List Editor
    Click Element    class:exit

Check Is New Student Added
    Page Should Contain    ${new student}    New student is not added

Deleting First Student
    Click Element    xpath://*[@id="modal-window"]//td[6]/i
    Click Element    xpath://*[@id="modal-window"]//button[1]

Add CV File
    Click Element    xpath://*[@id="modal-window"]//div[5]/div[1]/button
    Input Text    xpath://*[@id="modal-window"]//div[5]/div[1]/input     cv.docx

