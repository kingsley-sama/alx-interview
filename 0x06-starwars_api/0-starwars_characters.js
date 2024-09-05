#!/usr/bin/env node
const request = require('request');
request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (error, response, body) => {
  if (error) return error;
  if (response.statusCode === 200) {
    const nameLinks = JSON.parse(body).characters;
    getName(0, nameLinks);
  }
});
const getName = (id, nameArray) => {
  if (id === nameArray.length) return;
  request(nameArray[id], (error, response, body) => {
    if (error) return error;
    if (response.statusCode === 200) console.log(JSON.parse(body).name);
    getName(id + 1, nameArray);
  });
};
