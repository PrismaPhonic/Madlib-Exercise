from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

once_upon_a_time = Story(
        ["place", "noun", "verb", "adjective", "plural_noun"],
        """Once upon a time in a long-ago {place}, there lived a
        large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
        "Once upon a time"
    )

party_invitation = Story(
        ["name", "theme", "place", "day_of_the_week", "time", "verb", "animal", "body_part", "contact_information"],
        """{name} is having a {theme} party! It's going to be at {place}
            on {day_of_the_week}. Please make sure to show up at
            {time} or else you will be required to {verb} a/an 
            {animal} with your {body_part}""",
        "Party Invitation"
    )

excused = Story(
        ["name","adjective","noun"],
        """Please excuse {name}, who is far too {adjective} to attend {noun} class.""",
        "Excuse Hall Pass"
    )

vacation = Story(
        ["adjective","adjective_2","noun","noun_2","plural_noun","game","plural_noun_2","verb_ending_in_ing","verb_ending_in_ing_2","plural_noun_3",
        "verb_ending_in_ing_3","noun_3","plant","body_part","place","verb_ending_in_ing_4",
        "adjective_3","number","plural_noun_4"],
        """A vacation is when you take a trip to some {adjective} place
        with your {adjective_2} family. Usually you go to some place
        that is near a/an {noun} or up on a/an {noun_2}.
        A good vacation place is one where you can ride {plural_noun}
        or play {game} or go hunting for {plural_noun_2} . I like
        to spend my time {verb_ending_in_ing} or {verb_ending_in_ing_2}.
        When parents go on a vacation, they spend their time eating
        three {plural_noun_3} a day, and fathers play golf, and mothers
        sit around {verb_ending_in_ing_3}. Last summer, my little brother
        fell in a/an {noun_3} and got poison {plant} all
        over his {body_part}. My family is going to go to (the)
        {place}, and I will practice {verb_ending_in_ing_4}. Parents
        need vacations more than kids because parents are always very
        {adjective_3} and because they have to work {number}
        hours every day all year making enough {plural_noun_4} to pay
        for the vacation""",
        "Vacation"
    )

story_list = [once_upon_a_time,party_invitation,excused,vacation]


@app.route('/')
def home():
    """This will bring up a list of stories for the user to select"""
    return render_template('pickstory.html',stories = story_list,length = len(story_list))


@app.route('/form')
def form():
    """This will take the user to a form to fill in arguments""" 
    story_id = int(request.args.get('story'))
    story = story_list[story_id]   
    return render_template('madlib-form.html', words=story.words, id=story_id)

@app.route('/story')
def display_story():
    """This will route the user to a page where the story is displayed"""
    story_id = int(request.args.get('story'))
    story = story_list[story_id]
    story_text = story.generate(request.args)
    return render_template('story.html',story=story_text,name=story.title)
            
