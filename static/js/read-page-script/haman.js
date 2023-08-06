function fontSize(pix){
    $('#Fontsize,#Fontsize').html('Font: '+pix+'px');
}
alignTo = 'left';
function setAlign(position){
    alignTo = position;
    highlight = ['left','right','center'];
    highlight.forEach(element=>{
        if(element == position){
            $(`#${element}AlignImage`).css('border','1px solid #4caf50');
        }
        else{
            $(`#${element}AlignImage`).css('border','1px solid #ccc');
        }
    })
}
//menu
var drop = 0;
function hamMenu(){
    if(drop==0){
    $('.menu-frame').slideDown('fast');
    drop = 1;
}
else{
    $('.menu-frame').slideUp('fast');
    drop = 0;
}
}
var textAlign = 'left';
function applyFilters(){
    if (drop==1){
    $('.menu-frame').slideUp('fast');
    drop = 0;
    }
    $('.card-text').css({'font-size':$('#font-range').val()+'px','line-height':'unset','text-align':alignTo});
    
}
//ends