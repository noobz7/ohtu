*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123154231
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kalle  pete5143652654
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  \  kalle123154231
    Output Should Contain  Username and password are required

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123154231
    Input Login Command
