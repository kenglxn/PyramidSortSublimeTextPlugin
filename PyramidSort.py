import sublime, sublime_plugin

def pyramid_sort(txt):
	txt = list(filter(lambda s: s.strip(), txt))
	txt.sort(key = lambda s: len(s))
	return txt

class PyramidSortCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = [s for s in self.view.sel() if not s.empty()]
		if regions:			
			for r in regions:
				txt = self.view.substr(r)
				lines = txt.splitlines()
				lines = pyramid_sort(lines)
				self.view.replace(edit, r, u"\n".join(lines))
