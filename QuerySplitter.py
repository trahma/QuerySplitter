import sublime, sublime_plugin, webbrowser

def selections(view, default_to_all=True):
    """Return all non-empty selections in view
    If None, return entire view if default_to_all is True
    """
    regions = [r for r in view.sel() if not r.empty()]

    if not regions and default_to_all:
        regions = [sublime.Region(0, view.size())]

    return regions

class UrlSplitCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        """Main plugin logic for the 'urlsplit' command.
        """
        view = self.view
        for region in selections(view):
            s = view.substr(region)
            view.replace(edit, region, s.replace("&", "\n&").replace("?", "\n?"))


class UrlMergeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        """Main plugin logic for the 'urlmerge' command.
        """
        view = self.view
        for region in selections(view):
            s = view.substr(region)
            view.replace(edit, region, s.replace("\n&", "&").replace("\n?", "?"))

class ViewInBrowserCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        """Main plugin logic for the 'viewinbrowser' command.
        """
        view = self.view
        for region in selections(view):
            s = view.substr(region)
            webbrowser.open_new_tab(s.replace("\n&", "&").replace("\n?", "?"))
