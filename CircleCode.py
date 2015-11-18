# coding: utf8

import sublime, sublime_plugin
import re

class CircleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        # 多個 select item
        for path  in selection:
            if not path.empty():
                seltext = self.view.substr(path)
                seltext = self.circle(seltext)
                # 轉換成 php code
                #self.view.replace(edit, path, seltext)

    def circle(self, data):
        data = data.strip()
        pattern = r'array\((\d+)\)\s+{\s*(\[\d+\]\s*=>\s*int\(\d+\)\s*)+\}'
        if re.match(pattern, data):
            nr = re.search(pattern, data).group(1)
            ret = range(int(nr))
            pattern = r'\[(\d+)\]\s*=>\s*int\((\d+)\)'
            for idx, v in re.findall(pattern, data):
                ret[int(idx)] = v

        rueslt = '$tmp = [{0}];'.format(','.join([_ for _ in ret]))
        return rueslt