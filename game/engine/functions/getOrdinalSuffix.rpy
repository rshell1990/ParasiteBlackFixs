init python:
    # get *st *th *rd from an int
    def getOrdinalSuffix(n):
        n = int(n)
        if 11 <= (n % 100) <= 13:
            suffix = _('th')
        else:
            suffix = [_('th'), _('st'), _('nd'), _('rd'), _('th')][min(n % 10, 4)]
        return str(n) + suffix
