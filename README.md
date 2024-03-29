# Python Practice

Beginner exercises to learn Python.

## Instructions

## Summary

1. **Fizzbuzz** - Classic exercise to learn the basics of printing, looping, and conditionals.
   To run, type `python fizzbuzz.py`.

2. **Counting Words** - A program that parses a .txt file and extracts the 20 most common words on the file by counting each one of them. It also provides the total number of unique words in the file.
   To run, type `./wordcount.py file`, replacing `file` with the path to a .txt file.

   As an example, you can try the example file in this project.
   `./wordcount.py chomsky.txt`
   This will give you the top 40 words in Noam Chomsky's book "Syntactic Structures" and the total number of unique words.

3) **URL Shortener** - A program that receives a post request with a complete URL (e.g. https://www.github.com) and returns a shortened URL that can be accessed while the server is still running. [In progress]

   To run, type `python3 URLShortener.py`. On a another terminal window, type: `curl localhost:5000/url '{"url": "https://www.github.com"}'` and you will receive back a JSON with the original URL and its shortened version.

   Next step: when trying to access the URL, it should give you a status 301 message with the original location.
