Meteor.methods({
  getTexts: function() {
    // Twilio Credentials
    var accountSid = 'AC9f63ad6090b364bab2d4f1c49781db4a';
    var authToken = 'fd2aca32615d79b6b0fbfe8f63aaa347';
    var twilio = Twilio(accountSid, authToken);

    var twilioMessagesListSync = Meteor.wrapAsync(twilio.messages.list, twilio.messages);

    var result = twilioMessagesListSync(
      function (err, data) {
        var texts = [];
        data.messages.forEach(function (message) {
          var text = {
            to: message.to,
            from: message.from,
            body: message.body,
            dateSent: message.date_sent,
            status: message.status,
            direction: message.direction
          };
          texts.push(text);
          Texts.insert(text);
        })
      }
    );
	return texts;
  }
});