import media
import fresh_tomatoes

rudramadevi = media.Movie(
     "RUDRAMADEVI",
     "HISTORY,EPIC",
     "http://allindiaroundup.com/wp-content/uploads/2015/10/Rudhramadevi-"
     "Movie-Total-collections.png",
     "https://www.youtube.com/embed/uQbOYxLcGk4"
     )

bhajrangibhayijaan = media.Movie(
    "BHAJRANGI BHAYIJAAN",
    "DRAMA",
    "http://hityaflopmovieworld.com/wp-content/uploads/2018/03/"
    "Bajrangi-Bhaijaan.jpg",
    "https://www.youtube.com/embed/vyX4toD395U"
    )

pari = media.Movie(
    "PARI",
    "HORROR",
    "https://i2.wp.com/pandolin.com/wp-content/uploads/2018/01/"
    "Pari-cover.jpg?resize=1100%2C550&ssl=1",
    "https://www.youtube.com/embed/PQKu78NnyvU"
    )

omnamovenkatesaya = media.Movie(
    "OM NAMO VENKATESAYA",
    "HYSTERICAL",
    "https://www.apherald.com/ImageStore/images/movies/movies-wallpapers"
    "/Om-Namo-Venkatesaya-Movie-Latest-HD-Posters2.jpg",
    "https://www.youtube.com/embed/MG37Bp8BlXI"
    )


movies = [rudramadevi, bhajrangibhayijaan, pari, omnamovenkatesaya]
fresh_tomatoes.open_movies_page(movies)
