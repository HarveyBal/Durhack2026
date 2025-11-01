//set up server
const express = require('express');
const app = express();
const port = 8080;


//set up talk session
import { getTalkSession } from 'https://cdn.jsdelivr.net/npm/@talkjs/core@1.5.8';

const appId = 'tJU4ulfD';

const userId = 'Server';
const otherUserId = 'User';
const conversationId = 'globalConv';

const session = getTalkSession({
    // @ts-ignore
    host: 'durhack.talkjs.com',
    appId,
    userId,
});

session.currentUser.createIfNotExists({ name: 'Server' });
session.user(otherUserId).createIfNotExists({ name: 'Me' });

const conversation = session.conversation(conversationId);
conversation.createIfNotExists();
conversation.participant(otherUserId).createIfNotExists();
//listen for input


// Define a route for GET requests to the root URL
app.get('/send', (req, res) => {
  let { username, message } = req.query;
  conversation.send(username+": "+message);
});

// Start the server
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
}); 


