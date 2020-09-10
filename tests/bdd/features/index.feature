Feature: Home

Home Page

Scenario: default home
Given the window
Then the first item is "Motorola XOOM™ with Wi-Fi"

Scenario: sort by name
Given the window
When the user sorts alphabetically
Then the first item is "Dell Streak 7"

Scenario: search
Given the window
When the user searches "Sa"
Then the first item is "Samsung Gem™"
