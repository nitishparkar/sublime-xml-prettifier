import sublime, sublime_plugin
from TestXmlFormatter import Formatter

class PrettifyCommand(sublime_plugin.TextCommand):
  def prettify(self, text):
    return Formatter().format_string(text)

  def run(self, edit):
    sels = self.view.sel()
    res = self.prettify(self.view.substr(sels[0]))
    self.view.replace(edit, sels[0], res)
