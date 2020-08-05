# AWS-Twitch-Guesser
AWS Lambda function that connects to Twitch IRC and sends a list of users who answered the question correctly.

## Req:
- configured AWS API Gateway

## Parameters of POST request for API Gateway:
- `channel` - Channel for chat listening
- `word` - The hidden word
- `num_of_winners` - Maximum number of winners
