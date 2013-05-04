import sublime, sublime_plugin
from TestXmlFormatter import Formatter

class PrettifyCommand(sublime_plugin.TextCommand):
  def prettify(self, text):
    return Formatter().format_string(text)

  def run(self, edit):
    sels = self.view.sel()
    for selection in sels:
      res = self.prettify(self.view.substr(selection))
      self.view.replace(edit, selection, res)
