# Moodymix
Moodymix is a web application that allows for users to get song reccomendations based off selecting different emotions.

![Moodymix](https://github.com/alexbhas/moodymix/assets/56275911/092c9429-329f-4e77-aef9-48d5cef59560)

## How To Run
- Ensure that ```client = MongoClient('mongodb://localhost:27017/')``` in app.py points to the correct MongoDB server, with the database moodmix and collection songs having been created.
- Ensure all dependencies are installed for Python with pip install -r requirements.txt
- Ensure all dependencies are installed for Svelte with npm install in /svelte-app
- Run npm run build in /svelte-app (can also run npm run dev when making changes to just the front-end)
- Run python app.py, navigate to localhost:8000

## Tech Stack
- Python/Flask
- MongoDB/PyMongo
- Svelte

## Dependencies
- Install dependencies through npm install and requirements.txt
- Also ensure MongoDB is installed with appropriate database created

## Planned features
Currently, there is a limited number of songs in songs.json. This was just to have enough songs so that every emotion appears at least once for testing purposes. The idea is that, individuals will fill the list with their own songs and send people their custom emotion boards, to get song reccoemndations based off the user interpretation of the emotions a song invokes. I plan to eventually upgrade this application to allow users to build their song list in the front-end. I will host the application online and allow for users to genereate unique links to their Moodymix boards. 

