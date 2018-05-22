import webbrowser
import os
import re
main_page_head = '''
<!DOCTYPE html>
<html>
<head>
    <title>Movie trailer website</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://code.jquery.com/jquery-1.12.3.min.js" "
    "integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
        crossorigin="anonymous"></script>
        <link href="https://fonts.googleapis.com/css?family=Courgette" "
        "rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs"
        "/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/"
        "bootstrap.min.css" rel="stylesheet" type="text/css" />
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/"
    "bootstrap.min.js"></script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeY").attr("src", "#");
            })
        })
        function changeVideo(vId) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + vId;
            $("#myVideo").modal("show");
        }
    </script>
<style>
     .container {
            flex-wrap: wrap;
            display: flex;
        }
        body {
            margin: 0;
        }

        h1 {
            color:Red;
        }

        img {
            width:470px;
            height:400px;
            border-radius:25px;
        }
    .c:hover,
    .c1:hover,
    .c2:hover,
    .c3:hover
    {
        background-color: Salmon  ;
        visibility: visible;
        cursor: pointer;
        border-radius:10px;
    }

        .c{
           padding-left:40px;
           padding-bottom:40px;
           padding-right:40px;
           padding-top:40px;
           }
        .c1{
            padding-top: 40px;
            padding-left: 40px;
            padding-bottom:40px;
            padding-right: 40px;
        }
        .c2{
            padding-top: 40px;
            padding-left: 40px;
            padding-bottom:40px;
            padding-right: 40px;
        }
        .c3{
            padding-top: 40px;
            padding-left: 40px;
            padding-bottom:40px;
            padding-right: 40px;
        }
    </style>
    <title>Movie Trailers</title>
    <center><h1><font size="14"><b> Movie Trailer Website!</b>"
    "</font></h1></center>

    <hr>
</head>
'''
main_page_content = '''
<body>
        <div class="container">
            <div class="c" onclick="changeVideo('uQbOYxLcGk4')">
                <img  src="http://allindiaroundup.com/wp-content/uploads/2015/"
                "10/Rudhramadevi-Movie-Total-collections.png" "
                "alt="Rudramadevi">
                <figcaption style="text-align: center; color: white;">
                    <b>RUDRAMADEVI</b>

</div>
            <div class="c1" onclick="changeVideo('vyX4toD395U')">
                <img src="http://hityaflopmovieworld.com/wp-content/uploads"
                "/2018/03/Bajrangi-Bhaijaan.jpg" alt="Bhajrangi Bhaijaan">
                <figcaption style="text-align: center; color: white;">
                    <b>BHAJARANGI BHAYIJAAN</b>
                </figcaption>
            </div>
            <div class="c2" onclick="changeVideo('PQKu78NnyvU')">
                <img src = "https://i2.wp.com/pandolin.com/wp-content/"
                "uploads/2018/01/Pari-cover.jpg?resize=1100%2C550&ssl=1" "
                "alt="Pari">
                <figcaption style="text-align: center; color: white;">
                    <B>PARI-Not a fairy tale</B>
                </figcaption>
            </div>
            <div class="c3" onclick="changeVideo('MG37Bp8BlXI')">
                <img src="https://www.apherald.com/ImageStore/images/movies/"
                "movies-wallpapers/Om-Namo-Venkatesaya-Movie-Latest-HD-"
                "Posters2.jpg" alt="Om namo venkatesaya">
                <figcaption style="text-align: center; color: white;">
                    <B>OM NAMO VENKATESAYA</B>
                </figcaption>
            </div>
        </div>
       <div class="modal fade" id="myVideo" tabindex="-1" "
       "role="dialog" aria-labelledby="myModalLabel">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-footer">
                        <button type="button"class="btn btn-default" "
                        "data-dismiss="modal"><b>X</b></button>
                    <div class="modal-body">
                        <iframe id="myframeY" width="550" height="350" "
                        "src="" frameborder="0" allowfullscreen></iframe>
                       </div>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>

</html>
'''
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube"
"-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2 style = "color:white;">{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = "
        "re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or "
        "re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = "
        "youtube_id_match.group(0) if youtube_id_match else None
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            storyline=movie.storyline
        )
    return content


def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = "
    "main_page_content.format(movie_tiles=create_movie_tiles_content(movies))
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
