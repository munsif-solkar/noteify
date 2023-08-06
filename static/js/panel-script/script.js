 //add new
 $('#addNew').click(function () {
    var modal = document.getElementById('myModal');
    $('#myModal').css('display', 'block');
    //close Modal
    $('.close').click(function () { modal.style.display = 'none'; });
    window.onclick = function (event) {
      if (event.target == modal) {
        $('#myModal').css('display', 'none');
      }
    }
    //ends
  });
  //ends
  var wc = document.getElementById('wordsCount');
  var txa = document.getElementById('txtarea');
  function count() {
    wc.innerHTML = txa.value.replace(/\s/g, "").length + '&nbspwords';
  }



//search
    // in Out
    $('#search_toggle').click(function(){
        $('.search_page').fadeIn('fast',()=>{
          $('#search_field').focus();
            $('#close_search').click(()=>{
                $('.search_page').fadeOut('fast',()=>{
                    $('#search_field').val('');
                });
            });
        })
    })
    //ends

      //machine
const hide = (message) => {
	$('.searched_elements').html(message);
}
const searchElements=document.getElementsByClassName('main-card');
  function action() {
	$('.searched_elements').html('');
	var inpval = document.getElementById('search_field');
	Array.from(searchElements).forEach((element,index) => {
        const title = element.getElementsByClassName('card-title')[0].innerText;
        console.log(index);
		invl = inpval.value;
		find = title.toLowerCase().slice(0, invl.length)
		if (invl.length > 0) {
			if (invl.toLowerCase() == find) {
				$('.searched_elements').html($('.searched_elements').html() +
					`<section>
                        <a href=${element.href}>
                            <div class='suggest'>
				                <span id=title_>${element.getElementsByClassName('card-title')[0].innerText}</span><br>
                                <span id=date_>${element.getElementsByClassName('card-subtitle mb-2 text-muted')[0].innerText}<span><br>
                                <span id=prio_>${element.getElementsByClassName('prio')[0].innerText}<span>
                            </div>
                        </a>
				    </section>`
				)
				if (invl.toLowerCase() == title.toLowerCase()) {
					hide();
				}
			}
		}
		else {
			hide();
      $('.search_page').fadeOut('fast');
		}
	});
}
  //ends


//ends

//menu
var i = 0;
function hamMenu(){
if(i==0){
$('.menu-frame').slideDown('fast');
$('#addNew_toggleButton').css('transform','rotate(135deg)');
i = 1;
}
else{
$('.menu-frame').slideUp('fast');
$('#addNew_toggleButton').css('transform','rotate(-90deg)')
i = 0;
}
}
var textAlign = 'left';
function applyFilters(){
if (i==1){
$('.menu-frame').slideUp('fast');
i = 0;
}
$('.card-text').css({'font-size':$('#font-range').val()+'px','line-height':'unset','text-align':textAlign});

}
//ends