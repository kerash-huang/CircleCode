# coding: utf8
import sublime, sublime_plugin

class CircleCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        # 反白的字
        sel = self.view.sel()
        #strrr = self.view.substr(sublime.Region(0, self.view.size())).encode('utf8')
        self.view.set_status('selection%s' % (sel))
        #self.view.replace(edit, sublime.Region(indexPos, indexPos+1), word.decode('utf8'))
        #self.view.insert(edit, 0, strrr)

        # for selection  in self.view.sel():
        #     if not selection.empty():
        #         mystring = self.view.substr(selection)
        #         self.view.set_status('selection%s' % (mystring))
                #self.view.insert(edit, 0, mystring)