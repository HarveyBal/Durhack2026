//set up talk session

//set up server
const express = require('express');
const app = express();
const port = 8080;


//listen for input


// Define a route for GET requests to the root URL
app.get('/send', (req, res) => {
  let { username, message } = req.query;
  console.log(username +":"+ message);
    return fetch(
    `https://api-durhack.talkjs.com/v1/tJU4ulfD/conversations/globalConv/messages`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer sk_test_NFYeWRuqB7dgHwEv382IbOJMdQUjj1RE`,
      },
      body: JSON.stringify([
        {
          text: username+": "+message,
          sender: "Server",
          type: "UserMessage",
        },
      ]),
    }
  );
});

// Start the server
app.listen(port, () => {

  console.log(`Example app listening at http://localhost:${port}`);
}); 


