*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***
Get Posts
    Create Session    json    ${BASE_URL}
    ${response}=      Get Request    json    /posts
    Should Be Equal As Integers    ${response.status_code}    200
    ${first_post}=    To JSON    ${response.content}
    Log To Console    ${first_post[0]['title']}
