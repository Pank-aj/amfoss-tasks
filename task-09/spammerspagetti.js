var timer=setInterval(
function(){
    document.getElementsByClassName('composer_rich_textarea')[0].innerHTML="hi";
    $('.im_submit').trigger('mousedown');
clearInterval(timer);
} , 1000 ) ;
