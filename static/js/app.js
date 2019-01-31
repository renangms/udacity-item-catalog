// $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
$(".hanging-close, .modal-backdrop, .modal").click(function(event) {
  // Remove the src so the player itself gets removed, as this is the only
  // reliable way to ensure the video stops playing in IE
  $("#trailer-video-container").empty();
});
// Start playing the video whenever the trailer modal is opened
// $(document).on('click', '.movie-tile', function (event) {
$(".movie-poster-img").click(function(event) {
  var trailerYouTubeId = $(this).attr('trailer_youtube_id')
  console.log(trailerYouTubeId)
  var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
  $("#trailer-video-container").empty().append($("<iframe></iframe>", {
    'id': 'trailer-video',
    'type': 'text-html',
    'src': sourceUrl,
    'frameborder': 0
  }));
});


$(".brighten").click(function() {
  window.location = $(this).find("a").attr("href");
  return false;
});


