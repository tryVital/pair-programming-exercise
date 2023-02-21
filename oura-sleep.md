# Oura sleep processing library


## Introduction

Sleep trackers can occasionally incorrectly generate multiple sleep entries for many reasons
This can be either bad fit, the device slipping, the user of the device sleep walking, etc.

This library aims to apply some additional processing to the user's data to mittigate these issues.

### Requirements

- Develop a "reasonable" way of merging sleep objects that is efficient and has minimal impact when
the data is already "reasonable". You are to define what reasonable means in the context of this application.

- Merged sleeps must have way of combining sleep metrics in a numerically justified way.

- The stub code in `./oura_sleep.py` is specific to oura data. [See API docs](https://cloud.ouraring.com/v2/docs#operation/Multiple_daily_sleep_Documents_v2_usercollection_daily_sleep_get)
  As we aim to use the same processing functionality across all providers, the solution should be extendible to other types
  of sleep data like [fitbit](https://dev.fitbit.com/build/reference/web-api/sleep/get-sleep-log-by-date-range/)

- You are free to write any tests that proove that your implementation does what you expect.
