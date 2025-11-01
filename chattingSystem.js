import { getTalkSession } from 'https://cdn.jsdelivr.net/npm/@talkjs/core@1.5.8';
const appId = 'tJU4ulfD';

const userId = null;
const otherUserId = 'Nina';
const conversationId = 'my_conversation2';

const session = getTalkSession({
    // @ts-ignore
    host: 'durhack.talkjs.com',
    appId,
    userId,});

session.currentUser.createIfNotExists({ name: 'Frank' });
session.user(otherUserId).createIfNotExists({ name: 'Nina' });

const conversation = session.conversation(conversationId);
conversation.createIfNotExists();
conversation.participant(otherUserId).createIfNotExists();


function login(){
    username = document.getElementById("userName").value;
    console.log(username);
    document.getElementById("userForm").setAttribute("hidden","hidden");
    document.getElementById("chatDiv").removeAttribute("hidden");
    document.getElementById("chatBox").setAttribute("user-id","Frank"); // change to username in future

}


document.getElementById("submitUser").addEventListener('click',login);


