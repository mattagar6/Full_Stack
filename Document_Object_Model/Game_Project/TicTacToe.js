var allCells = document.querySelectorAll('.cell');

function changeMarker(){
  // 'this' is referring to the current element of allCells
  if (this.textContent === 'X') {
    this.textContent = 'O';
  } else if (this.textContent === 'O') {
    this.textContent = '';
  } else {
    this.textContent = 'X';
  }
}

for (var i = 0; i < allCells.length; i++) {
  allCells[i].addEventListener('click', changeMarker);
}
