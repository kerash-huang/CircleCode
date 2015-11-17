# coding: utf8
import sublime, sublime_plugin

class CircleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection    = self.view.sel()
        selectionLen = len(selection)
        content      = self.view.substr(sublime.Region(0, self.view.size())).encode('utf8')

        # 多個 select item
        for sel  in selection:
            if not sel.empty():
                seltext = self.view.substr(sel)
                self.circle(seltext)

    def circle(self, text):
        print(text)