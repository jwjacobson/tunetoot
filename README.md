# Tunetoot - a jazz repertoire management app

### Why build this app? The problem
An important part of learning to play jazz is memorizing tunes, usually taken from the canon of [jazz](https://en.wikipedia.org/wiki/List_of_jazz_standards) and [popular](https://en.wikipedia.org/wiki/Great_American_Songbook) standard songs.
These can number less than 10 for the beginning student, up to 100 or more for more advanced students, to hundreds or even over a thousand for professionals. Shared knowledge of a common set of tunes allows jazz musicians to successfully make music together with little to no preparation and is a distinctive feature of the artform.

My own experience learning to play jazz has included a fair amount of frustration in trying to grow my repertoire. Tunes have to be regularly integrated into practice so that they enter long-term memory. This isn't difficult when one only knows a few tunes, but as my own repertoire approached the 100-tune threshold, I had difficulty keeping them all straight, and it often felt that for every new tune I learned, another one would slip out of the rotation and be forgotten, necessitating tiresome relearning. I have talked to enough other players to know that this issue is not unique to me; it is a general problem for jazz musicians, at least at the student level.

### Towards a solution
This application will help the practicing jazz musician to manage their expanding repertoire, primarily by providing access to a database of tunes. At present, the default repertoire consists of 

The application will come preloaded with at least one repertoire, but users will also have the freedom to create their own from scratch or alter the existing database by adding, removing, or editing tunes. Crucially, each entry in the tune database will have a "last played/practiced" column to be updated whenever the user plays that tune. This will allow the user to easily see, for example, which tunes in their repertoire that they haven't played in the last two weeks, helping to keep learned tunes from being forgotten.

The app will also offer a "What tune should I learn/play?" feature, which will randomly select a tune from the user's repertoire based on user-provided parameters, which can include any attributes of a tune.

### App focus, or what this app is *not*
Inspired by the Unix philosophy of "do one thing and do it well", the focus of this app is repertoire management. It is not a general practice app, and it is not a tune *learning* app. There are plenty of other apps and resources that fulfill those functions. The app assumes the user has access to the materials they need to learn a tune (sheet music, recordings, etc.) outside of the app itself. What the app offers is easy and intuitive access to all tunes known by the user based on any desired criteria.

## Technical Details
### Structure
The backbone of the application is basic CRUD functionality, with users able to create an account, log in, and view and edit the tunes in their repertoire. At present, [Ethan Iverson's Compilation of 100 Standards](https://ethaniverson.com/a-new-meaning-old-approach-to-jazz-education/) is provided as a default option, or users can start with an empty repertoire to fill themselves.

The centerpiece of the app is the tune object, with attributes corresponding to an entry in a repertoire database. A tune currently has the following attributes:

* tune_id - primary key
* Title
* Composer
* Key
* Other keys - e.g., "I Love You" by Cole Porter is in F, but contains a modulation to A
* Form - e.g., AABA, 12-bar blues, etc.
* Style - e.g., bop, latin, ballad, etc.
* Meter
* Year
* Decade (automatically derived from year)

### To Do

Tunetoot is still far from the functionality I envision for it. At present it is not very useful.

In the future I plan to add the following features:

* Knowledge, Date started learning, and Date last played columns - stored on an association table connecting tune and user, these will allow the user to target tunes that need the most reinforcement
* Boolean repertoire search - to my mind the most elegant way to search the repertoire on the basis of any and all stored criteria
* Sort-on-click of repertoire display by field
* "What should I learn/play?" feature will randomly select a tune in the repertoire that matches the provided criteria
* A selection of color schemes named after famous players and representative of their style
* Hosting the site online for ease of use by the public

### Technologies
This app is built in **Flask** and also makes use of **SQLAlchemy** and **Jinja** templating. The database is **SQLite** with a migration to **Postgres** in the works. The front end is deliberately done in **vanilla HTML/CSS**. Originally I planned to use Boostrap to achieve a more contemporary look, but found I enjoyed the stripped-down aesthetic, which for me is reminiscent of the internet of my childhood.

### License
Tunetoot is [free software](https://www.fsf.org/about/what-is-free-software), released under version 3.0 of the GPL. Everyone has the right to use, modify, and distribute Tunetoot subject to the [stipulations](https://github.com/jwjacobson/tunetoot/blob/main/License.md) of that license.

### Acknowledgments
Thanks to [Michael Wormley](https://github.com/mwormley008) for debugging and moral support.
