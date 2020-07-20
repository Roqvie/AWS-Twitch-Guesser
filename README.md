# AWS-Twitch-Guessor
AWS Lambda function that connects to Twitch IRC and sends a list of users who answered the question correctly.

## Req:
- configured AWS API Gateway

## Parameetrs of POST request:
- `token` - OAuth Twitch token of account
- `username` - Username of account
- `channel` - Channel for chat listening
- `word` - The hidden word
- `num_of_winners` - Maximum number of winners
