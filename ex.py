import sublime
import sublime_plugin

def format(input):
    output = ""
    counter = 0
    SPACE = '  '
    for char in input:
        if char in "([{":
            counter += 1
            output += char + '\n' + SPACE * counter
        elif char in ")]}":
            counter -= 1
            output += '\n' + SPACE * counter + char
        elif char == ',':
            output += char + '\n' + SPACE * counter
        elif char not in ' \n':
            output += char
    return output

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 4, "Hello, asadssad!")

class BracketFormatterCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        whole_region = sublime.Region(0, self.view.size())
        text = self.view.substr(sublime.Region(0, self.view.size()))
        formatted_text = format(text)
        self.view.replace(edit, whole_region, formatted_text)