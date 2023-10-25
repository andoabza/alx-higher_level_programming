#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request(apiUrl, (error, response, body) => {
  if (error) throw (error);

  const todos = JSON.parse(body);
  const users = {};

  todos.forEach(todo => {
    const userId = todo.userId;
    const completed = todo.completed;

    if (!users[userId]) {
      users[userId] = {
        count: 0
      };
    }

    if (completed) {
      users[userId].count++;
    }
  });

  Object.keys(users).forEach(userId => {
    const count = users[userId].count;
    console.log(`'${userId}' :${count},`);
  });
});
