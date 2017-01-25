$(document).ready(animate);

function animate(){
  var progressBar = $(".project-progress-bar");
  var projStatus = progressBar.data('status');
  if (projStatus == "reject"){
    var accept = $("#accept");
    accept.attr("id", "reject");
    accept.find("label").text("Denied");
  }
  var point = progressBar.find("#" + projStatus);
  point.addClass('point--active');
  point.prevAll().addClass('point--complete');
  point.nextAll().removeClass('point--complete');
  
  fillProgressBar(projStatus);
}

function fillProgressBar(projStatus) {
  var fillPercent = 33;
  var step = 0;
  switch (projStatus) {
    case "Reject":
      console.log("hello");
      step = 3;
      break;
    case "Accept":
      step = 3;
      break;
    case "Pending":
      step = 2;
      break;
    case "Incomplete":
      step = 1;
      break;
    default:
      step = 0;
  }
  console.log(step*fillPercent);
  document.getElementById("bar_fill").style.width = (step*fillPercent) + "%";
}


/*
Point Animation

$('.point').on('click', function(e) {
  var getTotalPoints = $('.point').length,
    getIndex = $(this).index(),
    getCompleteIndex = $('.point--active').index();

  TweenMax.to($('.bar__fill'), 0.6, {
    width: (getIndex - 1) / (getTotalPoints - 1) * 100 + '%'
  });

  if (getIndex => getCompleteIndex) {
    $('.point--active').addClass('point--complete').removeClass('point--active');

    $(this).addClass('point--active');
    $(this).prevAll().addClass('point--complete');
    $(this).nextAll().removeClass('point--complete');
  }
});
 */

/*
  Demo Purposes

var progressAnimation = function() {
  var getTotalPoints = $('.point').length,
    getIndex = Math.floor(Math.random() * 4) + 1,
    getCompleteIndex = $('.point--active').index();

  TweenMax.to($('.bar__fill'), 0.6, {
    width: (getIndex - 1) / (getTotalPoints - 1) * 100 + '%'
  });

  if (getIndex => getCompleteIndex) {
    $('.point--active').addClass('point--complete').removeClass('point--active');

    $('.point:nth-child(' + (getIndex + 1) + ')').addClass('point--active');
    $('.point:nth-child(' + (getIndex + 1) + ')').prevAll().addClass('point--complete');
    $('.point:nth-child(' + (getIndex + 1) + ')').nextAll().removeClass('point--complete');
  }
};
*/