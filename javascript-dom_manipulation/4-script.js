#!/usr/bin/node
const addItem = document.querySelector('#add_item');
addItem.addEventListener('click', function () {
  const newList = document.createElement('li');
  newList.textContent = 'Item';
  document.querySelector('.my_list').appendChild(newList);
});
