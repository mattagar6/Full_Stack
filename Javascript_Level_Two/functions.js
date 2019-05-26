function hello(name = 'matt'){
  console.log('hello ' + name);
}

function addNum(num1, num2) {
  return num1 + num2;
}

//scope in JS
var v = 'GLOBAL V';
var stuff = 'GLOBAL STUFF';

function fun(stuff) {
    console.log(v);
    //stuff is only reassigned at a local level
    stuff = 'Reassign stuff inside function';
    console.log(stuff);
}

fun(stuff);

console.log(stuff);
