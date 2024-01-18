#!/usr/bin/node


; 'use strict';

const fetch = require('node-fetch');

function getCharacters(movieId) {
  const apiUrl = 'https://swapi.dev/api/';
  const movieUrl = `${apiUrl}films/${movieId}/`;

  // Fetch movie details
  fetch(movieUrl)
    .then(response => response.json())
    .then(movieData => {
      if (movieData.detail && movieData.detail === 'Not found') {
        console.log(`Movie with ID ${movieId} not found.`);
        process.exit(1);
      }

      // Extract character URLs from movie data
      const characterUrls = movieData.characters;

      // Fetch and print character names
      characterUrls.forEach(characterUrl => {
        fetch(characterUrl)
          .then(response => response.json())
          .then(characterData => {
            console.log(characterData.name);
          })
          .catch(error => console.error('Error fetching character:', error));
      });
    })
    .catch(error => console.error('Error fetching movie:', error));
}

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.log('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Ensure the provided Movie ID is a valid integer
if (isNaN(movieId) || !Number.isInteger(Number(movieId))) {
  console.log('Movie ID must be a valid integer.');
  process.exit(1);
}

getCharacters(movieId);
