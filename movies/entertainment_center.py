import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of boy", 
            "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg",
            "https://www.youtube.com/watch?v=KYz2wyBy3kc")

inception = media.Movie("Inception",
            "The implantation of another person's idea into a target's subconscious",
            "http://www.filmofilia.com/wp-content/uploads/2010/04/Inception_poster.jpg",
            "https://www.youtube.com/watch?v=YoHD9XEInc0")

blind_side = media.Movie("The Blind Side",
            "The Blind Side is a 2009 American semi-biographical sports drama film",
            "http://www.welovemoviesmorethanyou.com/wp-content/uploads/2011/12/The-Blind-Side-movie-poster.jpg",
            "https://www.youtube.com/watch?v=gvqj_Tk_kuM")

blackfish = media.Movie("BlackFish",
            "The Blind Side is a 2009 American semi-biographical sports drama film",
            "http://dl9fvu4r30qs1.cloudfront.net/7b/03/37a68be34eb79a6980421c957828/blackfish-poster.jpg",
            "https://www.youtube.com/watch?v=fLOeH-Oq_1Y")

dawg_fight = media.Movie("BlackFish",
            "The only way to escape the streets is to your way out",
            "http://mmaowl.com/wp-content/uploads/2015/03/B-w-RdW0AEUxR_.jpg",
            "https://www.youtube.com/watch?v=0Tyf4MW74Xg")

movies = [toy_story, inception, blind_side, blackfish, dawg_fight]

fresh_tomatoes.open_movies_page(movies)

