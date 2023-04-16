# TuneToot (working title)
## A jazz repertoire management app
***
### Coding Temple Capstone Project - Jeff Jacobson (Kekambas 111)
(note: for now this readme is a description of the project as I envision it. It will later become a description of the project as it exists)
***

### Why build this app? The problem
An important part of learning to play jazz is memorizing tunes, usually taken from the canon of [jazz](https://en.wikipedia.org/wiki/List_of_jazz_standards) and [popular](https://en.wikipedia.org/wiki/Great_American_Songbook) standard songs.
These can number less than 10 for the beginning student, up to 100 or more for more advanced students, to hundreds or even over a thousand for professionals. Shared knowledge of a common set of tunes allows jazz musicians to successfully make music together with little to no preparation and is a distinctive feature of the artform.

My own experience learning to play jazz has included a fair amount of frustration in trying to grow my repertoire. Tunes have to be regularly integrated into practice so that they enter long-term memory. This isn't difficult when one only knows a few tunes, but as my own repertoire approached the 100-tune threshold, I had difficulty keeping them all straight, and it often felt that for every new tune I learned, another one would slip out of the rotation and be forgotten, necessitating tiresome relearning. I have talked to enough other players to know that this issue is not unique to me; it is a general problem for jazz musicians, at least at the student level.

### Towards a solution
This application will help the practicing jazz musician to manage their expanding repertoire, primarily by providing access to a database of tunes. The application will come preloaded with at least one repertoire, but users will also have the freedom to create their own from scratch or alter the existing database by adding, removing, or editing tunes. Crucially, each entry in the tune database will have a "last played/practiced" column to be updated whenever the user plays that tune. This will allow the user to easily see, for example, which tunes in their repertoire that they haven't played in the last two weeks, helping to keep learned tunes from being forgotten.

The app will also offer a "What tune should I learn/play?" feature, which will randomly select a tune from the user's repertoire based on user-provided parameters, which can include any attributes of a tune.

If I succeed in making this app the way I imagine it, I will be a regular user!

### App focus, or what this app is *not*
Inspired by the Unix philosophy of "do one thing and do it well", the focus of this app is repertoire management. It is not a general practice app, and it is not a tune *learning* app. There are plenty of other apps and resources that fulfill those functions. The app assumes the user has access to the materials they need to learn a tune (sheet music, recordings, etc.) outside of the app itself. What the app offers is easy and intuitive access to all tunes known by the user based on any desired criteria.

---

## Technical Details
### Structure
As a CRUD application, the overall app structure will resemble the Flask app we made in Week 6. Users will be able to create an account, log in, and view and edit their repertoire. No interaction between users will be provided.

The centerpiece of the app will be the tune object, with attributes corresponding to an entry in a repertoire database.
At present, a tune is projected to have the following attributes:

* tune_id - primary key
* Title
* Composer
* Key
* Secondary Key - e.g., "I Love You" by Cole Porter is in F, but contains a modulation to A
* Form - e.g., AABA, 12-bar blues, etc.
* Style - e.g., bop, latin, ballad, etc.
* Year
* Decade - (can be derived from year?)
* Knowledge - know, learning, don't know - tunes in the repertoire marked 'don't know' are equivalent to tunes the user wants to learn
* Date started learning - can be null if the user knew the tune before starting to use the app, or the user can input a date
* Date last played - initial value same as Date started learning. This will be editable by the user in the event they played a tune without recording it in the app

Another possible field will be "keys known", since it is often desirable to know a tune in multiple or even all keys, rather than just the traditional key. I will hold off on this feature until I'm confident the basic app is coming together as I think it would introduce a lot of complexity.

In addition to the repertoire page, there will also be a "play/learn tune" page where students can input parameters and have the app randomly select a tune matching those parameters to learn or play.

For example, the user will be able to input, probably via a series of menus, that they want to play a Wayne Shorter tune that they already know. The app will return a randomly selected tune meeting those parameters. If the user accepts the tune, the tune will be considered "played" and the "Date last played" column will be updated to today's date in the database. If the user rejects the tune, the app will return a different tune meeting the same parameters. Any and all parameters can be used in any query. "Latin 12-bar blues in C# written by Burt Bacharach in 1923" would be a valid query, though it would always return 0 results.

### Technologies
Framework - Flask. I am already familiar with it from Week 6. This seems like a better idea than learning a new framework, and I already know it supports the desired functionality.
Frontend - Bootstrap + Javascript. Again, familiarity is key, and I'm happy with the visual presentation I've been able to achieve with Bootstrap. JS as needed.
Database - Leaning toward Postgres as the most professionally relevant.


### Future Development Plans
After CT, I plan to develop this app to run locally and use a TUI so it can be run from the terminal. This will be more in line with my own preferences as a user of the app.
