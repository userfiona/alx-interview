#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
request(url + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printInOrder(characters);
  }
}
);

async function printInOrder (characters) {
  for (const character of characters) {
    await new Promise((resolve, reject) => {
      request(character, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          console.log(JSON.parse(body).name);
          resolve();
        }
      });
    });
  }
}
