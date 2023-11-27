# Lærings program

Et quiz program lavet til en aflevering i programmering B.   
Det er et quiz program der lærer dig generel viden om verden. Alt fra geografi til matematik.

### Formål:

Formålet er at forstærke viden fra hele ens skolegang, derfor er der mange niche spørgsmål som man kan have glemt. Fx, datoer fra krige man har haft om i historie og matematiske eksempler.

### Målgruppe:

Målgruppen er folk i udskolingen. Dvs en alder på 14-17, spørgsmålene er også indrettet derefter. Da det hovedsageligt er denne aldersgruppe der ville have brug for at opfriske den viden quizzen tilbyder.

### Designmønstre:

Jeg har hovedsageligt brugt 2 designmønstre:

#### Procedural programming:
Definition fra wikipedia: Koden følger en procedureorienteret tilgang, hvor data og funktionalitet er struktureret omkring procedurer eller funktioner snarere end objekter.   
I min kode anvender jeg definerede funktioner såsom check_answer() og display_question(). Disse funktioner udfører specifikke opgaver, og de kaldes i en bestemt rækkefølge. Som derfor følger en procedure:
```python
def check_answer():
    global current_question
    if var.get() == answers[current_question]:
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect!", "Sorry, that's not correct.")
    current_question += 1
    if current_question < len(questions):
        display_question()
    else:
        messagebox.showinfo("End", "The quiz is over!")

# Display the next question:
def display_question():
    question_label.config(text=questions[current_question])
    for i in range(len(choices[current_question])):
        radio_buttons[i].config(text=choices[current_question][i], value=choices[current_question][i])
        radio_buttons[i].deselect()
    var.set(None)

```

#### Modularity:
Definition fra wikipedia: Modular design is based on the idea of dividing a complex system into smaller and simpler units, called modules.   
Jeg har ikke direkte brugt dette design pattern, men jeg har taget inspiration, fx bruger jeg det i min "check_answer" funktion:
```python
def check_answer():
    global current_question
    if var.get() == answers[current_question]:
        messagebox.showinfo("Correct!", "Your answer is correct!")
    else:
        messagebox.showerror("Incorrect!", "Sorry, that's not correct.")
    current_question += 1
    if current_question < len(questions):
        display_question() # <-----
    else:
        messagebox.showinfo("End", "The quiz is over!")
```
Her bruger jeg funktionen "display_question()", (foran <-----), til at delegere noget af funktionens arbejde til en anden funktion jeg har lavet specifikt til dette. 

### Beskrivelse af udviklingsprocessen:

Jeg startede med at brainstorme hvilken slags lærings program jeg ville skrive. Da jeg var kommet frem til en ide fandt jeg designmønstre der ville hjælpe mig med at udføre den. Og herefter skrev jeg koden.


### Beskrivelse af brugergrænsefladen:
Overordnet design:

![billede](https://github.com/albertsigp/Learning-thing/assets/32582639/4d55a70f-fb0e-4bf7-8e47-ac7e7c9912c4)


Grænsefladen er opbygget af 3 radio knapper som korresponderer til den svarmulighed der står ud for dem:
Ex: (What is the capital of France?)

![billede](https://github.com/albertsigp/Learning-thing/assets/32582639/7ce1d384-f098-489d-bb04-e6e76d014192)

Herefter kan man klikke submit, hvorefter programmet fortæller dig om dit svar er rigtigt eller forkert:

![billede](https://github.com/albertsigp/Learning-thing/assets/32582639/9683094f-02dc-427d-a4de-b6e29a05d146)



### Test af program:
| Input | Forventet output | Faktisk output |
| ----------- | ----------- | ----------- |
|Kør program | Program kører | Program kører|
|Svar spørsmål korrekt | print: "Spørgsmål korrekt" og skift til næste |print: "Spørgsmål korrekt" og skift til næste|
|Svar spørgmål forkert | print: "Spørgsmål forkert" og skift til næste |print: "Spørgsmål forkert" og skift til næste|
|Tryk på sluk knappen | Programmet slukker| Programmet slukker|
|Bliv færdig med quizzen|print "the quiz is over" og sluk quiz | printer: "the quiz is over" og slukker ikke|


For at teste programmet har jeg også svaret rigtigt og forkert på spørgsmålene:

![billede](https://github.com/albertsigp/Learning-thing/assets/32582639/32111d31-9846-4b62-87be-972ca9ff4d28)


