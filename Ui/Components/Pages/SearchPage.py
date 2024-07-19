from Core.Ui import *
from Services.Twitch.Gql import TwitchGqlModels
from Ui.Components.Operators.NavigationBar import PageObject
from Ui.Components.Operators.TabManager import TabManager


class SearchPage(TabManager):
    accountPageShowRequested = QtCore.pyqtSignal()

    def __init__(self, pageObject: PageObject, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent=parent)
        self.pageObject = pageObject
        self.home = Ui.Home(parent=self)
        self.home.searchResultWindowRequested.connect(self.openSearchResultTab)
        self.addTab(self.home, icon=Icons.HOME, closable=False)

    def openSearchResultTab(self, searchResult: TwitchGqlModels.Channel | TwitchGqlModels.Video | TwitchGqlModels.Clip) -> None:
        searchResultTab = Ui.SearchResult(searchResult, parent=self)
        searchResultTab.accountPageShowRequested.connect(self.accountPageShowRequested)
        self.setCurrentIndex(self.addTab(searchResultTab, icon=Icons.SEARCH))
        self.pageObject.show()