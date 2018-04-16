*** Settings ***
Suite Setup       Open site
Test Setup        LogIn
Test Teardown     Close Browser
Library           Selenium2Library
Resource          students_resource.robot

*** Test Cases ***
test01_new_student
    [Documentation]    Log in as administrator, open top menu,select
    ...     \ \ \ \ \ \ button 'students' and select group."
    [Tags]    add student
    [Setup]
    Open Top Menu
    Click Groups Button
    Select Group
    Click Edit Students List Button
    Click Add New Student Button
    Enter Student data
    Click Save Data Changes Button
    Click Exit Students List Editor
    Check Is New Student Added
    [Teardown]

test02_del_student
    [Tags]    del student
    Open Top Menu
    Click Groups Button
    Select Group
    Click Edit Students List Button
    Deleting First Student

test03_adding_cv
    [Tags]    CV
    Open Top Menu
    Click Groups Button
    Select Group
    Click Edit Students List Button
    Click Add New Student Button
    Add CV File
    Page Should Contain    cv.docx    CV is not download.
