# -*- coding: utf-8 -*-

import string,re

name = "typoincomplete"

typo_re = re.compile(u'([\u3131-\u318E]+)')
typo_error = u'\"%s\": 음절이 불완전합니다.  오타로 보입니다'

def check(msgid,msgstr):
    ret = 1
    errmsg = ''
    str = msgstr
    while 1:
        mo = typo_re.search(str)
        if mo:
            ret = 0
            if errmsg:
                errmsg += '\n'
            errmsg += typo_error % mo.group(1)
            str = str[mo.end():]
        else:
            break;
    return (ret, errmsg)

if __name__ == '__main__':
    import sys
    msgid = unicode(sys.stdin.readline(),'utf-8')
    msgstr = unicode(sys.stdin.readline(),'utf-8')
    t,e = check(msgid,msgstr)
    if not t:
        print e
    else:
        print 'Success'

# Local Variables:
# coding: utf-8
# End: