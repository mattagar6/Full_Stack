var headerOne = document.querySelector('#one');
var headerTwo = document.querySelector('#two');
var headerThree = document.querySelector('#three');

headerOne.addEventListener('mouseover', function(){
  headerOne.textContent = "I've been Hovered on";
  headerOne.style.color = 'red';
})

headerOne.addEventListener('mouseout', function(){
  headerOne.textContent = 'HOVER OVER ME';
  headerOne.style.color = 'black';
})

headerTwo.addEventListener('click', function(){
  headerTwo.textContent = 'Clicked On';
  headerTwo.style.color = 'blue';
})

headerThree.addEventListener('dblclick', function(){
  headerThree.textContent = 'Double Clicked On';
  headerThree.style.color = 'green';
})
