# MoodleVisualizer
***Created by Dulith Polpitiya***

This program receives Moodle log files as an input and displays a visualization that showcases how users interact with the website and their course.

## How to run

1. Before the playback can be accessed, all log files and marks files **must** be anonymized. The script to anonymize these files can be found [here](https://github.com/Nuveen540/MoodleAnonymizer).
2. Run ``app.py`` on your preferred Python interpreter, and access the host website.
3. Upload the log file to the label that says "events file" (this field is required), and upload the final marks file to the label that says "results file" (this field is optional).
4. Press upload.
5. Press 'Play' to begin the playback.

## Features

The Event Visualizer has a simple interface with various options affecting display.

* **Play button**: Plays the playback.
* **Pause button**: Pauses the playback.
* **Restart button**: Resets the playback to the beginning.
* **Speed**: Determines the speed of the playback. There are 6 different speed options, from slow to hyper fast.
* **Go to event**: Here, the user can enter a number, and upon pressing the 'Enter' button, the playback automatically skips to that event. This can be used to skip to a later event or to revert to a previous event. The playback will automatically be paused until the user presses the 'Play' button.
* **Enter button**: Confirms the user's choice.
* **Top 25%**: If the user provides a results file, then if this box is checked, then all students who received the top 25% of scores will be shown. Otherwise, these users will be hidden. Students who received the top 25% of scores are denoted with green dots.
* **Mid 50%**: If the user provides a results file, then if this box is checked, then all students who received the middle 50% of scores will be shown. Otherwise, these users will be hidden. Students who received the middle 50% of scores are denoted with yellow dots.
* **Bottom 25%**: If the user provides a results file, then if this box is checked, then all students who received the bottom 25% of scores will be shown. Otherwise, these users will be hidden. Students who received the bottom 25% of scores are denoted with red dots.
* **Event description**: This single line of text contains the following information: the current event, the user performing the event, the module accessed, and the time of the event. It also denotes whether the playback is paused.
