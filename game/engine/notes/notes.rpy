init -1 python:
    class Note(object):
        def __init__(self, name, text, journal_flag_persistent = False, journal_flag_delayed = False, trackTag = None):
            self.name = name
            self.text = text
            self.journal_flag_persistent = journal_flag_persistent
            self.journal_flag_delayed = journal_flag_delayed
            self.trackTag = trackTag

    def NoteUnlock(tag, Silent = False):
        if _in_replay:
            return
        Assert(tag in notesLib, "ERROR: Unlocked non-existant note-tag: %s" % tag)
        if tag not in store.unlockedNotes:
            store.unlockedNotes.add(tag)
            if not Silent:
                AddNotif(tra(_("New note: [note_title!t]"), scope = {"note_title":notesLib[tag].name}), Kind = "note_new")
        return

    def NoteLock(tag):
        if _in_replay:
            return
        Assert(tag in notesLib, "ERROR: Locked non-existant note-tag: %s" % tag)
        if tag in store.unlockedNotes:
            store.unlockedNotes.remove(tag)
        return