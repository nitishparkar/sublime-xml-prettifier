import sublime, sublime_plugin
from xml.dom import minidom

class PrettifyCommand(sublime_plugin.TextCommand):
  def prettify(self, text):
    parsed_string = minidom.parseString(text)
    return parsed_string.toprettyxml(indent="  ")

  def run(self, edit):
    sels = self.view.sel()
    for selection in sels:
      res = self.prettify(self.view.substr(selection))
      self.view.replace(edit, selection, res)
