## English localization (Ren'Py translate-ready text)
define l = Character("Lin Xia")
define c = Character("Chen Mo")

label start:
    "It rained all night. The eaves of the old bookshop dripped, steady, like they were counting something."
    l "You again? That's three times this week."
    c "I was in the area."
    l "In the area? You live on the east side. This is the west side."
    c "...The city's round."
    l "Pfft. Fine, I'll give you that one. Same book as always? Border Town?"
    c "No. Today I'm looking for a book with no ending."
    l "A book with no ending? Good luck finding one of those. Why not write your own?"
    menu:
        "\"Only if you're my first reader.\"":
            l "Deal. But if it's bad, I'm returning it."
        "\"I'd never want to finish it.\"":
            l "Then don't. The rain hasn't stopped anyway."
    return
