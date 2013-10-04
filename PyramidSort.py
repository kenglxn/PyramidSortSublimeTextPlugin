import sublime, sublime_plugin

def pyramid_sort(txt):
	txt = list(filter(lambda s: s.strip(), txt))
	txt.sort(key = lambda s: len(s))
	return txt

class PyramidSortCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			ls = self.view.line(s)
			txt = self.view.substr(ls)
			end = "\n" if txt[-1] == "\n" else ""
			lines = txt.splitlines()
			lines = pyramid_sort(lines)
			self.view.replace(edit, ls, u"\n".join(lines) + end)
