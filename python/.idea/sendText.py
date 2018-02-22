from twilio import rest

account_sid = ""
auth_token = ""
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body ="hello",
    to = "+7034032732",
    from_ = "+14158141829"
)
print message.sid