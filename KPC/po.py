# -*- coding: utf-8 -*-


class entry:
    def __init__(self):
        self.msgid = ''
        self.msgid_plural = ''
        self.msgstr = ''
        self.msgctxt = ''
        self.translator_comment = ''
        self.extracted_comment = ''
        self.references = []
        self.flags = set()
        self.keyid = ''

    # attributes handling
    def set_flag(self, flag):
        self.flags.add(flag)

    def unset_flag(self, flag):
        self.flags.remove(flag)

    def check_flag(self, flag):
        return flag in self.flags

    def is_fuzzy(self):
        return self.check_flag('fuzzy')

    def is_obsolete(self):
        return self.check_flag('obsolete')

    def is_untranslated(self):
        return (self.msgstr == '')

    def is_translated(self):
        return (not self.is_fuzzy() and
                not self.is_obsolete() and
                not self.is_untranslated())

    def is_no_wrap(self):
        return self.check_flag('no-wrap')

    def __repr__(self):
        return repr(self.msgid) + ':::' + repr(self.msgstr)


class catalog:
    def __init__(self):
        self.entries = []
        self.metadata = {}
        self.textdomain = ''
        self.language = 'ko'

    def add_entry(self, entry):
        if (entry.msgid == ''):         # header entry
            a = entry.msgstr.split('\n')
            for l in a:
                if len(l) == 0:
                    continue
                k, v = l.split(': ', 1)
                self.metadata[k] = v
        self.entries.append(entry)

    def settextdomain(self, d):
        self.textdomain = d


import os
import sys
class ignore:
    def __init__(self):
        self.ignore_file = ''

    def action(self, param):
        #ignore file 을 지정할 때와 안할 때 구분
        if 'file' in param:
            ignore_file = param.split(':',1)[1]
            if ignore_file[0] != '/':
                ignore_file = os.getcwd() + '/' + ignore_file
            if not os.path.exists(ignore_file):
                print('%s 파일이 없습니다.' % ignore_file)
                sys.exit(1)
        else:
            ignore_file = os.getcwd() + '/.ko-po-check-ignore'
            if not os.path.exists(ignore_file):
                open(ignore_file, 'w').close()

        #param 에 따른 동작 구분
        if 'default' == param:
            print('ignore 기본 파일 읽어오기')
            with open(ignore_file) as f:
                #파일을 줄별로 가져와 리스트에 넣는다. 이때 줄에서 #이후는 주석으로 간주해 '#' 이후 문자열은 제외한다.
                ignore_keyids = [n.split('#', 1)[0].strip() for n in f.read().splitlines()]
            return ignore_keyids
        elif 'file' in param:
            print('%s 파일 읽어오기' % ignore_file)
            with open(ignore_file) as f:
                #파일을 줄별로 가져와 리스트에 넣는다. 이때 줄에서 #이후는 주석으로 간주해 '#' 이후 문자열은 제외한다.
                ignore_keyids = [n.split('#', 1)[0].strip() for n in f.read().splitlines()]
            return ignore_keyids

        #add 와 clear 는 기본 파일에만 적용된다.
        elif 'add' in param:
            print('ignore 기본 파일에 추가')
            f = open(ignore_file,"a")
            for n in param.replace('add:','').split(','):
                f.write(n + "\n")
            f.close()
            f = open(ignore_file,"rb").read()
            print(f.decode("utf-8"))
            sys.exit(1)
        elif param == 'clear':
            print('ignore 기본 파일 초기화')
            if os.path.exists(ignore_file):
                os.remove(ignore_file)
                open(ignore_file, 'w').close()
            sys.exit(1)
