*** Settings ***
Documentation     Robot Framework test suite for Respa Admin UI using Selenium Webdriver.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://respa.koe.hel.ninja/ra
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    xxx
    Input Password    xxx
    Submit Credentials
    Resource Page Should Be Open

Create New Resource
    Open Resource Page
    Open New Resource Page
    Activate Finnish Language
    Activate Swedish Language
    Input Resource Name In Finnish
    Input Resource Name in English
    [Teardown]    Close Browser

*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Respa Admin - Log in

Input Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password    ${password}

Submit Credentials
    Submit Form    

Resource Page Should Be Open
    Title Should Be    Respa Admin - 

Open Resource Page
    Click Link    Resources

Open New Resource Page
    Click Link    partial link:Add a new resource

Activate Finnish Language
    Click Element    language-fi

Activate Swedish Language
    Click Element    language-sv

Input Resource Name In Finnish
    Input Text    id_name_fi    testresource

Input Resource Name in English
    Input Text    id_name_en    testresource
