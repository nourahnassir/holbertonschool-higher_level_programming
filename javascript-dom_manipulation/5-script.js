#!/usr/bin/node
const updateHeader = document.querySelector('#update_header');
updateHeader.addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});
