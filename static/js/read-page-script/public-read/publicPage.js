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
        $('.hybrid_text').css({'color':'#f8f8f8'});
        $('#copyright').css({'color':'#F4F4F4'});
        i++;
    }
    else{
        icon.src = '../static/light-mode.png';
        $('body').css({'background':'#F4F4F4'});
        $('.sec_').css({'background':'#fffffff8','box-shadow':'0px 0px 5px #ccc'});
        $('.sec_logo').css('filter','none');
        $('.card').css({'background':'#FFFFFF'});
        $('pre').css({'color':'#151719'});
        $('.hybrid_text').css({'color':'#444444'});
        $('#copyright').css({'color':'#1B1B1B'});
        i = 0;
    }
}


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

    doc.fromHTML($('.card-body').html(), 10, 10, {
        'width': 150,
            'elementHandlers': specialElementHandlers
    });
    doc.save($('.card-title').text()+'.pdf');

$('#arrow').replaceWith('<h6 class="card-title" id="arrow">&rarr;</h6>')
};
//ends

function saveNote(){
    $('.save_note').click(()=>{

    });
}
// add new
$('#addNew').click(function(){
    var modal = document.getElementById('myModal');
    $('#myModal').css('display','block');
    var wc = document.getElementById('wordsCount');
var txa = document.getElementsByClassName('card-text')[0];
wc.innerHTML = txa.innerText.replace(/\s/g,"").length + '&nbspwords';
    //close Modal
    $('.close').click(function(){modal.style.display = 'none';});
    window.onclick = function(event) {
    if (event.target == modal) {
     $('#myModal').css('display','none');
    }
}
    //ends
});
// ends
// count
var wc = document.getElementById('wordsCount');
var txa = document.getElementsByClassName('card-text')[0];
var count = txa.innerText.replace(/\s/g,"").length + '&nbspwords';
wc.innerHTML = count;
var textarea_count = document.getElementById('wordsCount_');
textarea_count.innerHTML = count;
var txa = document.getElementById('txtarea');
function countWords(){
counted = txa.value.replace(/\s/g,"").length + '&nbspwords';
textarea_count = counted;
}
// ends
