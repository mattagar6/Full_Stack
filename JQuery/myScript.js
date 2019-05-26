// google: 'jQuery events' for a long list of event listeners

$('h1').click(function(){
  console.log('There was a click');
});

// changes the color of an html element to red
// 'this' refers to whatever html element you are calling the function on
function changeColor(){
  $(this).css('color','red');
}

// apply the function 'changeColor' to each li tag upon a click
$('li').click(changeColor);

$('input').eq(0).keypress(function(){
  $('h3').toggleClass('turnRed');
});

// .on() method -> like 'addEventListener' in vanilla JS
$('li').on('dblclick',function(){
  $(this).toggleClass('turnBlue');
});

// animations in jQuery
$('input').eq(1).on('click',function(){
  $('body').fadeOut(3000);
})
