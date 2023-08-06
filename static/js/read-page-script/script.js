var i = 0;
function toogleDarkMode(){
icon = document.getElementById('darkMode');
    if(!i){
        icon.src = '../static/dark-mode.png';
        $('body').css({'background':'#161820'});
        $('.sec_').css({'background':'#151719','box-shadow':'0px 0px 5px #000'});
        $('.sec_logo').css('filter','contrast(0%)');
        $('.card').css({'background':'#151719'});
        $('pre').css({'color':'#ccc'});
        $('#copyright').css({'color':'#F4F4F4'});
        $('#publickey').css({'background':'#222222','color':'gray'})
        i++;
    }
    else{
        icon.src = '../static/light-mode.png';
        $('body').css({'background':'#F4F4F4'});
        $('.sec_').css({'background':'#fffffff8','box-shadow':'0px 0px 5px #ccc'});
        $('.sec_logo').css('filter','none')
        $('.card').css({'background':'#FFFFFF'});
        $('pre').css({'color':'#151719'});
        $('#copyright').css({'color':'#1B1B1B'});
        $('#publickey').css({'background':'#ffffff','color':'#000'})


        i = 0;
    }
}
//words count
var wc = document.getElementById('wordsCount');
var txa = document.getElementsByClassName('card-text')[0];
var count = txa.innerText.replace(/\s/g,"").length + '&nbspwords';
wc.innerHTML = count;
var textarea_count = document.getElementById('wordsCount_');
textarea_count.innerHTML = count;
var txa = document.getElementById('txtarea');
function countWords(){
textarea_count.innerHTML = txa.value.replace(/\s/g,"").length + '&nbspwords';
}
//text copy
var intr = setInterval(function(){ document.getElementById('copyButton').innerText = 'Copy'; }, 2000);
function copytext(){
var grab = document.getElementById('publickey');
var btn = document.getElementById('copyButton');
grab.select();
grab.setSelectionRange(0, 99999);
//navigator.clipboard.writeText(grab.value);
document.execCommand('copy')
btn.innerText='Copied!';
window.getSelection().removeAllRanges();
}

//confirmBox
function confirmAction(doThis,title,name){
    //$('.confMaster').css('display','block');
    $('#confirmTitle').html(title);
    if(name=='delete'){
        $('#fuckingDoIt').html('Delete');
    }
    else{
        $('#fuckingDoIt').html('Yes');
    }
    $('.confMaster').fadeIn('fast',function(){
        $('#fuckingDoIt').click(function(){window.location.href=doThis});
        $('.nope').click(function(){
            //$('.confMaster').css('display','none');
            $('.confMaster').fadeOut('fast');
        });

    });
}
//add new
$('#addNew').click(function(){
    var modal = document.getElementById('myModal');
    $('#myModal').css('display','block');
    //close Modal
    $('.close').click(function(){modal.style.display = 'none';});
    window.onclick = function(event) {
    if (event.target == modal) {
     $('#myModal').css('display','none');
    }
}
    //ends
});
//ends

//download pdf
function savePDF(){
var doc = new jsPDF();
doc.setFont('Sans Serif');
// doc.setCreationDate();
console.log(new Date().getDate())
var specialElementHandlers = {
    '.card': function (element, renderer) {
        return true;
    }
};
$('#arrow').replaceWith('<h6 class="card-title" id="arrow"></h6>')

    doc.fromHTML($('.card').html(), 10, 10, {
        'width': 150,
            'elementHandlers': specialElementHandlers
    });
    doc.save($('.card-title').text()+'.pdf');

$('#arrow').replaceWith('<h6 class="card-title" id="arrow">&rarr;</h6>')
};
//ends
///////Show time
function getSelectedText() {
    var selectedText = '';
    // window.getSelection
    if (window.getSelection) {
        selectedText = window.getSelection();
    }
    return selectedText
}
