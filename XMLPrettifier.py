import re
import xml.dom.minidom
import sublime, sublime_plugin

class PrettifyCommand(sublime_plugin.TextCommand):
  def prettify(self, text):
    pxml = xml.dom.minidom.parseString(text).toprettyxml()
    return pxml

  def run(self, edit):
    sels = self.view.sel()
    res = self.prettify(self.view.substr(sels[0]))
    self.view.replace(edit, sels[0], res)
