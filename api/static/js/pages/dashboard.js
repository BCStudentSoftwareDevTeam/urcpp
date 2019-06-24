$(document).ready(animate);

function animate(){
  var progressBar = $(".project-progress-bar");
  var projStatus = progressBar.data('status');
  // if (projStatus == "Reject"){
  //   var accept = $("#accept");
  //   accept.attr("id", "reject");
  //   document.getElementById("accept").setAttribute("id", "reject");
    
  //   accept.find("label").text("Denied");
  // }
  var point = progressBar.find("#" + projStatus);
  point.addClass('point--active');
  point.prevAll().addClass('point--complete');
  point.nextAll().removeClass('point--complete');
  
  fillProgressBar(projStatus);
}

function fillProgressBar(projStatus) {
  console.log(projStatus);
  var fillPercent = 25;
  var step = 0;
  switch (projStatus) {
    case "AllClosed":
      step = 6;
      break;
    case "Abstract":
      step = 5;
      break;
    case "Reject":
      step = 6;
      break;
    case "Accept":
      step = 4;
      break;
    case "Pending":
      step = 3;
      break;
    case "PanelClosed":
      step = 2;
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
