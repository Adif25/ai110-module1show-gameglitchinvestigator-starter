# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  First thing i noticed was that the range was wrong for each of the hard-med-easy. Than i noticed it kept saying the wrong hint. with higher and lower. Lastly, I couldn't even click new game.

aaa

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

I used claude, I first skimmed through code to look for any aditional mistakes. Than I wrote specfic mistakes and said only fix this. For example I said,"i need you fix my this app.py it. First of all its the normal and hard ranges need to be changed. It also needs to change the higher to lower and lower to higher because everytime it says lower for the number." I didnt tell like fix everything. I tried that first and start checking what is was doing it getting the wrong things fixed.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
I fixed on bug at time and than looked if it worked. Than I went back and wrote prompt and checked it. sometimes it would complete the wrong bug and actaully make it worse.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

Every time you interact with the app (click a button, type something), Streamlit reruns the entire app.py script from top to bottom. In the original code, random.randint() was called every rerun without checking if a secret already existed

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Go slowly, make sure it is actaully fixing the right code, istead of jumping into an new one. Play around with the app more and than write it down, what is going first before just jumping into claude.