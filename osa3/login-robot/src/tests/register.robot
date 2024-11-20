*** Settings ***
Resource  resource.robot
Test Setup  Input Newacc Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pete  erareika123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  pete  paskelli123
    Input Credentials  pete  erareika32
    Output Should Contain  User with username pete already exists

Register With Too Short Username And Valid Password
    Input Credentials  pe  erareika123
    Output Should Contain  New username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  pete147126973  erareika123
    Output Should Contain  New username must only use chars a-z

Register With Valid Username And Too Short Password
    Input Credentials  pete  era11
    Output Should Contain  New password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  pete  erafjoasfjojdv
    Output Should Contain  New password must also contain numbers
