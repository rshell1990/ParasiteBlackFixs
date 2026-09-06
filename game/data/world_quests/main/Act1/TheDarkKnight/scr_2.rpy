label qst_DarkKnight_2_returnToNyx:
    NYX @talk 'Ah yes, my men did report finding a few bodies turning up.'
    $ QstComplete(QstDarkKnight)
    NYX @laugh 'Nicely done, here... some coin as promised.' #Player earns X coins.
    $ PlayerAddItem("gold", 350)
    jump qst_bloodhound_0_pitch