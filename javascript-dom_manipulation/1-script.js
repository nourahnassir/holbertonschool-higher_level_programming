#!/usr/bin/node
const redHeader = document.querySelector('#red_header');
redHeader.addEventListener('click', function () {
  document.querySelector('header').style.color = '#FF0000';
});
