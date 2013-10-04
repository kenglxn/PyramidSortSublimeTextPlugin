import sublime, sublime_plugin

def pyramid_sort(txt):
	txt = filter(lambda s: s.strip(), txt)
	txt.sort(key = lambda s: len(s))
	return txt

class PyramidSortCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = [s for s in self.view.sel() if not s.empty()]
		if regions:			
			for r in regions:
				lr = self.view.line(r)
				txt = self.view.substr(lr)
				lines = txt.splitlines()
				lines = pyramid_sort(lines)
				self.view.replace(edit, lr, u"\n".join(lines))
