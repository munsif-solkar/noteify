//profile tab
$('.nav-profile-button').click(()=>{
	$('.drop-profile-tab').fadeIn('fast',()=>{
		$('.drop-profile-tab').addClass('visible');
	});
})
	window.onclick = function (event) {
		console.log(event.target);
		if($('.drop-profile-tab').hasClass('visible')){
			var targets = document.getElementsByClassName('avoid-click');
			if (!Array.from(targets).includes(event.target)) {
		        $('.drop-profile-tab').fadeOut('fast');
		        $('.drop-profile-tab').removeClass('visible');
		    }
	}
}